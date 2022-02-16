# MadHatter
## A toy cipher that conceals two plaintexts in the same ciphertext



###### Description

*  This is my implementation of the cipher described by Thomas Kaeding in his
paper: [Madhatter: A toy cipher that conceals two plaintexts in the same
ciphertext](https://eprint.iacr.org/2020/301.pdf).



###### Usage

*  *python madhatter.py [-e|-d|-h][-k "key"][-t "n"][-s "abcdefghi"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[-i "input_file"][-o "output_file"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;["plaintext1" "plaintext2" | "ciphertext1"]*

	*Options:\
		-e  Encrypts two plaintexts. The plaintexts will be provided\
&emsp;&emsp;either as operands to this command or inside an input\
&emsp;&emsp;file, separated by a blank line.\
		-d  Decrypts one ciphertext. The ciphertext will be provided\
&emsp;&emsp;either as an operand to this command or inside an input file.\
		-i  "-i filename". Read input text from "filename" file.\
&emsp;&emsp;In case of encryption, the two plaintexts must be separated\
&emsp;&emsp;by a new line. A new line is also mandatory at the end of\
&emsp;&emsp;the file.\
		-o  "-o filename". Writes output text to "filename" file.\
		-k  "-k key". Supply the program with a key, if needed.\
&emsp;&emsp;The default value of the key is "" (empty string).\
		-t  "-t n". Change the ternary digit position from 3\
&emsp;&emsp;(default position) to "n" (which must be 0, 1, 2 or 3).\
		-s  "-s abcdefghi". Change the set of nine symbols used by\
&emsp;&emsp;the program (which by default is "abcdefghi"). This\
&emsp;&emsp;option's argument could also be one of the following\
&emsp;&emsp;strings, in order to select one of the predefined sets:\
&emsp;&emsp;&emsp;&emsp;"numbers": "123456789"\
&emsp;&emsp;&emsp;&emsp;"cool1  ": "═╬╦╩╚╠╗╣║"\
&emsp;&emsp;&emsp;&emsp;"alike  ": "unmvwocea"\
&emsp;&emsp;&emsp;&emsp;"cool2  ": "─└┴│┼├┐┤┬"*
