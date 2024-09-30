student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
    #Access key and value

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

words_dict =  pandas.read_csv(r"C:\Users\maria\Documents\proyectos python\NATO-Alphabet\nato_phonetic_alphabet.csv")
words_data_frame = pandas.DataFrame(words_dict)

words_new= {row.letter: row.code for (index, row) in words_data_frame.iterrows()}



word = input("What do you want us to spell?")

result=[words_new.get(w) for w in word]

print(result)