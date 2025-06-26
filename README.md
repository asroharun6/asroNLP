
# AsroNLP

AsroNLP is a comprehensive Python library designed for text preprocessing, stemming, and sentiment analysis, specifically tailored for Bahasa Indonesia.

## Features

- **Text Cleaning**: Removes unnecessary characters and formats text.
- **Tokenization**: Splits text into individual words or tokens.
- **Stopword Removal**: Filters out common words that may not be useful in analysis.
- **Text Normalization**: Converts words to their base or root form.
- **Stemming**: Reduces words to their stem forms.
- **Sentiment Analysis**: Analyzes text to determine the sentiment as positive, negative, or neutral.

## Installation

To install AsroNLP, run the following command:

```bash
pip install AsroNLP==0.1.3

pip install nltk pandas openpyxl matplotlib swifter rich wordcloud Sastrawi packaging

latest one
pip install AsroNLP==0.1.18

make it Pyhton
from asro_nlp import AsroNLP
import nltk
nltk.download('punkt')
# nltk.download('popular')
# nltk.download()

# Create an instance of AsroNLP
nlp = AsroNLP()
# Specify the path to your input file and output file
input_path = 'input.xlsx'  # Sesuaikan dengan path file input Anda
output_path = 'output.xlsx'  # Sesuaikan dengan path file output Anda
# Process the data
try:
    nlp.preprocess_and_analyze(input_path, output_path)
    print("Data has been processed and saved successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

