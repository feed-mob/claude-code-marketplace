# PPT Generator Skill Examples

This document provides examples of how to use the enhanced PPT Generator skill to create professional PowerPoint presentations with advanced styling options, including FeedMob branding support.

## Basic Usage

### Example 1: Professional Presentation with Color Scheme

**Request:**
```
Create a PowerPoint presentation titled "Project Status Update" using the professional color scheme
```

**Command:**
```bash
python scripts/create_ppt.py --output project_status.pptx --title "Project Status Update" --color-scheme professional
```

**Result:**
- Creates a new PPTX file with a professional dark blue theme
- Title: "Project Status Update" with enhanced typography
- Uses Lato font with professional color palette

### Example 2: Simple Presentation with Title Slide

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

### Example 2: Modern Theme Presentation with Background Image

**Request:**
```
Create a presentation about quarterly results using the modern theme with a background image
```

**Command:**
```bash
python scripts/create_ppt.py \
  --output quarterly_results.pptx \
  --title "Quarterly Results 2024" \
  --subtitle "Q1-Q2 Performance" \
  --color-scheme modern \
  --background-image "company-bg.jpg"
```

**Result:**
- Creates a PPTX file with modern orange accent colors
- Title slide with background image
- Enhanced typography and spacing

### Example 3: Presentation with Multiple Slides

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

### Example 4: Enhanced Presentation with Color Scheme

**JSON File (professional_presentation.json):**
```json
{
  "color_scheme": "professional",
  "slides": [
    {
      "type": "title",
      "title": "Company Overview",
      "subtitle": "2024 Annual Report"
    },
    {
      "type": "section_header",
      "title": "Executive Summary",
      "subtitle": "Key Highlights"
    },
    {
      "type": "content",
      "title": "Key Achievements",
      "content": [
        "Record-breaking revenue growth",
        "Expanded to 5 new markets",
        "Launched 3 innovative products"
      ]
    },
    {
      "type": "comparison",
      "title": "Year-over-Year Comparison",
      "left_title": "2023",
      "right_title": "2024",
      "left_points": [
        "Revenue: $40M",
        "Markets: 8",
        "Products: 12"
      ],
      "right_points": [
        "Revenue: $50M",
        "Markets: 13",
        "Products: 15"
      ]
    },
    {
      "type": "two_column",
      "title": "Strategic Initiatives",
      "left_content": [
        "Market Expansion",
        "Digital Transformation",
        "Customer Experience"
      ],
      "right_content": [
        "Product Innovation",
        "Operational Excellence",
        "Talent Development"
      ]
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output company_overview.pptx --json professional_presentation.json
```

**Result:**
- Creates a presentation with professional dark blue theme
- Multiple slide types including section headers and comparison slides
- Consistent typography and styling throughout

### Example 5: Modern Theme with Image Effects

**JSON File (modern_presentation.json):**
```json
{
  "color_scheme": "modern",
  "slides": [
    {
      "type": "title",
      "title": "Product Launch",
      "subtitle": "New Features 2024",
      "background_image": "product-bg.jpg"
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
      "image_top": 2,
      "image_width": 4,
      "image_height": 2,
      "image_shadow": true
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output product_launch.pptx --json modern_presentation.json
```

**Result:**
- Creates a presentation with modern orange accent colors
- Title slide with background image
- Images with shadow effects
- Professional layout and spacing

### Example 6: Complex Presentation from JSON

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

## Advanced Professional Styling (Binance-Style)

### Example 7: Professional Title Slide with Binance Color Scheme

**Request:**
```
Create a professional presentation using the Binance color scheme with a modern title slide
```

**Command:**
```bash
python scripts/create_ppt.py \
  --output professional_presentation.pptx \
  --title "Quarterly Business Review" \
  --subtitle "Exceeding Expectations in 2024" \
  --color-scheme binance
```

