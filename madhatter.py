from arg_parser import parse_arguments, print_usage
from itertools import permutations
import sys

# 24 letters alphabet (removed least frequent two letters: 'j' and 'z')
# 'j' is replaced by i and 'z' is replaced by 's'
alphabet = "abcdefghiklmnopqrstuvwxy"
replacements = {'j': 'i', 'z': 's'}
key = ""
# Predefined sets of symbols
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # default symbols
symbols_set_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # "numbers"
symbols_set_2 = ['═', '╬', '╦', '╩', '╚', '╠', '╗', '╣', '║']  # "cool1"
symbols_set_3 = ['u', 'n', 'm', 'v', 'w', 'o', 'c', 'e', 'a']  # "alike"
symbols_set_4 = ['─', '└', '┴', '│', '┼', '├', '┐', '┤', '┬']  # "cool2"
ternary_digit = 3  # default ternary digit position


# Returns a 24 letter (two least frequent letter are removed) keyed alphabet.
# Removed letters are replaced in key using replacements dictionary.
def key_alphabet():
    global key
    keyed = ""
    # Put key in
    for letter in key:
        curr_letter = letter
        # Replace removed letters
        for _current, replacement in replacements.items():
            if curr_letter == _current:
                curr_letter = replacement
                break
        if letter not in keyed and letter in alphabet:
            keyed += curr_letter

    # Put in the rest of the alphabet
    for letter in alphabet:
        if letter not in keyed:
            keyed += letter

    return keyed


# Given a list of symbols, splits the symbols in four groups using
# the ternary digit
def group_symbols():
    global ternary_digit
    symbol_groups = []
    digit_bases = [2, 2, 2, 2]
    digit_bases[ternary_digit] = 3
    sym_index = 0
    for digit in digit_bases:
        block = []
        for i in range(0, digit):
            block.append(symbols[sym_index])
            sym_index += 1
        symbol_groups.append(block)
    return symbol_groups


# Increments a four-digits mixed-radix number
def increment_mixed_radix(digits, bases):
    if digits[3] < bases[3] - 1:
        digits[3] += 1
    elif digits[2] < bases[2] - 1:
        digits[2] += 1
        digits[3] = 0
    elif digits[1] < bases[1] - 1:
        digits[1] += 1
        digits[2] = 0
        digits[3] = 0
    elif digits[0] < bases[0] - 1:
        digits[0] += 1
        digits[1] = 0
        digits[2] = 0
        digits[3] = 0


# Returns a dictionary that contains the mapping of an alphabet to
# four-digit mixed-radix numbers
# If reverse is True then the returned dictionary is reversed.
def radix_map(keyed_alphabet, reverse=False):
    global ternary_digit
    radix_mapping = {}
    digit_base = [2, 2, 2, 2]
    digit_base[ternary_digit] = 3
    curr_digits = [0, 0, 0, 0]

    for letter in keyed_alphabet:
        if not reverse:
            radix_mapping[letter] = curr_digits.copy()
        else:
            string = ""
            for digit in curr_digits:
                string += str(digit)
            radix_mapping[string] = letter
        increment_mixed_radix(curr_digits, digit_base)

    return radix_mapping


# Using the letters from symbols, maps each letter from the
# keyed alphabet to a combination of some of those letters.
def letter_map(keyed_alphabet, radix_mapping):
    global ternary_digit
    letter_mapping = {}
    symbol_groups = group_symbols()

    # Map keyed alphabet letters
    for letter in keyed_alphabet:
        mapping = []
        aux_index = 0
        for digit in radix_mapping[letter]:
            mapping.append(symbol_groups[aux_index][digit])
            aux_index += 1
        letter_mapping[letter] = mapping

    return letter_mapping


# Creates the first cypher that contains the first plaintext and is used
# to encrypt the second plaintext
def first_encryption(plaintext, letter_mapping):
    cypher = []

    for letter in plaintext:
        if letter in alphabet:
            cypher.append(letter_mapping[letter])

    return cypher


# Generates permutations of four numbers and assigns them to the letters
# of the keyed alphabet.
# If reverse is true, the returned dictionary is reversed.
def permute_letters(keyed_alphabet, reverse=False):
    letter_permutations = {}
    perms = list(permutations([0, 1, 2, 3]))
    aux_index = 0
    for letter in keyed_alphabet:
        if not reverse:
            letter_permutations[letter] = perms[aux_index]
        else:
            string = ""
            for digit in perms[aux_index]:
                string += str(digit)
            letter_permutations[string] = letter
        aux_index += 1
    return letter_permutations


# Permute letters in the first cypher according to the second plaintext
# and generates the final cypher
def second_encryption(plaintext2, first_cypher, letter_permutations):
    final_cypher = []
    letter_index = 0
    for letter in plaintext2:
        if letter in alphabet:
            block = []
            for position in letter_permutations[letter]:
                block.append(first_cypher[letter_index][position])
            letter_index += 1
            final_cypher.append(block)

    return final_cypher


