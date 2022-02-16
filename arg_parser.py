
arg_options = ['e', 'd', 'i', 'o', 'k', 't', 's', 'h']
ret_options_dict = {}
flags = {"opt_encrypt": False,
         "opt_decrypt": False,
         "opt_input": False,
         "opt_output": False,
         "opt_key": False,
         "opt_ternary": False,
         "opt_symbols": False,
         "opt_help": False,
         "wrong_opts": False,
         "expect_opt_arg": False,
         "options_over": False,
         "working_mode_specified": False,
         "input_satisfied": 0}  # 0 - not, 1 - decrypt, 2 - encrypt
previous_option = ""
err_message = ""
usage = "Usage:\n\tpython madhatter.py [-e|-d|-h][-k \"key\"][-t \"n\"]" \
        "[-s \"abcdefghi\"]\n\t\t[-i \"input_file\"][-o \"output_file\"]\n" \
        "\t\t[\"plaintext1\" \"plaintext2\" | \"ciphertext1\"]\n\n" \
        "Options:\n" \
        "\t-e\tEncrypts two plaintexts. The plaintexts will be provided\n" \
        "\t\teither as operands to this command or inside an input\n" \
        "\t\tfile, separated by a blank line.\n" \
        "\t-d\tDecrypts one ciphertext. The ciphertext will be provided\n" \
        "\t\teither as an operand to this command or inside an input\n" \
        "\t\tfile.\n" \
        "\t-i\t\"-i filename\". Read input text from \"filename\" file.\n" \
        "\t\tIn case of encryption, the two plaintexts must be separated\n" \
        "\t\tby a new line. A new line is also mandatory at the end of\n" \
        "\t\tthe file\n" \
        "\t-o\t\"-o filename\". Writes output text to \"filename\" file.\n" \
        "\t-k\t\"-k key\". Supply the program with a key, if needed.\n" \
        "\t\tThe default value of the key is \"\" (empty string).\n" \
        "\t-t\t\"-t n\". Change the ternary digit position from 3\n" \
        "\t\t(default position) to \"n\" (which must be 0, 1, 2 or 3).\n" \
        "\t-s\t\"-s abcdefghi\". Change the set of nine symbols used by\n" \
        "\t\tthe program (which by default is \"abcdefghi\"). This\n" \
        "\t\toption's argument could also be one of the following\n" \
        "\t\tstrings, in order to select one of the predefined sets:\n" \
        "\t\t\t\"numbers\": \"123456789\"\n" \
        "\t\t\t\"cool1  \": \"═╬╦╩╚╠╗╣║\"\n" \
        "\t\t\t\"alike  \": \"unmvwocea\"\n" \
        "\t\t\t\"cool2  \": \"─└┴│┼├┐┤┬\"\n"


# Prints details about how the command should be used.
def print_usage():
    print(usage)


# Checks if an option (as "-h" for example) is correct.
def is_valid_option(argument):
    if len(argument) == 2 and argument[0] == '-' and argument[1] in arg_options:
        return True
    return False


# Checks if an option is syntactically placed correctly.
def option_position_check(option):
    global err_message
    # Check if an option argument was expected instead
    if flags["expect_opt_arg"]:
        err_message = "\tExpected an option argument for " + previous_option +\
                      ".\n" + "\tInstead, got -" + option + ".\n"
        return False
    # Check if an operand was present before this option
    if flags["options_over"]:
        err_message = "\tOptions should precede operands.\n"
        return False
    return True


# Encrypt option ("-e").
def case_encrypt():
    global err_message
    # Check syntax
    if not option_position_check('e'):
        return False
    # If -e/-d was not already specified
    if flags["working_mode_specified"]:
        err_message = "\tOptions -e and -d are mutually exclusive. Please use \
only one of them, \n\tonce only.\n"
        return False
    flags["opt_encrypt"] = True
    flags["working_mode_specified"] = True
    # Add entry in return dictionary
    ret_options_dict["encrypt"] = True
    return True


