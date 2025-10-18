import pyttsx3
from alphabet import nato_phonetic_alphabet
import time
from colorama import Fore, Back, Style
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config_path = Path(__file__).with_name("config.ini")
config.read(str(config_path))

# Line available in config under nato_phonetics!
speed = 150 
if config.has_section("nato_phonetics"):
    try:
        speed = config.getint("nato_phonetics", "speed", fallback=speed)
    except (ValueError, TypeError):
        pass

engine = pyttsx3.init()
engine.setProperty("rate", speed)

def run_nato_phonetics():
    print(
        f"""{Fore.LIGHTBLACK_EX}\nNATO phonetic alphabet{Style.RESET_ALL}
{Fore.CYAN}1: Sentence -> NATO phonetics (enter)
2: Nato phonetics -> Sentence
o: Options{Style.RESET_ALL}"""
    )
    chosen_mode = input(f"{Fore.LIGHTBLUE_EX}Choose operation mode:{Style.RESET_ALL}")

    def split_sentence(sentence, alphabet):
        completed_splitted_sentence = []
        for letter in sentence:
            if letter == " ":
                completed_splitted_sentence.append("|")
            elif letter == ".":
                completed_splitted_sentence.append("dot")
            else:
                # Pass through unsupported symbols instead of crashing
                completed_splitted_sentence.append(alphabet.get(letter.lower(), letter))
        return completed_splitted_sentence

    def sentence_to_nato():
        sentence = input("Enter sentence: ")

        mapped = split_sentence(sentence, nato_phonetic_alphabet)

        print("NATO:", " ".join("space" if x == "|" else x for x in mapped))
        for x in mapped:
            if x == "|":
                engine.say("space")
                engine.runAndWait()
                time.sleep(0.3)
            else:
                engine.say(x)
                engine.runAndWait()

    def nato_to_sentence():
        for i in nato_phonetic_alphabet: print(Fore.LIGHTBLACK_EX,i, ":", nato_phonetic_alphabet[i],Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX, "To use spaces just type in `space`", Style.RESET_ALL)
        nato = input("Enter NATO phonetics (REMEMBER CORRECT SPELLING): ")

        reverse = {v.lower(): k for k, v in nato_phonetic_alphabet.items()}
        tokens = [t.strip().lower() for t in nato.strip().split() if t.strip()]
        result_chars = []
        for t in tokens:
            if t in ("|", "/", "space"):
                result_chars.append(" ")
            elif t == "dot":
                result_chars.append(".")
            elif t in reverse:
                result_chars.append(reverse[t])
            else:

                result_chars.append("[" + t + "]")
        sentence = "".join(result_chars)
        print("Sentence:", sentence)

        if sentence:
            engine.say(sentence)
            engine.runAndWait()



    if chosen_mode == "1":
        sentence_to_nato()
    elif chosen_mode == "2":
        nato_to_sentence()
