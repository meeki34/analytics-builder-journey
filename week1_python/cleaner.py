import pandas as pd
<<<<<<< HEAD
from pathlib import Path
from datetime import datetime

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
LOG_FILE = Path("cleaning_log.txt")

OUTPUT_DIR.mkdir(exist_ok=True)
log_lines = []

log_lines.append(f"\n=== Cleaning Run: {datetime.now()} ===")

excel_files = list(INPUT_DIR.glob("*.xlsx"))

if not excel_files:
    print(f"No Excel files found in {INPUT_DIR.resolve()}")
else:
    for file_path in excel_files:
        print(f"\n--- Cleaning: {file_path.name} ---")
        log_lines.append(f"\nFile: {file_path.name}")
        
        df = pd.read_excel(file_path)
        original_rows = len(df)
        print(f"Original rows: {original_rows}")
        log_lines.append(f"Original rows: {original_rows}")

        # Clean logic
        if 'Merchant' in df.columns:
            df['Merchant'] = df['Merchant'].astype(str).str.strip().str.title()
        
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        before_dedup = len(df)
        df = df.drop_duplicates()
        removed = before_dedup - len(df)
        
        print(f"Removed {removed} duplicates")
        log_lines.append(f"Removed {removed} duplicates")
        
        output_path = OUTPUT_DIR / f"cleaned_{file_path.name}"
        df.to_excel(output_path, index=False)
        
        print(f"Saved to: {output_path}")
        print(f"Final rows: {len(df)}")
        log_lines.append(f"Final rows: {len(df)}")
        log_lines.append(f"Saved to: {output_path}")

# Save log
with open(LOG_FILE, "a") as f:
    f.write("\n".join(log_lines) + "\n")

print(f"\nDONE! Cleaned {len(excel_files)} file(s). Log saved to {LOG_FILE}")
=======
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
>>>>>>> master
