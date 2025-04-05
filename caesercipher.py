alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction =input("type 'encode'to encrypt, type 'decode'to decrypt:\n ").lower()
original_text=input("type your message:\n").lower()
shift_amount=int(input("type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Reverse shift if decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_shift_amount = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_shift_amount]
        else:
            output_text += letter  # Keeps spaces and punctuation

    print(f"Here is {encode_or_decode}d result: {output_text}")
    
    should_continue = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if should_continue == "yes":
        direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
        original_text = input("type your message:\n").lower()
        shift_amount = int(input("type the shift number:\n"))
        caesar(original_text, shift_amount, direction)
    elif should_continue == "no":
        print("Goodbye!")
    else:
        print("Goodbye!")

caesar(original_text, shift_amount, direction)

# the code below are a step by step of the above code

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)+shift_amount #7->9
#         shifted_position = shifted_position % len(alphabet) # to wrap around the alphabet
#         cipher_text+=alphabet[shifted_position] # to get the letter at the shifted position
        
#     print(f"the encoded text is :{cipher_text}")
 
# # Call the function with the input values   
# encrypt=encrypt(original_text, shift_amount)


# def decrypt(original_text, shift_amount):
#     decipher_text = ""
    
#     for letter in original_text:
#         if letter in alphabet:
#             shifted_position = alphabet.index(letter) - shift_amount
#             shifted_position = shifted_position % len(alphabet)
#             decipher_text += alphabet[shifted_position]
#         else:
#             decipher_text += letter  # Keep spaces, punctuation, etc.
        
#     print(f"The decoded text is: {decipher_text}")
    

# decrypt = (original_text=text , shift_amount=shift)
         
# Call the function with the input values
# decrypt(original_text, shift_amount)

# def ceasar(original_text, shift_amount , encode_or_decode):
#     output_text= ""
    
#     if encode_or_decode == "decode":
#             shift_amount *= -1
            
#     for letter in original_text:
#         if letter in alphabet:
#             shift_amount = alphabet.index(letter) + shift_amount
#             new_shift_amount =  shift_amount % len(alphabet)
#             output_text += alphabet[new_shift_amount]
#         else:
#             output_text += letter
        
#     print(f"Here is your result: {output_text}")
    
# ceasar(original_text, shift_amount, direction)

