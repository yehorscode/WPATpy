from colorama import Fore, Back, Style
import time

# Alphabet imports
from runs.nato_phonetics import run_nato_phonetics

print(
	f"""{Fore.GREEN}Welcome to the weird phonetic alphabets translator!{Style.RESET_ALL}
{Fore.CYAN}1: NATO phonetic alphabet
q/e/enter: Quit"""
)
chosen_action = input(f"{Fore.LIGHTBLUE_EX}Choose operation mode:{Style.RESET_ALL}")

if chosen_action == "1":
    run_nato_phonetics()
if chosen_action == "q" or chosen_action == "e" or chosen_action == "":
    print(f"{Fore.RED}Quitting..{Style.RESET_ALL}")
    quit()
