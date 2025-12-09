#!/usr/bin/env python3
"""Convert AUTOMATED-SCORES.csv to formatted Excel file."""

import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from collections import defaultdict

# File paths
CSV_PATH = "/home/user/GitHub-CDM-Research/Research Documentation/AUTOMATED-SCORES.csv"
EXCEL_PATH = "/home/user/GitHub-CDM-Research/Research Documentation/AUTOMATED-SCORES.xlsx"

# Style definitions
HEADER_FILL = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
TIER_S_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
TIER_A_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
MANUAL_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
EXCLUDED_FILL = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def read_csv():
    """Read and parse the CSV file."""
    rows = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        for row in reader:
            if len(row) >= 17:
                rows.append(row)
    return headers, rows

def extract_filename(path):
    """Extract just the filename from a path."""
    return path.split('/')[-1] if '/' in path else path

def parse_score(val):
    """Safely parse a score value."""
    try:
        return int(val) if val and val.strip() else 0
    except (ValueError, TypeError):
        return 0

def create_all_files_sheet(wb, headers, rows):
    """Create the main 'All Files' sheet with all data."""
    ws = wb.active
    ws.title = "All Files"

    # Simplified headers for readability
    display_headers = [
        "File Name", "Full Path", "Type", "Tier", "Category", "Status",
        "Banks", "Prod", "Quant", "Strategic", "Regulatory", "Recent",
        "Impl", "Asset Class", "Smart Contract", "Training", "Raw Score", "Priority"
    ]

    # Write headers
    for col, header in enumerate(display_headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = THIN_BORDER

    # Sort rows by raw_score descending
    sorted_rows = sorted(rows, key=lambda x: parse_score(x[15] if len(x) > 15 else '0'), reverse=True)

    # Write data rows
    for row_idx, row in enumerate(sorted_rows, 2):
        # Extract filename and prepare data
        filename = extract_filename(row[0])
        data = [filename, row[0]] + row[1:]

        for col_idx, value in enumerate(data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.border = THIN_BORDER
            cell.alignment = Alignment(vertical='center')

            # Apply number format to score columns
            if col_idx >= 7 and col_idx <= 17:
                try:
                    cell.value = int(value) if value and value.strip() else 0
                except (ValueError, TypeError):
                    pass

        # Apply row coloring based on priority
        priority = row[16] if len(row) > 16 else ""
        fill = None
        if priority == "S":
            fill = TIER_S_FILL
        elif priority == "A":
            fill = TIER_A_FILL
        elif priority == "MANUAL_REVIEW":
            fill = MANUAL_FILL
        elif priority == "EXCLUDED":
            fill = EXCLUDED_FILL

        if fill:
            for col_idx in range(1, len(data) + 1):
                ws.cell(row=row_idx, column=col_idx).fill = fill

    # Auto-fit column widths
    column_widths = [40, 80, 6, 6, 20, 20, 8, 8, 8, 10, 12, 8, 8, 12, 14, 10, 10, 10]
    for col_idx, width in enumerate(column_widths, 1):
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    # Freeze header row
    ws.freeze_panes = 'A2'

    return ws

def create_summary_sheet(wb, rows):
    """Create a summary statistics sheet."""
    ws = wb.create_sheet("Summary", 0)

    # Calculate statistics
    stats = defaultdict(int)
    tier_counts = defaultdict(int)
    category_counts = defaultdict(int)
    exclusion_counts = defaultdict(int)

    for row in rows:
        priority = row[16] if len(row) > 16 else "UNKNOWN"
        category = row[3] if len(row) > 3 else "UNKNOWN"
        exclusion = row[4] if len(row) > 4 else "UNKNOWN"

        tier_counts[priority] += 1
        category_counts[category] += 1
        if exclusion != "INCLUDE":
            exclusion_counts[exclusion] += 1

    # Title
    ws.cell(row=1, column=1, value="CDM Research Documentation - Scoring Summary")
    ws.cell(row=1, column=1).font = Font(bold=True, size=16)
    ws.merge_cells('A1:D1')

    # Total files
    ws.cell(row=3, column=1, value="Total Files:")
    ws.cell(row=3, column=2, value=len(rows))
    ws.cell(row=3, column=1).font = Font(bold=True)

    # Priority tier breakdown
    ws.cell(row=5, column=1, value="Priority Tier Breakdown")
    ws.cell(row=5, column=1).font = Font(bold=True, size=12)

    tier_order = ["S", "A", "B", "C", "D", "MANUAL_REVIEW", "EXCLUDED"]
    tier_labels = {
        "S": "Tier S (Score 100+)",
        "A": "Tier A (Score 50-99)",
        "B": "Tier B (Score 20-49)",
        "C": "Tier C (Score 5-19)",
        "D": "Tier D (Score <5)",
        "MANUAL_REVIEW": "PDFs (Manual Review)",
        "EXCLUDED": "Excluded"
    }

    row_num = 6
    for tier in tier_order:
        if tier_counts.get(tier, 0) > 0:
            ws.cell(row=row_num, column=1, value=tier_labels.get(tier, tier))
            ws.cell(row=row_num, column=2, value=tier_counts.get(tier, 0))
            row_num += 1

    # Category breakdown
    row_num += 1
    ws.cell(row=row_num, column=1, value="Category Breakdown")
    ws.cell(row=row_num, column=1).font = Font(bold=True, size=12)
    row_num += 1

    for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        ws.cell(row=row_num, column=1, value=category)
        ws.cell(row=row_num, column=2, value=count)
        row_num += 1

    # Exclusion reasons
    if exclusion_counts:
        row_num += 1
        ws.cell(row=row_num, column=1, value="Exclusion Reasons")
        ws.cell(row=row_num, column=1).font = Font(bold=True, size=12)
        row_num += 1

        for reason, count in sorted(exclusion_counts.items(), key=lambda x: -x[1]):
            ws.cell(row=row_num, column=1, value=reason)
            ws.cell(row=row_num, column=2, value=count)
            row_num += 1

    # Legend
    row_num += 2
    ws.cell(row=row_num, column=1, value="Color Legend")
    ws.cell(row=row_num, column=1).font = Font(bold=True, size=12)
    row_num += 1

    legend = [
        ("Tier S (Priority)", TIER_S_FILL),
        ("Tier A (High)", TIER_A_FILL),
        ("Manual Review", MANUAL_FILL),
        ("Excluded", EXCLUDED_FILL),
    ]

    for label, fill in legend:
        ws.cell(row=row_num, column=1, value=label)
        ws.cell(row=row_num, column=1).fill = fill
        row_num += 1

    # Set column widths
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 15

    return ws

def create_priority_sheet(wb, rows, priority, title):
    """Create a sheet filtered by priority."""
    filtered = [r for r in rows if len(r) > 16 and r[16] == priority]
    if not filtered:
        return None

    ws = wb.create_sheet(title)

    # Headers
    headers = ["File Name", "Tier", "Category", "Banks", "Prod", "Quant", "Strategic",
               "Regulatory", "Recent", "Impl", "Asset Class", "Smart Contract", "Raw Score"]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal='center', wrap_text=True)
        cell.border = THIN_BORDER

    # Sort by raw_score descending
    sorted_rows = sorted(filtered, key=lambda x: parse_score(x[15] if len(x) > 15 else '0'), reverse=True)

    # Write data
    for row_idx, row in enumerate(sorted_rows, 2):
        data = [
            extract_filename(row[0]),  # filename
            row[2],  # tier
            row[3],  # category
            parse_score(row[5]),   # banks
            parse_score(row[6]),   # production
            parse_score(row[7]),   # quant
            parse_score(row[8]),   # strategic
            parse_score(row[9]),   # regulatory
            parse_score(row[10]),  # recent
            parse_score(row[11]),  # impl
            parse_score(row[12]),  # asset_class
            parse_score(row[13]),  # smart_contract
            parse_score(row[15]),  # raw_score
        ]

        for col_idx, value in enumerate(data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.border = THIN_BORDER

    # Column widths
    widths = [50, 8, 20, 8, 8, 8, 10, 12, 8, 8, 12, 14, 10]
    for col_idx, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    ws.freeze_panes = 'A2'
    return ws

def main():
    """Main function to create the Excel file."""
    print("Reading CSV file...")
    headers, rows = read_csv()
    print(f"Found {len(rows)} rows")

    print("Creating Excel workbook...")
    wb = Workbook()

    # Create sheets
    create_all_files_sheet(wb, headers, rows)
    create_summary_sheet(wb, rows)
    create_priority_sheet(wb, rows, "S", "Tier S - Must Read")
    create_priority_sheet(wb, rows, "MANUAL_REVIEW", "PDFs - Manual Review")
    create_priority_sheet(wb, rows, "EXCLUDED", "Excluded Files")

    # Save workbook
    print(f"Saving to {EXCEL_PATH}...")
    wb.save(EXCEL_PATH)
    print("Done!")

if __name__ == "__main__":
    main()
