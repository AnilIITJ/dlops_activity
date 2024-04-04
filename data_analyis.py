import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data, roll_number):
    """Perform basic data analysis based on roll number."""
    if data is not None:
        if roll_number % 2 == 0:
            # Check for missing values
            missing_values = data.isnull().sum()
            if missing_values.any():
                print("Missing values found in the following columns:")
                print(missing_values[missing_values > 0])
            else:
                print("No missing values found.")
        else:
            # Encoding categorical values
            # Assuming 'Class' is the categorical column to be encoded
            if 'Class' in data.columns:
                data['Class'] = data['Class'].astype('category').cat.codes
                print("Categorical values in 'Class' column have been encoded.")
            else:
                print("No 'Class' column found for encoding.")

        # Rest of the analysis...

    """Perform basic data analysis."""
    if data is not None:
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()

def main():
    roll_number = int(input("Enter your roll number: "))
    file_path = input("Enter the path to the Excel file: ")
    data = load_data(file_path)
    analyze_data(data, roll_number)

if __name__ == "__main__":
    main()
