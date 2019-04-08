# -*- coding: utf-8 -*-
# Action Launcher Bot: This is a bot how can execute differents actions depends commands
# Code wrote by Zagur of PortalLinux.es and modified by NeoRanger of neositelinux.com
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
from os.path import exists
import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#user = [line.rstrip('\n') for line in open('user.txt','rt')]

TOKEN =  token.token_id
bot = telebot.TeleBot(TOKEN) # Creating our bot object.
bot.skip_pending=True # Skip the pending messages
##################################################################
#LISTENER                                                        #
##################################################################
def printUser(msg): #debug function (will print every message sent by any user to the console)
        print str(msg.chat.first_name) + " [" + str(msg.chat.id) + "]: " + msg.text

def listener(messages):
        for m in messages:
                cid = m.chat.id
                if m.content_type == 'text':
                        text = m.text
                        printUser(m) #print the sent message to the console

bot.set_update_listener(listener) #
##################################################################
#FUNCIONES PRINCIPALES DEL BOT (CON SEGURIDAD)                   #
##################################################################

@bot.message_handler(commands=['temp'])
def command_temp(m):
    temp = commands.getoutput('sudo vcgencmd measure_temp')
    send_message_checking_permission(m, temp)

@bot.message_handler(commands=['df'])
def command_espacio(m):
    info = commands.getoutput('inxi -p')
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
    send_message_checking_permission(m, u(screenfetch))

@bot.message_handler(commands=['who'])
def command_who(m):
    who = commands.getoutput('who')
    send_message_checking_permission(m, who)

@bot.message_handler(commands=['shutdown'])
def command_shutdown(m):
	shutdown = commands.getoutput('sudo shutdown -h now')
	send_message_checking_permission(m, shutdown)

@bot.message_handler(commands=['reboot'])
def command_reboot(m):
	reboot = commands.getoutput('sudo reboot')
	send_message_checking_permission(m, reboot)

@bot.message_handler(commands=['repoup'])
def command_repoup(m):
	repoup = commands.getoutput('sudo apt-get update')
	send_message_checking_permission(m, repoup)

@bot.message_handler(commands=['sysup'])
def command_sysup(m):
	sysup = commands.getoutput('sudo apt-get upgrade -y')
	send_message_checking_permission(m, sysup)

@bot.message_handler(commands=['distup'])
def command_distup(m):
	distup = commands.getoutput('sudo apt-get dist-upgrade -y')
	send_message_checking_permission(m, distup)

@bot.message_handler(commands=['osversion'])
def command_osversion(m):
    osversion = commands.getoutput('lsb_release -a')
    send_message_checking_permission(m, osversion)
#Otra forma: osversion = commands.getoutput('cat /etc/os-release')

@bot.message_handler(commands=['screens'])
def command_screens(m):
        screens = commands.getoutput('screen -ls | grep "pi" ')
        send_message_checking_permission(m, screens)

@bot.message_handler(commands=['weather'])
def command_weather(m):
	weather = commands.getoutput('inxi -w')
	send_message_checking_permission(m, weather)

def extract_arg(arg):
	return arg.split()[1:]

@bot.message_handler(commands=['tv_on_off'])
def command_tv_on_off(m):
        status = extract_arg(m.text)
        tv_on_off = commands.getoutput('sudo ./tv_on_off.sh'+status)
#        tv_on_off = subprocess(["sudo ./tv_on_off", status])
        send_message_checking_permission(m, tv_on_off)
		
@bot.message_handler(commands=['ps_ram'])
def command_ps_ram(m):
	ps_ram = commands.getoutput("ps aux | awk '{print $2, $4, $11}' | sort -k2r | head -n 10")
	send_message_checking_permission(m, ps_ram)
	
@bot.message_handler(commands=['ps_cpu'])
def command_ps_cpu(m):
	ps_cpu = commands.getoutput('ps -Ao user,uid,comm,pid,pcpu,tty --sort=-pcpu | head -n 6')
	send_message_checking_permission(m, ps_cpu)


