# place your code to clean up the data file below.

import os

def clean_data(input_path, output_path):
    data_folder = 'data'  # Relative path to the data directory from the script's location
    input_path = os.path.join(data_folder, input_path)
    output_path = os.path.join(data_folder, output_path)
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Initialize variables to track the column headers and whether they've been written
        column_headers = None
        headers_written = False
        cleaned_lines = []

        for line in lines:
            # Check if the line is a note (customize this based on your data's note format)
            if line.startswith('#') or line.strip() == '':
                continue  # Skip note lines and blank lines

            # Replace missing data indicators
            cleaned_line = line.replace('*', '0').replace('NA', '0').strip()

            # Check for column headers
            if 'Column1' in cleaned_line:  # Assuming 'Column1' is part of your column headers
                if not headers_written:
                    column_headers = cleaned_line
                    headers_written = True
                    cleaned_lines.append(column_headers + '\n')  # Write headers only once
            else:
                cleaned_lines.append(cleaned_line + '\n')

        # Write the cleaned data to a new file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.writelines(cleaned_lines)

        print(f'Cleaned data saved to {output_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Define the input and output paths
input_path = 'HIV_AIDS_Diagnoses_by_Neighborhood__Sex__and_Race_Ethnicity_20240219.csv'
output_path = 'clean_data.csv'


# Call the function to clean the data
clean_data(input_path, output_path)