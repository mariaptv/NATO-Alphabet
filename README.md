## **NATO Phonetic Alphabet Converter**

### **Purpose:**

This Python script converts a given word into its corresponding NATO phonetic alphabet equivalent. It uses a Pandas DataFrame to store the letter-to-code mapping from a CSV file.

### **How to Use:**

1. **Install Required Libraries:**
   - Ensure you have `pandas` installed. You can install it using pip:
     ```bash
     pip install pandas
     ```

2. **Prepare the CSV File:**
   - Create a CSV file named `nato_phonetic_alphabet.csv` with two columns: `letter` and `code`. Each row should contain a letter and its corresponding NATO phonetic code.

3. **Run the Script:**
   - Execute the Python script.
   - You will be prompted to enter a word.
   - The script will output the NATO phonetic equivalent of the entered word.

### **Code:**

```python
import pandas as pd

# Load the NATO phonetic alphabet data from the CSV file
student_data_frame = pd.read_csv(r"C:\Users\maria\Documents\proyectos python\NATO-Alphabet\nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to their NATO codes
words_new = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

# Get user input and convert it to uppercase
word = input("What do you want us to spell?").upper()

# Convert the word to its NATO phonetic equivalent
result = [words_new.get(w) for w in word]

# Print the result
print(result)
