def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt (E) or decrypt (D) a message? (E/D): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (an integer): "))
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
