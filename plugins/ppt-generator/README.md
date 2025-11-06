# PPT Generator Plugin

A Claude Code plugin that provides an Agent Skill for creating and editing PowerPoint presentations using Python and the python-pptx library.

## Features

- 🎯 **Easy Creation**: Quickly generate PowerPoint presentations from simple commands
- 📊 **Multiple Formats**: Support for command-line and JSON-based slide definitions
- 🖼️ **Image Support**: Add images to slides with custom positioning
- 📝 **Text Formatting**: Create title slides, content slides, and custom text layouts
- ✅ **Standard Format**: Generates standard .pptx files compatible with Microsoft PowerPoint, LibreOffice, and Google Slides

## Installation

This plugin is part of the FeedMob Claude Plugins marketplace. It will be automatically available when the plugin is installed.

## Usage

The PPT Generator skill will automatically activate when you mention:

- "Create a PowerPoint presentation"
- "Generate a PPT file"
- "Make a presentation about..."
- "Create slides for..."
- "Add slides to a presentation"

## Quick Start

### Simple Presentation

**Request:**
```
Create a PowerPoint presentation titled "Project Update"
```

**Result:**
- Creates a new PPTX file with a title slide

### Presentation with Multiple Slides

**Request:**
```
Create a presentation about quarterly results with slides for Introduction, Results, and Summary
```

**Result:**
- Creates a PPTX file with title slide and content slides

## Features

### Core Capabilities

- **Create New Presentations**: Generate fresh PowerPoint files from scratch
- **Add Slides**: Create title slides and content slides with different layouts
- **Add Text Content**: Insert titles, subtitles, and body text with bullet points
- **Insert Images**: Add images to slides from file paths with custom positioning
- **Set Layouts**: Use standard PowerPoint layouts (title slide, title and content, blank)

### Supported Slide Types

1. **Title Slide**: Title and optional subtitle
2. **Content Slide**: Title with bullet point content
3. **Blank Slide**: Custom layout for text and images

## Requirements

- Python 3.6 or higher
- python-pptx library (>=0.6.21)
- Image files must exist at specified paths (for image insertion)

## Usage Examples

### Example 1: Basic Presentation

```bash
python scripts/create_ppt.py --output meeting.pptx --title "Team Meeting"
```

### Example 2: Multiple Slides

```bash
python scripts/create_ppt.py \
  --output quarterly.pptx \
  --title "Q4 Results" \
  --slides "Introduction" "Financials" "Summary"
```

### Example 3: JSON-Based Creation

Create a `slides.json` file:
```json
{
  "slides": [
    {
      "type": "title",
      "title": "Company Overview",
      "subtitle": "2024 Annual Report"
    },
    {
      "type": "content",
      "title": "Highlights",
      "content": [
        "Record revenue growth",
        "Expanded to new markets",
        "Launched innovative products"
      ]
    }
  ]
}
```

Then run:
```bash
python scripts/create_ppt.py --output company.pptx --json slides.json
```

## How It Works

1. **Skill Detection**: Claude identifies when PPT creation is needed
2. **Content Analysis**: Understands the structure and content requirements
3. **Script Execution**: Runs the Python script with appropriate parameters
4. **File Generation**: Creates the .pptx file in the specified location
5. **Verification**: Confirms successful creation

## Skill Details

- **Name**: `ppt-generator`
- **Tools**: Read, Write, Bash
- **Language**: Python
- **Dependencies**: python-pptx>=0.6.21

## Advanced Features

### Custom Text Positioning

For blank slides, specify exact positions:
```json
{
  "type": "blank",
  "text": "Custom Text",
  "text_left": 2,
  "text_top": 1,
  "font_size": 24
}
```

### Image Insertion

Add images with custom positioning:
```json
{
  "type": "content",
  "title": "Product Screenshot",
  "content": ["New features"],
  "image": "screenshot.png",
  "image_left": 5,
  "image_top": 2
}
```

## Best Practices

1. **Plan Structure First**: Define slide structure before adding detailed content
2. **Use Appropriate Layouts**: Choose layouts that match content type
3. **Keep Text Concise**: Slides should have clear, brief content
4. **Optimize Images**: Ensure images are appropriately sized before insertion
5. **Test Output**: Open generated PPT to verify formatting

## Troubleshooting

### Script Not Found

Ensure you're running the script from the correct directory:
```bash
cd plugins/ppt-generator/skills
python scripts/create_ppt.py [options]
```

### Missing python-pptx Library

Install the required library:
```bash
pip install python-pptx
```

### Image Not Found

- Verify image file paths are correct
- Use absolute paths if relative paths don't work
- Check file permissions

### Invalid JSON Format

- Validate JSON syntax before running
- Ensure proper structure matches expected format
- Check for missing commas or brackets

## Contributing

Improvements to this plugin are welcome! You can:
- Add support for more slide layouts
- Enhance text formatting options
- Add support for charts and tables
- Improve error handling
- Provide feedback and suggestions

## Documentation

- [SKILL.md](skills/SKILL.md) - Detailed skill documentation
- [EXAMPLES.md](skills/EXAMPLES.md) - Usage examples and scenarios

## License

MIT
