import ecmwflibs
import eccodes
import cfgrib
import pandas as pd

def extract_data(file_path):
    # Open GRIB2 file
    with cfgrib.open_dataset(file_path) as ds:
        # Extract relevant information
        date_time = ds.time.values  # Assuming there is a time variable in the dataset
        topography = ds['Topography'].values  # Replace 'Topography' with the actual variable name
        amount_of_rain = ds['Amount_of_Rain'].values  # Replace 'Amount_of_Rain' with the actual variable name

    # Create a pandas DataFrame
    df = pd.DataFrame({
        'Date/Time': date_time,
        'Topography': topography,
        'Amount_of_Rain': amount_of_rain,
        # Add more columns as needed
    })

    # Convert time to a human-readable format if needed
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])

    return df

if __name__ == "__main__":
    file_path = 'your_file.grib2'  # Replace with the actual path to your GRIB2 file
    output_csv = 'output.csv'

    # Extract data
    data_frame = extract_data(file_path)

    # Save DataFrame to CSV file
    data_frame.to_csv(output_csv, index=False)
