# -*- coding: utf-8 -*-
# Action Launcher Bot: This is a bot how can shoots differents action depends commands
# Code wrote by Zagur of PortalLinux.es and modified by NeoRanger of neositelinux.com.ar
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
import sys
import json
from os.path import exists
import StringIO


triggers = {}
tfile = "triggers.json"
ignored = []
separator = '/'
#user = [line.rstrip('\n') for line in open('user.txt','rt')]

TOKEN =  token.token_id

bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True # Skip the pending messages
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

@bot.message_handler(commands=['ping']) 
def command_test(m):
    cid = m.chat.id
    bot.send_message(cid, "Pong")

@bot.message_handler(commands=['help']) 
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message(cid, "Comandos Disponibles: /help /ping /temp(admin) /free(admin) /df(admin) /uptime(admin) /info(admin) /who /repoup(admin) /sysup(admin) /distup(admin) /osversion(admin) /shutdown(admin) /reboot(admin)")

@bot.message_handler(commands=['temp']) 
def command_temp(m): 
    temp = commands.getoutput('sudo vcgencmd measure_temp')
    send_message_checking_permission(m, temp)
    
@bot.message_handler(commands=['df']) 
def command_espacio(m): 
    info = commands.getoutput('df -h')
    send_message_checking_permission(m, info)

@bot.message_handler(commands=['uptime']) 
def command_tiempo(m):
    tiempo = commands.getoutput('uptime')
    send_message_checking_permission(m, tiempo)
	
@bot.message_handler(commands=['free']) 
def command_libre(m): 
    libre = commands.getoutput('free -m')
    send_message_checking_permission(m, libre)

@bot.message_handler(commands=['info']) 
def command_info(m): 
    screenfetch = commands.getoutput('screenfetch -n')
    send_message_checking_permission(m, screenfetch)

@bot.message_handler(commands=['who']) 
def command_who(m): 
    who = commands.getoutput('who')
    send_message_checking_permission(m, who)
    
@bot.message_handler(commands=['shutdown']) 
def command_shutdown(m):
	shutdown = commands.getoutput('poweroff')
	send_message_checking_permission(m, shutdown)
    
@bot.message_handler(commands=['reboot']) 
def command_reboot(m):
	reboot = commands.getoutput('reboot')
	send_message_checking_permission(m, reboot)
	
@bot.message_handler(commands=['repoup']) 
def command_repoup(m):
	repoup = commands.getoutput('sudo apt-get update')
	send_message_checking_permission(m, repoup)
	
@bot.message_handler(commands=['sysup']) 
def command_sysup(m):
	sysup = commands.getoutput('sudo apt-get upgrade')
	send_message_checking_permission(m, sysup)
	
@bot.message_handler(commands=['distup']) 
def command_distup(m):
	distup = commands.getoutput('sudo apt-get dist-upgrade')
	send_message_checking_permission(m, distup)

@bot.message_handler(commands=['osversion']) 
def command_osversion(m):
    osversion = commands.getoutput('lsb_release -a')
    send_message_checking_permission(m, osversion)
#Otra forma: osversion = commands.getoutput('cat /etc/os-release')
	
@bot.message_handler(commands=['id']) 
def command_id(m): 
    cid = m.chat.id 
    bot.send_message(cid, cid)		

def send_message_checking_permission(m, response):
    cid = m.chat.id
    uid = m.from_user.id
    if uid != user.user_id:
        bot.send_message(cid, "You can't use the bot")
        return
    bot.send_message(cid, response)
    
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