# Decrypt option ("-d").
def case_decrypt():
    global err_message
    # Check syntax
    if not option_position_check('d'):
        return False
    # If -e/-d was not already specified
    if flags["working_mode_specified"]:
        err_message = "\tOptions -e and -d are mutually exclusive. Please use \
only one of them, \n\tonce only.\n"
        return False
    flags["opt_decrypt"] = True
    flags["working_mode_specified"] = True
    # Add entry in return dictionary
    ret_options_dict["encrypt"] = False
    return True


# Input file option ("-i").
def case_input(filename=""):
    global err_message
    global previous_option
    # Process the option
    if filename == "":
        # Check syntax
        if not option_position_check('i'):
            return False
        # Next argument should be this option's argument
        flags["expect_opt_arg"] = True
        previous_option = 'i'
        return True
    # Process the option's argument
    else:
        # Input file satisfies input condition
        if flags["opt_encrypt"]:
            flags["input_satisfied"] = 2
        if flags["opt_decrypt"]:
            flags["input_satisfied"] = 1
        flags["opt_input"] = True
        flags["expect_opt_arg"] = False
        previous_option = ""
        # Add entry in return dictionary
        ret_options_dict["input"] = (True, filename, None)
        return True


# Output file option ("-o").
def case_output(filename=""):
    global previous_option
    # Process the option
    if filename == "":
        # Check syntax
        if not option_position_check('o'):
            return False
        # Next argument should be this option's argument
        flags["expect_opt_arg"] = True
        previous_option = 'o'
        return True
    # Process the option's argument
    else:
        flags["opt_output"] = True
        flags["expect_opt_arg"] = False
        previous_option = ""
        # Add entry in return dictionary
        ret_options_dict["output"] = (True, filename)
        return True


# Key specification option ("-k").
def case_key(key=""):
    global previous_option
    # Process the option
    if key == "":
        # Check syntax
        if not option_position_check('k'):
            return False
        # Next argument should be this option's argument
        flags["expect_opt_arg"] = True
        previous_option = 'k'
        return True
    # Process the option's argument
    else:
        flags["opt_key"] = True
        flags["expect_opt_arg"] = False
        previous_option = ""
        # Add entry in return dictionary
        ret_options_dict["key"] = (True, key)
        return True


# Ternary digit position option ("-t").
def case_ternary(ternary=3):
    global previous_option
    # Process the option
    if ternary == 3:
        # Check syntax
        if not option_position_check('t'):
            return False
        # Next argument should be this option's argument
        flags["expect_opt_arg"] = True
        previous_option = 't'
        return True
    # Process the option's argument
    else:
        flags["opt_ternary"] = True
        flags["expect_opt_arg"] = False
        previous_option = ""
        # Add entry in return dictionary
        ret_options_dict["ternary"] = (True, ternary)
        return True


# Set symbols option ("-s").
def case_symbols(symbols=""):
    global previous_option
    # Process the option
    if symbols == "":
        # Check syntax
        if not option_position_check('s'):
            return False
        # Next argument should be this option's argument
        flags["expect_opt_arg"] = True
        previous_option = 's'
        return True
    # Process the option's argument
    else:
        flags["opt_symbols"] = True
        flags["expect_opt_arg"] = False
        previous_option = ""
        # Add entry in return dictionary
        ret_options_dict["symbols"] = (True, symbols)
        return True


# Help option ("-h").
def case_help():
    global err_message
    flags["opt_help"] = True
    err_message = "help"
    return False


