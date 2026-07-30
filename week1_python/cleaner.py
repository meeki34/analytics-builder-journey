import pandas as pd
import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

# Make sure folders exist
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

def clean_file(input_path):
    print(f"\n--- Cleaning: {input_path.name} ---")
    df = pd.read_excel(input_path)
    print(f"Original rows: {len(df)}")

    # 1. Clean Merchant
    if 'Merchant' in df.columns:
        df['Merchant'] = df['Merchant'].astype(str).str.strip().str.lower()

    # 2. Fix Date
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 3. Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before - after} duplicates")

    # 4. Save
    output_path = OUTPUT_DIR / f"cleaned_{input_path.name}"
    df.to_excel(output_path, index=False)
    print(f"Saved to: {output_path}")
    print(f"Final rows: {len(df)}")
    return output_path

# Main loop - cleans ALL Excel files in input/
files = list(INPUT_DIR.glob("*.xlsx")) + list(INPUT_DIR.glob("*.xls"))

if not files:
    print(f"No Excel files found in {INPUT_DIR}")
    print("Drop your dirty Excel files there!")
else:
    for file in files:
        clean_file(file)
    print(f"\nDONE! Cleaned {len(files)} file(s). Check output folder.")