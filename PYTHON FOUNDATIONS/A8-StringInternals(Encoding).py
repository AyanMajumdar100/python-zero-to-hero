# UNICODE CHARACTER POINTS
# From character to integer
char_to_int = ord('A')
print(f"ord('A') : {char_to_int}")      # ord('A') : 65

# From integer to character
int_to_char = chr(65)
print(f"chr(65)  : '{int_to_char}'")    # chr(65)  : 'A'

# ENCODING BYTES
# Let's use an emoji to really see how UTF-8 handles complex characters
message = "Hello 🌍"
print(f"Original text : '{message}' (Type: {type(message).__name__})")
# OUTPUT : Original text : 'Hello 🌍' (Type: str)

# Translating the Unicode string into raw bytes
# Notice the 'b' prefix in the output, which stands for 'bytes'
encoded_message = message.encode('utf-8')
print(f"Encoded bytes : {encoded_message} (Type: {type(encoded_message).__name__})")
# '🌍' takes up 4 separate bytes (\xf0\x9f\x8c\x8d)
# OUTPUT : Encoded bytes : b'Hello \xf0\x9f\x8c\x8d' (Type: bytes)


print("\n--- Decoding back to String ---")
# Translating the raw bytes back into a human-readable string
decoded_message = encoded_message.decode('utf-8')
print(f"Decoded text  : '{decoded_message}' (Type: {type(decoded_message).__name__})")



# ENCODING/DECODING ACCEPTS 2 PARAMETERS (encoding, errors)
# The full signature
string = "Awesome 💀"
string.encode(encoding="utf-8", errors="strict")
bytes.decode(encoding="utf-8", errors="strict")


# ERROR TYPES : 
text = "Cafe ☕"
# 1. "strict" (Default) - CRASHES
# text.encode("ascii") -> UnicodeEncodeError!
# 2. "ignore" - Silently drops the character that doesn't fit
print(text.encode("ascii", errors="ignore"))
# Output: b'Cafe '

# 3. "replace" - Replaces the character with a standard question mark '?'
print(text.encode("ascii", errors="replace"))
# Output: b'Cafe ?'

# 4. "backslashreplace" - Keeps the data safe by converting it to a Python escape code
print(text.encode("ascii", errors="backslashreplace"))
# Output: b'Cafe \\u2615'


# EXAMPLES - Decoding failures (Corrupted Bytes to UTF-8)

# The \xff byte is invalid in UTF-8
corrupt_bytes = b"Hello \xff World"

# 1. "strict" (Default) - CRASHES
corrupt_bytes.decode("utf-8")           # WILL GIVE -> UnicodeDecodeError!

# 2. "ignore" - Just skips the corrupted byte entirely
print(corrupt_bytes.decode("utf-8", errors="ignore"))   # Output: 'Hello  World'

# 3. "replace" - Swaps the bad byte for the official Unicode Replacement Character ()
print(corrupt_bytes.decode("utf-8", errors="replace"))  # Output: 'Hello  World'


# BASE TRANSITIONS INT <---> (Hex, Binary, Oct)

# Binary"1101" into a base-10 integer.
print(int("1101",2))        # 13

# Hexadecimal (Base 16) to Int          # Valid characters are 0-9 and A-F
print(int("1A", 16))        # Output: 26

# Octal (Base 8) to Int                 # Valid characters are 0-7
print(int("17", 8))         # Output: 15

# It even works if the string has standard Python prefixes (0x, 0b, 0o)
print(int("0x1A", 16))      # Output: 26

# BASE 10 TO OTHER BASES (STRING)
number = 26
# Integer to Binary String              # Adds the '0b' prefix
print(bin(number))          # Output: '0b11010'

# Integer to Hexadecimal String         # Adds the '0x' prefix
print(hex(number))          # Output: '0x1a'

# Integer to Octal String               # Adds the '0o' prefix
print(oct(number))          # Output: '0o32'