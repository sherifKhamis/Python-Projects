# Basic Python program that encodes and decodes with the caesar cypher algorithm

mode = input("Type 'Encode' to encrypt or 'Decode' to decrypt: ")
message = input("Input your message you want to encrypt or decrypt: ").lower()
shift_no = int(input("Type the shift number: "))
ordered_alphabet = "abcdefghijklmnopqrstuvwxyz" * shift_no
result = ""

if mode == "Encode":
    for letter in message:
        result += ordered_alphabet[ordered_alphabet.index(letter) + shift_no]
elif mode == "Decode":
    for letter in message:
        result += ordered_alphabet[ordered_alphabet.index(letter) - shift_no]

print(result)

