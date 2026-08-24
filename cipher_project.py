# The strip and upper makes it so that there wont be errors when matching cases
choice = input('Pick a cipher; Caesar, Atbash or Wingding? ').strip().upper()
decision = input('Encrypt or Decrypt? ').strip().upper()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cipher():
    text = input('Enter text to cipher: ')
    match choice:
        case 'CAESAR':
            shift1 = int(input('Shift? ').strip())
            return caesar(shift1, text)
        case 'ATBASH':
            return atbash(text)
        case 'WINGDING':
            return wingding(text)

def caesar(shift2, text): # The encrypt boolean can be determed by other functions (below)

    if not 1 <= shift2 <= 25:
        return 'Shift must be an integer between 1 and 25'

    if decision == 'DECRYPT': # Checks if its decrypt, then reverses the shift
        shift2 = -shift2
    
    shifted_alphabet = alphabet[shift2:] + alphabet[:shift2]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    ciphered_text = text.translate(translation_table)
    return ciphered_text

def atbash(text):

    shifted_alphabet = 'zyxwvutsrqponmlkjihgfedcba'

    if decision == 'DECRYPT':
        translation_table = str.maketrans(shifted_alphabet + shifted_alphabet.upper(), alphabet + alphabet.upper())
    else: translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    ciphered_text = text.translate(translation_table)
    return ciphered_text

def wingding(text):

    shifted_alphabet = '♋︎♌︎♍︎♎︎♏︎♐︎♑︎♒︎♓︎🙰🙵●︎❍︎■︎□︎◻︎❑︎❒︎⬧︎⧫︎◆︎❖︎⬥︎⌧︎⍓︎⌘︎'
    shifted_alphabet_upper = '✌︎👌︎👍︎👎︎☜︎☞︎☝︎☟︎✋︎☺︎😐︎☹︎💣︎☠︎⚐︎🏱︎✈︎☼︎💧︎❄︎🕆︎✞︎🕈︎✠︎✡︎☪︎'

    if decision == 'DECRYPT':
        translation_table = str.maketrans(shifted_alphabet + shifted_alphabet_upper, alphabet + alphabet.upper())
    else: translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet_upper)

    ciphered_text = text.translate(translation_table)
    return ciphered_text
print(cipher())