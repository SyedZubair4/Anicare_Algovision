def caesar_cipher_encrypt(text, shift):
    """
    Encrypts a given text using Caesar cipher with a specified shift.

    :param text: The plaintext to be encrypted.
    :param shift: The number of shifts to apply to the plaintext.
    :return: The encrypted ciphertext.
    """
    encrypted_text = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char in alpha:
            index = (alpha.index(char) + shift) % 26
            encrypted_text += alpha[index]
        elif char.upper() in alpha.upper():
            index = (alpha.upper().index(char.upper()) + shift) % 26
            encrypted_text += alpha.upper()[index]
        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts a given ciphertext using Caesar cipher with a specified shift.

    :param ciphertext: The ciphertext to be decrypted.
    :param shift: The number of shifts applied to the plaintext during encryption.
    :return: The decrypted plaintext.
    """
    decrypted_text = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for char in ciphertext:
        if char in alpha:
            index = (alpha.index(char) - shift) % 26
            if index < 0:
                index += 26
            decrypted_text += alpha[index]
        elif char.upper() in alpha.upper():
            index = (alpha.upper().index(char.upper()) - shift) % 26
            if index < 0:
                index += 26
            decrypted_text += alpha.upper()[index]
        else:
            decrypted_text += char

    return decrypted_text