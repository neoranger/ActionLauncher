# -*- coding: utf-8 -*-
## Action Launcher Bot: This is a bot how can shoots differents action depends commands
## Code wrote by Zagur of PortalLinux.es and modified for NeoRanger of neositelinux.com.ar
## For a good use of the bot please read the README file
 
import telebot 
from telebot import types 
import time 
import random
import datetime
import os
import commands
import token
 
TOKEN =  token.token_id
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba) 
#############################################
#Funciones
@bot.message_handler(commands=['temp']) 
def command_kick(m): 
    temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd/ measure_temp')
    cid = m.chat.id 
    bot.send_photo( cid, temp)


 
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
