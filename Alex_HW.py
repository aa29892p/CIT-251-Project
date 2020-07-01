

binary_int = int("0100000101010011010001010100011101000110010101010100010001000111010011010101011001000110010000010100011001010111", 2)
byte_number = binary_int.bit_length() + 7 // 8

binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()




print(f"This is my converted ascii_test: {ascii_text}")


i = 0

temp_list = []

# There are only 26 possible shifts with the Caesar cipher -- performed 27 to ensure I am getting a repeat

for x in range(27):
    shift = x

    encrypted_text = ascii_text # decoded variable from above

    answer_text = ""

    for char in encrypted_text:

        # check if character is an uppercase letter
        if char.isupper():

            # find the position in 0-25 ---- using 'ord' to return the Unicode code point for a one-character string
            char_unicode = ord(char)

            char_index = ord(char) - ord("A")

            # perform the negative shift
            new_index = (char_index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # make the new text answer possibility
            answer_text = answer_text + new_character

        else:

            # failsafe incase a random lowercase letter was addded
            answer_text += char


    i = i + 1
    print(f"Decrypted text option {i}: {answer_text}")
    temp_list.append(answer_text)

print(f"The password you are looking for is: {temp_list[18]}")
