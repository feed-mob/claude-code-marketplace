---
name: ppt-generator
description: Create professional PowerPoint presentations with enhanced styling, themes, and layout options. Use when you need to generate PPT files with modern design elements.
allowed-tools: Read, Write, Bash
---

# PPT Generator

This skill creates professional PowerPoint presentations using the python-pptx library with enhanced styling capabilities inspired by modern business presentations. It supports advanced features including multiple color schemes (FeedMob, Binance, professional, modern, corporate), professional typography, custom layouts, and image effects.

## Instructions

When invoked, this skill will:

1. **Identify requirements**: Understand what kind of presentation needs to be created
2. **Apply styling**: Select appropriate color scheme and typography based on context
3. **Create PPT structure**: Set up a new PowerPoint file with enhanced styling
4. **Add content**: Populate slides with titles, text, and images with professional formatting
5. **Save output**: Generate the final .pptx file in the specified location

## Features

### Core Capabilities

- **Create new presentations**: Generate fresh PowerPoint files with professional styling
- **Multiple color schemes**: Choose from FeedMob, Binance (default), professional, modern, or corporate themes
- **FeedMob branding**: Native support for FeedMob color scheme with custom slide layouts
- **Advanced layouts**: Create section headers, comparison slides, two-column layouts, metrics dashboards
- **Typography**: Professional fonts (Arial) with consistent sizing and colors
- **Image effects**: Add shadows, proper sizing, and positioning for images
- **Background styling**: Gradient backgrounds and image support for title slides
- **Professional templates**: Corporate-quality slide designs with company-specific styling

### NEW: Professional Design Principles Integration

#### Intelligent Background & Logo System
- **Automatic background selection**: Choose appropriate background images based on slide content keywords
- **Smart logo insertion**: Automatically add logos to slides without backgrounds for brand consistency
- **Content-aware matching**: Backgrounds selected by analyzing slide titles and content for context
- **Flexible control**: Enable/disable automatic backgrounds and logos via command line or JSON
- **Professional positioning**: Logos placed strategically (bottom-right by default) with transparency
- **Theme consistency**: Backgrounds and logos complement the chosen color scheme

#### Design Principles Implementation
- **6x6 Rule**: Automatically optimize content to maximum 6 lines per slide, 6 words per line
- **Typography Standards**: Title ≥28pt, Body ≥18pt with Arial sans-serif font
- **60-30-10 Color Rule**: 60% primary color, 30% secondary, 10% accent for visual harmony
- **Visual Hierarchy**: Automatic emphasis for first items, action words, and metrics with colors
- **Grid Alignment System**: 12x8 grid for precise element positioning and balance
- **White Space Optimization**: 20% minimum margins for improved readability
- **Content Simplification**: Automatic truncation of long text with ellipsis for clarity

### Background Selection Logic

The system intelligently selects backgrounds based on content:

- **Business/Professional**: Uses corporate-style backgrounds (bg4.jpg, bg5.jpg)
- **Technology/Digital**: Uses tech-themed backgrounds (bg2.png, bg3.png)
- **Analytics/Data**: Uses data-visualization backgrounds (bg3.png)
- **Marketing/Growth**: Uses marketing-focused backgrounds (bg1.jpg)
- **General Content**: Uses appropriate backgrounds for overviews, introductions, features, benefits

### Logo Insertion Rules

- **Added to**: Content slides, comparison slides, visual content, two-column layouts
- **Not added to**: Title slides, section headers, metrics dashboards, slides with existing backgrounds
- **Positioning**: Bottom-right corner with subtle transparency
- **Selection**: Random from available FeedMob logo assets

### Enhanced Slide Types

- **FeedMob title slides**: Gradient backgrounds with orange accent bars and 52pt white titles
- **FeedMob content slides**: Blue accent bar with gray title background and green bullet points
- **Professional title slides**: Solid color background with large 54pt titles (Binance style)
- **Visual content slides**: Bullet points with image support and colored accent bars
- **Metrics dashboard slides**: Grid layout with colorful KPI boxes (up to 4 metrics)
- **Content slides**: Professional bullet points with consistent styling
- **Section headers**: Eye-catching gradient backgrounds
- **Comparison slides**: Side-by-side content with colored backgrounds
- **Two-column slides**: Balanced content layout
- **Blank slides**: Canvas for custom layouts with shapes and text

### Supported Operations

- Apply professional color schemes (FeedMob, Binance, Professional, Modern, Corporate)
- Create FeedMob-branded title slides with gradient backgrounds
- Create FeedMob content slides with custom styling
- Create professional title slides with solid color backgrounds
- Create metrics dashboards with colorful KPI boxes
- Create visual content slides with images and accent bars
- Add section headers with gradient backgrounds
- Generate comparison and two-column layouts
- Style text with professional Arial fonts and colors
- Add images with shadow effects
- Create custom shapes with text
- Format text with consistent typography

## JSON Configuration (Enhanced)

The JSON format now supports automatic background and logo control:

```json
{
  "color_scheme": "feedmob",
  "auto_backgrounds": true,
  "auto_logos": true,
  "slides": [
    {
      "type": "title",
      "title": "Company Overview"
    },
    {
      "type": "content",
      "title": "Technology Features",
      "content": ["Cloud platform", "Real-time analytics", "Mobile support"]
    }
  ]
}
```

### JSON Options

- **auto_backgrounds** (boolean): Enable automatic background selection (default: true)
- **auto_logos** (boolean): Enable automatic logo insertion (default: true)

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

**3. Enhanced command-line creation with color scheme:**
```bash
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation" --color-scheme feedmob
```

**4. Presentation with background image:**
```bash
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation" --background-image "bg.jpg"
```

**5. Presentation with automatic backgrounds and logos (NEW):**
```bash
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation" --color-scheme feedmob
```

**6. Disable automatic backgrounds or logos:**
```bash
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation" --no-auto-backgrounds
python scripts/create_ppt.py --output presentation.pptx --title "My Presentation" --no-auto-logos
```

The script will:
- Create a new PowerPoint presentation with professional styling
- Apply FeedMob or Binance color scheme by default (or selected alternative theme)
- **NEW**: Automatically select background images based on slide content (enabled by default)
- **NEW**: Automatically add logos to slides without backgrounds (enabled by default)
- Add slides with enhanced typography and layout
- Insert text and images with proper formatting
- Save the final .pptx file
- Handle errors gracefully with clear messages

## Usage Examples

**Create a FeedMob-branded presentation:**
```
Create a PowerPoint presentation about FeedMob platform using FeedMob color scheme
```

**Create a professional presentation:**
```
Create a PowerPoint presentation about project status (uses Binance style by default)
```

**Add slides with enhanced styling:**
```
Generate a PPT with title slide and 3 content slides about quarterly results (uses FeedMob styling)
```

**Create presentation with section headers:**
```
Make a PowerPoint from this outline: Introduction, Features, Benefits, Conclusion with section headers (uses FeedMob theme)
```

**Create comparison slides:**
```
Create a presentation comparing our product vs competitors using FeedMob colors
```

**Add images with effects:**
```
Create a FeedMob presentation and add the logo image to the title slide with shadow effects
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



