import pandas as pd
import os

# Folder where your CSVs are stored
data_folder = "data/bronze"

# Loop through all CSV files in the folder
for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(data_folder, file_name)
        try:
            # StatCan CSVs usually have metadata rows at the top.
            # Adjust header row if needed (here assuming header is row 12 → index 11).
            df = pd.read_csv(file_path, header=11)

            print(f"\n✅ File: {file_name}")
            print("--- Columns ---")
            print(df.columns.tolist())

            print("\n--- First 5 Rows ---")
            print(df.head())

        except Exception as e:
            print(f"\n Could not read {file_name}: {e}")
# This script reads all CSV files in the specified folder,
# prints their column names and the first 5 rows of each file.