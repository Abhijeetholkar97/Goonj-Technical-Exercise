import requests
import csv
import sys

# 1. Configuration 
URL = "https://mocki.io/v1/db20b606-ab10-48f9-9e58-9e3102c7c3cd"
OUTPUT_CSV = "low_quantity_report.csv"

# 2.  Fetch Data 
try:
    resp = requests.get(URL)
    resp.raise_for_status()
    items = resp.json()
except requests.RequestException as e:
    print(f"Error fetching data from {URL}: {e}", file=sys.stderr)
    sys.exit(1)

# 3. Filter Items 
low_qty_items = [itm for itm in items if itm.get("quantity", 0) < 50]

# 4. Write CSV Report 
with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Header row
    writer.writerow(["item_id", "item_name", "quantity", "location"])
    # Data rows
    for itm in low_qty_items:
        writer.writerow([
            itm.get("item_id", ""),
            itm.get("item_name", ""),
            itm.get("quantity", ""),
            itm.get("location", "")
        ])

print(f"Report generated: {OUTPUT_CSV}")
