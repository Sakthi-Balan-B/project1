import csv
from collections import Counter

# Define the list to store programming languages
languages = []
path = r'D:\Sakthi_the_mass\IITM\TDS\Project1\pro1 (1)\repositories.csv'

# Read the CSV file with UTF-8 encoding
with open(path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Get and clean up the language field (ignore empty values)
        language = row.get('language', '').strip()
        if language:
            languages.append(language)

# Count the occurrence of each language
language_counts = Counter(languages)

# Find the most common language
most_common_language = language_counts.most_common(1)

# Print the result
if most_common_language:
    print(most_common_language[0][0])
else:
    print("No language data found.")
