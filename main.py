import ctypes
import string
import os
import time

# IMPORTANT VARIABLES
USE_WEBHOOK = True
discordWebhookURL = "[INSERT DISCORD WEBHOOK URL HERE]"

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:
    import requests
except ImportError:
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()

url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by https://www.youtube.com/@hassamohammed")
        else:
            print(f'\33]0;Nitro Generator and Checker - Made by https://www.youtube.com/@hassamohammed\a',
                  end='', flush=True)

        print(""" $$\                                                                       
$$ |                                                                      
$$$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$  __$$\  \____$$\ $$  _____|$$  _____| \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ |  $$ | $$$$$$$ |\$$$$$$\  \$$$$$$\   $$$$$$$ |$$ / $$ / $$ |$$ /  $$ |
$$ |  $$ |$$  __$$ | \____$$\  \____$$\ $$  __$$ |$$ | $$ | $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$  |
\__|  \__| \_______|\_______/ \_______/  \_______|\__| \__| \__| \______/ 
                                                        """)
        time.sleep(2)
        self.slowType("Made by: https://www.youtube.com/@hassamohammed", .02)
        time.sleep(1)
        self.slowType(
            "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:
            self.slowType(
                "To continue please input the number '1': ", .02, newLine=False)
            url = discordWebhookURL
            discordWebhookURL2 = input()
            webhook = discordWebhookURL2 if discordWebhookURL2 != "" else None
            
            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by https://www.youtube.com/@hassamohammed")
                print("")
            else:
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by https://www.youtube.com/@hassamohammed\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro:str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"WORKING NITRO CODE FOUND, REDEEM IT NOW! @everyone \n{nitro}"
                ).execute()

            return True
        else:
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()