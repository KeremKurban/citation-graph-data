import pandas as pd
import sys
import os

def clean_data(input_path, output_format='csv'):
    # Determine input format from the file extension
    input_format = os.path.splitext(input_path)[1].lower()

    # Load the data based on the input format
    if input_format == '.json':
        df = pd.read_json(input_path, lines=True)
    else:  # Default to CSV if not JSON
        df = pd.read_csv(input_path)

    # Define the columns to clean
    columns_to_clean = ['title', 'abstract']

    # Replace illegal characters in the specified columns
    for col in columns_to_clean:
        df[col] = df[col].astype(str).str.replace('"', '')  # Remove double quotes
        df[col] = df[col].astype(str).str.replace("'", '')  # Remove single quotes

    # Save the cleaned data in the desired format
    if output_format == 'json':
        df.to_json(input_path.replace('.csv', '.json').replace('.json', '_cleaned.json'), orient='records', lines=True)
    else:
        df.to_csv(input_path.replace('.json', '.csv').replace('.csv', '_cleaned.csv'), index=False)

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'csv'
    clean_data(input_path, output_format)

