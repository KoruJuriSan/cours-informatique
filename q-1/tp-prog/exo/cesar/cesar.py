import math

def get_alpha_order(letter: str):
    return ord(letter)-64

def get_ascii_of_alpha_order(alpha_order: int):
    return alpha_order + 64

def cesar(word: str = "", space: int = 1):
    new_word = ""
    for letter in word:
        if (letter.isalpha()):
            letter_order = get_alpha_order(letter)
            nb_letter_in_alpha = 26 
            assert  1 <= letter_order <= nb_letter_in_alpha
            letter_order += space
            letter_order -= nb_letter_in_alpha*(math.ceil(letter_order / nb_letter_in_alpha)-1)
            new_word += chr(get_ascii_of_alpha_order(letter_order))
        else:
            new_word += letter
    return new_word

word = input("Enter the text to transform: ").upper()
spacing = -1
while spacing < 0:
    try:
        spacing = int(input("Enter the spacing of the cesar code: "))
    except:
        pass
print(cesar(word, spacing))