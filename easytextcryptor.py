#EasyTextCryptor by Dmitry https://github.com/gtashnik
#Licensed under GPL v3

import random
from re import *
from random import choice
from re import  findall

#FUNCTIONS of MENU1 

def vozvrat(txt):
		tmp = r"[0-9]+"
		return findall(tmp, txt)
    
def decrypt(message, final="", keys=[]):
	keys = input('Write or paste the key: ')	
	for index, symbol in enumerate(message):
		final += chr((ord(symbol) - int(vozvrat(keys)[index]) - 13) % 26 + ord('A'))
	return final
	
def encrypt(message, final="", keys=[]):
	for symbol in message:
		key = random.randint(0, 25)
		keys.append(str(key))
		final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
	return final, '.'.join(keys)


# END of functions of MENU1

def menu1():
	print('#')
	print("Easy Text Cryptor v1 by Dmitry https://github.com/gtashnik")
	print('#')
	print('# Please remember, that ONLY LATIN LETTERS ARE ALLOWED  ')
	print('# Do not use figures like 123 or any symbols like !,.@ etc.')
	print('#')
	print('Please, type in to choose: ')
	print("1 - Encrypt text")
	print('2 - Decrypt text')
	print('0 - Exit menu')
	menu1 = int(input())
	
	if menu1 == 1:
		inputMessage = input("Type in or past the message you want to be encrypted:  ").upper()
		print("---------------------- ")
		result = encrypt(inputMessage)
		f = open( ('encrypted_v.txt'), 'w', encoding='utf-8'	) # creatig a file to write
		f.write('The first block is encrypted text \n')
		f.write('The second block is a unique key to decrypt this text message \n\n\n')
		for item in result:
			f.write('%s\n\n' % item)
		f.close()
		print('Encrypted message is written in file encrypted_v.txt in a folder where this program is located')

	elif menu1 == 2:
		inputMessage = input("Type in or past the message you want to be decrypted:  ").upper()
		print("---------------------- ")
		result = decrypt(inputMessage)
		f = open( ('decrypted_v.txt'), 'w', encoding='utf-8'	) # creatig a file to write
		f.write('Decrypted message: \n\n')
		f.write(str(result))
		f.write('\n\n')
		f.write('# In case you found lot of characters T in text,  instead of character T between words should be " " ')
		f.close()
		print("---------------------- ")
		print('Decrypted message is saved in file decrypted_v.txt in a folder where this program is located')

		
		
	elif menu1 == 0:
		print('Bye')
		exit()
	else:
		print('You inputted wrong menu number. PLease, execute this program again') 
		
# END of MENU1	

#begin of program

menu1()

#end of program
	