**Result:**
- Creates a presentation with exact Binance colors (dark blue #0E2841, etc.)
- Professional title slide with solid color background
- Arial font matching corporate standards
- Large, prominent title (54pt) with subtitle

### Example 8: Binance-Style Presentation with JSON

**JSON File (binance_style.json):**
```json
{
  "color_scheme": "binance",
  "slides": [
    {
      "type": "title",
      "title": "Strategic Partnership Announcement",
      "subtitle": "FeedMob x Binance",
      "professional_style": true
    },
    {
      "type": "visual_content",
      "title": "Key Partnership Benefits",
      "content": [
        "Enhanced liquidity provision",
        "Advanced trading algorithms",
        "Cross-platform integration",
        "Global market access"
      ],
      "image": "partnership_chart.png"
    },
    {
      "type": "metrics_dashboard",
      "title": "Performance Metrics",
      "metrics": [
        {"label": "Trading Volume", "value": "$2.5B"},
        {"label": "Active Users", "value": "1.2M"},
        {"label": "Market Coverage", "value": "180+"},
        {"label": "Success Rate", "value": "98.5%"}
      ]
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output partnership_announcement.pptx --json binance_style.json
```

**Result:**
- Professional title slide with dark blue background
- Visual content slide with image and bullet points
- Metrics dashboard with colorful KPI boxes
- Consistent Binance color scheme throughout

### Example 9: Corporate Presentation with Multiple Layouts

**JSON File (corporate_overview.json):**
```json
{
  "color_scheme": "binance",
  "slides": [
    {
      "type": "title",
      "title": "Annual Business Review",
      "subtitle": "Innovation & Growth",
      "professional_style": true
    },
    {
      "type": "section_header",
      "title": "Financial Performance",
      "subtitle": "Record-Breaking Results"
    },
    {
      "type": "metrics_dashboard",
      "title": "2024 Key Metrics",
      "metrics": [
        {"label": "Revenue", "value": "$850M"},
        {"label": "Growth", "value": "+45%"},
        {"label": "Users", "value": "15M"},
        {"label": "Markets", "value": "120"}
      ]
    },
    {
      "type": "visual_content",
      "title": "Strategic Initiatives",
      "content": [
        "Global market expansion",
        "Technology infrastructure upgrades",
        "Product portfolio diversification",
        "Strategic partnerships"
      ],
      "image": "initiatives_diagram.png"
    },
    {
      "type": "comparison",
      "title": "Year-over-Year Comparison",
      "left_title": "2023",
      "right_title": "2024",
      "left_points": [
        "Revenue: $585M",
        "Users: 10M",
        "Markets: 85",
        "Growth: +12%"
      ],
      "right_points": [
        "Revenue: $850M",
        "Users: 15M",
        "Markets: 120",
        "Growth: +45%"
      ]
    }
  ]
}
```

## New Slide Types

### Visual Content Slide
Type: `visual_content`
- Title with colored accent bar
- Bullet points on the left side
- Image on the right side (if provided)
- Professional Arial typography

### Metrics Dashboard Slide
Type: `metrics_dashboard`
- Grid layout with up to 4 metric boxes
- Large colored metric values
- Descriptive labels below each value
- Different accent colors for each metric

### Professional Title Slide
Type: `title` with `professional_style: true`
- Solid color background (dark blue)
- Large title text (54pt)
- Optional subtitle at bottom
- Perfect for corporate presentations

## FeedMob Theme Examples

### Example 10: FeedMob-Branded Presentation

**Request:**
```
Create a FeedMob-branded presentation about the platform's features
```

**Command:**
```bash
python scripts/create_ppt.py \
  --output feedmob_platform.pptx \
  --title "FeedMob Platform Overview" \
  --subtitle "Performance Marketing Solutions" \
  --color-scheme feedmob
```

**Result:**
- Creates a presentation with FeedMob's signature colors
- Blue primary (#058DC7) with orange accent (#ED561B)
- Gradient title slide with orange accent bar
- 52pt white title on FeedMob blue background

### Example 11: FeedMob Presentation with JSON

**JSON File (feedmob_demo.json):**
```json
{
  "title": "FeedMob Product Showcase",
  "color_scheme": "feedmob",
  "slides": [
    {
      "type": "title",
      "title": "FeedMob Platform Overview",
      "subtitle": "Performance Marketing Solutions",
      "professional_style": true,
      "background_image": "assets/backgrounds/image6.png"
    },
    {
      "type": "content",
      "title": "Key Features",
      "content": [
        "Real-time analytics dashboard",
        "AI-powered campaign optimization",
        "Multi-platform integration",
        "Comprehensive reporting tools"
      ],
      "image": "assets/logos/image14.png"
    },
    {
      "type": "visual_content",
      "title": "Performance Metrics",
      "content": [
        "Conversion rate optimization",
        "Audience targeting precision",
        "ROI tracking and analysis",
        "Automated budget allocation"
      ],
      "image": "assets/backgrounds/image24.png"
    },
    {
      "type": "metrics_dashboard",
      "title": "Platform Performance",
      "metrics": [
        {
          "label": "Active Campaigns",
          "value": "1,247"
        },
        {
          "label": "Conversion Rate",
          "value": "4.8%"
        },
        {
          "label": "Monthly Revenue",
          "value": "$2.3M"
        },
        {
          "label": "User Satisfaction",
          "value": "96%"
        }
      ]
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output feedmob_showcase.pptx --json feedmob_demo.json
```

**Result:**
- FeedMob-branded title slide with gradient background
- Custom FeedMob content slides with blue accent bars
- Metrics dashboard using FeedMob color palette
- Professional styling with extracted logos and backgrounds

## Enhanced Features (NEW)

### Example 12: Design Principles in Action

**Request:**
```
Create a professional presentation applying all design principles with enhanced visual design
```

**JSON File (design_principles.json):**
```json
{
  "color_scheme": "feedmob",
  "auto_backgrounds": true,
  "auto_logos": true,
  "slides": [
    {
      "type": "title",
      "title": "Design Excellence Framework",
      "subtitle": "Professional Standards Applied"
    },
    {
      "type": "content",
      "title": "6x6 Rule Implementation",
      "content": [
        "Maximum six bullet points per slide",
        "Maximum six words per bullet point",
        "Clear concise messaging improves",
        "Better readability achieved",
        "Professional appearance maintained"
      ]
    },
    {
      "type": "visual_content",
      "title": "Visual Hierarchy System",
      "content": [
        "Primary emphasis with bold colors",
        "Action words highlighted automatically",
        "Metrics displayed in orange accent",
        "Grid-aligned perfect positioning",
        "White space properly utilized"
      ]
    },
    {
      "type": "metrics_dashboard",
      "title": "Design Quality Metrics",
      "metrics": [
        {"label": "Typography Score", "value": "95%"},
        {"label": "Color Harmony", "value": "88%"},
        {"label": "Layout Balance", "value": "92%"},
        {"label": "Visual Impact", "value": "96%"}
      ]
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output design_excellence.pptx --json design_principles.json
```

**Result:**
- **6x6 Rule Applied**: Content automatically optimized to maximum 6 lines, 6 words per line
- **Typography Standards**: Titles at 44pt, body text at 20pt (≥18pt requirement met)
- **Visual Hierarchy**: First bullet point emphasized, action words highlighted, metrics in accent colors
- **Grid Alignment**: All elements perfectly aligned to 12x8 grid system
- **60-30-10 Color Rule**: 60% primary colors, 30% secondary, 10% accents for visual harmony
- **White Space**: Proper 20% margins maintained for readability
- **Auto Features**: Backgrounds and logos intelligently added based on content

### Example 13: Automatic Backgrounds and Logos

**Request:**
```
Create a professional presentation with automatic backgrounds and logos
```

**Command:**
```bash
python scripts/create_ppt.py \
  --output auto_enhanced.pptx \
  --title "Technology Platform Overview" \
  --subtitle "Digital Solutions 2024" \
  --slides "Platform Features" "Analytics Dashboard" "Mobile Integration" \
  --color-scheme feedmob
```

**Result:**
- Title slide with technology-themed background (auto-selected from "Technology" keywords)
- Content slides with appropriate backgrounds based on content:
  - "Platform Features": Technology background
  - "Analytics Dashboard": Data/analytics background
  - "Mobile Integration": Technology background
- Logos automatically added to slides without existing backgrounds
- Professional FeedMob color scheme throughout

### Example 13: JSON with Enhanced Features

**JSON File (enhanced_demo.json):**
```json
{
  "color_scheme": "feedmob",
  "auto_backgrounds": true,
  "auto_logos": true,
  "slides": [
    {
      "type": "title",
      "title": "Business Intelligence Platform",
      "subtitle": "Data-Driven Solutions"
    },
    {
      "type": "content",
      "title": "Key Features",
      "content": [
        "Real-time data processing",
        "Advanced analytics engine",
        "Interactive dashboards",
        "Automated reporting"
      ]
    },
    {
      "type": "visual_content",
      "title": "Performance Analytics",
      "content": [
        "High-speed processing",
        "Scalable architecture",
        "Cloud-native design",
        "Enterprise security"
      ]
    },
    {
      "type": "metrics_dashboard",
      "title": "Platform Statistics",
      "metrics": [
        {"label": "Data Processed", "value": "10TB/day"},
        {"label": "Query Speed", "value": "<100ms"},
        {"label": "Uptime", "value": "99.99%"},
        {"label": "Users", "value": "50K+"}
      ]
    }
  ]
}
```

**Command:**
```bash
python scripts/create_ppt.py --output enhanced_demo.pptx --json enhanced_demo.json
```

**Result:**
- Title slide with business-themed background (from "Business Intelligence" keywords)
- Content slide with technology background (from "analytics engine" keywords)
- Visual content slide with data/analytics background (from "Performance Analytics" keywords)
- Metrics dashboard without background (as per rules) but with logo added
- All slides maintain FeedMob branding and professional styling

### Example 14: Disable Automatic Features

**Command to disable backgrounds only:**
```bash
python scripts/create_ppt.py \
  --output clean_presentation.pptx \
  --title "Clean Presentation" \
  --slides "Content Slide 1" "Content Slide 2" \
  --no-auto-backgrounds
```

**Command to disable logos only:**
```bash
python scripts/create_ppt.py \
  --output no_logos.pptx \
  --title "No Logos Presentation" \
  --slides "Content Slide 1" "Content Slide 2" \
  --no-auto-logos
```

**Command to disable both:**
```bash
python scripts/create_ppt.py \
  --output minimal.pptx \
  --title "Minimal Presentation" \
  --slides "Content Slide 1" "Content Slide 2" \
  --no-auto-backgrounds \
  --no-auto-logos
```

### Background and Logo Selection Logic

#### Automatic Background Selection

The system analyzes slide titles and content to select appropriate backgrounds:

1. **Business/Professional Keywords**:
   - Triggers: "business", "professional", "corporate", "meeting", "presentation"
   - Backgrounds: bg4.jpg, bg5.jpg (corporate style)

2. **Technology/Digital Keywords**:
   - Triggers: "technology", "digital", "platform", "software", "app", "online"
   - Backgrounds: bg2.png, bg3.png (tech theme)

3. **Analytics/Data Keywords**:
   - Triggers: "analytics", "data", "metrics", "performance", "reporting"
   - Backgrounds: bg3.png (data visualization)

4. **Marketing/Growth Keywords**:
   - Triggers: "marketing", "growth", "campaign", "audience", "conversion"
   - Backgrounds: bg1.jpg (marketing focus)

5. **General Content Keywords**:
   - Triggers: "overview", "introduction", "summary", "conclusion", "features", "benefits"
   - Backgrounds: Various appropriate backgrounds

#### Logo Insertion Rules

**Logos are added to:**
- Content slides (without backgrounds)
- Comparison slides
- Visual content slides (without backgrounds)
- Two-column slides
- Blank slides (without other images)

**Logos are NOT added to:**
- Title slides
- Section header slides
- Metrics dashboard slides
- Slides that already have background images

**Logo Properties:**
- Position: Bottom-right corner (configurable)
- Size: 1x1 inch
- Transparency: 30% (subtle appearance)
- Selection: Random from available FeedMob logos
- Z-order: Sent to back to avoid interference with content

## Color Schemes

### FeedMob Style (NEW)
- **Primary**: Blue (#058DC7)
- **Secondary**: Medium Dark (#158158)
- **Accent1**: Green (#50B432)
- **Accent2**: Orange (#ED561B)
- **Accent3**: Yellow (#EDEF00)
- **Accent4**: Cyan (#24CBE5)
- **Accent5**: Light Green (#64E572)
- **Background**: White (#FFFFFF)
- **Background Alt**: Light Gray (#F3F3F3)
- **Typography**: Arial font family
- **Special Features**: Gradient backgrounds, custom accent bars, intelligent background/logo system

### Binance Style
- **Primary**: Dark Blue (#0E2841)
- **Secondary**: Light Gray (#E8E8E8)
- **Accent1**: Medium Blue (#156082)
- **Accent2**: Orange (#E97132)
- **Accent3**: Green (#196B24)
- **Accent4**: Light Blue (#0F9ED5)
- **Accent5**: Purple (#A02B93)
- **Typography**: Arial font family

### Professional
- **Primary**: Dark Blue (#0E2841)
- **Secondary**: Light Gray (#E8E8E8)
- **Accent**: Teal (#00B5AD)

### Modern
- **Primary**: Medium Blue
- **Secondary**: Very Light Gray
- **Accent**: Orange (#E97132)

## Tips and Best Practices

1. **Plan your structure first**: Define all slides before adding detailed content
2. **Use appropriate slide types**:
   - `title` with `professional_style: true` for corporate title slides
   - `visual_content` for slides with images and bullet points
   - `metrics_dashboard` for KPI and data presentations
   - `comparison` for side-by-side comparisons
   - `content` for traditional bullet point slides
3. **Keep text concise**: Slides should have clear, brief content
4. **Test image paths**: Ensure all image files exist before running the script
5. **Use JSON for complex presentations**: JSON format is more flexible for detailed presentations
6. **Choose Binance scheme for corporate presentations**: Best matches professional standards
7. **Leverage the metrics dashboard**: Perfect for financial and business reviews

## Error Handling

The script handles common errors gracefully:

- **Missing python-pptx**: Shows installation instructions
- **Invalid JSON**: Displays JSON parsing errors
- **Missing image files**: Shows warning but continues
- **Invalid file paths**: Provides clear error messages
