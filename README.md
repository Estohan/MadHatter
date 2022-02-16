# MadHatter
## A toy cipher that conceals two plaintexts in the same ciphertext



###### Description

*  This is my implementation of the cipher described by Thomas Kaeding in his
paper: [Madhatter: A toy cipher that conceals two plaintexts in the same
ciphertext](https://eprint.iacr.org/2020/301.pdf).

* It can encrypt two plaintexts (either provided inside a text file or as arguments to the command) or decrypt a cyphertext that was created using this implementation. In order to obtain a particular encryption, additional options can be supplied: an alphabet key, the symbols for the digits of the mixed-radix numbers or which digit of those numbers is the ternary digits. However, if any of these is used, the same options are necessary when decrypting.



###### Usage

*  Run *"python madhatter.py -h"* in order to display the description below:

&emsp;&emsp;*python madhatter.py [-e|-d|-h][-k "key"][-t "n"][-s "abcdefghi"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[-i "input_file"][-o "output_file"]\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;["plaintext1" "plaintext2" | "ciphertext1"]*\
\
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



###### Examples

* Encryption using the "cool1" predefined set of symbols:\
&emsp;*> python madhatter.py -e -i "input.txt" -s "cool1" -o "output.txt"*
\
\
**input.txt:**
<pre>As for the Hobbits of the Shire, with whom these tales are concerned,
in the days of their peace and prosperity they were a merry folk. They
dressed in bright colours, being notably fond of yellow and green; but they
seldom wore shoes, since their feet had tough leathery soles and were clad in
a thick curling hair, much like the hair of their heads, which was commonly
brown. Thus, the only craft little practised among them was shoe-making; but
they had long and skillful fingers and could make many other useful and comely
things. Their faces were as a rule good-natured rather than beautiful, broad,
bright-eyed, red-cheeked, with mouths apt to laughter, and to eating and
drinking. And laugh they did, and eat, and drink, often and heartily, being
fond of simple jests at all times, and of six meals a day (when they could
get them). They were hospitable and delighted in parties, and in presents,
which they gave away freely and eagerly accepted.

    Frodo drew the Ring out of his pocket again and looked at it. It now
appeared plain and smooth, without mark or device that he could see. The gold
looked very fair and pure, and Frodo thought how rich and beautiful was its
colour, how perfect was its roundness. It was an admirable thing and
altogether precious. When he took it out he had intended to fling it from him
into the very hottest part of the fire. But he found now that he could not do
so, not without a great struggle. He weighed the Ring in his hand, hesitating,
and forcing himself to remember all that Gandalf had told him; and then with
an effort of will he made a movement, as if to cast it away - but he found
that he had put it back in his pocket.</pre>
\
**output.txt:**
<pre>Cypher:
═╗╚╦╠║╬╦╠═║╦╬╚╣╦╠╬╣╦╬╚╗╩╚╣═╩═╣╦╠╣╩╚═╣╬╦╚╦═╣╚═╣╦╚╚║═╩╩╚╬╗╠╬╦║╦╬╚╣╠═║╦╗╬╚╩╣═╩╚╠═╣╦
╬║╠╦╩═╣╚╩╚═║╠╣╦╬╠╦═╣╠╬╗╩═╚╩║╩╚╗╬═╣╩╚╗╬╩╠═╩╚╣╦╬╚╣═╩╠║╩╚╬╗╚═╩╣═╦╠╣╠╬╦║═╠╣╦╩╗╬╚╚═╗╦
╠═╣╩╦╠╣═╬║╦╠═╚╗╦╬╦╠╣╣═╦╠╦╚═║╣╬╦╚╦╚╬╗║═╦╚╠═╦╣╠╬╣╦╗╦╚╬═╦╠╣╠╦═╗╚╩═║╬╗╦╚╬╩╚╗╚╣═╩═╣╦╠
═╠╗╦╚╦═╗╩║╬╠╬╦╠║╦╚╬╣╠═╦║╬╩╚╗╚═╩╣═╠╣╦╚║╩═╦╣╠╬╚╬║╦╠═╣╦╗═╦╚╦═║╚╣╦╠═╦╚═╗╗╬╦╚╦═╗╠╚╬║╦
╣╬╠╦╣╬╦╚╦║╠╬╬╦╚║╠╣═╦╦╠╣╬╚═║╩╚╗╬╩╬╠║╩╬╗╩╚╣╩═╚╦╠═╣╬╠╩║╬╗╩╠╣═╦╠╦╬╣╠═╦╠╣╗═╦╚╩═║╠═╣╦╠
╬╠╦╣╠╬╣╦║╬╠╩╦║═╠╬╚╣╦╠╣╩══╗╩╠╬╗╩╚╣═╩╚╦═╣╠╬║╩╠╦═╠╗╠╬╣╦╦╣═╠╬╠║╦╦║╬╠╠═╣╦╠═╗╦╩╚║═╬╗╦╚
═╚╣╦╣╦╬╠═║╩╚╚╗═╩╣╚╩═╬╗╚╩═╦╚║╦╚╬╣╠╣═╩╬╦╚╣╚╬╩╣╬╠╣╦╠╦╬║╣═╚╦╠╣═╦═║╩╚╬╦╚╗╚═╩╗╬╚╗╦╬╣╚╦
╚╗╬╩╚═╗╦═╚╣╦╠═╣╩║╬╩╠╦═║╠╚╬╣╦╗╬╚╦╦═╠╗╦╬╣╚║═╦╠╩╬║╠╠═╣╦╣╩╠═╠╣═╩╦╚╬╣╬╠╩╗╦═╗╚╬╦╚╗╠═╦╗
═╚╗╩╬╦╣╠═╣╦╠═╦╠╣╗╬╚╦╣═╦╚╩╚╬╣╬╗╚╩╗╬╚╩╩╣═╚╣╦╠═╬╩╠║╠║╦╬╦╠═╣╣═╩╠╠╗╦═╬╚╦╣╠═║╩╩╗╬╠╚╬╣╦
╣╬╠╦╠╣═╦╦╬║╠╚═╣╩╣╦╚╬╠╦═╣╬║╦╠╠║╬╦═║╚╩╬╗╦╚═╚╦║╣═╦╠╗╩╚╬═╩╚╣╠╣╦═╩╚═║╣╬╦╠╠║╦═╠╣═╦╠═╣╦
╗╬╚╩╚═╩╣═╚╗╦╠═╦╗╬╗╩╚╚╣╦╬╚╣╩╬╩╚═╗╣═╩╚╣╩╠══╦╠╣╚╗╦═╬╩╚╗╚═╩╣═╦╠╣╬╠╣╦╩║╠╬╦╠╬║╚╣╬╦═╩╠╣
═╦╣╠╦║╬╠═╗╦╚╗╬╦╚╦═╗╠╩╠╬╗╠═╦╣╦╬╠╣═╦╠╣╚═╦║═╠╣╩═╦╚╗╦╗═╠║═╩╚╚╬╗╦╦═╚╗╬╗╩╚╣═╩╚╩═║╚═║╦╚
╠╗═╩╚╦═║╚╣╬╩╬╣╦╠═╠╩╣╩╚═║╚╬╗╦╗═╚╩╚╣╩═╗╦╚═╩═║╚╬╣╦╠╠═╩║╩╬╣╚═║╦╚╣═╩╚╠═╣╩╚═║╩╩╠╗═╦╠═╣
╗╬╩╚╚═╣╩╣═╠╦╣═╩╚╦═╗╚═║╩╚╦╬╣╠╬╦╚╣═╠║╦╩╚╬╗╚═╩╣╣═╦╠═║╩╚╠╬╦╣═╚╣╩═╣╦╠═╚╗╦╗═╦╠╠╬║╦╬╗╠╩
╩╣═╚╩╚═║╚═╦║╩═╚╣╩╠╬╗╗═╦╚╬║╠╦╚║═╦╚╬╣╦╩║╠═╩═║╠╦╚╬╣╦╗╚╬╩╠═╣╠╬╩║╣═╦╚╠╬╣╦╣╬╦╚╩╬╗╠╬╗╦╚
╗╩╬╚═╣╩╚╚╣╬╩║╠╦╬╩╬╗╚╚═╣╩╣═╦╠╣╬╦╚╬╗╦╚╠╣╩═║╬╩╠╚╦═║╬╦╠╣╚╗═╦║═╦╠╚╬╗╩═╣╠╩║═╩╚╩╬╗╚╬╗╩╚
═╣╠╩╦╠═╣╚║╬╦╬╣╦╠═╦╗╚║═╚╦╗╬╩╚╩═║╚╬║╦╠═╣╠╦╠═╗╦╗═╚╦╠═╩║╬╚╣╦╚╬╦╗╚═╗╩╗╩╚╬╣═╩╚╦═╣╠═╩╠║
╗╬╩╠╦═╗╚╬║╦╠╬╠╦║╚═╣╩╣╬╚╦╦╣═╠═╠║╩╚═╦╗╠═╗╩║═╩╚╬╚╗╦╚═╗╩╚╣╦═╚╬╣╩╚╬╩╗╚╬╗╩╣═╩╚╣╦╠═╩╠╬║
╣═╩╚╦═╗╚╠═╗╦╣═╠╩╣╬╦╚╬╦╚╗╩═╚╗╚╗═╦╬╗╦╚═╦╠╗║╬╦╠╠╗╩═║═╩╚╠╣═╩╣═╠╩╦═╠║╩╬╚╣╩╣═╠═║╦╠╩═║╚
╬╗╦╚╗╩╚══╣╦╠╦╠╬╣╦╬╠║╦═╗╚╬╗╦╚═╠╗╦║═╦╚╦╬╣╚╬╣╩╚╠╣═╩╦╠═╗╠═╩║╦═╚╗╩╠═╗╠═╦╣╩═║╠╦╚═╗╚╗╦╬
╩╬║╠╬╦╚╣╚╬╩╗═╚╣╩╦═╣╠╬╣╦╠╚╣╩╬╦╠╬║╣═╦╠═╦╠║╣╬╩╚╩╠═╣╚═╦╗╦╬╚╗═╦╠╗╚═╦║╬╚╣╦═║╠╩╠═╣╦╠╣═╩
╬╠╩║╩╚╬╗╚═╩╣╩═╚║╦╬╗╚╩╚═╗╦║╠╬╚╗╩╬═╣╩╚╦╣═╠═║╚╩╣╬╦╠╠═║╦╚╗═╦═║╦╚╦╣╠═╬║╦╠╩╗╠╬═╦╣╠╬╣╦╠
╠╣═╦═╦╚╗╦║╬╠╦╗═╚╣╬╦╠╩╬╣╚═╩╠╣╣═╦╠╩═╚╗╬╦╚╣╚╬╦╣═╠╗╦╬╦╚╗╦╗═╚╬╗╚╩╩╬╣╚╬╦╠╣═╠╣╦╗═╦╠╠╬╣╦
╦╗═╚╬╚╗╩╩═╣╚╦╠═╣╦╣╠╬╬╩╚╗╚═╩╣═╚╗╦╗╬╦╚╦═╣╚═╣╦╠╚═╦╗╣╩╚╬╩╚╬╗║═╩╚╦═║╠╬╩╚╣╠═╩╣═╣╦╚╬╣╠╦
╬╣╚╦╚═╗╦╠╗═╦╣═╦╚╠╬╣╦═║╚╩╗╩╚═╩╚═╣╩╗╬╚╦╣═╠╩╬║╠═╣╦╠╦╗╠═╬╦╠╣═╠╣╦═╗╦╠═╦╚║╩╣╚═╠═╣╦╣╦═╠
═╗╩╠╦╣╠══╗╦╠╠╬╩╗║═╩╚╬╩╚╗╚╣╩═╩╠═║╬╣╚╦╣╬╩╚╚╬╗╩═╚╩╣╬╦╠║╚╗╦═║╬╦╚╩╚╬╗╗╬╩╚╬╦╚╣╣╩╠══╦╚╗
╣╚╩╬═╩╗╚╣═╚╩╗╬╩╚╦═╣╠╬╣╦╠═╗╚╦╚╬╗╦╗═╠╦╚╬╩╗╬╚╣╦╣═╦╠╦═╗╚╬╩╚╗║═╩╚╦╬╗╚═╗╩╚╦═╗╚╬╦╚╗═╠╗╦
╠╦═╗╣╬╠╦║═╩╚╦╚╬╗╗═╩╠═╩║╚╬╦╚╗═╚╩╗╦╚╗═╦╚╬╗╠═╦╗╩═╣╠╦╚═╗╚╣╩╬╚╩═╗╚═╣╩╬╚╩╗╩╚╣══╣╦╠║╬╩╠
╗╠═╦║╚═╩╗╠═╦╗╚═╦╗╚╬╦╗╠═╦╣╠═╦╗╚═╦╗╚╬╩╗╚═╦╗╚╬╦╗╠═╦╗╠═╦╣╠╬╦║╚═╩╗╚╬╦╗╠═╩╣╚╬╦║╠═╦╗╚╬╩
╣╠═╦╗╚╬╦╗╚═╦╗╚╬╦╗╠═╦╣╚═╩╣╠═╦╗╚═╦╣╠╬╦╗╚╬╩║╚═╩╣╠═╩║╠╬╩╣╚═╦╣╠═╦║╚═╩╗╚╬╦╗╚═╩║╠═╦╣╚╬╦
╗╚╬╦╗╠═╦╣╚╬╦║╠═╦║╠╬╦║╚═╩║╠═╩║╚╬╦╣╠═╩╣╠═╦╣╠═╦║╠╬╦╗╚╬╩║╠╬╦╗╚═╦╗╚╬╩╗╚═╦╣╠═╩╣╠═╩╗╚╬╩
║╚═╩║╠═╩╣╠═╦║╠╬╦╗╚═╦╗╚╬╦╗╠═╦╣╚╬╦║╠═╦║╠╬╦║╚═╩╣╠╬╩║╠═╩╣╠═╦╗╚═╦╣╠═╩║╠╬╦╗╚═╦╗╠═╦╗╚═╦
║╠╬╩╗╠╬╩╣╚═╩╣╠═╦╗╚╬╦╗╚╬╩╣╚═╩╣╠═╦║╠╬╩║╚═╦╣╚╬╦╣╚╬╩╣╠═╩╗╠═╦╗╚═╩╣╠═╦╗╚╬╩╗╚╬╩╣╚═╩╣╠═╦
║╠═╩╗╚╬╩╣╚═╩╣╠═╦║╠╬╩╗╠╬╩╣╠═╦╣╠╬╦╣╠═╦╣╚═╩╣╚╬╦║╠╬╦║╚╬╦║╚═╩╗╚╬╩╗╚═╦╣╚═╦╣╠═╩╣╠═╦╗╚═╦
╗╚╬╦╗╠═╦╗╠═╦╣╠═╦╣╠═╩║╚═╩╗╚═╩╣╚═╩╗╚╬╩╣╠═╦╗╠═╦║╚═╩╗╚╬╦║╚╬╦╗╚═╦╣╠╬╦╗╚╬╩║╚═╩╣╠═╦║╠╬╦
╗╚═╦╗╚╬╦╗╠═╦║╚═╩╗╚╬╦║╚╬╦╣╠╬╦╣╠═╦║╠╬╦╣╠═╦╗╚╬╦╗╚╬╩║╠╬╦╗╠╬╩╣╚═╩║╚═╩║╚═╦╣╚═╩╗╚╬╩╣╚═╩
╣╠═╦║╠╬╩╗╚═╩╗╚═╦║╚╬╩╣╠═╦╗╚═╦╗╠╬╩╗╚═╦║╠╬╩║╠═╦╣╠╬╦╣╠═╦╣╠═╦╣╠═╩║╠╬╩╗╚═╦╗╚╬╦╗╠═╦╣╠═╦
╗╚═╦╗╚═╩╣╠═╦╣╠╬╦╣╠═╩║╠╬╩╗╚═╦║╚═╦║╚═╦╣╠═╦║╚╬╦╗╚╬╩╣╠═╦╗╠═╦╣╠╬╩╣╠╬╩</pre>


* Decryption of the cyphertext obtained above:\
&emsp;*> python madhatter.py -d -i "input.txt" -s "cool1" -o "output.txt"*
\
\
**input.txt:**
<pre>═╗╚╦╠║╬╦╠═║╦╬╚╣╦╠╬╣╦╬╚╗╩╚╣═╩═╣╦╠╣╩╚═╣╬╦╚╦═╣╚═╣╦╚╚║═╩╩╚╬╗╠╬╦║╦╬╚╣╠═║╦╗╬╚╩╣═╩╚╠═╣╦
╬║╠╦╩═╣╚╩╚═║╠╣╦╬╠╦═╣╠╬╗╩═╚╩║╩╚╗╬═╣╩╚╗╬╩╠═╩╚╣╦╬╚╣═╩╠║╩╚╬╗╚═╩╣═╦╠╣╠╬╦║═╠╣╦╩╗╬╚╚═╗╦
╠═╣╩╦╠╣═╬║╦╠═╚╗╦╬╦╠╣╣═╦╠╦╚═║╣╬╦╚╦╚╬╗║═╦╚╠═╦╣╠╬╣╦╗╦╚╬═╦╠╣╠╦═╗╚╩═║╬╗╦╚╬╩╚╗╚╣═╩═╣╦╠
═╠╗╦╚╦═╗╩║╬╠╬╦╠║╦╚╬╣╠═╦║╬╩╚╗╚═╩╣═╠╣╦╚║╩═╦╣╠╬╚╬║╦╠═╣╦╗═╦╚╦═║╚╣╦╠═╦╚═╗╗╬╦╚╦═╗╠╚╬║╦
╣╬╠╦╣╬╦╚╦║╠╬╬╦╚║╠╣═╦╦╠╣╬╚═║╩╚╗╬╩╬╠║╩╬╗╩╚╣╩═╚╦╠═╣╬╠╩║╬╗╩╠╣═╦╠╦╬╣╠═╦╠╣╗═╦╚╩═║╠═╣╦╠
╬╠╦╣╠╬╣╦║╬╠╩╦║═╠╬╚╣╦╠╣╩══╗╩╠╬╗╩╚╣═╩╚╦═╣╠╬║╩╠╦═╠╗╠╬╣╦╦╣═╠╬╠║╦╦║╬╠╠═╣╦╠═╗╦╩╚║═╬╗╦╚
═╚╣╦╣╦╬╠═║╩╚╚╗═╩╣╚╩═╬╗╚╩═╦╚║╦╚╬╣╠╣═╩╬╦╚╣╚╬╩╣╬╠╣╦╠╦╬║╣═╚╦╠╣═╦═║╩╚╬╦╚╗╚═╩╗╬╚╗╦╬╣╚╦
╚╗╬╩╚═╗╦═╚╣╦╠═╣╩║╬╩╠╦═║╠╚╬╣╦╗╬╚╦╦═╠╗╦╬╣╚║═╦╠╩╬║╠╠═╣╦╣╩╠═╠╣═╩╦╚╬╣╬╠╩╗╦═╗╚╬╦╚╗╠═╦╗
═╚╗╩╬╦╣╠═╣╦╠═╦╠╣╗╬╚╦╣═╦╚╩╚╬╣╬╗╚╩╗╬╚╩╩╣═╚╣╦╠═╬╩╠║╠║╦╬╦╠═╣╣═╩╠╠╗╦═╬╚╦╣╠═║╩╩╗╬╠╚╬╣╦
╣╬╠╦╠╣═╦╦╬║╠╚═╣╩╣╦╚╬╠╦═╣╬║╦╠╠║╬╦═║╚╩╬╗╦╚═╚╦║╣═╦╠╗╩╚╬═╩╚╣╠╣╦═╩╚═║╣╬╦╠╠║╦═╠╣═╦╠═╣╦
╗╬╚╩╚═╩╣═╚╗╦╠═╦╗╬╗╩╚╚╣╦╬╚╣╩╬╩╚═╗╣═╩╚╣╩╠══╦╠╣╚╗╦═╬╩╚╗╚═╩╣═╦╠╣╬╠╣╦╩║╠╬╦╠╬║╚╣╬╦═╩╠╣
═╦╣╠╦║╬╠═╗╦╚╗╬╦╚╦═╗╠╩╠╬╗╠═╦╣╦╬╠╣═╦╠╣╚═╦║═╠╣╩═╦╚╗╦╗═╠║═╩╚╚╬╗╦╦═╚╗╬╗╩╚╣═╩╚╩═║╚═║╦╚
╠╗═╩╚╦═║╚╣╬╩╬╣╦╠═╠╩╣╩╚═║╚╬╗╦╗═╚╩╚╣╩═╗╦╚═╩═║╚╬╣╦╠╠═╩║╩╬╣╚═║╦╚╣═╩╚╠═╣╩╚═║╩╩╠╗═╦╠═╣
╗╬╩╚╚═╣╩╣═╠╦╣═╩╚╦═╗╚═║╩╚╦╬╣╠╬╦╚╣═╠║╦╩╚╬╗╚═╩╣╣═╦╠═║╩╚╠╬╦╣═╚╣╩═╣╦╠═╚╗╦╗═╦╠╠╬║╦╬╗╠╩
╩╣═╚╩╚═║╚═╦║╩═╚╣╩╠╬╗╗═╦╚╬║╠╦╚║═╦╚╬╣╦╩║╠═╩═║╠╦╚╬╣╦╗╚╬╩╠═╣╠╬╩║╣═╦╚╠╬╣╦╣╬╦╚╩╬╗╠╬╗╦╚
╗╩╬╚═╣╩╚╚╣╬╩║╠╦╬╩╬╗╚╚═╣╩╣═╦╠╣╬╦╚╬╗╦╚╠╣╩═║╬╩╠╚╦═║╬╦╠╣╚╗═╦║═╦╠╚╬╗╩═╣╠╩║═╩╚╩╬╗╚╬╗╩╚
═╣╠╩╦╠═╣╚║╬╦╬╣╦╠═╦╗╚║═╚╦╗╬╩╚╩═║╚╬║╦╠═╣╠╦╠═╗╦╗═╚╦╠═╩║╬╚╣╦╚╬╦╗╚═╗╩╗╩╚╬╣═╩╚╦═╣╠═╩╠║
╗╬╩╠╦═╗╚╬║╦╠╬╠╦║╚═╣╩╣╬╚╦╦╣═╠═╠║╩╚═╦╗╠═╗╩║═╩╚╬╚╗╦╚═╗╩╚╣╦═╚╬╣╩╚╬╩╗╚╬╗╩╣═╩╚╣╦╠═╩╠╬║
╣═╩╚╦═╗╚╠═╗╦╣═╠╩╣╬╦╚╬╦╚╗╩═╚╗╚╗═╦╬╗╦╚═╦╠╗║╬╦╠╠╗╩═║═╩╚╠╣═╩╣═╠╩╦═╠║╩╬╚╣╩╣═╠═║╦╠╩═║╚
╬╗╦╚╗╩╚══╣╦╠╦╠╬╣╦╬╠║╦═╗╚╬╗╦╚═╠╗╦║═╦╚╦╬╣╚╬╣╩╚╠╣═╩╦╠═╗╠═╩║╦═╚╗╩╠═╗╠═╦╣╩═║╠╦╚═╗╚╗╦╬
╩╬║╠╬╦╚╣╚╬╩╗═╚╣╩╦═╣╠╬╣╦╠╚╣╩╬╦╠╬║╣═╦╠═╦╠║╣╬╩╚╩╠═╣╚═╦╗╦╬╚╗═╦╠╗╚═╦║╬╚╣╦═║╠╩╠═╣╦╠╣═╩
╬╠╩║╩╚╬╗╚═╩╣╩═╚║╦╬╗╚╩╚═╗╦║╠╬╚╗╩╬═╣╩╚╦╣═╠═║╚╩╣╬╦╠╠═║╦╚╗═╦═║╦╚╦╣╠═╬║╦╠╩╗╠╬═╦╣╠╬╣╦╠
╠╣═╦═╦╚╗╦║╬╠╦╗═╚╣╬╦╠╩╬╣╚═╩╠╣╣═╦╠╩═╚╗╬╦╚╣╚╬╦╣═╠╗╦╬╦╚╗╦╗═╚╬╗╚╩╩╬╣╚╬╦╠╣═╠╣╦╗═╦╠╠╬╣╦
╦╗═╚╬╚╗╩╩═╣╚╦╠═╣╦╣╠╬╬╩╚╗╚═╩╣═╚╗╦╗╬╦╚╦═╣╚═╣╦╠╚═╦╗╣╩╚╬╩╚╬╗║═╩╚╦═║╠╬╩╚╣╠═╩╣═╣╦╚╬╣╠╦
╬╣╚╦╚═╗╦╠╗═╦╣═╦╚╠╬╣╦═║╚╩╗╩╚═╩╚═╣╩╗╬╚╦╣═╠╩╬║╠═╣╦╠╦╗╠═╬╦╠╣═╠╣╦═╗╦╠═╦╚║╩╣╚═╠═╣╦╣╦═╠
═╗╩╠╦╣╠══╗╦╠╠╬╩╗║═╩╚╬╩╚╗╚╣╩═╩╠═║╬╣╚╦╣╬╩╚╚╬╗╩═╚╩╣╬╦╠║╚╗╦═║╬╦╚╩╚╬╗╗╬╩╚╬╦╚╣╣╩╠══╦╚╗
╣╚╩╬═╩╗╚╣═╚╩╗╬╩╚╦═╣╠╬╣╦╠═╗╚╦╚╬╗╦╗═╠╦╚╬╩╗╬╚╣╦╣═╦╠╦═╗╚╬╩╚╗║═╩╚╦╬╗╚═╗╩╚╦═╗╚╬╦╚╗═╠╗╦
╠╦═╗╣╬╠╦║═╩╚╦╚╬╗╗═╩╠═╩║╚╬╦╚╗═╚╩╗╦╚╗═╦╚╬╗╠═╦╗╩═╣╠╦╚═╗╚╣╩╬╚╩═╗╚═╣╩╬╚╩╗╩╚╣══╣╦╠║╬╩╠
╗╠═╦║╚═╩╗╠═╦╗╚═╦╗╚╬╦╗╠═╦╣╠═╦╗╚═╦╗╚╬╩╗╚═╦╗╚╬╦╗╠═╦╗╠═╦╣╠╬╦║╚═╩╗╚╬╦╗╠═╩╣╚╬╦║╠═╦╗╚╬╩
╣╠═╦╗╚╬╦╗╚═╦╗╚╬╦╗╠═╦╣╚═╩╣╠═╦╗╚═╦╣╠╬╦╗╚╬╩║╚═╩╣╠═╩║╠╬╩╣╚═╦╣╠═╦║╚═╩╗╚╬╦╗╚═╩║╠═╦╣╚╬╦
╗╚╬╦╗╠═╦╣╚╬╦║╠═╦║╠╬╦║╚═╩║╠═╩║╚╬╦╣╠═╩╣╠═╦╣╠═╦║╠╬╦╗╚╬╩║╠╬╦╗╚═╦╗╚╬╩╗╚═╦╣╠═╩╣╠═╩╗╚╬╩
║╚═╩║╠═╩╣╠═╦║╠╬╦╗╚═╦╗╚╬╦╗╠═╦╣╚╬╦║╠═╦║╠╬╦║╚═╩╣╠╬╩║╠═╩╣╠═╦╗╚═╦╣╠═╩║╠╬╦╗╚═╦╗╠═╦╗╚═╦
║╠╬╩╗╠╬╩╣╚═╩╣╠═╦╗╚╬╦╗╚╬╩╣╚═╩╣╠═╦║╠╬╩║╚═╦╣╚╬╦╣╚╬╩╣╠═╩╗╠═╦╗╚═╩╣╠═╦╗╚╬╩╗╚╬╩╣╚═╩╣╠═╦
║╠═╩╗╚╬╩╣╚═╩╣╠═╦║╠╬╩╗╠╬╩╣╠═╦╣╠╬╦╣╠═╦╣╚═╩╣╚╬╦║╠╬╦║╚╬╦║╚═╩╗╚╬╩╗╚═╦╣╚═╦╣╠═╩╣╠═╦╗╚═╦
╗╚╬╦╗╠═╦╗╠═╦╣╠═╦╣╠═╩║╚═╩╗╚═╩╣╚═╩╗╚╬╩╣╠═╦╗╠═╦║╚═╩╗╚╬╦║╚╬╦╗╚═╦╣╠╬╦╗╚╬╩║╚═╩╣╠═╦║╠╬╦
╗╚═╦╗╚╬╦╗╠═╦║╚═╩╗╚╬╦║╚╬╦╣╠╬╦╣╠═╦║╠╬╦╣╠═╦╗╚╬╦╗╚╬╩║╠╬╦╗╠╬╩╣╚═╩║╚═╩║╚═╦╣╚═╩╗╚╬╩╣╚═╩
╣╠═╦║╠╬╩╗╚═╩╗╚═╦║╚╬╩╣╠═╦╗╚═╦╗╠╬╩╗╚═╦║╠╬╩║╠═╦╣╠╬╦╣╠═╦╣╠═╦╣╠═╩║╠╬╩╗╚═╦╗╚╬╦╗╠═╦╣╠═╦
╗╚═╦╗╚═╩╣╠═╦╣╠╬╦╣╠═╩║╠╬╩╗╚═╦║╚═╦║╚═╦╣╠═╦║╚╬╦╗╚╬╩╣╠═╦╗╠═╦╣╠╬╩╣╠╬╩</pre>
\
**output.txt:**
<pre>First text:
asforthehobbitsoftheshirewithwhomthesetalesareconcernedinthedaysoftheirpeaceandp
rosperitytheywereamerryfolktheydressedinbrightcoloursbeingnotablyfondofyellowand
greenbuttheyseldomworeshoessincetheirfeethadtoughleatherysolesandwerecladinathic
kcurlinghairmuchlikethehairoftheirheadswhichwascommonlybrownthustheonlycraftlitt
lepractisedamongthemwasshoemakingbuttheyhadlongandskillfulfingersandcouldmakeman
yotherusefulandcomelythingstheirfaceswereasarulegoodnaturedratherthanbeautifulbr
oadbrighteyedredcheekedwithmouthsapttolaughterandtoeatinganddrinkingandlaughthey
didandeatanddrinkoftenandheartilybeingfondofsimpleestsatalltimesandofsixmealsada
ywhentheycouldgetthemtheywerehospitableanddelightedinpartiesandinpresentswhichth
eygaveawayfreelyandeagerlyacceptedxx

Second text:
frododrewtheringoutofhispocketagainandlookedatititnowappearedplainandsmoothwitho
utmarkordevicethathecouldseethegoldlookedveryfairandpureandfrodothoughthowrichan
dbeautifulwasitscolourhowperfectwasitsroundnessitwasanadmirablethingandaltogethe
rpreciouswhenhetookitouthehadintendedtoflingitfromhimintotheveryhottestpartofthe
firebuthefoundnowthathecouldnotdosonotwithoutagreatstruggleheweighedtheringinhis
handhesitatingandforcinghimselftorememberallthatgandalfhadtoldhimandthenwithanef
fortofwillhemadeamovementasiftocastitawaybuthefoundthathehadputitbackinhispocket
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</pre>