def encrypt(plaintext1, plaintext2):
    global ternary_digit
    keyed_alphabet = key_alphabet()
    # print(keyed_alphabet)
    radix_mapping = radix_map(keyed_alphabet)
    # print(radix_mapping)
    letter_mapping = letter_map(keyed_alphabet, radix_mapping)
    # print(letter_mapping)
    first_cypher = first_encryption(plaintext1, letter_mapping)
    # print(first_cypher)
    letter_permutations = permute_letters(keyed_alphabet)
    # print(letter_permutations)
    final_cypher = second_encryption(plaintext2, first_cypher, letter_permutations)
    # print(final_cypher)
    return final_cypher


# Returns the group in which a letter is placed inside the four
# groups of symbols
def symbol_index(letter, groups):
    if letter in symbols:
        index = 0
        for group in groups:
            if letter in group:
                return index
            index += 1
    else:
        return None


# Extracts the second plaintext and returns it alongside the second cypher
def first_decryption(cypher, letter_permutation):
    global ternary_digit
    # Break cypher into blocks
    _cypher = []
    plaintext2 = []
    first_cypher = []
    for k in range(0, int(len(cypher)/4)):
        block = [cypher[k*4], cypher[k*4+1], cypher[k*4+2], cypher[k*4+3]]
        _cypher.append(block)
    # Knowing the ternary_digit and the symbols used, find the permutation used
    # and therefore the letters of the second plaintext
    symbol_groups = group_symbols()
    for block in _cypher:
        permutation = ""
        first_cypher_block = ['x', 'x', 'x', 'x']
        for letter in block:
            index = symbol_index(letter, symbol_groups)
            permutation += str(index)
            first_cypher_block[index] = letter
        if permutation not in letter_permutation:
            print("Given ternary digit position is wrong!")
            exit()
        plaintext2.append(letter_permutation[permutation])
        first_cypher.append(first_cypher_block)

    return plaintext2, first_cypher


# Knowing the mixed-radix mapping, extract the first plaintext
def second_decryption(first_cypher, radix_mapping):
    first_plaintext = []
    symbol_groups = group_symbols()
    for block in first_cypher:
        digits = ""
        for letter in block:
            digit = ""
            for group in symbol_groups:
                if letter in group:
                    digit = str(group.index(letter))
            digits += digit
        first_plaintext.append(radix_mapping[digits])

    return first_plaintext


def decrypt(cypher):
    keyed_alphabet = key_alphabet()
    # print(keyed_alphabet)
    radix_mapping_rev = radix_map(keyed_alphabet, True)  # reversed
    # print(radix_mapping_rev)
    letter_permutations = permute_letters(keyed_alphabet, True)  # reversed
    # print(letter_permutations)
    second_plaintext, first_cypher = first_decryption(cypher, letter_permutations)
    # print(first_cypher)
    # print(second_plaintext)
    first_plaintext = second_decryption(first_cypher, radix_mapping_rev)
    # print(first_plaintext)
    return first_plaintext, second_plaintext


def print_result(to_file, o_file, string, message=""):
    # Optional message before the string
    if message:
        if to_file:
            o_file.write((message + "\n"))
        else:
            print(message)
    line = ""
    for symbol in string:
        line += symbol
        if len(line) == 80:
            if to_file:
                o_file.write(line + "\n")
            else:
                print(line)
            line = ""
    if to_file:
        o_file.write(line + "\n")
    else:
        print(line)


