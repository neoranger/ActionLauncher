#!/bin/bash
while true
do
python2 /home/pi/Documents/git/ActionLauncher/action_launcher.py
echo "¡The bot is crashed!"
#echo "ActionLauncherBot is crashed" | mail -s "Aviso" example@gmail.com
echo "Rebooting in:"
for i in 1
do
echo "$i..."
done
echo "###########################################"
echo "#Bot is restarting now                    #"
echo "###########################################"
done
