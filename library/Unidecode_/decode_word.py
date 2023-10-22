from unidecode import unidecode

string_with_accents = "Héllo Wörld"
string_without_accents = unidecode(string_with_accents)

print(string_with_accents)
# Output: Héllo Wörld

print(string_without_accents)
# Output: Hello World

from unidecode import unidecode

# Example 1: Removing diacritics from accented characters
accents_str = "Café Mélange"
clean_str = unidecode(accents_str)
print(clean_str)  # Output: Cafe Melange

# Example 2: Converting non-Latin characters to closest ASCII characters
non_latin_str = "こんにちは"
ascii_str = unidecode(non_latin_str)
print(ascii_str)  # Output: kon'nichiwa