def main():
    global symbols
    global ternary_digit
    global key
    i_file = None
    o_file = None

    # Parse parameters
    ((correct_args, err_msg), settings) = parse_arguments(sys.argv)
    # print("-------------------- * --------------------")
    # print("Parameters:")
    # for key, value in settings.items():
    #     print("\t" + key + "\t", value)
    # if not settings:
    #     print("\tNone")
    # print("-------------------- * --------------------")

    if not correct_args:
        if err_msg != "help":
            print("Incorrect call! :(")
            print(err_msg, end="")
            print("\tUse \"-h\" option to see usage.\n")
            exit()
        else:
            print_usage()
            exit()

    # Set key, if one was provided.
    if settings["key"][0]:
        key = settings["key"][1]

    # Set symbols, if provided.
    if settings["symbols"][0]:
        sym_word = settings["symbols"][1]
        if sym_word == "numbers":
            symbols = symbols_set_1
        elif sym_word == "cool1":
            symbols = symbols_set_2
        elif sym_word == "alike":
            symbols = symbols_set_3
        elif sym_word == "cool2":
            symbols = symbols_set_4
        else:
            sym_list = list(settings["symbols"][1])
            if len(sym_list) != 9:
                print("Exactly nine symbols are required.")
                print(len(sym_list), " were given: ", sym_list)
                exit()
            else:
                symbols = sym_list

    # Set ternary digit position, if one was provided
    if settings["ternary"][0]:
        new_position = int(settings["ternary"][1])
        if new_position < 0 or new_position > 3:
            print("Ternary digit position should be 0, 1, 2 or 3.")
            print(new_position, " was given.")
            exit()
        else:
            ternary_digit = new_position

    plaintext_1 = ""
    plaintext_2 = ""
    cypher = ""

    # ============================ Encryption mode ============================
    if settings["encrypt"]:

        # Reading from input
        aux_plaintext_1 = ""
        aux_plaintext_2 = ""
        if settings["input"][0]:
            i_file = open(settings["input"][1], 'r', encoding="utf-8")
            print("Opened input file for reading.")
            first_text = True
            while True:
                line = i_file.readline()
                if line == "":
                    break
                elif line == "\n":
                    first_text = False
                else:
                    if first_text:
                        aux_plaintext_1 += line[:-1].lower()
                    else:
                        aux_plaintext_2 += line[:-1].lower()
            if len(aux_plaintext_2) == 0:
                print("No blank line found in the input file.")
                print("Encrypting only ONE text!")
        else:
            aux_plaintext_1 = settings["input"][1].lower()
            aux_plaintext_2 = settings["input"][2].lower()

        # Remove all characters that are not in the alphabet.
        # Then add padding if needed, so that both texts are of equal length.
        for letter in aux_plaintext_1:
            if letter in alphabet:
                plaintext_1 += letter
        for letter in aux_plaintext_2:
            if letter in alphabet:
                plaintext_2 += letter
        l1 = len(plaintext_1)
        l2 = len(plaintext_2)
        if l1 != l2:
            if l1 < l2:
                plaintext_1 += 'x' * (l2 - l1)
            else:
                plaintext_2 += 'x' * (l1 - l2)
        r = len(plaintext_1) % 4
        if r != 0:
            plaintext_1 += 'x' * r
            plaintext_2 += 'x' * r

        # Encryption
        print("Plaintext 1 length: ", len(plaintext_1), " characters.")
        print("Plaintext 2 length: ", len(plaintext_2), " characters.")
        cypher = encrypt(plaintext_1, plaintext_2)
        flat_cypher = ""
        for block in cypher:
            flat_cypher += "".join(block)
        print("Encrypted to a cypher of ", len(flat_cypher), " characters.")

        # Writing to output
        if settings["output"][0]:
            o_file = open(settings["output"][1], 'w', encoding="utf-8")
            print("Opened output file for writing.")
        print_result(settings["output"][1], o_file, flat_cypher, "Cypher:")

    # ============================ Decryption mode ============================
    else:
        # Reading from input
        if settings["input"][0]:
            i_file = open(settings["input"][1], 'r', encoding="utf-8")
            print("Opened input file for reading.")
            while True:
                line = i_file.readline()
                if line == "":
                    break
                else:
                    cypher += line[:-1].lower()
        else:
            cypher = settings["input"][1].lower()

        # If the length of the cypher is not divisible by four, abort operation
        # print("Cypher len: ", len(cypher))
        if len(cypher) % 4 != 0:
            print("Cypher of incorrect length (", len(cypher), ")!", sep="")
            print("Length must be divisible by four.")
            if settings["input"][0]:
                i_file.close()
            exit()

        # Check if the cypher symbols and the ones used for decryption match.
        cypher_symbols = []
        for letter in cypher:
            if letter not in cypher_symbols:
                cypher_symbols.append(letter)
            if len(cypher_symbols) == 9:
                break
        for symbol in cypher_symbols:
            if symbol not in symbols:
                print("Cypher symbols and given symbols (or default ones) "
                      "do not match.")
                print("Please specify the correct symbols.")
                if settings["input"][0]:
                    i_file.close()
                exit()

        # Decryption
        print("Cypher length: ", len(cypher), " characters.")
        plaintext_1, plaintext_2 = decrypt(cypher)
        plaintext_1 = "".join(plaintext_1)
        plaintext_2 = "".join(plaintext_2)
        print("Decrypted to:")
        print("\tPlaintext 1 of ", len(plaintext_1), " characters,")
        print("\tPlaintext 2 of ", len(plaintext_2), " characters.")

        # Writing to output
        if settings["output"][0]:
            o_file = open(settings["output"][1], 'w', encoding="utf-8")
            print("Opened output file for writing.")
        print_result(settings["output"][1], o_file, plaintext_1, "First text:")
        print_result(settings["output"][1], o_file, plaintext_2, "\nSecond text:")

    if settings["input"][0]:
        print("Input file closed.")
        i_file.close()
    if settings["output"][0]:
        print("Output file closed.")
        o_file.close()


if __name__ == "__main__":
    main()
