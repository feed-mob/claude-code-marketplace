---
name: ppt-generator
description: Create and edit PowerPoint presentations. Use when you need to generate PPT files, create slides, add text or images to presentations.
allowed-tools: Read, Write, Bash
dependencies: python-pptx>=0.6.21
---

# PPT Generator

This skill creates and edits PowerPoint presentations using the python-pptx library. It supports basic functionality for creating slides, adding text content, and inserting images.

## Instructions

When invoked, this skill will:

1. **Identify requirements**: Understand what kind of presentation needs to be created
2. **Create PPT structure**: Set up a new PowerPoint file with appropriate slides
3. **Add content**: Populate slides with titles, text, and images as specified
4. **Save output**: Generate the final .pptx file in the specified location

## Features

### Core Capabilities

- **Create new presentations**: Generate fresh PowerPoint files from scratch
- **Add slides**: Create title slides and content slides with different layouts
- **Add text content**: Insert titles, subtitles, and body text
- **Insert images**: Add images to slides from file paths
- **Set layouts**: Use standard PowerPoint layouts (title slide, title and content, blank, etc.)

### Supported Operations

- Create title slide with title and subtitle
- Add content slides with title and bullet points
- Insert images into slides
- Format text (bold, italic, font size)
- Set slide layouts programmatically

## Implementation

The skill uses Python with the python-pptx library to process PowerPoint files. Run the processing script:

```bash
python scripts/create_ppt.py [options]
```

### Script Usage

The script supports multiple ways to create presentations:

**1. Simple command-line creation:**
```bash
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation"
```

**2. JSON-based content definition:**
```bash
python scripts/create_ppt.py --output presentation.pptx --json slides.json
```

**3. Interactive mode:**
```bash
python scripts/create_ppt.py --output presentation.pptx --interactive
```

The script will:
- Create a new PowerPoint presentation
- Add slides based on provided content
- Insert text and images as specified
- Save the final .pptx file
- Handle errors gracefully with clear messages

## Usage Examples

**Create a simple presentation:**
```
Create a PowerPoint presentation about project status
```

**Add slides with content:**
```
Generate a PPT with title slide and 3 content slides about quarterly results
```

**Create presentation from outline:**
```
Make a PowerPoint from this outline: Introduction, Features, Benefits, Conclusion
```

**Add images to slides:**
```
Create a presentation and add the logo image to the title slide
```

## Requirements

- Python 3.6 or higher
- python-pptx library (>=0.6.21)
- Image files must exist at specified paths (for image insertion)

## Output

- A .pptx file saved to the specified location
- Standard PowerPoint format compatible with Microsoft PowerPoint, LibreOffice, and Google Slides
- Preserves all formatting and layout settings

## Best Practices

- **Plan structure first**: Define the slide structure before adding detailed content
- **Use appropriate layouts**: Choose layouts that match the content type
- **Keep text concise**: Slides should have clear, concise text
- **Optimize images**: Ensure images are appropriately sized before insertion
- **Test output**: Open the generated PPT to verify formatting

For detailed examples, see [EXAMPLES.md](EXAMPLES.md).
