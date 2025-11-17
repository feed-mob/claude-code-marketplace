# Direct Spend Visualizer Plugin

A Claude Code plugin that provides an Agent Skill for visualizing FeedMob direct spend data as ASCII line charts.

## Features

- 📊 **ASCII Line Charts**: Generate visual spend trend charts directly in your terminal
- 💰 **Dual Metrics**: Display both net spend and gross spend on the same chart
- 📅 **Date Range Analysis**: Visualize spend data across custom date ranges
- 🔢 **Detailed Breakdown**: View comprehensive data tables with daily totals
- 🎯 **Multi-Campaign Support**: Handle multiple click URL IDs simultaneously
- 💵 **USD Currency**: All spend values displayed in USD with proper formatting

## Installation

This plugin is part of the FeedMob Claude Plugins marketplace. It will be automatically available when the plugin is installed.

### Prerequisites

1. **Python 3.6 or higher**
2. **FeedMob MCP Server**: This plugin requires the FeedMob MCP server to be installed and configured

### Environment Configuration

Before using this plugin, you must set the following environment variables:

```bash
export FEEDMOB_KEY=your_feedmob_api_key
export FEEDMOB_SECRET=your_feedmob_api_secret
export FEEDMOB_API_BASE=https://xxx.xxx.xxx
```

You can add these to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) to make them permanent:

```bash
# Add to ~/.bashrc or ~/.zshrc
export FEEDMOB_KEY=your_feedmob_api_key
export FEEDMOB_SECRET=your_feedmob_api_secret
export FEEDMOB_API_BASE=https://xxx.xxx.xxx
```

### MCP Server Configuration

The plugin includes a `.mcp.json` file that configures the FeedMob MCP server. Ensure this is properly loaded in your Claude Code environment.

## Usage

The Direct Spend Visualizer skill will automatically activate when you mention:

- "Show direct spend for click_url 22271"
- "Visualize spend data for the last 30 days"
- "Chart the spending for campaigns"
- "Display spend trends"
- "Show me a chart of direct spend"

## Quick Start Examples

### Example 1: Single Campaign Visualization

**Request:**
```
Show me direct spend for click_url 22271 for the last 7 days
```

**Result:**
- ASCII line chart showing net and gross spend trends
- Detailed data table with daily breakdown
- Total spend summary

### Example 2: Multiple Campaigns

**Request:**
```
Visualize direct spend for click_urls 22271, 22272, and 22273 from 2025-11-01 to 2025-11-14
```

**Result:**
- Separate chart for each click URL ID
- Comparative spend analysis
- Individual totals for each campaign

### Example 3: Custom Date Range

**Request:**
```
Chart direct spend for the last 30 days for click_url 22271
```

**Result:**
- Extended timeline visualization
- Month-long spend trend analysis

## How It Works

1. **API Data Retrieval**: Fetches direct spend data using the FeedMob MCP API (`mcp__feedmob__get_direct_spends`)
2. **Data Processing**: Saves API response to temporary JSON file
3. **Visualization**: Executes Python script to generate ASCII charts
4. **Display**: Presents charts, legends, and data tables to the user

## Output Format

The visualization includes:

1. **ASCII Line Chart**
   - Y-axis: Spend values in USD with $ formatting
   - X-axis: Dates
   - N markers: Net Spend data points
   - G markers: Gross Spend data points
   - Automatic scaling based on data range

2. **Legend**
   - Clear explanation of chart symbols
   - Net Spend (N) vs Gross Spend (G)

3. **Data Table**
   - Daily breakdown with dates
   - Net spend and gross spend columns
   - Campaign names
   - Total spend summary
   - All values in USD currency

## Script Reference

### visualize_direct_spend.py

**Location:** `skills/scripts/visualize_direct_spend.py`

**Usage:**
```bash
# From file
python scripts/visualize_direct_spend.py /tmp/direct_spend_data.json

# From stdin
cat data.json | python scripts/visualize_direct_spend.py
echo '{"data": [...]}' | python scripts/visualize_direct_spend.py
```

**Input Format:**
```json
{
  "status": 200,
  "data": [
    {
      "feedmob_click_url_id": 22271,
      "campaign_name": "Campaign Name",
      "date": "2025-11-07",
      "feedmob_net_spend": 119.92,
      "feedmob_gross_spend": 78.00
    }
  ]
}
```

**Features:**
- Handles multiple click URL IDs
- Automatic chart scaling
- Both net and gross spend visualization
- Detailed numeric breakdown
- Summary statistics

## API Integration

This plugin uses the FeedMob MCP API to retrieve direct spend data:

**Tool:** `mcp__feedmob__get_direct_spends`

**Parameters:**
- `start_date`: Start date in YYYY-MM-DD format
- `end_date`: End date in YYYY-MM-DD format  
- `click_url_ids`: Array of click URL IDs (as strings)

**Example Call:**
```json
{
  "start_date": "2025-11-07",
  "end_date": "2025-11-14",
  "click_url_ids": ["22271", "22272"]
}
```

## Best Practices

1. **Date Ranges**: For large date ranges, consider breaking into smaller periods for better visualization
2. **Multiple Campaigns**: The script automatically creates separate charts for each click URL ID
3. **Data Availability**: If no data is returned, verify the date range and click URL IDs are correct
4. **Currency**: All spend values are in USD and displayed with $ symbol
5. **Format Consistency**: Always use YYYY-MM-DD date format

## Troubleshooting

### Environment Variables Not Set

**Problem:** Plugin cannot connect to FeedMob API

**Solution:** Ensure environment variables are properly exported:
```bash
export FEEDMOB_KEY=your_key
export FEEDMOB_SECRET=your_secret
export FEEDMOB_API_BASE=https://api.feedmob.com
```

Verify they are set:
```bash
echo $FEEDMOB_KEY
echo $FEEDMOB_SECRET
echo $FEEDMOB_API_BASE
```

### No Data Returned

**Problem:** API returns empty data set

**Possible Causes:**
- Invalid click URL IDs
- Date range outside available data
- Authentication issues

**Solution:** 
- Verify click URL IDs are correct
- Check date range is valid
- Confirm API credentials are correct

### Script Execution Error

**Problem:** Python script fails to run

**Solution:**
```bash
# Check Python version
python --version  # Should be 3.6 or higher

# Test script directly
python plugins/direct-spend-visualizer/skills/scripts/visualize_direct_spend.py --help
```

### Chart Display Issues

**Problem:** Chart appears malformed or unreadable

**Possible Causes:**
- Terminal width too narrow
- Too many data points for date range

**Solution:**
- Increase terminal width
- Reduce date range for better visualization
- Use smaller subsets of data

## Skill Details

- **Name**: `direct-spend-visualizer`
- **Version**: 1.0.0
- **Tools**: Read, Write, Bash, Task
- **Language**: Python 3.6+
- **Dependencies**: FeedMob MCP Server
- **MCP Tools**: `mcp__feedmob__get_direct_spends`

## Contributing

Improvements to this plugin are welcome! You can:
- Add support for additional chart types
- Enhance visualization formatting
- Add export capabilities (CSV, PNG, etc.)
- Improve data aggregation options
- Add support for more metrics
- Provide feedback and suggestions

## Documentation

- [SKILL.md](skills/SKILL.md) - Detailed skill documentation
- [.mcp.json](.mcp.json) - MCP server configuration

## License

MIT

## Support

For issues or questions:
- Contact: dev@feedmob.com
- FeedMob Documentation: https://feedmob.com/docs
