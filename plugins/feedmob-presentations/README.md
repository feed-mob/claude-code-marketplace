# PPT Generator Plugin

A comprehensive Claude Code plugin for creating, editing, and analyzing PowerPoint presentations through multiple approaches: Python-based creation, direct OOXML manipulation, and template workflows.

## Features

### Core Capabilities
- 🎯 **Python-based Creation**: Generate presentations programmatically with python-pptx
- 🔧 **OOXML Manipulation**: Direct XML editing for advanced control
- 📋 **Template Workflows**: Work with existing templates
- 🎨 **Professional Styling**: Multiple color schemes and design principles
- 🖼️ **Smart Assets**: Automatic background selection and logo insertion
- 🏷️ **Footer Branding**: Automatic FeedMob logo in footer on every slide
- 📊 **Multiple Formats**: Command-line, JSON, and programmatic APIs
- ✅ **Standard Format**: Compatible with PowerPoint, LibreOffice, Google Slides

### Advanced Features
- 📝 **Text Operations**: Extract, replace, and format text across slides
- 🔄 **Slide Management**: Rearrange, duplicate, and delete slides via OOXML
- 🎨 **Design Principles**: Built-in support for 6x6 rule, 60-30-10 color rule
- 🔍 **Analysis Tools**: Text inventory, structure validation
- 📐 **Layout Control**: Professional grid-based positioning

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

## Three Approaches to PowerPoint

This plugin supports three complementary workflows:

### 1. Python-based Creation (python-pptx)

**Best for**: Creating new presentations from scratch with professional styling.

```bash
python scripts/create_ppt.py --output presentation.pptx --json slides.json
```

**Capabilities**:
- Professional color schemes (FeedMob, Binance, Modern, Corporate)
- Automatic background selection and optional content logos
- Footer logo on every slide for consistent branding
- Multiple slide layouts (title, content, metrics dashboard, comparison)
- Advanced typography and visual effects

### 2. OOXML Manipulation

**Best for**: Advanced editing beyond library capabilities, bulk operations.

```bash
# Unpack PPTX
python scripts/ooxml_helpers.py unpack presentation.pptx

# Edit XML files directly
# Modify ppt/slides/*.xml, ppt/presentation.xml, etc.

# Repack
python scripts/ooxml_helpers.py repack unpacked_dir presentation.pptx -o modified.pptx
```

**Capabilities**:
- Rearrange slides by modifying XML
- Bulk text replacement across all slides
- Access comments, speaker notes, animations
- Fine-grained control over formatting

### 3. Template Workflows

**Best for**: Working with existing branded templates.

**Workflow**:
1. Extract template content inventory
2. Generate replacement text as JSON
3. Apply replacements programmatically
4. Validate and output modified presentation

## Core Features

### Creation Features

- **Multiple Color Schemes**: FeedMob, Binance, Professional, Modern, Corporate
- **Smart Backgrounds**: Automatic selection based on content keywords
- **Footer Branding**: FeedMob logo automatically added to every slide footer
- **Logo Insertion**: Optional content logos for specific slide types
- **Professional Layouts**: Title, content, metrics, comparison, two-column slides
- **Design Principles**: 6x6 rule, 60-30-10 color rule, grid alignment

### Supported Slide Types

1. **Title Slide**: Title and optional subtitle
2. **Content Slide**: Title with bullet point content
3. **Blank Slide**: Custom layout for text and images

## Requirements

**Core Requirements**:
- Python 3.6+
- python-pptx >= 0.6.21

**Optional Tools**:
- markitdown (text extraction)
- LibreOffice (validation and conversion)
- zipfile (OOXML manipulation, built-in to Python)

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

- **Name**: `feedmob-presentations`
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

## OOXML Helper Scripts

The plugin includes powerful OOXML manipulation tools:

### Unpack PPTX
```bash
python scripts/ooxml_helpers.py unpack presentation.pptx -o unpacked/
```

### Text Inventory
```bash
python scripts/ooxml_helpers.py inventory presentation.pptx -o inventory.json
```

### Bulk Text Replacement
```bash
python scripts/ooxml_helpers.py replace presentation.pptx "Old Text" "New Text" -o modified.pptx
```

### Validate Structure
```bash
python scripts/ooxml_helpers.py validate presentation.pptx
```

### Repack to PPTX
```bash
python scripts/ooxml_helpers.py repack unpacked/ presentation.pptx -o modified.pptx
```

## Design Principles

This plugin follows professional presentation design standards:

### Typography
- **Title**: ≥28pt for readability
- **Body**: ≥18pt minimum
- **Fonts**: Web-safe fonts (Arial, Helvetica)
- **Consistency**: Limited font variations

### Layout
- **6x6 Rule**: Max 6 lines per slide, 6 words per line
- **20% Margins**: Minimum white space
- **Grid System**: 12x8 grid for alignment
- **Visual Balance**: Even weight distribution

### Color
- **60-30-10 Rule**: 60% primary, 30% secondary, 10% accent
- **Max 4 Colors**: Per chart/visualization
- **Consistent Mapping**: Same colors for same data
- **Accessibility**: WCAG AA contrast ratios

### Content
- **Content-Informed Design**: Design serves content
- **Strong Hierarchy**: Clear visual priorities
- **Readable Contrast**: Sufficient color contrast
- **Professional Quality**: Business-ready output

## Best Practices

### Planning
- Define structure before detailed content
- Choose approach based on task (creation vs editing)
- Use content-informed design principles

### Implementation
- Python-pptx for new presentations
- OOXML for advanced operations
- Validate after major changes
- Keep text concise (6x6 rule)

### Quality Assurance
- Test in multiple applications
- Verify accessibility (contrast, font size)
- Validate OOXML structure
- Check on actual display device

## Troubleshooting

### Script Not Found

Ensure you're running the script from the correct directory:
```bash
cd plugins/feedmob-presentations/skills
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

- [SKILL.md](skills/SKILL.md) - Comprehensive skill documentation with examples and design principles
- [ooxml.md](skills/ooxml.md) - OOXML structure and manipulation guide

## Advanced Topics

### OOXML Structure

PPTX files are ZIP archives containing:
- `ppt/presentation.xml` - Slide order and IDs
- `ppt/slides/*.xml` - Individual slide content
- `ppt/slideLayouts/` - Layout templates
- `[Content_Types].xml` - File type declarations
- `ppt/_rels/*.rels` - Relationship definitions

See [ooxml.md](skills/ooxml.md) for complete reference.

### Direct XML Editing

For operations beyond python-pptx:
1. Unpack PPTX (it's a ZIP)
2. Edit XML files
3. Repack to PPTX
4. Validate structure

**Critical**: Invalid OOXML creates corrupted files. Always validate.

### Color Palettes

Built-in professional palettes:
- **FeedMob**: Teal (#00B5AD), Gray, Blue
- **Binance**: Gold (#F0B90B), Black, White
- **Professional**: Navy, Gray, Blue
- **Modern**: Black, Coral, Mint
- **Corporate**: Charcoal, Gold, White

See SKILL.md for complete palette definitions.

## License

MIT



