"""
This script:-
1. Loads MockDonations.csv
2. Parses donation_date (DD/MM/YYYY)
3. Filters to the last 3 months
4. Finds donors whose total donations > ₹10,000 and writes donors_over_10000.csv
5. Aggregates by city (distinct donors + total amount) and writes city_donation_summary.csv
"""

import os
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd

# 1. Config 
INPUT_CSV         = 'MockDonations.csv'
THRESHOLD_AMOUNT  = 10_000
OUTPUT_TOP_DONORS = 'donors_over_10000.csv'
OUTPUT_BY_CITY    = 'city_donation_summary.csv'

# 1. Check file exists 
if not os.path.isfile(INPUT_CSV):
    print(f"Error: '{INPUT_CSV}' not found.", file=sys.stderr)
    sys.exit(1)

# 2. Load & parse dates 
try:
    df = pd.read_csv(INPUT_CSV)
    # Parse donation_date with day-first format
    df['donation_date'] = pd.to_datetime(df['donation_date'], dayfirst=True)
except Exception as e:
    print(f"Failed to load or parse '{INPUT_CSV}': {e}", file=sys.stderr)
    sys.exit(1)

# 3. Filter to last 3 months
now        = datetime.now()
three_mo_ago = now - relativedelta(months=3)
recent_df  = df[df['donation_date'] >= three_mo_ago].copy()

# 4. Total by donor 
donor_totals = (
    recent_df
    .groupby(['donor_name'], as_index=False)['amount'].sum().rename(columns={'amount': 'TotalAmount'})
)

# 5. Export donors over threshold 
top_donors = donor_totals[donor_totals['TotalAmount'] > THRESHOLD_AMOUNT]
top_donors.to_csv(OUTPUT_TOP_DONORS, index=False)

# 6. Aggregate by city 
city_summary = (
    recent_df
    .groupby('city')
    .agg(
        NumberOfDonors=('donor_name', 'nunique'),
        TotalAmount    =('amount', 'sum')
    )
    .reset_index()
)
city_summary.to_csv(OUTPUT_BY_CITY, index=False)

# 7. Done 
print(f" {len(top_donors)} donors with total >₹{THRESHOLD_AMOUNT} → {OUTPUT_TOP_DONORS}")
print(f" {len(city_summary)} cities summarized → {OUTPUT_BY_CITY}")
