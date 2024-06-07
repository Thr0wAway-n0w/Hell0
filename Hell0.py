def yeep():  
    os.system('python3 -m pip install pyqt5 --upgrade')
    os.system('pip3 install colorama')
    os.system('pip3 install pillow')
    os.system('pip3 install ascii_magic')
    os.system('pip3 install pyautogui')
    os.system('sudo apt install libncurses5-dev')
    os.system('sudo apt install ncurses-hexedit')
    os.system('pip3 install httpx')
    os.system('pip3 install trio')
    os.system('pip3 install geopy')
    os.system("pip3 install xdotool")
    os.system("sudo apt install xdotool")
    os.system('pip install --upgrade pytz')
    os.system("sudo apt install python3-docker")
    os.system("sudo apt install bb")
    os.system("pip3 install dnspython")
    os.system("sudo apt install proxychains")
    os.system('pip3 install reportlab')
    os.system('sudo apt install lynx')
    os.system('sudo apt install gnome-terminal')
    os.system('sudo apt install gnome-terminal-data')
import os
os.system('pip3 install tk')
os.system('pip3 install termcolor')
import subprocess
import re
import tk
import termcolor
import colorama
from termcolor import colored
import time
os.system("pip3 install asyncio")
import asyncio   

def header():
    print("\033[92m☠\033[91m----------------------------------------------------\033[0mWelcome To \033[31mHELL\033[0m.\033[92m0\033[0m\033[91m-----------------------------------------------------------------\033[92m☠\033[0m")
    print("                                                    \033[31m☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠\033[0m                                                             ")
    print(" ")
def change():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

def update():
    os.system("sudo apt-get update")
    os.system("sudo apt full-upgrade -y")
    os.system("sudo apt autoremove")
def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')

def peey():
    clear_screen()
    print(colored("-------------------------------------------------------------------------------FIRST TIME RUNNING?----------------------------------------------------------------------------------", 'yellow', attrs=['reverse', 'blink', 'bold']))  
    print("1) Upgrade Linux")
    print("2) First Time Using?")
    print("3) I've Used This Before")  
    option = input("> ")

    if option == "1":
        os.system("sudo apt-get update")
        os.system("sudo apt full-upgrade -y")
        os.system("sudo apt autoremove")
    elif option == "2":
        yeep()
    elif option == "3":
        time.sleep(.1)

clear_screen()
print(colored("------------------------------------------------------------------------ARE YOU RUNNING IN A VIRTUAL ENVIRONMENT?------------------------------------------------------------------------", 'yellow', attrs=['reverse', 'blink', 'bold']))  
print("1) Yes")
print("2) No")  
option = input("> ")
    
if option == "1":
    peey()
elif option == "2":
    print(colored("TYPE/RUN THE COMMAND 'pipenv shell'. THEN 'cd' TO THE FILES LOCATION and RUN Hell0.py AGAIN!", 'red', attrs=['reverse', 'blink', 'bold'])) 
    time.sleep(1)
    os.system("pip3 install pipenv")
    exit()

import sys
import json
import requests
from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init
from PIL import ImageEnhance
from ascii_magic import AsciiArt
from geopy.distance import geodesic
import tk
from tkinter import *
from tkinter import simpledialog
import base64
import curses, random
import webbrowser
import pyautogui
import trio
import xdotool
import pexpect
import httpx
import threading
import shutil
import urllib.parse
import socket
import hashlib
import atexit
import aiohttp

num_xterms = 0

screen = curses.initscr()
width = screen.getmaxyx()[1]
height = screen.getmaxyx()[0]
size = width * height
char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
b = []

curses.curs_set(0)
curses.start_color()
curses.init_pair(1, 0, 0)
curses.init_pair(2, 1, 0)
curses.init_pair(3, 3, 0)
curses.init_pair(4, 4, 0)
screen.clear()
for i in range(size + width + 1):
    b.append(0)

start_time = time.time()

while time.time() - start_time < 6:
    for i in range(int(width / 9)):
        b[int((random.random() * width) + width * (height - 1))] = 65
    for i in range(size):
        b[i] = int((b[i] + b[i + 1] + b[i + width] + b[i + width + 1]) / 4)
        color = (4 if b[i] > 15 else (3 if b[i] > 9 else (2 if b[i] > 4 else 1)))
        if (i < size - 1):
            screen.addstr(int(i / width),
                          i % width,
                          char[(9 if b[i] > 9 else b[i])],
                          curses.color_pair(color) | curses.A_BOLD)

    screen.refresh()
    screen.timeout(30)
    if (screen.getch() != -1):
        break

curses.endwin()
screen.clear

try:
    my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')
except OSError as e:
    
    print(f'Could not load the image, server said: {e.code} {e.msg}')
my_art.to_terminal()

_command = " -f /path/to/.conf"

def func(request_type):
    return getattr(requests, request_type)

class MyClientSession(aiohttp.ClientSession):
    def __init__(self):
        super().__init__()
        atexit.register(self.close)

async def close(self):
    await super().close()

async def main():
    session = MyClientSession()
    # Use your client session here
    await session.get('http://example.com')
    await session.close()

def install_pipenv():
    os.system('pip3 install pipenv')
   
