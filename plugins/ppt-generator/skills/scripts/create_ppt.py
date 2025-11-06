#!/usr/bin/env python3
"""
PPT Generator Script
Creates PowerPoint presentations using python-pptx library.
Supports creating slides with text and images.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
except ImportError:
    print("Error: python-pptx library is required. Install it with: pip install python-pptx")
    sys.exit(1)


def create_title_slide(prs: Presentation, title: str, subtitle: Optional[str] = None):
    """Create a title slide with title and optional subtitle."""
    slide_layout = prs.slide_layouts[0]  # Title slide layout
    slide = prs.slides.add_slide(slide_layout)

    title_shape = slide.shapes.title
    title_shape.text = title

    if subtitle:
        subtitle_shape = slide.placeholders[1]
        subtitle_shape.text = subtitle

    return slide


def create_content_slide(prs: Presentation, title: str, content: List[str]):
    """Create a content slide with title and bullet points."""
    slide_layout = prs.slide_layouts[1]  # Title and content layout
    slide = prs.slides.add_slide(slide_layout)

    title_shape = slide.shapes.title
    title_shape.text = title

    content_shape = slide.placeholders[1]
    tf = content_shape.text_frame
    tf.text = content[0] if content else ""

    # Add remaining content as bullet points
    for text in content[1:]:
        p = tf.add_paragraph()
        p.text = text
        p.level = 0

    return slide


def create_blank_slide(prs: Presentation):
    """Create a blank slide."""
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    return slide


def add_text_to_slide(slide, text: str, left: float = 1, top: float = 1,
                      width: float = 8, height: float = 1, font_size: int = 18):
    """Add text box to a slide."""
    left_inches = Inches(left)
    top_inches = Inches(top)
    width_inches = Inches(width)
    height_inches = Inches(height)

    textbox = slide.shapes.add_textbox(left_inches, top_inches, width_inches, height_inches)
    text_frame = textbox.text_frame
    text_frame.text = text

    # Set font size
    paragraph = text_frame.paragraphs[0]
    paragraph.font.size = Pt(font_size)

    return textbox


def add_image_to_slide(slide, image_path: str, left: float = 1, top: float = 1,
                       width: Optional[float] = None, height: Optional[float] = None):
    """Add an image to a slide."""
    if not Path(image_path).exists():
        print(f"Warning: Image file not found: {image_path}")
        return None

    left_inches = Inches(left)
    top_inches = Inches(top)

    if width and height:
        width_inches = Inches(width)
        height_inches = Inches(height)
        return slide.shapes.add_picture(image_path, left_inches, top_inches,
                                       width=width_inches, height=height_inches)
    else:
        return slide.shapes.add_picture(image_path, left_inches, top_inches)


def create_presentation_from_json(json_data: Dict, output_path: str):
    """Create a presentation from JSON data structure."""
    prs = Presentation()

    slides_data = json_data.get('slides', [])

    for slide_data in slides_data:
        slide_type = slide_data.get('type', 'content')

        if slide_type == 'title':
            title = slide_data.get('title', '')
            subtitle = slide_data.get('subtitle')
            create_title_slide(prs, title, subtitle)

        elif slide_type == 'content':
            title = slide_data.get('title', '')
            content = slide_data.get('content', [])
            if isinstance(content, str):
                content = [content]
            slide = create_content_slide(prs, title, content)

            # Add image if specified
            if 'image' in slide_data:
                image_path = slide_data['image']
                add_image_to_slide(slide, image_path,
                                 left=slide_data.get('image_left', 5),
                                 top=slide_data.get('image_top', 2))

        elif slide_type == 'blank':
            slide = create_blank_slide(prs)

            # Add text if specified
            if 'text' in slide_data:
                add_text_to_slide(slide, slide_data['text'],
                                left=slide_data.get('text_left', 1),
                                top=slide_data.get('text_top', 1),
                                font_size=slide_data.get('font_size', 18))

            # Add image if specified
            if 'image' in slide_data:
                add_image_to_slide(slide, slide_data['image'],
                                 left=slide_data.get('image_left', 1),
                                 top=slide_data.get('image_top', 1))

    prs.save(output_path)
    print(f"Successfully created presentation: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


def create_simple_presentation(title: str, output_path: str, slides: Optional[List[Dict]] = None):
    """Create a simple presentation with title slide and optional content slides."""
    prs = Presentation()

    # Create title slide
    create_title_slide(prs, title)

    # Add content slides if provided
    if slides:
        for slide_info in slides:
            slide_title = slide_info.get('title', '')
            slide_content = slide_info.get('content', [])
            if isinstance(slide_content, str):
                slide_content = [slide_content]
            create_content_slide(prs, slide_title, slide_content)

    prs.save(output_path)
    print(f"Successfully created presentation: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


def main():
    parser = argparse.ArgumentParser(
        description='Create PowerPoint presentations using python-pptx'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output file path for the PPTX file'
    )
    parser.add_argument(
        '--title',
        help='Title for the presentation (creates title slide)'
    )
    parser.add_argument(
        '--json', '-j',
        help='JSON file containing slide definitions'
    )
    parser.add_argument(
        '--subtitle',
        help='Subtitle for the title slide'
    )
    parser.add_argument(
        '--slides',
        nargs='+',
        help='Additional slide titles (creates content slides)'
    )

    args = parser.parse_args()

    # Ensure output path has .pptx extension
    output_path = args.output
    if not output_path.endswith('.pptx'):
        output_path += '.pptx'

    try:
        if args.json:
            # Create from JSON file
            with open(args.json, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            create_presentation_from_json(json_data, output_path)

        elif args.title:
            # Create simple presentation
            slides_data = []
            if args.slides:
                for slide_title in args.slides:
                    slides_data.append({'title': slide_title, 'content': []})

            create_simple_presentation(args.title, output_path, slides_data)

        else:
            print("Error: Either --title or --json must be provided")
            parser.print_help()
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error creating presentation: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
