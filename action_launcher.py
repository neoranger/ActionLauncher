# -*- coding: utf-8 -*-
# Action Launcher Bot: This is a bot how can shoots differents action depends commands
# Code wrote by Zagur of PortalLinux.es and modified for NeoRanger of neositelinux.com.ar
# For a good use of the bot please read the README file

import telebot 
from telebot import types 
import time 
import random
import datetime
import token
import user
import os
import subprocess
import commands
 
TOKEN =  token.token_id

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages):
	for m in messages: 
		cid = m.chat.id 
		if m.content_type == 'text':
			print ("[" + str(cid) + "]: " + m.text)
bot.set_update_listener(listener) #  
#############################################
#Funciones

#Guardo el user_id que da Telegram para compararlo y securizar el bot
id_user = cid

if id_user == user.user_id :
	@bot.message_handler(commands=['help']) 
	def command_ayuda(m): 
		cid = m.chat.id 
		bot.send_message( cid, "Comandos Disponibles: /help /temp /libre /pwd /espacio /tiempo /info /who /apagar /reiniciar")

	@bot.message_handler(commands=['temp']) 
	def command_temp(m): 
		temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd/ measure_temp')
		cid = m.chat.id 
		bot.send_message( cid, temp)

	@bot.message_handler(commands=['pwd']) 
	def command_pwd(m): 
		pwd = commands.getoutput('pwd')
		cid = m.chat.id 
		bot.send_message( cid, pwd)
    
	@bot.message_handler(commands=['espacio']) 
	def command_espacio(m): 
		info = commands.getoutput('df -h')
		cid = m.chat.id 
		bot.send_message( cid, info)
    
	@bot.message_handler(commands=['tiempo']) 
	def command_tiempo(m): 
		tiempo = commands.getoutput('uptime')
		cid = m.chat.id 
		bot.send_message( cid, tiempo)
    
	@bot.message_handler(commands=['libre']) 
	def command_libre(m): 
		libre = commands.getoutput('free -m')
		cid = m.chat.id 
		bot.send_message( cid, libre)
 
	@bot.message_handler(commands=['info']) 
	def command_libre(m): 
		screenfetch = commands.getoutput('screenfetch -n')
		cid = m.chat.id 
		bot.send_message( cid, screenfetch) 

#@bot.message_handler(commands=['who']) 
#def command_libre(m): 
#    who = commands.getoutput('who')
#    cid = m.chat.id 
#    bot.send_message( cid, who) 
    
#@bot.message_handler(commands=['apagar']) 
#def command_apagar(m): 
#    apagar = commands.getoutput('poweroff')
#    cid = m.chat.id 
#    bot.send_message( cid, apagar) 
    
#@bot.message_handler(commands=['reiniciar']) 
#def command_reboot(m): 
#    reiniciar = commands.getoutput('reboot')
#    cid = m.chat.id 
#    bot.send_message( cid, reiniciar)

	@bot.message_handler(commands=['id']) 
	def command_id(m): 
		cid = m.chat.id 
		bot.send_message( cid, cid )
 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
