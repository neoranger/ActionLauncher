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

def is_recent(m):
    return (time.time() - m.date) < 60

#Check if Triggers file exists.
if exists(tfile):
    with open(tfile) as f:
        triggers = json.load(f)
else:
    #print("Triggers file not found, creating.")
    with open(tfile,'w') as f:
        json.dump({}, f)

#Function to add new Trigger - Response
def newTrigger(trigger, response):
    triggers[trigger.lower()] = response
    with open(tfile, "w") as f:
        json.dump(triggers, f)
    #print("triggers file saved")
    
#Delete whitespaces at start & end
def trim(s):
    i = 0
    while(s[i] == ' '):
        i += 1
    s = s[i:]
    i = len(s)-1
    while(s[i] == ' '):
        i-= 1
    s = s[:i+1]
    return s    

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

#Adds another trigger-response. ex: "/add Hi / Hi!! :DD"
@bot.message_handler(commands=['add'])
def add(m):
    cid = m.chat.id
    text = m.text[4:]
    #print("Apending :" + text)
    try:
        i = text.rindex(separator)
        #print("I value = " + str(i))
        tr = text[:i]
        re = text[i+1:]
        tr = trim(tr)
        re = trim(re)
        #print("TR = [" + tr + "] - RE = [" + re + "]")
        newTrigger(tr,re)
        bot.send_message(cid, "Trigger Added: Trigger["+tr+"] - Response["+re+"]")
    except:
        bot.send_message(cid, "Bad Arguments.")

#Answers with the size of triggers.
@bot.message_handler(commands=['size'])
def size(m):
    cid = m.chat.id
    bot.send_message(cid, "Size of Triggers list = " + str(len(triggers)))

@bot.message_handler(commands=['ping']) 
def command_test(m):
    cid = m.chat.id
    bot.send_message(cid, "Pong")

@bot.message_handler(commands=['help']) 
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message(cid, "Comandos Disponibles: /help /ping /temp /free /df /uptime /info /who /repoup /sysup /distup /shutdown /reboot")

@bot.message_handler(commands=['temp']) 
def command_temp(m): 
    temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd/ measure_temp')
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
	repoup = commands.getoutput('sudo aptitude update')
	send_message_checking_permission(m, repoup)
	
@bot.message_handler(commands=['sysup']) 
def command_sysup(m):
	sysup = commands.getoutput('sudo aptitude upgrade')
	send_message_checking_permission(m, sysup)
	
@bot.message_handler(commands=['distup']) 
def command_distup(m):
	distup = commands.getoutput('sudo aptitude dist-upgrade')
	send_message_checking_permission(m, distup)
	
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
    
#Catch every message, for triggers :D
@bot.message_handler(func=lambda m: True)
def response(m):
    if(m.from_user.id in ignored):
        return
    #print("Checking for triggers in Message [" + m.text + "]")
    for t in triggers:
        if t in m.text:
            bot.reply_to(m, triggers[t])
    pass

#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
