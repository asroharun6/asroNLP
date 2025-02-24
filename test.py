from asronlp import AsroNLP  # Adjust the import statement according to your file and class name

def main():
    # Create an instance of AsroNLP
    nlp_processor = AsroNLP()

    # Define the path to your input Excel file
    input_path = 'dataset.xlsx'  # Update this path as needed

    # Define the output file path
    output_path = 'output.xlsx'  # This will be the path for the processed data

    # Run the preprocessing and analysis function
    result_df = nlp_processor.preprocess_and_optionally_stem_and_analyze(input_path, output_path=output_path)

    # Optionally, print or handle the result DataFrame
    if result_df is not None:
        print(result_df.head())  # Preview the first few rows of the processed DataFrame

if __name__ == "__main__":
    main()