# Unrecognized option or option argument.
def case_default(argument):
    global err_message
    global previous_option
    global ret_options_dict
    # Check if an option's argument is expected.
    # If so, process it.
    if flags["expect_opt_arg"]:
        if previous_option == 'i':
            case_input(argument)
        elif previous_option == 'o':
            case_output(argument)
        elif previous_option == 'k':
            case_key(argument)
        elif previous_option == 't':
            case_ternary(argument)
        elif previous_option == 's':
            case_symbols(argument)
    # Else, it must be an operand
    else:
        if flags["opt_input"]:
            err_message = "\tUnexpected operand or unrecognized option (\"" +\
                          argument + "\").\n"
            return False
        elif flags["input_satisfied"] == 2 and flags["opt_encrypt"]:
            err_message = "\tToo many plaintexts.\n" + \
                          "\tOnly two plaintexts are required when \
encrypting.\n"
            return False
        elif flags["input_satisfied"] == 1 and flags["opt_decrypt"]:
            err_message = "\tToo many ciphertexts.\n" + \
                          "\tOnly one ciphertext is required when \
decrypting.\n"
            return False
        else:
            flags["input_satisfied"] += 1
        flags["options_over"] = True
    return True


# Dictionary that contains the above functions, used to easily add new
# command options and process existing ones.
process_arg = {"e": case_encrypt,
               "d": case_decrypt,
               "i": case_input,
               "o": case_output,
               "k": case_key,
               "t": case_ternary,
               "s": case_symbols,
               "h": case_help,
               "default": case_default}


# Check if arguments are correct
#   Returned value is a tuple of a tuple and a dictionary.
#   - The first member (the tuple) contains a bool value tells if the command
#   was called correctly and an error message (empty in case of success).
#   - The second member (the dictionary) contains the parameters passed to the
#   program.
#
#       ((True/False, ""/"Message") OR (False, "help"),
#        {"encrypt": (True/False),
#         "input": (True/False, file_name/plaintext_1, None/plaintext_2),
#         "output": (True/False, file_name/None),
#         "key": (True/False, key/None),
#         "ternary": (True/False, position/None),
#         "symbols": (True/False, symbols/None}
#       )
def parse_arguments(argv):
    global err_message
    argv = argv[1:]  # remove first argument (program name)
    arg_nr = len(argv)
    good_syntax = True
    good_logic = True

    # Check syntax
    for idx in range(arg_nr):
        current_arg = argv[idx]
        # If argument is an option
        if is_valid_option(current_arg):
            if not process_arg[current_arg[1]]():
                good_syntax = False
                break
        # If argument is an option argument or an operand
        else:
            if not process_arg["default"](current_arg):
                good_syntax = False
                break
    if flags["expect_opt_arg"]:
        good_syntax = False
        err_message = "\tOption \"-" + previous_option + "\" expected an \
argument but was not followed by one.\n"

    # Check logic
    if len(err_message) == 0:
        if flags["opt_encrypt"] and not flags["input_satisfied"] == 2:
            err_message = "\tTwo plaintexts are needed when encrypting.\n" + \
                          "\tPlease provide them as arguments or inside an input \
file.\n"
            good_logic = False
        if flags["opt_decrypt"] and not flags["input_satisfied"] == 1:
            err_message = "\tCiphertext is needed when decrypting.\n" + \
                          "\tPlease provide it as argument or inside an input \
file."
            good_logic = False
        if not flags["opt_encrypt"] and not flags["opt_decrypt"]:
            err_message = "\tOperation not specified.\n" + \
                          "\tPlease use -e for encryption or -d for decryption.\n"
            good_logic = False
    else:
        return (False, err_message), {}

    if not good_syntax or not good_logic:
        return (False, err_message), {}

    # Add remaining entries in return dictionary
    if not flags["opt_input"]:
        if flags["opt_encrypt"]:
            ret_options_dict["input"] = (False, argv[arg_nr-2], argv[arg_nr-1])
        else:
            ret_options_dict["input"] = (False, argv[arg_nr - 1], None)
    if not flags["opt_output"]:
        ret_options_dict["output"] = (False, None)
    if not flags["opt_key"]:
        ret_options_dict["key"] = (False, None)
    if not flags["opt_ternary"]:
        ret_options_dict["ternary"] = (False, None)
    if not flags["opt_symbols"]:
        ret_options_dict["symbols"] = (False, None)

    return (True, ""), ret_options_dict
