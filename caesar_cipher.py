# Day 8
LOGO = (
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)


def shift_symbol(symbol, shift, is_encrypt):
    symbol_ascii = ord(symbol)
    new_symbol_ascii = symbol_ascii
    # Positive Shift if Encrypt
    if is_encrypt:
        new_symbol_ascii += shift
    # Negative Shift if Decrypt
    else:
        new_symbol_ascii -= shift

    # Capital Letters Wrap Around Positive Shift
    if new_symbol_ascii > 90 and 65 <= symbol_ascii <= 90:
        new_symbol_ascii = 64 + (new_symbol_ascii - 90)
        return chr(new_symbol_ascii)
    # Capital Letters Wrap Around Negative Shift
    elif new_symbol_ascii < 65 and 65 <= symbol_ascii <= 90:
        new_symbol_ascii = (new_symbol_ascii - 65) + 91
        return chr(new_symbol_ascii)

    # Lowercase Letters Wrap Around Positive Shift
    if new_symbol_ascii > 122 and 97 <= symbol_ascii <= 122:
        new_symbol_ascii = 96 + (new_symbol_ascii - 122)
        return chr(new_symbol_ascii)
    # Lowercase Letters Wrap Around Negative Shift
    elif new_symbol_ascii < 97 and 97 <= symbol_ascii <= 122:
        new_symbol_ascii = (new_symbol_ascii - 97) + 123
        return chr(new_symbol_ascii)

    # Capital Letters and Lowercase Letters No Wrap Around
    if 65 <= symbol_ascii <= 90 or 97 <= symbol_ascii <= 122:
        return chr(new_symbol_ascii)

    # Symbols
    return symbol


def caesar_cipher(text, shift, direction):
    new_text = ""
    is_encrypt = direction == "encode"

    for symbol in text:
        new_text += shift_symbol(symbol, shift, is_encrypt)

    if is_encrypt:
        print(f"The encoded text is: {new_text}\n")
    else:
        print(f"The decoded text is: {new_text}\n")


def main():
    print(LOGO)
    continue_program = True
    while continue_program:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
        if direction != "encode" and direction != "decode":
            print("Invalid Argument: Expected 'encode' or 'decode'.")
            continue

        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n")) % 26
        caesar_cipher(text, shift, direction)

        result = input("Would you like to continue? 'Yes' or 'No'\n").lower()
        continue_program = result != "no"

    print("Goodbye")


if __name__ == "__main__":
    main()
