def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


try:
    message = input("Enter the message: ")
    shift = int(input("Enter shift value: "))
    choice = input("Type encrypt or decrypt: ").lower()

    print("Result:", caesar_cipher(message, shift, choice))

except:
    print("Invalid input. Please enter correct values.")