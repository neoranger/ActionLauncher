# -*- coding: utf-8 -*-
## Action Launcher Bot: This is a bot how can shoots differents action depends commands
## Code wrote by Zagur of PortalLinux.es and modified for NeoRanger of neositelinux.com.ar
## For a good use of the bot please read the README file
 
import telebot 
from telebot import types 
import time 
import random
import datetime
import token
import os
from subprocess import commands
 
TOKEN =  token.token_id
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages):
	for m in messages: 
		cid = m.chat.id 
		if m.content_type == 'text':
			print ( "[" + str(cid) + "]: " + m.text )
bot.set_update_listener(listener) #  
#############################################
#Funciones
@bot.message_handler(commands=['temp']) 
def command_temp(m): 
    temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd/ measure_temp')
    cid = m.chat.id 
    bot.send_photo( cid, temp)

@bot.message_handler(commands=['actualizar']) 
def command_update(m): 
    update = commands.getoutput('sudo pacman -Syu')
    cid = m.chat.id 
    bot.send_photo( cid, update)

 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
