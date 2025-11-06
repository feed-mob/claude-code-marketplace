# PPT Generator Skill Examples

This document provides examples of how to use the PPT Generator skill to create PowerPoint presentations.

## Basic Usage

### Example 1: Simple Presentation with Title Slide

**Request:**
```
Create a PowerPoint presentation titled "Project Status Update"
```

**Command:**
```bash
python scripts/create_ppt.py --output project_status.pptx --title "Project Status Update"
```

**Result:**
- Creates a new PPTX file with a title slide
- Title: "Project Status Update"

### Example 2: Presentation with Multiple Slides

**Request:**
```
Create a presentation about quarterly results with slides for Introduction, Q1 Results, Q2 Results, and Summary
```

**Command:**
```bash
python scripts/create_ppt.py \
  --output quarterly_results.pptx \
  --title "Quarterly Results 2024" \
  --slides "Introduction" "Q1 Results" "Q2 Results" "Summary"
```

**Result:**
- Creates a PPTX file with 5 slides:
  1. Title slide: "Quarterly Results 2024"
  2. Content slide: "Introduction"
  3. Content slide: "Q1 Results"
  4. Content slide: "Q2 Results"
  5. Content slide: "Summary"

## JSON-Based Creation

### Example 3: Complex Presentation from JSON

**JSON File (slides.json):**
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
      "title": "Executive Summary",
      "content": [
        "Record-breaking revenue growth",
        "Expanded to 5 new markets",
        "Launched 3 innovative products"
      ]
    },
    {
      "type": "content",
      "title": "Financial Highlights",
      "content": [
        "Revenue: $50M (up 25%)",
        "Profit margin: 18%",
        "Market share: 12%"
      ]
    },
    {
      "type": "blank",
      "text": "Thank You",
      "text_left": 3,
      "text_top": 3,
      "font_size": 48
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output company_overview.pptx --json slides.json
```

**Result:**
- Creates a presentation with 4 slides:
  1. Title slide with title and subtitle
  2. Content slide with bullet points
  3. Content slide with financial data
  4. Blank slide with large "Thank You" text

### Example 4: Presentation with Images

**JSON File (presentation_with_images.json):**
```json
{
  "slides": [
    {
      "type": "title",
      "title": "Product Launch",
      "subtitle": "New Features 2024"
    },
    {
      "type": "content",
      "title": "Product Screenshots",
      "content": [
        "New user interface",
        "Enhanced performance",
        "Mobile app support"
      ],
      "image": "screenshots/product.png",
      "image_left": 5,
      "image_top": 2
    },
    {
      "type": "blank",
      "image": "logo.png",
      "image_left": 3,
      "image_top": 2
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output product_launch.pptx --json presentation_with_images.json
```

**Result:**
- Creates a presentation with images embedded in slides
- Images are positioned as specified in the JSON

## Common Scenarios

### Scenario 1: Meeting Presentation

**Use Case:** Create a quick presentation for a team meeting

**Request:**
```
Create a meeting presentation with agenda items: Welcome, Updates, Discussion, Action Items
```

**Implementation:**
```bash
python scripts/create_ppt.py \
  --output meeting.pptx \
  --title "Team Meeting - $(date +%Y-%m-%d)" \
  --slides "Welcome" "Updates" "Discussion" "Action Items"
```

### Scenario 2: Project Proposal

**Use Case:** Create a project proposal presentation

**JSON Structure:**
```json
{
  "slides": [
    {
      "type": "title",
      "title": "Project Proposal: Website Redesign",
      "subtitle": "Q2 2024 Initiative"
    },
    {
      "type": "content",
      "title": "Objectives",
      "content": [
        "Improve user experience",
        "Increase conversion rate",
        "Modernize design"
      ]
    },
    {
      "type": "content",
      "title": "Timeline",
      "content": [
        "Phase 1: Design (2 weeks)",
        "Phase 2: Development (4 weeks)",
        "Phase 3: Testing (1 week)"
      ]
    },
    {
      "type": "content",
      "title": "Budget",
      "content": [
        "Design: $10,000",
        "Development: $25,000",
        "Testing: $5,000",
        "Total: $40,000"
      ]
    }
  ]
}
```

### Scenario 3: Training Material

**Use Case:** Create training slides

**Request:**
```
Create training slides for "Introduction to Python" with sections: Basics, Data Types, Control Flow, Functions
```

**Implementation:**
```bash
python scripts/create_ppt.py \
  --output python_training.pptx \
  --title "Introduction to Python" \
  --subtitle "Training Session" \
  --slides "Basics" "Data Types" "Control Flow" "Functions"
```

## Advanced Features

### Custom Text Positioning

For blank slides, you can specify exact positions:

```json
{
  "slides": [
    {
      "type": "blank",
      "text": "Custom Positioned Text",
      "text_left": 2,
      "text_top": 1,
      "font_size": 24
    }
  ]
}
```

### Multiple Images

You can add multiple elements to blank slides:

```json
{
  "slides": [
    {
      "type": "blank",
      "text": "Company Logo",
      "text_left": 1,
      "text_top": 1,
      "font_size": 18,
      "image": "logo.png",
      "image_left": 5,
      "image_top": 2
    }
  ]
}
```

## Tips and Best Practices

1. **Plan your structure first**: Define all slides before adding detailed content
2. **Use appropriate slide types**:
   - `title` for title slides
   - `content` for slides with bullet points
   - `blank` for custom layouts
3. **Keep text concise**: Slides should have clear, brief content
4. **Test image paths**: Ensure all image files exist before running the script
5. **Use JSON for complex presentations**: JSON format is more flexible for detailed presentations

## Error Handling

The script handles common errors gracefully:

- **Missing python-pptx**: Shows installation instructions
- **Invalid JSON**: Displays JSON parsing errors
- **Missing image files**: Shows warning but continues
- **Invalid file paths**: Provides clear error messages
