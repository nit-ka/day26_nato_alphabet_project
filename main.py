import pandas

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#
# # Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}


def change_into_phonetic_code_word():
    user_input = input("Enter a word: ").upper()
    try:
        code_words_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        change_into_phonetic_code_word()
    else:
        print(code_words_list)


change_into_phonetic_code_word()