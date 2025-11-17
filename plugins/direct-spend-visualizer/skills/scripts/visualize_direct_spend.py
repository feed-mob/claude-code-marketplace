#!/usr/bin/env python3
"""
Visualize direct spend data from FeedMob API as line charts.

This script takes JSON data from the FeedMob get_direct_spends API and creates
line charts showing net_spend and gross_spend over time for one or more click URLs.
All spend values are displayed in USD currency.
"""

import json
import sys
from datetime import datetime
from collections import defaultdict


def parse_direct_spend_data(data):
    """Parse direct spend data and organize by click URL ID."""
    spend_by_url = defaultdict(list)

    for record in data:
        click_url_id = record['feedmob_click_url_id']
        spend_by_url[click_url_id].append({
            'date': record['date'],
            'net_spend': record['feedmob_net_spend'],
            'gross_spend': record['feedmob_gross_spend'],
            'campaign_name': record.get('campaign_name', 'Unknown')
        })

    # Sort each URL's data by date
    for url_id in spend_by_url:
        spend_by_url[url_id].sort(key=lambda x: x['date'])

    return spend_by_url


def create_ascii_line_chart(data, title, width=60, height=15):
    """Create an ASCII line chart for the given data."""
    if not data:
        return "No data to display"

    dates = [record['date'] for record in data]
    net_spends = [record['net_spend'] for record in data]
    gross_spends = [record['gross_spend'] for record in data]

    # Find min and max values for scaling
    all_values = net_spends + gross_spends
    min_val = min(all_values)
    max_val = max(all_values)

    if max_val == min_val:
        max_val = min_val + 1  # Avoid division by zero

    # Create the chart
    chart = []
    chart.append("\n" + "=" * width)
    chart.append(title.center(width))
    chart.append("=" * width)
    chart.append("")

    # Scale values to chart height
    def scale(value):
        return int((value - min_val) / (max_val - min_val) * (height - 1))

    net_scaled = [scale(v) for v in net_spends]
    gross_scaled = [scale(v) for v in gross_spends]

    # Build the chart from top to bottom
    for row in range(height - 1, -1, -1):
        line = []

        # Y-axis label (in USD)
        value = min_val + (row / (height - 1)) * (max_val - min_val)
        line.append(f"${value:7.2f} |")

        # Plot points
        for i in range(len(dates)):
            if net_scaled[i] == row and gross_scaled[i] == row:
                line.append("*")  # Both at same point
            elif net_scaled[i] == row:
                line.append("N")  # Net spend
            elif gross_scaled[i] == row:
                line.append("G")  # Gross spend
            else:
                line.append(" ")

            if i < len(dates) - 1:
                line.append(" ")

        chart.append("".join(line))

    # X-axis
    chart.append("        +" + "-" * (width - 10))

    # Date labels (show first, middle, and last)
    if len(dates) >= 3:
        date_line = "         "
        date_line += dates[0]
        date_line += " " * (width - len(dates[0]) - len(dates[-1]) - 12)
        date_line += dates[-1]
        chart.append(date_line)
    elif len(dates) > 0:
        chart.append(f"         {dates[0]}")

    chart.append("")
    chart.append("Legend: N = Net Spend, G = Gross Spend, * = Both")
    chart.append("")

    # Data table
    chart.append("Detailed Data (USD):")
    chart.append("-" * width)
    chart.append(f"{'Date':<12} {'Net Spend':>13} {'Gross Spend':>13}")
    chart.append("-" * width)

    total_net = 0
    total_gross = 0

    for i, date in enumerate(dates):
        net = net_spends[i]
        gross = gross_spends[i]
        total_net += net
        total_gross += gross
        chart.append(f"{date:<12} ${net:>12.2f} ${gross:>12.2f}")

    chart.append("-" * width)
    chart.append(f"{'TOTAL':<12} ${total_net:>12.2f} ${total_gross:>12.2f}")
    chart.append("=" * width)

    return "\n".join(chart)


def visualize_direct_spend(json_data):
    """Main function to visualize direct spend data."""
    try:
        # Parse JSON if it's a string
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data

        # Extract the data array
        if isinstance(data, dict) and 'data' in data:
            records = data['data']
        else:
            records = data

        if not records:
            return "No direct spend data found for the specified parameters."

        # Organize data by click URL ID
        spend_by_url = parse_direct_spend_data(records)

        # Create charts for each click URL
        output = []

        for click_url_id, url_data in spend_by_url.items():
            campaign_name = url_data[0]['campaign_name']
            title = f"Click URL #{click_url_id}: {campaign_name}"
            chart = create_ascii_line_chart(url_data, title)
            output.append(chart)

        return "\n\n".join(output)

    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON data - {e}"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r') as f:
            json_data = f.read()
    else:
        # Read from stdin
        json_data = sys.stdin.read()

    result = visualize_direct_spend(json_data)
    print(result)
