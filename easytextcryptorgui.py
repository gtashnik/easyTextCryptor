# Easy text cryptor GUI by Dmitry https://github.com/gtashnik
# License: Mozilla public license v2

import tkinter #importing tkinter
from tkinter import * # importing graphic interface
import tkinter.messagebox as box #importing dialog box for tkinter

import random
from re import *
from random import choice
from re import  findall


window = Tk() #making a main window

window.title('Easy text cryptor by Dmitry') #title for window

# INITIALIZING VARIABLES

textMessage = '' # creating a variable for text message
textMessage2 = '' # creating a variable for text message

#global keys
#keys = '' # creating a key variable

#FUNCTIONS 

def vozvrat(txt):
	tmp = r"[0-9]+"
	return findall(tmp, txt)
    
def decrypt(message, final="", keys=[]):
	#global keys
	#keys = '18.13.23.19.25.18.6.12.20.17' # Getting the private key to decrypt message	
	keys2 = entKey.get() # Getting the private key to decrypt message
	keys = str(keys2)
	for index, symbol in enumerate(message):
		final += chr((ord(symbol) - int(vozvrat(keys)[index]) - 13) % 26 + ord('A'))
	return final
	
def encrypt(message, final="", keys=[]):
	for symbol in message:
		key = random.randint(0, 25)
		keys.append(str(key))
		final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
	return final, '.'.join(keys)

def cryptMsg(): #ENCRYPTING OUW MESSAGE
	textMessage = inputMsg.get('1.0', END+ '-1c').upper() #GETTING THE TEXT OF THE MESSAGE
	if (textMessage == ''):
		box.showerror('Message is empty!', 'Please type in text in message or paste in using ctrl + v')
	else:
		result = encrypt(textMessage)
		f = open( ('encrypted.txt'), 'w', encoding='utf-8'	) # creatig a file to write
		f.write('The first block is encrypted text \n')
		f.write('The second block is a unique key to decrypt this text message \n\n\n')
		for item in result:
			f.write('%s\n\n' % item)
		f.close()	
		box.showinfo('Message was encrypted', 'Message was encrypted and saved into file "encrypted.txt" which is located in the same folder with this program. ')
	

def decryptMsg():
	textMessage = inputMsg.get('1.0', END+ '-1c').upper() #GETTING THE TEXT OF THE MESSAGE
	if (textMessage == ''):
		box.showerror('Message is empty!', 'Please type in text in message or paste in using ctrl + v')
	else:
		result = decrypt(textMessage)
		f = open( ('decrypted.txt'), 'w', encoding='utf-8'	) # creatig a file to write
		f.write('Decrypted message: \n\n')
		f.write(str(result))
		f.write('\n\n')
		f.write('# In case you found lot of characters T in text,  instead of character T between words should be " " ')
		f.close()
		box.showinfo('Message was decrypted', 'Message was decrypted and saved into file "decrypted.txt" which is located in the same folder with this program.')

def about():
	box.showinfo('About easy text cryptor', 'Easy text cryptor \n\nCreated by Dmitry\nhttps://github.com/gtashnik\n\nThis program uses the most powerful crypto method. \n\n You can use it for free under MPL v2 license')

def howToUse():
	box.showinfo('How to use', 'To encrypt message just input or paste text using ctrl + v inside the textbox and click on button "Encrypt message".\n\nDO NOT USE SYMBOLS LIKE 123.,@ etc. or ANY SPACES IN MESSAGE!\n\nThen the encrypted message and unique key will be generated.\n\nTo decrypt text just paste it and also unique key and click on button "decrypt message" ')
# END OF FUNCTIONS

# GUI elements 


titlLbl = Label( window, text = 'Easy text cryptor')
titlLbl.pack(padx = 20, pady = 0)
titlLbl.config(font=("Courier", 30))  # making a text confir for label


#frame2.pack(side = LEFT)
titlInput = Label( window, text = 'Input text to encrypt or decrypt')
titlInput.pack(padx = 20, pady = 0)
titlInput.config(font=("Courier", 15))  # making a text confir for label
inputMsg = Text(window, width=50, height=5,) # making a text field to input text
inputMsg.pack(padx = 0, pady = 10)

btn_encrypt = Button( window, text = 'Encrypt message' , command=cryptMsg ) # button to encrypt message
btn_encrypt.pack(padx = 0, pady = 10)

frame = Frame( window ) #creating a frame for generate button
frame.pack(padx = 0, pady = 0)
entKey = Entry( frame) # the entry field for key to decrypt message
entKey.pack(side = RIGHT, padx = 0, pady = 10)

entLbl = Label(frame, text = 'Please, paste in the key \n to decrypt message: ')
entLbl.pack(side = LEFT, padx = 0, pady = 10)

btn_decrypt = Button( window, text = 'Decrypt message' , command=decryptMsg ) # button to encrypt message
btn_decrypt.pack(padx = 0, pady = 10)

frame2 = Frame( window ) #creating a frame2 for buttons
frame2.pack(padx = 0, pady = 0)

btn_info = Button( frame2, text = 'About' , command=about ) # button to show about dialog
btn_info.pack(side = LEFT, padx = 0, pady = 10)

btn_howto = Button( frame2, text = 'How to use' , command=howToUse ) # button to show about how to use dialog
btn_howto.pack(side = LEFT, padx = 0, pady = 10)

btn_close = Button( frame2, text = 'Close program' , command=exit ) # button to close the program
btn_close.pack(side = LEFT, padx = 0, pady = 10)

#btn_about = 

# --- End of GUI elements




# -----

window.mainloop() #closing GUI