@bot.message_handler(commands=['server_torrent_restart'])
def command_torrent_res(m):
    torrent_res = commands.getoutput('sudo service transmission-daemon restart')
    send_message_checking_permission(m, torrent_res)

##################################################################
#FUNCIONES SIN SEGURIDAD (SIMPLES)                               #
##################################################################
@bot.message_handler(commands=['id'])
def command_id(m):
    cid = m.chat.id
    bot.send_message(cid, cid)

@bot.message_handler(commands=['ping'])
def command_test(m):
    cid = m.chat.id
    bot.send_message(cid, "Pong")

@bot.message_handler(commands=['help'])
def command_ayuda(m):
    cid = m.chat.id
    bot.send_message(cid, "Comandos Disponibles: /help\n /ping\n /temp(admin)\n /free(admin)\n /df(admin)\n /uptime(admin)\n /info(admin)\n /who\n /repoup(admin)\n /sysup(admin)\n /distup(admin)\n /screens(admin)\n /osversion(admin)\n /weather(admin)\n /nmap_all(admin)\n /nmap_active(admin)\n /start_nginx(admin)\n /stop_nginx(admin)\n /restart_nginx(admin)\n /bot_update(admin)\n /shutdown(admin)\n /reboot(admin)\n /ps_ram(admin)\n /ps_cpu(admin)\n")

#@bot.message_handler(commands=['apache'])
#def command_test(m):
#    cid = m.chat.id
#    bot.send_document(cid, '/home/ubuntu/apache2.conf','rb')

##################################################################
#MANEJO DEL SERVIDOR NGINX Y UPDATE DEL BOT VIA GIT              #
##################################################################
@bot.message_handler(commands=['start_nginx'])
def command_start_nginx(m):
	nginx_start = commands.getoutput('sudo service nginx start')
	send_message_checking_permission(m, nginx_start)

@bot.message_handler(commands=['stop_nginx'])
def command_stop_nginx(m):
	nginx_stop = commands.getoutput('sudo service nginx stop')
	send_message_checking_permission(m, nginx_stop)

@bot.message_handler(commands=['restart_nginx'])
def command_restart_nginx(m):
	nginx_restart = commands.getoutput('sudo service nginx restart')
	send_message_checking_permission(m, nginx_restart)

@bot.message_handler(commands=['bot_update'])
def command_bot_update(m):
    git_pull = commands.getoutput('git pull')
    send_message_checking_permission(m, git_pull)

@bot.message_handler(commands=['nmap_all'])
def command_nmap_all(m):
        nmap_all = commands.getoutput('sudo nast -m -i eth0')
        send_message_checking_permission(m, nmap_all)

@bot.message_handler(commands=['nmap_active'])
def command_nmap_active(m):
        nmap_active = commands.getoutput('sudo nast -g -i eth0')
        send_message_checking_permission(m, nmap_active)

##################################################################
# FUNCION PARA CHEQUEAR PERMISOS A LA HORA DE EJECUTAR COMANDOS  #
##################################################################
def send_message_checking_permission(m, response):
    cid = m.chat.id
    uid = m.from_user.id
    if uid != user.user_id:
        bot.send_message(cid, "You can't use the bot")
        return
    else:
        bot.send_message(cid, "Triggering...")
        bot.send_message(cid, response)

#def send_message_checking_permission(m, response):
#    try:
#        cid = m.chat.id
#        uid = m.from_user.id
#        if uid != user.user_id:
#            bot.send_message(cid, "You can't use the bot")
#        return
#        bot.send_message(cid, response)
#
#    except Exception as e:
#        bot.reply_to(m, 'ops, hubo un error')
#        bot.send_message(cid, str(e))

##################################################################
#PETICIONES                                                      #
##################################################################
print ("Bot Started")
print ("Thanks for using ActionLauncherBot. Please visit us: https://www.neositelinux.com")
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
