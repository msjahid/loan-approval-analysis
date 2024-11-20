import pandas as pd
import re

# Simulate a dummy dataset if the file doesn't exist
try:
    df = pd.read_csv('../raw/loan_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Creating a dummy dataset for testing...")
    # Creating a dummy dataset
    data = {
        "Loan_ID": ["LP001002", "LP001003", "LP001005"],
        "Gender": ["Male", "Female", None],
        "Married": ["Yes", None, "No"],
        "ApplicantIncome": [5849, 4583, 3000],
        "LoanAmount": [None, 128, 66],
    }
    df = pd.DataFrame(data)

except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    df = None  # Ensure `df` is defined even if file loading fails

# If dataset is created or loaded successfully, proceed with renaming columns
if df is not None:
    # Function to clean and rename columns
    def format_column_name(df):
        # Define a function to format a single column name
        def format_single_column_name(column_name):
            # Check if the column already contains underscores
            if '_' in column_name:
                return column_name  # Return the original column name if it already contains underscores

            # Replace camel case with underscores
            column_name = re.sub(r'(?<!^)(?=[A-Z])', '_', column_name)
            return column_name  # Return the modified column name

        # Apply format_single_column_name function to each column name
        mapped_names = [format_single_column_name(col) for col in df.columns]

        # Create a dictionary mapping original column names to modified column names
        column_mapping = dict(zip(df.columns, mapped_names))

        # Rename columns using the mapping
        df = df.rename(columns=column_mapping)

        # Convert column names to lowercase
        df.columns = df.columns.str.lower()

        return df

    # Apply the column renaming function
    df = format_column_name(df)

    # Handle missing values
    for column in df.columns:
        try:
            # Fill missing values with the mode (most frequent value) for each column
            df[column].fillna(df[column].mode()[0], inplace=True)
        except Exception as e:
            print(f"Error processing column '{column}': {e}")

    # Save the updated CSV file
    try:
        updated_file_path = '../raw/cleaned_data.csv'
        df.to_csv(updated_file_path, index=False)
        print(f"Updated dataset saved successfully at {updated_file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the updated dataset: {e}")
