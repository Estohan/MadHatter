# MadHatter
## A toy cipher that conceals two plaintexts in the same ciphertext



###### Description

*  This is my implementation of the cipher described by Thomas Kaeding in his
paper: [Madhatter: A toy cipher that conceals two plaintexts in the same
ciphertext](https://eprint.iacr.org/2020/301.pdf).



###### Usage

*  *python madhatter.py [-e|-d|-h][-k "key"][-t "n"][-s "abcdefghi"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[-i "input_file"][-o "output_file"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;["plaintext1" "plaintext2" | "ciphertext1"]*

	Options:\
		*-e*&emsp;Encrypts two plaintexts. The plaintexts will be provided either as operands to this command or inside an input file, separated by a blank line.\
		*-d*&emsp;Decrypts one ciphertext. The ciphertext will be provided either as an operand to this command or inside an input file.\
		*-i*&emsp;"-i filename". Read input text from "filename" file. In case of encryption, the two plaintexts must be separated by a new line. A new line is also mandatory at the end of the file.\
		*-o*&emsp;"-o filename". Writes output text to "filename" file.\
		*-k*&emsp;"-k key". Supply the program with a key, if needed. The default value of the key is "" (empty string).\
		*-t*&emsp;"-t n". Change the ternary digit position from 3 (default position) to "n" (which must be 0, 1, 2 or 3).\
		*-s*&emsp;"-s abcdefghi". Change the set of nine symbols used by the program (which by default is "abcdefghi"). This option's argument could also be one of the following strings, in order to select one of the predefined sets:\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*"numbers"*:&emsp;"123456789"\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*"cool1"*:&emsp;"═╬╦╩╚╠╗╣║"\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*"alike"*:&emsp;"unmvwocea"\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;*"cool2"*:&emsp;"─└┴│┼├┐┤┬"*