def clone_repo(url, folder_name):
    clear_screen()
    ascii_banner()
    print(colored("CLONING REPOSITORY...", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    os.system('git clone ' + url)
    os.chdir(folder_name)
    os.system("git fetch")
    os.system("git pull")
    clear_screen()

def install_requirements():
    clear_screen()
    ascii_banner()
    print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    os.system('python3 -m pip install -r requirements.txt')
    clear_screen()

def search_username(username, script_name):   
    print(colored("User 0sint", 'red', attrs=['reverse', 'blink', 'bold']))
    os.system('python3 ./' + script_name + ' ' + username)

def search_email(email, script_name):
    print(colored("Email 0sint", 'red', attrs=['reverse', 'blink', 'bold']))
    os.system(script_name + ' ' + email)


    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    recycle_bin_path = os.path.join(desktop_path, 'Recycle Bin')
    if not os.path.exists(recycle_bin_path):
        trash_path = os.path.join(desktop_path, 'Trash')
        if os.path.exists(trash_path):
            recycle_bin_path = trash_path

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
    
        if os.path.isdir(item_path) and item in folders_to_delete:
            shutil.move(item_path, recycle_bin_path)

def ascii_banner():
    try:
        my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')      
    except OSError as e:
        print(f'Could not load the image, server said: {e.code} {e.msg}')
    my_art.to_terminal()

def multi_banner():
    print("            \033[93m⣀⣤⠶⠖⢛⣻⡿\033[31m                         ⣀⡔                 ")
    print("            \033[93m ⢠⣶⣋⣩⣤⠶⠾⣿⡁\033[31m                 ⢀⣀⣴⣿⠋                ")  
    print("            \033[93m ⠈⠉⠉\033[97m⣠⣴⣾⣿⣿⣿⣷⣄              \033[91m⣴⣿⣿⣿⣿⣿⣷\033[31m⣤⣀⣀⡤")             
    print("            \033[97m  ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧    ⢀⣠⣴⣶⡇  \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏              ")
    print("            \033[97m  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆ ⣠⣶⣿⣿⣿⣿⠃  \033[91m⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              ")
    print("            \033[97m  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠃  \033[91m⢠⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿              ")
    print("            \033[97m  ⣿⣿⣿⣿⣿⡿⣫⣷⣾⣿⣿⣿⣿⣿⣿⣿⡏   \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿              ")
    print("          \033[97m   ⢀⣿⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟    \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⡄             ")
    print("          \033[97m   ⢪⣿⣿⢟⣽⣿⣿⡿⣫⣽⣿⣿⣿⣿⣿⡟    \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣷⣝⠿⣿⣏             ")
    print("         \033[97m    ⢹⣫⣶⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⣿⣿⡁⡀  \033[91m⢠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣷⣮⣃             ")
    print("      \033[97m   ⢀⣠⣤⣶⣿⣿⡿⠟⢭⣾⡿⣻⣿⣿⣿⣿⣿⣿⣿⡟⠁   \033[91m⢹⣿⣿⣿⣿⣿⣿⣿⣯⣻⠿⠮⠙⠿⣿⣿⣿⣶⣤⣄⡀        ")
    print("     \033[97m⣀⣤⣶⣿⡿⠿⠿⠿⢛⠋   ⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃    \033[91m⢈⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃  ⣀⣈⣙⣛⣛⣻⠿⠿⢿⣶⣤⣀    ")
    print("  \033[97m⢀⣴⣿⠟⠉ ⣰⣾⣿⣿⣿⣿⣿⡿⣷⣦⡀⠈⠿⣿⣿⣿⣿⣿⣿⣏⠁     \033[91m⢼⣿⣿⣿⣿⣿⣿⠛ ⣠⣶⡿⣿⣿⣿⣿⣿⣿⣿⣆  ⠹⣿⣷⣄  ")
    print(" \033[97m⣴⣿⡿⠋   ⢿⣿⡿⣿⣿⣿⣿⣿⣮⣟⢿⣦⣴⣿⣿⣿⣿⣿⡏⠃      \033[91m⠘⢸⣿⣿⣿⣿⣿⣷⣾⠟⣫⣾⣿⣿⣿⣿⡿⣟⣿⡿   ⠈⠻⣿⣧⡀")
    print("\033[97m⢊⢼⠟     ⠘⢿⣿⣮⣻⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⡇        \033[91m⢸⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⢯⣾⣿⡿⠁     ⠹⠗⠈")
    print("      \033[97m   ⠈⠻⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇        \033[91m⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⠟          ")
    print("     \033[97m      ⠹⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿         \033[91m ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣿⡿⠃           ")
    print("     \033[97m       ⠈⢿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⡿⠃         \033[91m ⣿⡿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⠟⠁            ")
    print("      \033[97m       ⢀⡟⣿⣿⣶⣽⡛⠛⠛⠛⠉           \033[31m⢰⣿⠃\033[91m ⠉⠉⠛⣫⣵⣿⣿⣿⢹⡄             ")
    print("      \033[93m      ⢀⡾⣵⣿⣿⡿⣿⡟              \033[31m⣰⡿⠃     ⢹⡿⠿⣿⣿⣷⣻⣄⡀           ")
    print("      \033[93m    ⠐⠚⣛⣼⣿⣿⡟⠂⢸⠁            \033[31m⢀⣾⠏        ⡇⠘⠹⣿⣿⣷⣍⣙⠃          ")
    print("      \033[93m    ⠒⠛⠛⠛⠛⠋  ⠘             \033[31m⢾⣇     ⣀⣠⣤⠴⠗⠚⠛⠛⣯⠉⠉⠉⠉          ")
    print("                                \033[31m⠈⠛⠷⠶⠖⠛⠋⠉⠁⣀ ⢀⣀⣠⡴⠟              ")
    print("                                \033[31m      ⠉⠛⠻⠿⡍⠉⠁                 \033[97m")

def multi_manner():
    print("            \033[93m       \033[31m                         ⣀⡔                 ")
    print("            \033[93m          \033[31m                 ⢀⣀⣴⣿⠋                ")  
    print("            \033[93m    \033[97m                      \033[91m⣴⣿⣿⣿⣿⣿⣷\033[31m⣤⣀⣀⡤")             
    print("            \033[97m                        \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏              ")
    print("            \033[97m                        \033[91m⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              ")
    print("            \033[97m                       \033[91m⢠⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿              ")
    print("            \033[97m                      \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿              ")
    print("          \033[97m                        \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⡄             ")
    print("          \033[97m                       \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣷⣝⠿⣿⣏             ")
    print("         \033[97m                    ⡀  \033[91m⢠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣷⣮⣃             ")
    print("      \033[97m                           \033[91m⢹⣿⣿⣿⣿⣿⣿⣿⣯⣻⠿⠮⠙⠿⣿⣿⣿⣶⣤⣄⡀        ")
    print("     \033[97m                            \033[91m⢈⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃  ⣀⣈⣙⣛⣛⣻⠿⠿⢿⣶⣤⣀    ")
    print("  \033[97m                                \033[91m⢼⣿⣿⣿⣿⣿⣿⠛ ⣠⣶⡿⣿⣿⣿⣿⣿⣿⣿⣆  ⠹⣿⣷⣄  ")
    print(" \033[97m                                 \033[91m⠘⢸⣿⣿⣿⣿⣿⣷⣾⠟⣫⣾⣿⣿⣿⣿⡿⣟⣿⡿   ⠈⠻⣿⣧⡀")
    print("\033[97m                                   \033[91m⢸⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⢯⣾⣿⡿⠁     ⠹⠗⠈")
    print("      \033[97m                             \033[91m⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⠟          ")
    print("     \033[97m                              \033[91m ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣿⡿⠃           ")
    print("     \033[97m                              \033[91m ⣿⡿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⠟⠁            ")
    print("      \033[97m                             \033[31m⢰⣿⠃\033[91m ⠉⠉⠛⣫⣵⣿⣿⣿⢹⡄             ")
    print("      \033[93m                            \033[31m⣰⡿⠃     ⢹⡿⠿⣿⣿⣷⣻⣄⡀           ")
    print("      \033[93m                          \033[31m⢀⣾⠏        ⡇⠘⠹⣿⣿⣷⣍⣙⠃          ")
    print("      \033[93m                          \033[31m⢾⣇     ⣀⣠⣤⠴⠗⠚⠛⠛⣯⠉⠉⠉⠉          ")
    print("                                \033[31m⠈⠛⠷⠶⠖⠛⠋⠉⠁⣀ ⢀⣀⣠⡴⠟              ")
    print("                                \033[31m      ⠉⠛⠻⠿⡍⠉⠁                 \033[97m")

def multi_major():
    print("            \033[93m⣀⣤⠶⠖⢛⣻⡿\033[31m                    ")
    print("            \033[93m ⢠⣶⣋⣩⣤⠶⠾⣿⡁\033[31m                 ") 
    print("            \033[93m ⠈⠉⠉\033[97m⣠⣴⣾⣿⣿⣿⣷⣄              ")           
    print("            \033[97m  ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧    ⢀⣠⣴⣶⡇ ")
    print("            \033[97m  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆ ⣠⣶⣿⣿⣿⣿⠃  ")
    print("            \033[97m  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠃  ")
    print("            \033[97m  ⣿⣿⣿⣿⣿⡿⣫⣷⣾⣿⣿⣿⣿⣿⣿⣿⡏  ")
    print("          \033[97m   ⢀⣿⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟    ")
    print("          \033[97m   ⢪⣿⣿⢟⣽⣿⣿⡿⣫⣽⣿⣿⣿⣿⣿⡟    ")
    print("         \033[97m    ⢹⣫⣶⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⣿⣿⡁⡀ ")
    print("      \033[97m   ⢀⣠⣤⣶⣿⣿⡿⠟⢭⣾⡿⣻⣿⣿⣿⣿⣿⣿⣿⡟⠁  ")
    print("     \033[97m⣀⣤⣶⣿⡿⠿⠿⠿⢛⠋   ⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃    ")
    print("  \033[97m⢀⣴⣿⠟⠉ ⣰⣾⣿⣿⣿⣿⣿⡿⣷⣦⡀⠈⠿⣿⣿⣿⣿⣿⣿⣏⠁  ")
    print(" \033[97m⣴⣿⡿⠋   ⢿⣿⡿⣿⣿⣿⣿⣿⣮⣟⢿⣦⣴⣿⣿⣿⣿⣿⡏⠃    ")
    print("\033[97m⢊⢼⠟     ⠘⢿⣿⣮⣻⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⡇    ")
    print("      \033[97m   ⠈⠻⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       ")
    print("     \033[97m      ⠹⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿         ")
    print("     \033[97m       ⠈⢿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⡿⠃       ")
    print("      \033[97m       ⢀⡟⣿⣿⣶⣽⡛⠛⠛⠛⠉          ")
    print("      \033[93m      ⢀⡾⣵⣿⣿⡿⣿⡟            ")
    print("      \033[93m    ⠐⠚⣛⣼⣿⣿⡟⠂⢸⠁         ")
    print("      \033[93m    ⠒⠛⠛⠛⠛⠋  ⠘     ")

def devil():
    clear_screen()
    time.sleep(.02)
    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⠀⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠂⡠⠪⡻⣿⣿⣿⣿⣿⣿⠘⣿⢿⣿⣿⣿⣿⡟⡑⢁⠂⢄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠑⠠⢃⢳⢹⣿⣿⣿⣿⢏⢊⣏⢼⣿⣿⣿⡟⡼⢄⠣⡐⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠑⢊⠔⢊⡆⣿⣿⣿⣄⢻⢘⠷⣥⣿⣿⣿⡇⡅⢨⠒⠤⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⢊⡡⠔⢹⢆⣿⣿⣿⡮⣚⢗⢯⣔⠝⣿⣿⡇⡅⠂⡥⢒⠐⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠉⠄⢒⠈⡜⣸⣻⣛⡿⣃⠻⠇⢳⢹⡟⢘⣿⣷⢈⠑⡐⠤⠉⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
    ⣿⣿⣷⣝⢿⣟⢭⣿⣽⣯⣿⣽⣿⠿⠋⡁⠀⠀⠀⠈⠥⠈⢀⠌⣤⣭⣭⣭⡸⣰⢥⣬⣷⡿⡓⣬⣭⣭⣥⡡⢐⠠⠉⠤⠀⠀⠀⠀⢙⠩⣿⣿⣿⣿⣽⣯⣿⢻⣿⣯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣧⢻⣷⣝⢿⡿⠟⢋⠠⡀⠆⡀⠅⠀⠠⠉⠤⢒⣤⣾⣿⣿⣿⣿⣷⠮⠣⢹⡫⠪⠾⣿⣿⣿⣿⣿⣦⡐⢡⠤⠁⠀⠀⠇⠀⠆⠀⣉⠛⢿⣿⢟⣵⡿⣱⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⠙⢋⠁⡐⢂⡁⢆⠁⠢⠁⠠⣔⣡⣴⢾⣛⣿⣭⣿⣶⣾⣿⣿⣿⡷⠈⠾⣿⣿⣿⣿⣶⣾⣯⣽⣛⡷⢦⣤⣐⠄⠁⠈⠰⡁⠄⡔⢂⠄⣉⠛⢽⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠁⠐⠈⠐⠄⠀⠘⠀⠠⢪⡴⡟⣯⣵⣾⣿⢿⠛⡿⠍⠙⠒⠚⠛⠋⠉⠛⠋⠙⠛⠓⠒⠚⠩⠽⠛⠻⢿⣿⣾⣽⢻⢶⡕⠠⠀⠊⠐⠁⠒⠠⠰⠀⢻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⡀⠀⠀⠀⠐⠀⠀⡌⠁⣸⣴⡿⡟⣏⣧⡼⠞⠁⠀⠀⡀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠈⠑⠾⣼⣉⢻⢿⣾⣌⡆⠰⠀⠠⠀⠀⠁⠀⠀⠸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠠⡠⡀⠢⠠⠄⡄⡀⣾⡿⣣⣴⣿⣿⠟⠀⠀⣰⠀⠘⢸⠇⠀⠠⠐⢀⠂⠄⢀⠂⠀⠰⡷⠃⠀⢠⠘⠢⡘⢿⣿⣾⣼⢻⣿⢰⢀⠄⠄⠄⢂⠔⡄⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⡃⠎⡓⠦⢄⣒⠐⠙⠿⣮⣻⠿⠃⠀⠀⠑⣼⡀⠄⢀⠀⣠⠁⡈⠄⡐⠈⠠⠀⢄⠀⠀⠠⠀⣼⢁⠀⠈⢊⠻⡿⣫⡾⠟⠈⣀⡢⢥⢒⡑⠆⡀⢸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⠁⠆⡁⢎⠅⣒⠂⠎⡡⢀⠖⡀⠠⠌⠀⡀⠀⠀⠀⢂⢲⡇⠠⠐⠠⠀⡁⢂⠁⢸⣦⠅⠂⠀⠈⠀⠀⠈⡄⠈⠒⡄⠨⡙⠄⢎⠂⡥⠠⠙⠀⠀⣼⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢇⡀⠀⠠⠘⠈⠆⡚⣈⠡⠎⡰⢁⠎⠱⣘⠂⢎⣐⠠⡀⢞⣷⠀⠌⡀⢁⠀⢂⠈⣼⡻⢘⠠⢢⢘⡀⠍⠦⠘⡌⢡⠘⣅⢒⠩⡀⠇⠰⠈⠀⠀⣰⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⣣⣿⣟⣤⣀⠀⠀⠀⠀⠀⠊⠐⠁⡁⢌⠳⠀⡜⠢⠠⡜⣨⠢⡈⠀⠠⠐⠠⢈⠀⠀⢉⠔⠥⡩⢄⠊⠴⣈⠡⣃⠐⠌⠂⠐⠀⠀⠀⠀⠀⣀⣤⡺⣿⣮⢿⣿⣿⣿⣿
    ⣿⣿⡿⣱⣿⢏⣾⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠈⠀⠴⠑⡈⢆⠳⠘⡀⡔⡊⠄⠠⠁⠂⠄⡈⢀⢂⠣⡄⡑⠪⡔⡈⠂⠱⠀⠀⠀⠀⠀⢀⢠⣶⣶⣿⣿⣿⣿⡝⣿⣧⣻⣿⣿⣿
    ⣿⡿⣵⣿⢯⣿⣿⡿⠿⣿⣿⣿⡇⠀⠁⠀⠀⠀⠀⠀⠁⢈⡄⢆⠣⠜⠀⡔⡘⠀⠠⠁⠂⠀⡄⠡⠘⠰⢌⡐⠤⡁⠉⠀⠀⠀⠀⠀⠀⢸⡄⣿⣿⣿⡿⠿⣿⣿⣞⣿⣷⢻⣿⣿
    ⣿⣳⣿⢏⣿⣿⣿⡇⠀⠈⠛⠿⣧⠀⠀⠀⠀⠀⠀⠂⠈⠀⠀⠀⠒⠈⠃⠠⠁⠄⠀⠐⡀⠰⠀⠀⠉⠁⠂⠄⠠⠀⠄⠀⠂⠀⠀⠀⠀⠸⢰⡿⠛⠋⢀⢢⣿⣿⣿⡜⣿⣧⢿⣿
    ⣯⣿⡟⣾⣿⣿⣿⣿⣦⠈⠀⠄⠈⠀⠀⠀⠄⠠⠀⠐⠀⠀⠂⠐⠠⠒⠈⠀⠁⢀⠐⠀⡀⠀⠈⠀⠀⠃⠆⠀⠄⠀⠀⠂⠀⡀⠄⠂⠀⠀⡌⠀⠠⠠⣠⣿⣿⣿⣿⣿⣹⣿⡞⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠠⠀⠂⠀⠐⠈⠀⢁⠀⠉⠐⠠⣀⠠⠀⠄⠂⡀⠂⠄⠀⠄⠁⠌⡐⠠⠀⠄⠀⠀⠠⠀⠒⠤⠀⠌⠐⠀⠰⠁⠠⠁⠀⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡀⠀⠀⠠⠀⡀⠐⠠⠈⠄⠁⠂⠄⠁⢀⠈⠀⠄⠁⡀⠈⠀⡀⠄⠀⠄⠀⡀⠄⠁⠂⠁⠂⠄⠂⢀⠀⡈⠂⠀⠀⠀⡆⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠠⠀⠀⠀⠐⠀⠠⠀⠀⠀⠈⠀⠄⠁⠂⡀⠂⠄⡁⢀⠐⡀⠄⠂⡐⢀⠂⢄⠔⠊⠁⠁⠀⠠⠀⠀⡀⢠⠁⠀⠠⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀⢀⣠⡄⣠⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⡤⣀⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀⣿⣿⡃⣟⣳⣧⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀⢴⣿⣻⢛⣻⣷⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀⠈⠉⠈⠉⠁⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⡈⠀⠀⠀⠐⢀⡈⠀⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠡⠀⠄⠂⡀⠀⠀⠈⠀⠠⠔⠀⠀⠀⠀⠈⢳⠄⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠐⠀⠌⠀⠂⠄⠀⠄⢂⠠⠁⠌⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠄⡁⠄⠠⢀⠀⢐⡀⠁⠀⠊⠀⢜⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠐⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠠⠐⠐⠋⠀⠀⠀⠀⠀⠀⠀⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿
    ⣿⣿⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣵⠀⠀⠀⠀⠀⠀⠀⢁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣻⣿
    ⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣟⣷⣷⠀⠈⠀⡄⠈⠀⠀⡀⠄⠀⢀⠀⠀⡀⠀⠄⠈⠀⢄⠀⢀⢰⠀⠈⠀⣼⣮⡻⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣿⣿
    ⣿⣿⡝⣿⣧⢿⣿⣿⣿⣿⣿⣿⢟⣯⡿⣫⣾⣿⣿⡇⠀⠀⠃⣽⡄⣼⠀⡄⠈⠀⠀⠁⠀⢠⠀⢠⡀⣴⠀⣾⠇⠀⠀⠀⣿⣿⣿⣮⣻⣮⡻⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣾⣿⣿
    ⣿⣿⣿⣞⢿⣷⡻⣿⡿⢟⣫⣵⣿⣿⣹⣿⣿⣿⣿⡇⠀⠀⠀⠈⠀⣿⠐⣿⢀⡆⣤⠀⣠⠈⠀⣼⠁⢻⣦⠉⠀⠀⠂⠀⣿⣿⣿⣿⣷⢻⣿⣷⣽⣻⠿⣿⡟⣵⣿⢯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣮⢿⣿⣕⢶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣧⠀⠀⡀⠀⡘⢥⠀⠛⢸⢇⣿⡀⣿⡆⠀⠙⠀⢸⠀⠀⠀⠀⠁⣸⣿⣿⣿⢿⣷⣶⣶⣶⣶⣶⣶⢦⣾⡿⣣⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣧⡹⣿⣧⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⡀⠀⠀⠀⠀⠈⠙⠀⠛⠁⠀⠀⠀⠀⢀⢣⠀⠈⢠⣿⣿⠋⠀⠀⠀⠉⢻⣿⣿⠟⣡⣿⠟⣹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⣌⢻⣷⣼⣿⣿⠛⠛⢻⡟⣿⡟⢻⡗⠀⢀⠀⠐⣆⣄⠀⠀⠀⠀⠀⠀⡀⢀⠀⢀⠀⠂⠁⠀⡄⡘⠛⠃⠀⠊⠙⡗⠀⠀⠛⣡⣾⣿⣡⣾⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣯⡳⢶⣯⣝⢿⣿⣿⡏⣆⡀⠄⡀⠇⠻⡆⢄⡀⠀⠀⠀⢀⠀⠣⡀⠡⠀⠀⠌⣰⣶⣿⣿⣦⠀⣠⣿⠆⢸⢸⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⢿⣷⣽⣻⢿⣮⣻⣧⣋⣶⠀⠠⠀⠘⠃⠘⠇⢹⠃⡿⠀⠀⠠⠘⢄⠀⠀⠈⠙⢏⣿⢟⣵⢟⢉⣷⠁⠀⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣻⢿⣿⣾⣽⣹⣿⡳⣷⠀⠐⡀⢂⠐⠀⡀⢀⠁⠠⠀⠀⡀⠄⠑⠀⠁⢀⠙⠧⣽⣾⣿⠟⠁⢀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⡿⢿⣿⣿⣿⣿⣾⣽⢻⡿⢿⣿⣾⣯⣤⣄⡂⠌⠠⠐⠠⠈⠄⠁⠂⣀⡀⠀⠡⠐⡀⢀⠀⠄⠀⡀⠠⡀⢀⣾⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⢹⣿⣿⣿⡿⣱⡟⣽⣷⣮⢿⣟⢿⣛⣛⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⡧⣦⣄⣐⡀⠠⠈⠐⢀⣁⣴⡿⣵⣿⣿⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡟⣾⣿⡟⣵⣿⣷⣼⣿⣿⡿⣽⢟⣾⣿⣿⣿⣷⡻⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣾⢏⣾⣿⣿⣿⡝⣷⡻⣿⣿⣷⣵⣿⣾⣽⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⢻⣿⣧⡻⣿⣿⣿⡿⣟⣾⢯⣾⣿⣿⣿⣿⣿⣷⡽⣷⡻⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣫⣿⣿⣿⣿⣿⣿⣞⢿⣝⢿⣿⣿⣿⡿⣻⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣶⣯⣽⣾⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣿⣝⣿⣿⣿⣿⣿⡿⣳⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣾⣭⣷⣿⣿⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣟⣻⣯⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣞⢿⣿⣿⡟⣵⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣿⣻⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣯⣻⢟⣾⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')
    clear_screen
    time.sleep(.02)
    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⠀⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠂⡠⠪⡻⣿⣿⣿⣿⣿⣿⠘⣿⢿⣿⣿⣿⣿⡟⡑⢁⠂⢄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠑⠠⢃⢳⢹⣿⣿⣿⣿⢏⢊⣏⢼⣿⣿⣿⡟⡼⢄⠣⡐⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠑⢊⠔⢊⡆⣿⣿⣿⣄⢻⢘⠷⣥⣿⣿⣿⡇⡅⢨⠒⠤⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⢊⡡⠔⢹⢆⣿⣿⣿⡮⣚⢗⢯⣔⠝⣿⣿⡇⡅⠂⡥⢒⠐⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠉⠄⢒⠈⡜⣸⣻⣛⡿⣃⠻⠇⢳⢹⡟⢘⣿⣷⢈⠑⡐⠤⠉⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
    ⣿⣿⣷⣝⢿⣟⢭⣿⣽⣯⣿⣽⣿⠿⠋⡁⠀⠀⠀⠈⠥⠈⢀⠌⣤⣭⣭⣭⡸⣰⢥⣬⣷⡿⡓⣬⣭⣭⣥⡡⢐⠠⠉⠤⠀⠀⠀⠀⢙⠩⣿⣿⣿⣿⣽⣯⣿⢻⣿⣯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣧⢻⣷⣝⢿⡿⠟⢋⠠⡀⠆⡀⠅⠀⠠⠉⠤⢒⣤⣾⣿⣿⣿⣿⣷⠮⠣⢹⡫⠪⠾⣿⣿⣿⣿⣿⣦⡐⢡⠤⠁⠀⠀⠇⠀⠆⠀⣉⠛⢿⣿⢟⣵⡿⣱⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⠙⢋⠁⡐⢂⡁⢆⠁⠢⠁⠠⣔⣡⣴⢾⣛⣿⣭⣿⣶⣾⣿⣿⣿⡷⠈⠾⣿⣿⣿⣿⣶⣾⣯⣽⣛⡷⢦⣤⣐⠄⠁⠈⠰⡁⠄⡔⢂⠄⣉⠛⢽⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠁⠐⠈⠐⠄⠀⠘⠀⠠⢪⡴⡟⣯⣵⣾⣿⢿⠛⡿⠍⠙⠒⠚⠛⠋⠉⠛⠋⠙⠛⠓⠒⠚⠩⠽⠛⠻⢿⣿⣾⣽⢻⢶⡕⠠⠀⠊⠐⠁⠒⠠⠰⠀⢻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⡀⠀⠀⠀⠐⠀⠀⡌⠁⣸⣴⡿⡟⣏⣧⡼⠞⠁⠀⠀⡀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠈⠑⠾⣼⣉⢻⢿⣾⣌⡆⠰⠀⠠⠀⠀⠁⠀⠀⠸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠠⡠⡀⠢⠠⠄⡄⡀⣾⡿⣣⣴⣿⣿⠟⠀⠀⣰⠀⠘⢸⠇⠀⠠⠐⢀⠂⠄⢀⠂⠀⠰⡷⠃⠀⢠⠘⠢⡘⢿⣿⣾⣼⢻⣿⢰⢀⠄⠄⠄⢂⠔⡄⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⡃⠎⡓⠦⢄⣒⠐⠙⠿⣮⣻⠿⠃⠀⠀⠑⣼⡀⠄⢀⠀⣠⠁⡈⠄⡐⠈⠠⠀⢄⠀⠀⠠⠀⣼⢁⠀⠈⢊⠻⡿⣫⡾⠟⠈⣀⡢⢥⢒⡑⠆⡀⢸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⠁⠆⡁⢎⠅⣒⠂⠎⡡⢀⠖⡀⠠⠌⠀⡀⠀⠀⠀⢂⢲⡇⠠⠐⠠⠀⡁⢂⠁⢸⣦⠅⠂⠀⠈⠀⠀⠈⡄⠈⠒⡄⠨⡙⠄⢎⠂⡥⠠⠙⠀⠀⣼⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢇⡀⠀⠠⠘⠈⠆⡚⣈⠡⠎⡰⢁⠎⠱⣘⠂⢎⣐⠠⡀⢞⣷⠀⠌⡀⢁⠀⢂⠈⣼⡻⢘⠠⢢⢘⡀⠍⠦⠘⡌⢡⠘⣅⢒⠩⡀⠇⠰⠈⠀⠀⣰⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⣣⣿⣟⣤⣀⠀⠀⠀⠀⠀⠊⠐⠁⡁⢌⠳⠀⡜⠢⠠⡜⣨⠢⡈⠀⠠⠐⠠⢈⠀⠀⢉⠔⠥⡩⢄⠊⠴⣈⠡⣃⠐⠌⠂⠐⠀⠀⠀⠀⠀⣀⣤⡺⣿⣮⢿⣿⣿⣿⣿
    ⣿⣿⡿⣱⣿⢏⣾⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠈⠀⠴⠑⡈⢆⠳⠘⡀⡔⡊⠄⠠⠁⠂⠄⡈⢀⢂⠣⡄⡑⠪⡔⡈⠂⠱⠀⠀⠀⠀⠀⢀⢠⣶⣶⣿⣿⣿⣿⡝⣿⣧⣻⣿⣿⣿
    ⣿⡿⣵⣿⢯⣿⣿⡿⠿⣿⣿⣿⡇⠀⠁⠀⠀⠀⠀⠀⠁⢈⡄⢆⠣⠜⠀⡔⡘⠀⠠⠁⠂⠀⡄⠡⠘⠰⢌⡐⠤⡁⠉⠀⠀⠀⠀⠀⠀⢸⡄⣿⣿⣿⡿⠿⣿⣿⣞⣿⣷⢻⣿⣿
    ⣿⣳⣿⢏⣿⣿⣿⡇⠀⠈⠛⠿⣧⠀⠀⠀⠀⠀⠀⠂⠈⠀⠀⠀⠒⠈⠃⠠⠁⠄⠀⠐⡀⠰⠀⠀⠉⠁⠂⠄⠠⠀⠄⠀⠂⠀⠀⠀⠀⠸⢰⡿⠛⠋⢀⢢⣿⣿⣿⡜⣿⣧⢿⣿
    ⣯⣿⡟⣾⣿⣿⣿⣿⣦⠈⠀⠄⠈⠀⠀⠀⠄⠠⠀⠐⠀⠀⠂⠐⠠⠒⠈⠀⠁⢀⠐⠀⡀⠀⠈⠀⠀⠃⠆⠀⠄⠀⠀⠂⠀⡀⠄⠂⠀⠀⡌⠀⠠⠠⣠⣿⣿⣿⣿⣿⣹⣿⡞⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠠⠀⠂⠀⠐⠈⠀⢁⠀⠉⠐⠠⣀⠠⠀⠄⠂⡀⠂⠄⠀⠄⠁⠌⡐⠠⠀⠄⠀⠀⠠⠀⠒⠤⠀⠌⠐⠀⠰⠁⠠⠁⠀⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡀⠀⠀⠠⠀⡀⠐⠠⠈⠄⠁⠂⠄⠁⢀⠈⠀⠄⠁⡀⠈⠀⡀⠄⠀⠄⠀⡀⠄⠁⠂⠁⠂⠄⠂⢀⠀⡈⠂⠀⠀⠀⡆⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠠⠀⠀⠀⠐⠀⠠⠀⠀⠀⠈⠀⠄⠁⠂⡀⠂⠄⡁⢀⠐⡀⠄⠂⡐⢀⠂⢄⠔⠊⠁⠁⠀⠠⠀⠀⡀⢠⠁⠀⠠⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀\033[11m\033[41m⢀⣠⡄⣠\033[0m⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31m\033[41m⣠⣠⡤⣀\033[0m⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀\033[31m\033[41m⣿⣿⡃⣟⣳⣧\033[0m⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀\033[31m\033[41m⢴⣿⣻⢛⣻⣷\033[0m⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀\033[31m\033[41m⠉⠉⠉⠉\033[0m⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀\033[31m\033[41m⠈⠉⠈⠉⠁\033[0m⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⡈⠀⠀⠀⠐⢀⡈⠀⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠡⠀⠄⠂⡀⠀⠀⠈⠀⠠⠔⠀⠀⠀⠀⠈⢳⠄⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠐⠀⠌⠀⠂⠄⠀⠄⢂⠠⠁⠌⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠄⡁⠄⠠⢀⠀⢐⡀⠁⠀⠊⠀⢜⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠐⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠠⠐⠐⠋⠀⠀⠀⠀⠀⠀⠀⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿
    ⣿⣿⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣵⠀⠀⠀⠀⠀⠀⠀⢁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣻⣿
    ⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣟⣷⣷⠀⠈⠀⡄⠈⠀⠀⡀⠄⠀⢀⠀⠀⡀⠀⠄⠈⠀⢄⠀⢀⢰⠀⠈⠀⣼⣮⡻⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣿⣿
    ⣿⣿⡝⣿⣧⢿⣿⣿⣿⣿⣿⣿⢟⣯⡿⣫⣾⣿⣿⡇⠀⠀⠃⣽⡄⣼⠀⡄⠈⠀⠀⠁⠀⢠⠀⢠⡀⣴⠀⣾⠇⠀⠀⠀⣿⣿⣿⣮⣻⣮⡻⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣾⣿⣿
    ⣿⣿⣿⣞⢿⣷⡻⣿⡿⢟⣫⣵⣿⣿⣹⣿⣿⣿⣿⡇⠀⠀⠀⠈⠀⣿⠐⣿⢀⡆⣤⠀⣠⠈⠀⣼⠁⢻⣦⠉⠀⠀⠂⠀⣿⣿⣿⣿⣷⢻⣿⣷⣽⣻⠿⣿⡟⣵⣿⢯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣮⢿⣿⣕⢶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣧⠀⠀⡀⠀⡘⢥⠀⠛⢸⢇⣿⡀⣿⡆⠀⠙⠀⢸⠀⠀⠀⠀⠁⣸⣿⣿⣿⢿⣷⣶⣶⣶⣶⣶⣶⢦⣾⡿⣣⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣧⡹⣿⣧⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⡀⠀⠀⠀⠀⠈⠙⠀⠛⠁⠀⠀⠀⠀⢀⢣⠀⠈⢠⣿⣿⠋⠀⠀⠀⠉⢻⣿⣿⠟⣡⣿⠟⣹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⣌⢻⣷⣼⣿⣿⠛⠛⢻⡟⣿⡟⢻⡗⠀⢀⠀⠐⣆⣄⠀⠀⠀⠀⠀⠀⡀⢀⠀⢀⠀⠂⠁⠀⡄⡘⠛⠃⠀⠊⠙⡗⠀⠀⠛⣡⣾⣿⣡⣾⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣯⡳⢶⣯⣝⢿⣿⣿⡏⣆⡀⠄⡀⠇⠻⡆⢄⡀⠀⠀⠀⢀⠀⠣⡀⠡⠀⠀⠌⣰⣶⣿⣿⣦⠀⣠⣿⠆⢸⢸⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⢿⣷⣽⣻⢿⣮⣻⣧⣋⣶⠀⠠⠀⠘⠃⠘⠇⢹⠃⡿⠀⠀⠠⠘⢄⠀⠀⠈⠙⢏⣿⢟⣵⢟⢉⣷⠁⠀⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣻⢿⣿⣾⣽⣹⣿⡳⣷⠀⠐⡀⢂⠐⠀⡀⢀⠁⠠⠀⠀⡀⠄⠑⠀⠁⢀⠙⠧⣽⣾⣿⠟⠁⢀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⡿⢿⣿⣿⣿⣿⣾⣽⢻⡿⢿⣿⣾⣯⣤⣄⡂⠌⠠⠐⠠⠈⠄⠁⠂⣀⡀⠀⠡⠐⡀⢀⠀⠄⠀⡀⠠⡀⢀⣾⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⢹⣿⣿⣿⡿⣱⡟⣽⣷⣮⢿⣟⢿⣛⣛⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⡧⣦⣄⣐⡀⠠⠈⠐⢀⣁⣴⡿⣵⣿⣿⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡟⣾⣿⡟⣵⣿⣷⣼⣿⣿⡿⣽⢟⣾⣿⣿⣿⣷⡻⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣾⢏⣾⣿⣿⣿⡝⣷⡻⣿⣿⣷⣵⣿⣾⣽⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⢻⣿⣧⡻⣿⣿⣿⡿⣟⣾⢯⣾⣿⣿⣿⣿⣿⣷⡽⣷⡻⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣫⣿⣿⣿⣿⣿⣿⣞⢿⣝⢿⣿⣿⣿⡿⣻⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣶⣯⣽⣾⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣿⣝⣿⣿⣿⣿⣿⡿⣳⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣾⣭⣷⣿⣿⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣟⣻⣯⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣞⢿⣿⣿⡟⣵⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣿⣻⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣯⣻⢟⣾⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''') 

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')


def gahhh():
    clear_screen()
    devil()
    devil()
    devil()
    devil()
    devil()
    clear_screen()
    time.sleep(.5)
    print(colored("NOW LEAVING Hell0...", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)      
    exit()


def pwnd():
    os.system('git clone https://github.com/Thr0wAway-n0w/pwnd.git')
    os.chdir('pwnd')
    os.system("git fetch")
    os.system("git pull")
    os.system('python3 pwnd.py')
    main_menu()
    
def get_zipcodes_within_distance(zipcode, distance):
    api_url = f"https://www.zipcodeapi.com/rest/izWpWpWIjGWMm3p59jfXYW0wNltt2UoB4JbMxGo0juQx5CYekdtCG4vTTbNaNPSN/radius.json/{zipcode}/{distance}/mile"
    response = requests.get(api_url)
    data = response.json()
    zipcodes = data["zip_codes"]
    sorted_zipcodes = sorted(zipcodes, key=lambda x: x["distance"])
    return sorted_zipcodes

def colorize_distance(distance):
    if distance == 0:
        return "\033[97m" 
    elif distance <= 10:
        return "\033[37m"  
    elif distance <= 20:
        return "\033[90m" 
    elif distance <= 30:
        return "\033[92m" 
    elif distance <= 40:
        return "\033[93m" 
    elif distance <= 50:
        return "\033[33m"  
    elif distance < 60:
        return "\033[93m"  
    elif distance < 70:
        return "\033[31m" 
    elif distance < 80:
        return "\033[36m" 
    else:
        return "\033[34m"  

def geo_menu():
    clear_screen()
    ascii_banner()
    print(colored("Geo-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)    
    header()
    print("                      \033[92m1\033[0m) ZipCodes                                                               \033[92m2\033[0m) Go To \033[31mHELL          ")
    option = input("> ")
    if option == "1":
        clear_screen()
        zip_menu()
        what_now()
    elif option == "2":
        clear_screen
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        geo_menu()  

def get_zip_details(zipcode):
    url = f"https://www.zipcodeapi.com/rest/QuwEnYrHY739Pt0cXLNf9rpITpOMljbGCelpkWalWL2PAPSySLbWcLDv05Zuwwnu/info.json/{zipcode}/radians"
    response = requests.get(url) 
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
def zip_menu():
    clear_screen()
    ascii_banner()
    print(colored("Zipcode-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)
    header()
    print("\033[96mLIMIT DISTANCE OR USE YOUR OWN API KEY")
    print(" ")
    print("Select Option:")
    print("1) Find Nearby Zip codes")
    print("2) Indepth Scan")
    option = input("> ")

    if option == "1":
        print("Enter a ZIP CODE:")
        zipcode = input("> ")
        print("Enter the DISTANCE in miles:")
        distance = int(input("> "))
        zipcodes = get_zipcodes_within_distance(zipcode, distance)

        print("Zip codes within", distance, "miles of", zipcode, ":")
        for zip_info in zipcodes:
            print(colorize_distance(zip_info["distance"]), zip_info["zip_code"], "-", zip_info["distance"])

    elif option == "2":
        print("Enter a ZIP CODE:")
        zipcode = input("> ")
        print("Enter the DISTANCE in miles:")
        distance = int(input("> "))
        zipcodes = get_zipcodes_within_distance(zipcode, distance)

    if zipcodes:
        print("Zip codes within", distance, "miles of", zipcode, ":")
        for zip_info in zipcodes:
            details = get_zip_details(zip_info["zip_code"])
            if details:
                print(colorize_distance(zip_info["distance"]), zip_info["zip_code"], "-", zip_info["distance"])
                print("\tCity:", details["city"])
                print("\tState:", details["state"])
            else:
                print("Error: Zip details not found for", zip_info["zip_code"])
    else:
        print("Error: Zip codes data not found. Please check the input and try again.")

    if option == "1":
        return option
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        zip_menu() 

def ddos_install():
    os.system("git clone https://github.com/HyukIsBack/KARMA-DDoS.git")
    os.chdir("KARMA-DDoS")
    os.system("git fetch")
    os.system("git pull")    
    os.system("python3 -m pip install -r requirements.txt")
    os.system("sudo chmod +x ./setup.py")
    os.system("sudo python3 ./setup.py install")
    os.system("python3 main.py")

def send_command_to_xterms():
    command = simpledialog.askstring("Enter Command", "Enter command to send to xterm windows (or type 'exit' to quit):")
    global num_xterms
    processes = []
    for i in range(num_xterms):
        process = subprocess.Popen(['xterm', '-e', 'python3', '-c', f"import Hell0; Hell0.ddos_install(); {command}"])
        processes.append(process)

    for process in processes:
        process.communicate()
    
    print(f"Command '{command}' sent to all xterm windows.")
    
def multi_menu():
    global num_xterms
    clear_screen()
    multi_banner()
    print(colored("Multi-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)    
    header()
    print("\033[93m1\033[0m) SplitScreen Multi\033[95m Neat\033[97m and \033[95mContained\033[97m, produces \033[95m1 extra \033[97minstance by halving the terminal\033[0m")
    print(" ")
    print("\033[93m2\033[0m) Xterm Multi\033[91m Unlimited \033[97mQuantity, \033[91mEACH \033[97mgets it's \033[91mOWN UNIQUE Mac and IP Addresses")
    print(" ")
    print("\033[92m3\033[0m)\033[91m ×͜× \033[97mDDoS Playground\033[91m ×͜× \033[95mOR\033[92m 3.0\033[0m GO \033[41mGORILLA MONSOON MODE\033[0m")
    print(" ")
    print("\033[91m4)\033[40m Run\033[0m")
    choice = input(">  ")
    
    if choice == "1":
        clear_screen()
        multi_mode()
        multi_major()
        time.sleep(10)
        clear_screen()
        main_menu()
    elif choice == "2":
        clear_screen()
        multi_manner()
        multi_multi()   
    elif choice == "3":
        clear_screen()
        multi_manner()
        ddos_play()   
    elif choice == "3.0":
        clear_screen()
        multi_manner()
        jam()
        ddos_play()
    elif choice == "4":
        clear_screen()
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        multi_menu()                

def jam():
    print(colored("ACTIVATING GORILLA MONSOON MODE...", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'shift', 'd')
    time.sleep(1)
    pyautogui.typewrite('bb\n')
    time.sleep(1)
    pyautogui.typewrite('y\n')
    time.sleep(1)
    pyautogui.typewrite('8\n')
    
def multi_mode():
    pyautogui.hotkey('ctrl', 'shift', 'd')
    time.sleep(.01)
    pyautogui.typewrite('python3 Hell0.py +1\n')

def multi_multi():
    clear_screen()
    multi_manner()
    header()
    print("\033[0mThe First Four Instances are \033[92mPre-Postioned\033[0m. Personal Preference is 5. \033[91mDrag/drop\033[92m ⇘\033[0m for Additional Instances \033[91mIf\033[0m Higher Number was Specified") 
    global num_xterms
    num_xterms = int(input("Enter the number of xterms to open: "))
    os.chdir(os.path.join(os.getenv("HOME"), "Desktop"))

    positions = [
        "center",
        "topright",
        "topleft",
        "bottomleft",
        "bottomright",
        "topcenter",
        "bottomcenter",
        "leftcenter",
        "rightcenter"
    ]

    if num_xterms >= len(positions):
        print("Unless You're Quantum Computing, You Don't Need that Many; Stop Being Ridiculous")
        num_xterms = len(positions) - 1

    for i in range(num_xterms):
        ip_address = f"192.168.1.{i + 9}"
        mac_address = f"00:11:22:33:44:5{i}"
        
        position = positions[i]
        
        if position == "center":
            geometry = "80x24+0+0"
        elif position == "topright":
            geometry = "80x24-0+0"
        elif position == "topleft":
            geometry = "80x24+0+0" 
        elif position == "bottomleft":
            geometry = "80x24+0-0"
        elif position == "bottomright":
            geometry = "80x24-0-0"
        elif position == "topcenter":
            geometry = "80x24-0+0"
        elif position == "bottomcenter":
            geometry = "80x24-0-0"
        elif position == "leftcenter":
            geometry = "80x24+0-0"
        elif position == "rightcenter":
            geometry = "80x24-0-0"
        
        os.system(f'sudo xterm -geometry {geometry} -hold -e "ifconfig eth0 {ip_address} hw ether {mac_address} && python3 -c \'import Hell0; Hell0.main_menu()\'" &')
    
    root = tk.Tk()
    root.withdraw()

    exit(0)
    what_now()
    
def ddos_play():
    clear_screen()
    multi_manner()
    print("\033[0mThe First Four Instances are \033[92mPre-Postioned\033[0m. \033[91mDrag/drop\033[92m ⇘\033[0m for Your 5th Xterm")
    
    
    global num_xterms
    num_xterms = 5
    os.chdir(os.path.join(os.getenv("HOME"), "Desktop"))

    positions = [
        "center",
        "topright",
        "topleft",
        "bottomleft",
        "bottomright",
    ]

    for i in range(num_xterms):
        ip_address = f"192.168.1.{i + 9}"
        mac_address = f"00:11:22:33:44:5{i}"
        
        position = positions[i]
        
        if position == "center":
            geometry = "80x24+0+0"
            
                        
            os.system(f'sudo xterm -geometry {geometry} -hold -e "python3 -c \'import Hell0; Hell0.ddos_install()\'" &')
        elif position == "topright":
            geometry = "80x24-0+0"
            
                        
            os.system(f'sudo xterm -geometry {geometry} -hold -e "python3 -c \'import Hell0; Hell0.sql_attack()\'" &')
        elif position == "topleft":
            geometry = "80x24+0+0" 
            
                        
            os.system(f'sudo xterm -geometry {geometry} -hold -e "python3 -c \'import Hell0; Hell0.simba_menu()\'" &')       
        elif position == "bottomleft":
            geometry = "80x24+0-0"
            
                        
            os.system(f'sudo xterm -geometry {geometry} -hold -e "python3 -c \'import Hell0; Hell0.prox()\'" &')
        elif position == "bottomright":
            geometry = "80x24-0-0"
            
                        
            os.system(f'sudo xterm -geometry {geometry} -hold -e "python3 -c \'import Hell0; Hell0.cyber()\'" &')           
            
    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring(" ", "COVER THIS WITH TOP LEFT XTERM (or type 'exit' to quit): ")
    exit_command = "exit"  
    while True:
        if command and command != exit_command:
            send_command_to_xterms()
        else:
            main_menu()

    exit(0)

def what_now():
    print(colored("Where To?", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)     
    print
    print(" ")
    print("\033[91m1)\033[0m Go Back to \033[41mHell\033[0m")
    print("\033[91m2) \033[31mGAHHH! IT BURNS!!!\033[0m")
    choice = input("YOU CHOOSE: ")

    if choice == "1":
        change()
        main_menu()
    elif choice == "2":
        gahhh()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        menu() 

def repo():
    clear_screen()
    ascii_banner()
    print(colored("--------------------------------------------------------------------PLEASE NOTE--------------------------------------------------------------------", 'yellow', attrs=['reverse', 'blink', 'bold']))
    time.sleep(3)
    clear_screen()
    ascii_banner()
    print(colored("                                     ANY AND ALL TOOLS DOWNLOADED FROM HER WILL BE SAVED TO THE BORROWED TOOL FOLDER.                               ", 'red', attrs=['reverse', 'bold']))    
    print(colored("                                    ⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪                                ", 'yellow', attrs=['reverse', 'bold'])) 
    time.sleep(4)
    os.system("git clone https://github.com/Thr0wAway-n0w/Borrowed2.git")
    os.chdir("Borrowed2")
    os.system("python3 ch3r0.py")
    what_now()
 
def run_terminal_commands():
    protected_file = input("File to Protect: ")
    tripwire_file = input("Tripwire File: ")
    subprocess.run(["git", "clone", "https://github.com/vrikodar/Bullet"])
    os.chdir("Bullet")
    subprocess.run(["sudo", "chmod", "+x", "install.sh"])
    subprocess.run(["sudo", "bash", "install.sh"])
    subprocess.run(["gnome-terminal", "python3 dead.py", protected_file, "http://0.0.0.0:8080/",tripwire_file])
    time.sleep(2)
    pyautogui.typewrite('python3 dead.py ')
    pyautogui.typewrite(protected_file)
    pyautogui.typewrite(' http://0.0.0.0:8080/')
    pyautogui.typewrite(tripwire_file)     

def run_http_server():
    subprocess.run(["python3", "-m", "http.server", "8080"])



def deadman():
    clear_screen()
    ascii_banner()
    print(colored("--------------------------------------PLEASE NOTE!--------------------------------------", 'yellow', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    clear_screen()
    ascii_banner()
    header()
    print(colored("BEFORE HITTING ENTER IN THE POP UP WINDOW, PUT YOUR CONFIDENTIAL FILE IN THE BULLET FOLDER", 'red', attrs=['reverse', 'bold'])) 
    time.sleep(3)
    print(colored("----------YOUR TRIPWIRE FILE MUST GO ON THE DESKTOP. MODIFY AS YOU SEE FIT.----------", 'red', attrs=['reverse', 'bold'])) 
    time.sleep(3)
    run_terminal_commands()
    run_http_server()


def passw():
    clear_screen()
    ascii_banner()            
    print(colored("PASSWORDS", 'red', attrs=['reverse', 'bold']))     
    header()
    print("                  \033[91m1\033[0m) Pwnd                           \033[91m2\033[0m) HashBreak                           \033[91m3\033[0m) SecLists                                       ") 
    print(" ")
    print("                                               \033[41m SELECT NON-OPTION FOR MAIN MENU\033[0m ")
    print(" ")
    print("                                 \033[94m FOR OPTION DESCRIPTION; TYPE OPTION NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m HashBreak")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")      
    choice = input("\033[94mSelect an option: ")
    if choice == "1":
        pwnd()
    elif choice == "2":
        os.system("git clone https://github.com/AnonymousAt3/hashbreak.git")
        os.chdir("hashbreak")
        os.system("sudo chmod +x ./install.sh")
        os.system("sudo bash ./install.sh")
        os.system("sudo chmod +x ./hashbreak.sh")
        os.system("sudo bash ./hashbreak.sh")
        clear_screen()
        ascii_banner()
        header()
        what_now()
    elif choice == "3":
        os.system("sudo apt install seclists")
        os.system("seclists")
        what_now()
    elif choice == "Pwnd":
        print(" ")
        print("\033[96mPass Pwnd Checker")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mPython3 Program That Searches User input utilizing HaveIBeenPwnd.com's API to identify if password is secure or leaked":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        passw()    
    elif choice == "HashBreak":
        print(" ")
        print("\033[96mHashBreak Hashed Password Cracker")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mCracks multiple different types of Hashed Passwords utilizing a simple straightforward interface. ":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        passw()            
    elif choice == "SecLists":
        print(" ")
        print("\033[96mSecLists")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mRepo for Password Lists, Payloads and various other Goodies":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        passw()      
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        main_menu() 
        
def tfiles():
    clear_screen()
    ascii_banner()            
    print(colored("FORBIDDEN KNOWLEDGE", 'red', attrs=['reverse', 'bold']))     
    header()
    print("             \033[91m1\033[0m) Anarchist Cookbook             \033[91m2\033[0m) Black Circle             \033[91m3\033[0m) DoomsDay             \033[91m4\033[0m) Omnipotent Inc.                                   ") 
    print(" ")
    print("                            \033[91m5\033[95m) Firearm Manuals                               \033[91m6\033[95m) US Military Manuals")                                                                        
    print(" ")
    print("                                                             \033[91m7\033[0m\033[0m \033[0m) \033[31mRUN")
    print(" ")
    print("                               \033[94m FOR OPTION DESCRIPTION; TYPE OPTION NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m Anarchist Cookbook")
    print("                                                                       \033[91m  ~~~~~~~~~~~~~")     
    choice = input("\033[94mSelect an option: ")
    if choice == "1":
        clear_screen()
        os.system("lynx $dump http://www.textfiles.com/anarchy/") 
        tfiles()  
    elif choice == "2":
        clear_screen()
        os.system("lynx $dump http://www.textfiles.com/groups/BLACKCIRCLE/") 
        tfiles()
    elif choice == "3":
        os.system("lynx $dump http://www.textfiles.com/survival/")
        tfiles()
    elif choice == "4":
        os.system("lynx $dump http://www.textfiles.com/groups/OMNIPOTENT/")
        tfiles()   
    elif choice == "5":
        os.system("lynx $dump http://pdf.textfiles.com/manuals/FIREARMS/")
        tfiles()   
    elif choice == "6":
        os.system("lynx $dump http://pdf.textfiles.com/manuals/MILITARY/")
        tfiles()
    elif choice == "7":
        clear_screen()
        ascii_banner()
        header()
        what_now()
    elif choice == "Anarchist Cookbook":
        print(" ")
        print("\033[96mAnarchist Cookbook")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mThe Classic Banned Text. Also contains the Updated JollyRoger Version, Scams, Hacks, Lock picking, Incindiaries, Weapons, Inflict pain/Torture, and anything that goes BOOM ":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles()     
    elif choice == "Black Circle":
        print(" ")
        print("\033[96mBlack Circle")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mBlack Circle Productions, an IRC-centric anarchy and hacking group from the mid 90's, wrote this series of files to encourage people to cause mayhem":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles() 
    elif choice == "DoomsDay":
        print(" ")
        print("\033[96mDooms Day")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mA lot of survivalist files are dedicated to preparing for a coming collapse of society, assuming the worst and preparing for it. They're not waiting for the calvary; they're looking to eat the horses if they come this way.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles() 
    elif choice == "Omnipotent Inc.":
        print(" ")
        print("\033[96mOmnipotent Inc.")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mThe Reflex created files for Anarchy (bombs, poisons made from common plants, ect.) as well as Revenge. His hallmarks were good spelling, nice formatting, and intense hate of a guy named 'Rumpus'":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles()
    elif choice == "Firearm Manuals":
        print(" ")
        print("\033[96mFirearm Manuals")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mEnough Said...":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles() 
    elif choice == "US Military Manuals":
        print(" ")
        print("\033[96mUS Military Manuals")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mBroad assortment from Dear ol' Uncle Sam. Weapons, Tanks, Situational Training, Marksmanship, etc":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        tfiles()                                           
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        tfiles() 

def osintio():
    print("\033[0mBot's Found On Telegram")  
    print(" ")
    print("\033[96m0sintioBot")
    print(" ")
    print("", end="", flush=True) 
    for char in " \033[92mMirror of Russian Bot. Most well rounded and extensive results. 7 Day use without subscription \033[91mOR\033[0m just make new telegram with Burner numbers 'MUST BE VERIFIED'":
        print(char, end="", flush=True) 
        time.sleep(.04)
    time.sleep(1.5)
    tsar()
        
def tsar():
    print(" ")
    print("\033[96mTsar SnusBot")
    print(" ")
    print("", end="", flush=True) 
    for char in " \033[92mAKA @snusdb_bot. Decent for Breached Data \033[92mCOMPLETELY FREE*\033[0m 'minus the cost of your Soul, if you still have one'":
        print(char, end="", flush=True) 
        time.sleep(.04)
    time.sleep(3)    
    breach()
        
def breach():
    clear_screen()
    ascii_banner()            
    print(colored("DATA BREACH DATA", 'red', attrs=['reverse', 'bold']))     
    header()
    print("                      \033[92m1\033[0m) Bots                                                               \033[92m2\033[0m) LeakSeek          ") 
    print(" ")
    print("                                               \033[41m SELECT NON-OPTION FOR MAIN MENU\033[0m ")
    print(" ")
    print("                                 \033[94m FOR OPTION DESCRIPTION; TYPE OPTION NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m LeakSeek")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")   
    choice = input("\033[0mSelect an option: ")
    if choice == "1":
        osintio() 
        time.sleep(1)
        tsar()
    elif choice == "2":
        clear_screen()
        ascii_banner()
        gitlab()
        what_now()
    elif choice == "Bots":
        print(" ")
        print("\033[96mTelegram Bots")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mLists Two Known Telegram Bots that allow for Instant DataBreach Results Based on User Query":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        breach()
    elif choice == "LeakSeek":
        print(" ")
        print("\033[96mLeakSeek")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mPython3 Program That Searches Various Data Breach Sources for a query String of Any Length. Modest in Size; currently 5.6 Million Credentials only":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        breach()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        main_menu() 
        
def forbidden():
    clear_screen()
    ascii_banner()            
    print(colored("PASSWORDS/DATA LEAKS/FORBIDDEN KNOWLEDGE", 'red', attrs=['reverse', 'bold']))     
    header()
    print("                      \033[91m1\033[0m) Passwords                      \033[91m2\033[0m) DataBreach                     \033[91m3\033[0m) The Text Files          ") 
    print(" ")
    print("                                               \033[41m SELECT NON-OPTION FOR MAIN MENU\033[0m ")
    print(" ")
    choice = input("\033[94mSelect an option: ")
    if choice == "1":
        passw()
    elif choice == "2":
        breach()
    elif choice == "3":
        tfiles()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        main_menu() 
def main_menu():
    clear_screen()
    ascii_banner()            
    header()
    print("       \033[91m1\033[0m) Usernames                 \033[91m4\033[0m) Frameworks            \033[91m7\033[0m) GEO-0sint               \033[91m10\033[0m) Passwords/Data Leaks/Forbidden Knowledge") 
    print("       \033[91m2\033[0m) Emails/Phone #'s          \033[91m5\033[0m) Unclassified          \033[91m8\033[0m) DeadMan Switch          \033[91m11\033[0m) MULTI-MODE\033[0m")
    print("       \033[91m3\033[0m) Networks                  \033[91m6\033[0m) Cameras               \033[91m9\033[0m) Tool Repo-Depo          \033[91m666\033[0m) \033[41mGAHH! IT BURNS!!!\033[0m")

    print(" ")
    choice = input("\033[94mSelect an option: ")

    if choice == "1":
        menu1()
    elif choice == "2":
        emails_menu()
    elif choice == "3":
        networks_menu()
    elif choice == "4":
        frameworks_menu()
    elif choice == "5":
        unclassified_menu()
    elif choice == "6":
        cameras_menu()
    elif choice == "7":
        geo_menu()   
    elif choice == "8":
        clear_screen()
        deadman()
    elif choice == "9":
        clear_screen()
        ascii_banner()
        repo()  
    elif choice == "10":
        clear_screen()
        ascii_banner()
        forbidden()
    elif choice == "11":
        clear_screen()
        multi_banner 
        multi_menu() 
    elif choice == "666":
        clear_screen()
        ascii_banner()
        gahhh()
    elif choice == "Hidden":
        os.system("git clone https://github.com/Thr0wAway-n0w/Hide.git")
        os.chdir("Hide")
        os.system("python3 Shhh.py")
        what_now()
        clear_screen()
        ascii_banner()
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        main_menu()         

def again1():
    print("Search Again?")
    choice = input("Yes or No?: ")
    
    if choice == "Yes":
        username = input("User To Search: ")
        os.system(f'pipenv run maigret {username} --self-check --top-sites 1800 --no-recursion --retries 2 --timeout 35 --stats --graph --html')
        again1()
    elif choice == "No":
        clear_screen()
        ascii_banner()
        what_now()
        

def menu1():
    install_pipenv()
    menu()
def menu():
    change()  
    clear_screen()    
    while True:
        clear_screen()
        try:
            my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')        
        except OSError as e:
            print(f'Could not load the image, server said: {e.code} {e.msg}')
        my_art.to_terminal()    
        print(colored("USERNAME-0SINT", 'red', attrs=['reverse', 'blink', 'bold']))
        time.sleep(.01) 
        header()
        print("\033[91m1\033[0m) Maigret")
        print("\033[91m2\033[0m) Slash")
        print("\033[91m3\033[0m) Sherlock")
        print("\033[91m4\033[0m) AliaStorm")
        print("\033[91m5)\033[40m Run\033[0m")
        print("                               \033[94m FOR PROGRAM DESCRIPTION; TYPE PROGRAM NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m Maigret")
        print("                                                                         \033[91m  ~~~~~~~~~~~~~")
        choice = input("\033[0mSelect an option: ")
        async def main(username):
            os.system(f'pipenv run maigret {username} --self-check --top-sites 1800 --no-recursion --retries 1 --timeout 35 --stats --graph --html')
        if choice == '1':
            os.system("pip3 install maigret")
            username = input("Enter a username to search: ")
            html_file1 = f'report_{username}_plain.html'
            html_file2 = f'report_{username}_graph.html'
            print(colored("She THICC...", 'red', attrs=['reverse', 'blink', 'bold']))
            time.sleep(2)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(username))
            while True:
                option = input("Select an option: \033[91m1\033[0m) Search Again, \033[91m2\033[0m) Main Menu, \033[91m3\033[97m) IF\033[0m you ran Maigret ").upper()
                if option == '1':
                    clear_screen()
                    again1()
                elif option == '3':
                    user_home = os.path.expanduser('~')
                    os.chdir(os.path.join(user_home, 'Desktop', 'reports'))
                    html_file1 = f'report_{username}_plain.html'
                    html_file2 = f'report_{username}_graph.html'
                    if os.path.exists(html_file1):
                        webbrowser.open(os.path.join(os.getcwd(), html_file1))
                    if os.path.exists(html_file2):
                        webbrowser.open(os.path.join(os.getcwd(), html_file2))
                        clear_screen()
                        what_now()
                    else:
                        print(f"Error: File {html_file} not found")
            else:
                what_now()          
        if choice == '2':
            clone_repo('https://github.com/theahmadov/slash.git', 'slash')
            install_requirements()
            user_or_email = input("Enter a User or Email to search: ")
            search_username(user_or_email, 'slash.py')
        elif choice == '3':          
            clone_repo('https://github.com/sherlock-project/sherlock.git', 'sherlock')
            install_requirements()
            os.chdir('sherlock')
            user_or_email = input("Enter a Username to search: ")          
            search_username(user_or_email, 'sherlock.py --nsfw')
        elif choice == '4':
            clone_repo('https://github.com/AnonCatalyst/AliaStorm.git', 'AliaStorm')
            subprocess.run(["pip3", "install", "-r", "requirements.txt", "--break-system-packages"])
            clear_screen()
            username = input("Input User to Search: ")
            subprocess.run(["python3", "aliastorm.py", username])
            what_now()
        elif choice == '5':
            clear_screen()
            ascii_banner()
            what_now()
        elif choice == "Maigret":
            print(" ")
            print("\033[96mMaigret")
            print(" ")
            print("", end="", flush=True) 
            for char in " \033[92mScrapes Web For User Profile Information from 1,800 Sites. Pulls Bio's, Names, UserId tokens, profile pics etc. Tests and removes non working sites. Opens web browser with results and spider graph.":
                print(char, end="", flush=True) 
                time.sleep(.04)  
            time.sleep(3)
            menu()       
        elif choice == "Slash":
            print(" ")
            print("\033[96mSlash")
            print(" ")
            print("", end="", flush=True) 
            for char in " \033[92mScrapes web for usernames, Pastebins, Github, personal info. Leak check for Email Addresses as well":
                print(char, end="", flush=True) 
                time.sleep(.04)  
            time.sleep(3)
            menu()           
        elif choice == "Sherlock":
            print(" ")
            print("\033[96mSherlock")
            print(" ")
            print("", end="", flush=True) 
            for char in " \033[92mUsername search across many sites. Also has a fair amount of false positives but includes NSFW sites. The OG, both Slash and Maigret were created in their own respective attempts to improve the project":
                print(char, end="", flush=True) 
                time.sleep(.04)  
            time.sleep(3)
            menu()  
        elif choice == "AliaStorm":
            print(" ")
            print("\033[96mAliaStorm")
            print(" ")
            print("", end="", flush=True) 
            for char in " \033[92mUsername search. When selecting options, avoid including html information in the Results for readibility.":
                print(char, end="", flush=True) 
                time.sleep(.04)  
            time.sleep(3)
            menu()                   
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            clear_screen()
            ascii_banner()
            menu()        

        
        while True:
            option = input("Select an option: \033[91m1\033[0m) Search Again, \033[91m2\033[0m) Main Menu, \033[91m3\033[97m) IF\033[0m you ran Maigret ").upper()
            if option == '1':
                clear_screen()
                again1()
            elif option == '3':
                user_home = os.path.expanduser('~')
                os.chdir(os.path.join(user_home, 'Desktop', 'maigret', 'reports'))
                html_file1 = f'report_{username}_plain.html'
                html_file2 = f'report_{username}_graph.html'
                if os.path.exists(html_file1):
                    webbrowser.open(os.path.join(os.getcwd(), html_file1))
                if os.path.exists(html_file2):
                    webbrowser.open(os.path.join(os.getcwd(), html_file2))
                else:
                    print(f"Error: File {html_file} not found")
            else:
                what_now()

def landlubber():
    os.system("git clone https://github.com/drooling/phosint")
    os.chdir("phosint")
    os.system("git fetch")
    os.system("git pull")
    os.system("pip install -r requirements.txt")
    os.system("git pull")
    os.system("git fetch")
    clear_screen()

    print("Please Input Number \033[92m EXAMPLE 1112223333")
    choice = input("enter: ")

    try:
        subprocess.run(["python3", "phosint.py", choice])
    except Exception as e:
        print(f"Error: {e}")
        what_now()


def cellphone():
    clear_screen()
    init()
    api_url = "https://api.numlookupapi.com/v1/validate/"
    api_key = "num_live_KitBuwvasNy0xZ6nLt8wXJPK930NDTfS0GSLaVIr"
    print("\033[92mEXAMPLE NUMBER +19998887777\033[0m")
    phone_number = input("Enter a cellphone number: ")
    url = f"{api_url}{phone_number}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"{json.dumps(data, indent=4)}")
        for key, value in data.items():
            print(f"{Fore.MAGENTA}{key} : {Fore.GREEN}{value}{Style.RESET_ALL}")
        what_now()
    else:
        print(f"Error: {response.status_code}")
        what_now()

def emails_menu():
    clear_screen()
    ascii_banner()    
    print(colored("EMAIL / PHONE 0SINT", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01) 
    header()
    print("Sub Menu:")
    print(" ")
    print("\033[91m1\033[0m)\033[92m EMAIL \033[0m")
    print("\033[91m2\033[0m)\033[92m PHONE \033[92m")
    print("\033[91m3)\033[40m Run\033[0m") 
    print("                                \033[94m  FOR OPTION DESCRIPTION; TYPE OPTION NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m EMAIL")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")
    choice = input("\033[0mSelect an option: ")

    if choice == '1':
        venv_command = "python3 -m venv .lib_venv"
        os.system(venv_command)               
        subprocess.run(['git', 'clone', 'https://github.com/megadose/holehe'])
        os.chdir('holehe')
        os.system('docker build . -t my-holehe-image')
        clear_screen()
        email = input('Enter the email to search: ')
        subprocess.run(['docker', 'run', 'my-holehe-image', email])        
        process = subprocess.Popen(['docker', 'run', 'my-holehe-image', 'holehe', email], stdout=subprocess.PIPE)
        result = process.communicate()[0].decode('utf-8')
        result_output = result.replace('[+]', f'{Fore.GREEN}[+]{Style.RESET_ALL}')
        result_output = result_output.replace('[-]', f'{Fore.RED}[-]{Style.RESET_ALL}')
        result_output = result_output.replace('[x]', f'{Fore.YELLOW}[x]{Style.RESET_ALL}')
        result_output = result_output.replace('[!]', f'{Fore.MAGENTA}[!]{Style.RESET_ALL}')
        print(result_output)
        what_now()
    elif choice == "2":
        clear_screen()
        ascii_banner()
        print("1) Land Line")
        print("2) Cell Phone")
        choice = input("Select an option: ")
        if choice == "1":
            landlubber()
        if choice == "2":
            cellphone()
        else:
            what_now()
    elif choice == "3":
        clear_screen()
        ascii_banner()
        what_now()
    elif choice == "EMAIL":
        print(" ")
        print("\033[96mHolehe")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mWill Return list of sites that an email is registered on. Does contain False Negatives.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        emails_menu()
    elif choice == "PHONE":
        print(" ")
        print("\033[96mPhone Numbers")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mIf Landline, will return names of people Associated with that number as well as their physical Address. Cellphone's return Carrier information and General Location data":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        emails_menu()  
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        emails_menu()   

def gitlab():
    clear_screen()
    ascii_banner()
    header()
    print(colored("CLONING LeakSeek", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    os.system("git clone https://gitlab+deploy-token-4261899:gldt-Sz_XsWRrBG5sdVU2jXNE@gitlab.com/us3run0wn/LeakSeek.git")
    os.chdir("LeakSeek")
    os.system("git fetch")
    os.system("git pull")
    os.system("python3 LeakSeek.py")
    what_now()
    
def clone_repo2(url, folder_name):
    venv_command = "python3 -m venv .lib_venv"
    os.system(venv_command)        
    os.chdir('holehe')
    os.system('git clone ' + url)
    os.chdir(folder_name)
    os.system("git fetch")
    os.system("git pull")

def wifi_boost():
    os.system("git clone https://github.com/Takaklas/Wifi-Indoor-Location.git")
    os.chdir("Wifi-Indoor-Location")
    os.system("git fetch")
    os.system("git pull")
    subprocess.run(["python3", "net.py"])
    networks_menu()

def sql_attack():
    os.system('sudo apt install tor')
    os.system('sudo apt install torbrowser-launcher')
    os.system('sudo service tor start') 
    os.system('git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev')
    os.chdir('sqlmap-dev')
    os.system("git fetch")
    os.system("git pull")
    clear_screen()
    print(colored("SQL ATTACK", 'red', attrs=['reverse', 'blink', 'bold']))
    target_url = input("Enter the target URL: ")
    
     
    sqlmap_command = f'python3 sqlmap.py -u "{target_url}" -f --banner --dbs -g --tor -a --os-shell --batch'
    os.system(sqlmap_command)
    what_now()

def lynis_sys():
    os.system("git clone https://github.com/CISOfy/lynis")
    os.chdir("lynis")
    os.system("git fetch")
    os.system("git pull")
    clear_screen()
    ascii_banner()
    print("Selection:")
    print("\033[91m1\033[0m) System Audit")
    print("\033[91m2\033[0m) GO-BACK")
    choice = input("Enter your choice: ")

    if choice == '1':
        os.system("./lynis audit system")
        what_now()
    elif choice == '2':
        print("\033[91mGO-BACK\033[0m")
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        change()     
        networks_menu()
        
def ip_lookup():
    clear_screen()
    ascii_banner() 
    subprocess.call(['git', 'clone', 'https://gitlab.com/Ar-baaz/IP-Lookup-Tool.git'])
    os.chdir('IP-Lookup-Tool')
    subprocess.call(['python3', '-m', 'pip', 'install', 'flask'])
    subprocess.call(['python3', '-m', 'pip', 'install', 'ipapi'])
    os.system('python3 app.py')

def chop_chop():
    clear_screen()
    print(colored("                             OPTIMIZING WiFi                           ", 'red', attrs=['reverse', 'blink', 'bold']))
    print("\033[0mYOU HAVE \033[91m30\033[0m SECONDS\033[0m TO\033[0m \033[91mDISCONNECT\033[0m THEN \033[91mRECONNECT\033[0m YOUR WIFI. \033[91mCHOP CHOP!!!\033[0m")

def unclassified_menu():
    change()
    clear_screen()
    ascii_banner()
    print(colored("Unclassified-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01) 
    header()
    print("\033[91m1\033[0m) WebHound")
    print("\033[91m2\033[0m) Ominis-Osint")
    print("\033[91m3\033[0m) SockPuppet")
    print("\033[91m4)\033[40m Run\033[0m")    
    print("                               \033[94m FOR PROGRAM DESCRIPTION; TYPE PROGRAM NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m WebHound")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")
    choice = input("\033[0mSelect an option: ")
    if choice == "1":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))       
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/WebHound"])
        os.chdir("WebHound")
        print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        subprocess.run(["python3", "install.py"])
        subprocess.run(["python3", "webhound.py"])
        what_now()
    elif choice == "2":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))   
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/Ominis-Osint"])
        os.chdir("Ominis-Osint")
        print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        os.system("python3 -m pip install -r requirements.txt")
        os.system(f"sudo chmod +x ./install.sh")
        os.system("sudo bash ./install.sh")    
        os.system("python3 ominis.py")
        what_now()
    elif choice == "3":
        print(colored("CTRL + X TO EXIT PUPPET DETAILS", 'red', attrs=['reverse', 'blink', 'bold']))        
        os.system("git clone https://github.com/jaskaran2002/Sock-Puppet-Generator.git")
        os.chdir("Sock-Puppet-Generator")
        os.system("git fetch")
        os.system("git pull")
        os.system("python3 main.py")
        time.sleep(3)
        os.system("nano output.json")
        clear_screen()
        ascii_banner()
        change()
        unclassified_menu()
    elif choice == "4":
        clear_screen()
        ascii_banner()
        what_now()
    elif choice == "WebHound":
        print(" ")
        print("\033[96mWebHound")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mSearch String In Google, Bing, DuckDuckGo etc. Returns results from each platorm with Titles, URL's and Descriptions":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        unclassified_menu()   
    elif choice == "Ominis-Osint":
        print(" ")
        print("\033[96mOminis-Osint")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mTimeline Specific Search - General String Query with Multi-Proxy Rotation to avoid detection":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        unclassified_menu()
    elif choice == "SockPuppet":
        print(" ")
        print("\033[96mSockPuppet")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mGenerate Random Personal Details For SockPuppet Accounts":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        unclassified_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        change()
        unclassified_menu()     

def simba_menu():
    clear_screen()
    ascii_banner()
    print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))
    header()
    subprocess.run(["git", "clone", "https://github.com/SxNade/Simba"])
    os.chdir("Simba")
    clear_screen()
    ascii_banner()
    print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
    header()
    os.system("sudo chmod +x simba")
    clear_screen()
    ascii_banner()
    print(colored("Web Header Scan", 'red', attrs=['reverse', 'blink', 'bold']))
    header()
    url = input("url to scan: ")
    subprocess.run(["./simba", "--link", url])
    what_now()

def subdomains():
    clear_screen()
    ascii_banner()
    os.system("sudo apt install sublist3r")
    clear_screen()
    ascii_banner()
    print(colored("Example Domain: REDDIT.COM", 'red', attrs=['reverse', 'blink', 'bold']))
    url = input("Enter Domain: ")
    subprocess.run(["sublist3r", "-d", url])
    what_now()    

def prox():
    clear_screen()
    ascii_banner
    print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))
    header()
    subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/LuminaProxy.git"])
    os.chdir("LuminaProxy")
    clear_screen()
    ascii_banner()
    print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
    header()
    os.system("python3 install.py")
    subprocess.run(["python3", "lumina.py"])
    what_now()    

def cyber():
    clone_command = "git clone https://github.com/AnonymousAt3/cybermap.git"
    os.system(clone_command)
    os.system("git fetch")
    os.system("git pull")
    chmod_command = "sudo chmod +x cybermap/cybermap.sh"
    os.system(chmod_command) 
    bash_command = "bash cybermap/cybermap.sh"
    os.system(bash_command) 

def networks_menu():
    clear_screen()
    ascii_banner()
    print(colored("Networks-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01) 
    header()
    print("\033[95m1\033[0m) CyberMap \033[95mINFO\033[0m")
    print("\033[91m2\033[0m) Sql-map \033[91mATCK\033[0m")
    print("\033[95m3\033[0m) Lynis \033[95mINFO\033[0m")
    print("\033[95m4\033[0m) IP-Lookup \033[95mINFO\033[0m")    
    print("\033[95m5\033[0m) PortScan \033[95mINFO\033[0m")
    print("\033[95m6\033[0m) Simba \033[95mINFO\033[0m")
    print("\033[95m7\033[0m) ProxyScrape \033[95mINFO\033[0m")    
    print("\033[92m8\033[0m) WiFi\033[92m TWEAK\033[0m") 
    print("\033[95m9\033[0m) Subdomains \033[95mINFO\033[0m") 
    print("\033[91mUFO\033[0m) UFONET \033[91mATCK\033[0m")     
    print("\033[91m10)\033[40m Run\033[0m")    
    print("                               \033[94m FOR PROGRAM DESCRIPTION; TYPE PROGRAM NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m CyberMap")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")
    choice = input("\033[0mSelect an option: ")
    if choice == '1':
        cyber()
    elif choice == "2": 
        sql_attack()
    elif choice == "3":
        lynis_sys()
        what_now()
    elif choice == "4":
        clear_screen()
        ascii_banner()
        print(colored("Select 1 to Continue", 'red', attrs=['reverse', 'blink', 'bold']))
        time.sleep(.01) 
        header()
        print("1) Open '\033[91mREFRESH URL IF NEEDED\033[0m'")
        print("2) Main Menu")
        choice = input("Select choice: ")
        
        if choice == "1": 
            webbrowser.open("http://127.0.0.1:5000")
            ip_lookup()            
            what_now()
        
        if choice == "2":
            clear_screen()
            main_menu()         
    
    elif choice == "5":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        subprocess.run(["git", "clone", "https://github.com/Thr0wAway-n0w/borrowed.git"])
        os.chdir("borrowed")
        clear_screen()
        ascii_banner()
        print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        os.system("python3 -m pip install -r requirements.txt")
        subprocess.run(["python3", "ports.py"])
        what_now()       
    elif choice == "6":
        simba_menu()
    elif choice == "7":
        prox()
    elif choice == "8":
        clear_screen()
        print(colored("                             OPTIMIZING WiFi                           ", 'red', attrs=['reverse', 'blink', 'bold']))
        print("\033[91m\033[95m-----------------------------------\033[97m30\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m29\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m28\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m27\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m26\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m25\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m24\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m23\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m22\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[97m21\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m20\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m19\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m18\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m17\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m16\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m15\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m14\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m13\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m12\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[93m11\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m10\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m09\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m08\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m07\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m06\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m05\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m04\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m03\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m02\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m01\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91m\033[95m-----------------------------------\033[31m00\033[95m-----------------------------------\033[97m\033[0m")
        time.sleep(1)
        chop_chop()
        print("\033[91mC\033[0m")
        time.sleep(.05)
        chop_chop()   
        print("\033[91mCH\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHO\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP C\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP CH\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP CHO\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP CHOP\033[0m")
        time.sleep(.05)
        chop_chop()
        print("\033[91mCHOP CHOP!\033[0m")
        time.sleep(.05)
        chop_chop()     
        print("\033[91mCHOP CHOP!!\033[0m")
        time.sleep(.05)
        chop_chop() 
        print("\033[91mCHOP CHOP!!!\033[0m")
        time.sleep(.05)
        chop_chop()
        time.sleep(2)
        clear_screen()
        print("\033[91mTYPE IN THE BSSID STRING THAT IS \033[96mCLOSEST\033[91m TO 30 IN SIGNAL LEVEL\033[0m")
        wifi_boost()
        what_now()
    elif choice == '9':
        subdomains()
    elif choice == '10':
        clear_screen()
        ascii_banner()
        what_now()
    elif choice == 'UFO':
        clear_screen()
        ascii_banner()
        os.system("git clone https://github.com/epsylon/ufonet.git")
        os.chdir("ufonet")
        os.system("git fetch")
        os.system("git pull")
        os.system("sudo apt install python3-pycurl")
        os.system("sudo apt install python3-geoip")
        os.system("sudo apt install libgeoip-dev")
        os.system("sudo apt install libgeoip1")
        os.system("sudo apt install python3-whois")
        os.system("sudo apt install python3-requests")
        os.system("sudo apt install python3-scapy")
        os.system("pip3 install GeoIP")
        os.system("pip3 install python-geoip")
        os.system("pip3 install pygeoip")
        os.system("pip3 install requests")
        os.system("pip3 install pycurl")
        os.system("pip3 install whois")
        os.system("pip3 install scapy-python3")
        os.system("sudo chmod +x ufonet")
        os.system("python3 ./ufonet --gui")
        what_now()        
    elif choice == "CyberMap":
        print(" ")
        print("\033[96mCyberMap")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mScan Ports, Detect Heartbleed, os, Network, HostNames, Firewalls, IP's, and Both TCP and UDP Protocols":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu()
    elif choice == "Sql-map":
        print(" ")
        print("\033[96mSql-map")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[91mAutomated sql Injection and Database Takeover Tool":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "Lynis":
        print(" ")
        print("\033[96mLynis")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mSecurity auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "IP-Lookup":
        print(" ")
        print("\033[96mIP-Lookup")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mProvides a simple web interface where you can enter an IP address and retrieve its corresponding location information.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "PortScan":
        print(" ")
        print("\033[96mPortScan")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mSlightly Modified Quick Open Port Scanner for URL's":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "Simba":
        print(" ")
        print("\033[96mSimba")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mWeb Header Security Scanner for URL's":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "ProxyScrape":
        print(" ")
        print("\033[96mProxyScrape")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mScrapes for free proxies. Tests list and returns all validated proxies from list.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "WiFi":
        print(" ")
        print("\033[96mOptimize WiFi")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mManipulate WiFi Interface to ensure the Fastest speed for That network":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "Subdomains":
        print(" ")
        print("\033[96mSubdomains")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[95mLists Known Subdomains for Any domain user inputs":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    elif choice == "UFONET":
        print(" ")
        print("\033[96mUFONET")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[91mMultiAttack Protocol for DoS and DDoS Attacks using Zombie Servers across the Globe.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        networks_menu() 
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        networks_menu()     

    
def frameworks_menu():
    clear_screen()
    ascii_banner()
    print(colored("Frameworks-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01) 
    header()
    print("\033[95m1\033[0m) Maryam")
    print("\033[95m2\033[0m) Mr.Holmes 'TYPE \033[92m2.1\033[0m FOR LINUX/MAC, TYPE \033[92m2.2\033[0m FOR WINDOWS")
    print("\033[95m3\033[0m) Coeus")
    print("\033[91m4)\033[40m Run\033[0m")
    print("                               \033[94m FOR PROGRAM DESCRIPTION; TYPE PROGRAM NAME \033[0mAS IT APPEARS\033[90m Example:\033[92m Maryam")
    print("                                                                         \033[91m  ~~~~~~~~~~~~~")
    choice = input("\033[0mSelect an option: ")

    if choice == '1':
        install_command = "pip install git+https://github.com/saeeddhqan/maryam.git"
        os.system(install_command)
        run_command = "maryam -s"
        os.system(run_command)
        show_command = "show modules"
        what_now()
    elif choice == '2.1':
        clone_command = "git clone https://github.com/Lucksi/Mr.Holmes"
        os.system(clone_command)
        update_command = "sudo apt-get update"
        os.system(update_command)
        os.chdir("Mr.Holmes")
        os.system("git fetch")
        os.system("git pull")        
        venv_command = "python3 -m venv .lib_venv"
        os.system(venv_command)
        chmod_command = "sudo chmod +x install.sh"
        os.system(chmod_command)
        install_command = "sudo bash install.sh"
        os.system(install_command)
        activate_command = "source .lib_venv/bin/activate"
        os.system(activate_command)
        requirements_command = "pip3 install -r requirements.txt"
        os.system(requirements_command)
        run_script_command = "sudo python3 MrHolmes.py"
        os.system(run_script_command) 
        what_now() 
    elif choice == '2.2':
        clone_command = "git clone https://github.com/Lucksi/Mr.Holmes"
        os.system(clone_command)
        os.chdir("Mr.Holmes")
        os.system("git fetch")
        os.system("git pull")
        install_command = "Install.cmd"
        os.system(install_command)
        run_script_command = "python3 MrHolmes.py"
        os.system(run_script_command)  
        what_now()   
    elif choice == "3":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/Coeus-Framework.git"])
        os.chdir("Coeus-Framework")
        os.system("git fetch")
        os.system("git pull")
        clear_screen()
        ascii_banner()
        print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
        header()
        os.system("python3 -m pip install -r requirements.txt")
        clear_screen()
        ascii_banner()
        print(colored("Refresh Browser If Required...", 'red', attrs=['reverse', 'blink', 'bold']))       
        header()
        webbrowser.open("http://127.0.0.1:5000")        
        os.system("python3 webui.py")
        what_now()
    elif choice == "4":
        clear_screen()
        ascii_banner()
        what_now()
    elif choice == "Maryam":
        print(" ")
        print("\033[96mMaryam")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mExtensive Osint Framework. Just type 'show modules' after cloning in to see options":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        frameworks_menu() 
    elif choice == "Mr.Holmes":
        print(" ")
        print("\033[96mMr.Holmes")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mWell Rounded Osint Tool utilizing a Web interface. Emails, Usernames, Phone numbers, Names, ect.":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        frameworks_menu() 
    elif choice == "Coeus":
        print(" ")
        print("\033[96mCoeus")
        print(" ")
        print("", end="", flush=True) 
        for char in " \033[92mJust a Web Interface/Repository of Online Resources":
            print(char, end="", flush=True) 
            time.sleep(.04)  
        time.sleep(3)
        frameworks_menu()    
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        frameworks_menu()     
    
def cameras_menu():
    clear_screen()
    ascii_banner()
    print(colored("Traffic-Cam Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01) 
    header()
    print("\033[91m1\033[0m) \033[91mU\033[97mS\033[94mA\033[0m")
    print("\033[91m2\033[0m) UK")
    print("\033[91m3)\033[40m Run\033[0m")
    choice = input("Select an option: ")

    if choice == "1":
        usa_menu()
    elif choice == "2":
        uk_menu()
    elif choice == "3":
        clear_screen()
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        cameras_menu()     

def cam_menu():
    clear_screen()
    ascii_banner()
    print("Enter TOWN NAME (ex. Norfolk)")
    TN = input("> ")
    print("Enter STATE ABBREVIATION (ex. VA)")
    SA = input("> ")
    print("Enter STREET NAME (ex. Lucas)")
    SN = input("> ")
    print("Enter STREET SUFFIX (ex. Road)")
    SB = input("> ")
    print("Enter STREET NUMBER (ex. 430)")
    SNB = input("> ")

    address = f"{SNB} {SN} {SB}, {TN}, {SA}"
    api_key = "AIzaSyDsvdPFQSi5Oc14mSCNivuc-afU5Gg-83o"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()

    if response["status"] == "OK":
        results = response["results"]
        if len(results) != 1:
            print("THIS LOCATION IS NOT A GOOD POINT OF REFERENCE, PLEASE SELECT ANOTHER")
        else:
            location = results[0]["geometry"]["location"]
            LAT = location["lat"]
            LONG = location["lng"]
            new_url = f"https://trafficview.org/live_traffic/#9/{LAT}/{LONG}"
            webbrowser.open_new_tab(new_url)
            cameras_menu()
    else:
        error_message = response.get("error_message", "Unknown Error")
        print("Error occurred:", error_message)
        cameras_menu()

def usa_menu():
    clear_screen()
    ascii_banner()
    print(colored("USA Sub-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)
    header()
    print('1) \033[95mCalifornia\033[0m')
    print('2) \033[95mDelaware\033[0m')
    print('3) \033[95mMississippi\033[0m')
    print('4) \033[95mNebraska\033[0m')
    print('5) \033[95mNevada\033[0m')
    print('6) \033[95mTennessee\033[0m')
    print('7) \033[95mTexas\033[0m ZOOM OUT')
    print('8) Search Nearest by Address \033[95mAZ\033[0m, \033[95mCA\033[0m, \033[95mDEL\033[0m, \033[95mFL\033[0m, \033[95mGA\033[0m, \033[95mMD\033[0m, \033[95mVA\033[0m, \033[95mVT\033[0m')
    print("\033[41m9)\033[40m Run\033[0m")
    choice = input("Select an option: ")

    if choice == "1":
        webbrowser.open("https://cwwp2.dot.ca.gov/vm/nomap.htm")
    elif choice == "2":
        webbrowser.open("https://deldot.gov/map/index.shtml")
    elif choice == "3":
        webbrowser.open("https://www.mdottraffic.com/default.aspx?fullsite=1")
    elif choice == "4":
        webbrowser.open("https://lincolnne.maps.arcgis.com/apps/MapTour/index.html?appid=80596d640a63496e84f02bf26ca105bb")
    elif choice == "5":
        webbrowser.open("https://www.nvroads.com/")
    elif choice == "6":
        webbrowser.open("https://www.knoxvilletn.gov/residents/streets_traffic_transit/tdot_smart_way_traffic_cameras")
    elif choice == "7":
        webbrowser.open("https://its.txdot.gov/its/District/AMA")
    elif choice == "8":
        cam_menu()
    elif choice == "9":
        clear_screen()
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        usa_menu()     

def uk_menu():
    clear_screen()
    ascii_banner()
    print(colored("UK Sub-Menu", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)    
    header()
    print("\033[91m1\033[0m) London")
    print("\033[91m2)\033[40m Run\033[0m")
    choice = input("Select an option: ")

    if choice == "1":
        webbrowser.open("https://www.tfljamcams.net/")
    elif choice == "2": 
        clear_screen()
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        uk_menu()     
    

if __name__ == "__main__":
    main_menu()
