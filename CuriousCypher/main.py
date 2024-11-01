import os
import random
import shutil
import time
import hashlib
from lib.humanName import HumanNames
from lib.nameOfMonth import MonthNames
from lib.animal import AnimalList

class BaseText:
    dict = ["admin", "itadmin", "administrator", "theadmins", "admins", "me", 
            "password", "123456", "iloveyou"]
    years = range(1945, 2025)
    months = range(1, 13)  
    symbols = ["#", "@", "!", "$", "/", "*", "&", "^", "+", "^", "~", "?"]

def GeneratePassword():
    passwords = []
    TheText = BaseText.dict
    years = BaseText.years
    months = BaseText.months  
    symbols = BaseText.symbols
    NamaCowok = HumanNames.get_names("indonesian", "male")
    NamaCewek = HumanNames.get_names("indonesian", "female")
    month_names = MonthNames().months["en"]
    HewanInstance = AnimalList()
    Hewan = HewanInstance.get_animals()

    random_numbers = [str(random.randint(100, 999)) for _ in range(10)]

    def add_variations(base):
        return [
            base,  
            base.lower(),  
            base.upper(),  
            base.capitalize(),  
            ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(base)]) 
        ]

    for text in TheText:
        variations = add_variations(text)

        for variant in variations:
            for year in years:
                for symbol in symbols:
                    passwords.append(f"{variant}{symbol}{year}")
                    passwords.append(f"{year}{symbol}{variant}")
                    passwords.append(f"{symbol}{variant}{year}")
                    passwords.append(f"{variant}{year}{symbol}")

                for number in random_numbers:
                    passwords.append(f"{variant}{number}")
                
                for symbol in symbols:
                    passwords.append(f"{variant}{symbol}{number}")

                for month in months:
                    month_name = month_names[month - 1]  
                    passwords.append(f"{variant}{symbol}{month}")
                    passwords.append(f"{month}{symbol}{variant}")
                    passwords.append(f"{symbol}{variant}{month}")
                    passwords.append(f"{variant}{month}{symbol}")
                    passwords.append(f"{variant}{symbol}{month_name}")
                    passwords.append(f"{month_name}{symbol}{variant}")
                    passwords.append(f"{symbol}{variant}{month_name}")
                    passwords.append(f"{variant}{month_name}{symbol}")

            for name in NamaCowok + NamaCewek:
                for symbol in symbols:
                    passwords.append(f"{variant}{random.choice(random_numbers)}")  
                    mixed_case_name = ''.join([c.upper() if i % 2 == 1 else c.lower() for i, c in enumerate(name)])
                    passwords.append(f"{mixed_case_name}{random.choice(random_numbers)}")
                    passwords.append(f"{variant}{symbol}{name}")
                    passwords.append(f"{name}{symbol}{variant}")
                    passwords.append(f"{symbol}{variant}{name}")
                    passwords.append(f"{variant}{name}{symbol}")

            for animal in Hewan:
                for symbol in symbols:
                    passwords.append(f"{variant}{symbol}{animal}")  
                    passwords.append(f"{animal}{symbol}{variant}")
                    passwords.append(f"{symbol}{variant}{animal}")
                    passwords.append(f"{variant}{animal}{symbol}")

            for number in random_numbers:
                passwords.append(f"{variant}{number}")  
                passwords.append(f"{variant}{number}{random.choice(symbols)}")  
                passwords.append(f"{number}{variant}") 
                passwords.append(f"{variant}{random.choice(symbols)}{number}") 

            passwords.append(variant)

    return list(set(passwords))

def LoadingSpinner():
    spinner = ['|', '/', '-', '\\']
    for _ in range(20): 
        for symbol in spinner:
            print(f'\rLoading {symbol}', end='', flush=True)
            time.sleep(0.1)

class Colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    magenta = '\033[95m'
    reset = '\033[0m'

def StartHybridAttack(target_hash, hash_algorithm="sha256"):
    passwords = GeneratePassword()
    for password in passwords:
        if hash_algorithm == "sha256":
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        elif hash_algorithm == "md5":
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        elif hash_algorithm == "sha1":
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
        elif hash_algorithm == "sha512":
            hashed_password = hashlib.sha512(password.encode()).hexdigest()
        else:
            print(Colors.red + f"Hash algorithm {hash_algorithm} is not supported." + Colors.reset)
            return None

        if hashed_password == target_hash:
            print(Colors.green + f"Password found: {password}" + Colors.reset)
            return password
        print(Colors.yellow + f"Trying: {Colors.green}{password}" + Colors.reset)
    
    print(Colors.red + "Password not found." + Colors.reset)
    return None

def clear():
    if os.name == "nt":
        os.system("cls") 
    else:
        os.system("clear")

def Menu():
    clear()

    terminal_width = shutil.get_terminal_size().columns

    banner = """_____         _   _____                 
|  |  |___ ___| |_|   __|___ ___ ___ ___ 
|     | .'|_ -|   |   __| . |  _|  _| -_|
|__|__|__,|___|_|_|__|  |___|_| |___|___|
@adjisan"""

    centered_banner = "\n".join(line.center(terminal_width) for line in banner.splitlines())
    
    print(Colors.blue + centered_banner + Colors.reset)

    info = f"""{Colors.green}Hashforce 2024
{Colors.red}Version    : {Colors.reset}3_ThreeTon
{Colors.red}Creator    : {Colors.reset}github.com/adjidev

{Colors.red}Legal Disclaimer:{Colors.reset}
This tool is designed for educational purposes only. Unauthorized use of this tool
to crack or compromise the security of systems is prohibited.
"""
    print(info)

    hashMenu = """Select Hash Type:
{1}---[  MD5    ]
{2}---[  SHA256 ]
{3}---[  SHA512 ]
{4}---[  SHA-1  ]
{0}---[  EXIT   ]"""
    print(hashMenu)

    choice = input(Colors.magenta + "Enter a Number\n~#" + Colors.reset)
    if choice == "1":
        hash_type = "md5"
    elif choice == "2":
        hash_type = "sha256"
    elif choice == "3":
        hash_type = "sha512"
    elif choice == "4":
        hash_type = "sha1"
    elif choice == "0":
        print(Colors.red + "Exiting..." + Colors.reset)
        return
    else:
        print(Colors.red + "Invalid selection. Try again." + Colors.reset)
        Menu()
        return

    target_hash = input(Colors.green + "Target hash: " + Colors.reset)
    LoadingSpinner()
    print(Colors.yellow + f"Starting attack using {hash_type.upper()}..." + Colors.reset)
    StartHybridAttack(target_hash, hash_type)

Menu()