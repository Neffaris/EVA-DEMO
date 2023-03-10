from requests import get

import system_login_screen
import time
import pyttsx3
import speech_recognition as sr
import pyautogui
from os import system
import threading
import platform
import subprocess
from datetime import datetime
from datetime import date
from preferredsoundplayer import playsound

def evaMainCore(user):

    try:
        def show_time_and_date():
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            print("  Czas:", current_time,"|", today)

        engine = 0 # Dotyczy Text-to-Speech
        is_listening = False # Dotyczy Speech Recognition

        waiting_for_a_command = True
        while waiting_for_a_command is True:

            def cls():
                system('cls||clear')

            show_time_and_date_handler = threading.Thread(target=show_time_and_date, args=())
            show_time_and_date_handler.start()
            print("")
            print(" ", user, end='')
            command = input(" >| ")

            if command == "microtest":  # PRÓBA MIKROFONU
                try:
                    r = sr.Recognizer()

                    print(" SYSTEM: ")
                    def talk(tekst):
                        if engine == pyttsx3.init():
                            engine.say(tekst)
                            engine.runAndWait()

                    def get_text():
                        with sr.Microphone() as source:
                            # noinspection PyBroadException
                            try:
                                print(" EVA: Naciśnij Ctrl + C aby przestać słuchać.")
                                print(" EVA: Słucham...")
                                if engine == pyttsx3.init():
                                    engine.say("Słucham")
                                    engine.runAndWait()
                                audio = r.listen(source)
                                listening = r.recognize_google(audio, language='pl-PL')
                                if listening != "":
                                    return listening
                                return 0
                            except Exception:
                                return 0

                    while True:
                        txt = get_text()
                        if not txt == 0:
                            talk(txt)
                            print(" EVA: Słyszę cie głośno i wyraźnie :)")
                            print(" EVA: Mikrofon działa poprawnie")
                            if engine == pyttsx3.init():
                                engine.say("Słyszę cię głośno i wyraźnie, mikrofon działa poprawnie")
                                engine.runAndWait()
                            break
                        else:
                            print(" EVA: Nie słyszę cię")
                            print(" EVA: Wpisz Y aby powtórzyć próbę lub N aby zakończyć test")
                            if engine == pyttsx3.init():
                                engine.say("Nie słyszę cię")
                                engine.say("Wpisz Y aby powtórzyć próbę lub")
                                engine.say("N aby zakończyć test")
                                engine.runAndWait()
                            print(user, end='')
                            micro_test_decision = input(" >| ")
                            if micro_test_decision == "Y" or micro_test_decision == "y":
                                continue
                            if micro_test_decision == "N" or micro_test_decision == "n":
                                break
                            else:
                                print(" EVA: Nie rozumiem, przerywam test")
                                if engine == pyttsx3.init():
                                    engine.say(" Nie rozumiem, przerywam test")
                                    engine.runAndWait()
                                break
                except KeyboardInterrupt:
                    print(" EVA: Przestaje słuchać. Użyto Ctrl + C")
                    time.sleep(1)
                    if engine == pyttsx3.init():
                        engine.say("Przestaje słuchać")
                        engine.runAndWait()
        # Wezwanie EVY
            elif command == "Słuchaj" or command == "słuchaj" or command == "listen" or command == "Listen": # WYKONYWANIE POLECENIA GŁOSOWEGO
                try:
                    r = sr.Recognizer()
                    is_listening = True
                    def get_text():
                        with sr.Microphone() as source:
                            # noinspection PyBroadException
                            try:
                                print(" EVA: Naciśnij Ctrl + C aby przestać słuchać.")
                                print(" EVA: Słucham...")
                                if engine == pyttsx3.init():
                                    engine.say("Słucham")
                                    engine.runAndWait()
                                audio = r.listen(source)
                                listening = r.recognize_google(audio, language='pl-PL')
                                if listening != "":
                                    return listening
                                return 0
                            except Exception:
                                return 0

                    def sound_command(condition):
                        if condition == False:
                            if engine == pyttsx3.init():
                                print(" EVA: Przepraszam, nie rozumiem")
                                print(" EVA: proszę powtórzyć")
                                engine.say("Przepraszam nie rozumiem, proszę powtórzyć")
                                engine.runAndWait()
                            else:
                                print(" EVA: Przepraszam, nie rozumiem")
                                print(" EVA: proszę powtórzyć")
                            r = sr.Recognizer()
                            is_listening = True
                            def get_text():
                                with sr.Microphone() as source:
                                    # noinspection PyBroadException
                                    try:
                                        print(" EVA: Naciśnij Ctrl + C aby przestać słuchać.")
                                        print(" EVA: Słucham...")
                                        if engine == pyttsx3.init():
                                            engine.say("Słucham")
                                            engine.runAndWait()
                                        audio = r.listen(source)
                                        listening = r.recognize_google(audio, language='pl-PL')
                                        if listening != "":
                                            return listening
                                        return 0
                                    except Exception:
                                        return 0

                            loop_checker = 2
                            while loop_checker > 1:
                                txt = get_text()

                                match txt:

                                    case txt if txt:
                                        pyautogui.typewrite(txt)
                                        pyautogui.press('enter')
                                        loop_checker = 0
                                    case _:
                                        # print(" EVA: Przepraszam, nie rozumiem")
                                        # print(" EVA: proszę powtórzyć")
                                        # time.sleep(1)
                                        if engine == pyttsx3.init():
                                            print(" EVA: Przepraszam, nie rozumiem")
                                            print(" EVA: proszę powtórzyć")
                                            engine.say("Przepraszam nie rozumiem, proszę powtórzyć")
                                            engine.runAndWait()
                                        else:
                                            print(" EVA: Przepraszam, nie rozumiem")
                                            print(" EVA: proszę powtórzyć")
                                        loop_checker = 2
                                        break
                        else:
                            pass
                    def run_voice_recognizer():
                        loop_checker = 2
                        while loop_checker > 1:
                            txt = get_text()

                            match txt:

                                case txt if txt:
                                    pyautogui.typewrite(txt)
                                    pyautogui.press('enter')
                                    loop_checker = 0
                                case _:
                                    time.sleep(2)
                                    print(" EVA: Przepraszam, nie rozumiem")
                                    print(" EVA: proszę powtórzyć")
                                    if engine == pyttsx3.init():
                                        engine.say("Przepraszam nie rozumiem")
                                        engine.say("proszę powtórzyć")
                                        engine.runAndWait()
                                    loop_checker = 2
                    run_voice_recognizer()
                except KeyboardInterrupt:
                    print(" EVA: Przestaje słuchać. Użyto Ctrl + C")
                    time.sleep(1)
                    if engine == pyttsx3.init():
                        engine.say("Przestaje słuchać")
                        engine.runAndWait()
            elif command == "hej" or command == "cześć" or command == "elo" or command == "witaj" or command == "Witaj":
                print(" EVA: Witaj :)")
                if engine == pyttsx3.init():
                    engine.say("Witaj")
                    engine.runAndWait()
                continue
            elif command == "Note" or command == "note" or command == "Notatnik" or command == "notatnik": # URUCHAMIANIE EDYTOR TEKSTU
                print(" EVA: Uruchamiam edytor tekstu")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam edytor tekstu")
                    engine.runAndWait()
                print(" SYSTEM: ")
                def notepad():
                    if platform.system() == "Windows":
                        system("notepad.exe")
                    if platform.system() == "Linux":
                        system("mousepad||gedit")
                    # MAC OS
                    # if platform.system() == "Darwin":
                    #     system()
                notepad_handler = threading.Thread(target=notepad, args=())
                notepad_handler.start()
                continue
            elif command == "calc" or command == "Calc" or command == "Kalkulator" or command == "kalkulator": # URUCHAMIA KALKULATOR
                print(" EVA: Uruchamiam kalkulator")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam kalkulator")
                    engine.runAndWait()
                print(" SYSTEM: ")
                def calc():
                    if platform.system() == "Windows":
                        system("calc.exe")
                calc_handler  = threading.Thread(target=calc, args=())
                calc_handler.start()
            elif command == "co tam u ciebie":
                print(" EVA: Wszystko dobrze, dziękuję :)")
                if engine == pyttsx3.init():
                    engine.say("Wszystko dobrze, dziękuję")
                    engine.runAndWait()
                continue
            elif command == "whoami":  # WYŚWIETLA AKTUALNEGO UŻYTKOWNIKA EVA
                # print("")
                print(" EVA: Zalogowany jako: '", user, "'")
                continue
            elif command == "cls" or command == "clear":  # CLS
                cls()
                continue
            elif command == "chrome": # URUCHAMIA GOOGLE CHROME
                print(" EVA: Uruchamiam program 'Google Chrome'")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam program google chrome")
                    engine.runAndWait()
                print(" SYSTEM: ")
                def run_chrome():
                    if platform.system() == "Windows":
                        system('start chrome')
                    if platform.system() == "Linux":
                        system('chromium-browser > /dev/null 2>&1')
                run_chrome()
            elif command == "chrome -i": # URUCHAMIA GOOGLE CHROME W TRYBIE INCOGNITO
                print(" EVA: Uruchamiam program 'Google Chrome' w trybie incognito")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam program google chrome w trybie incognito")
                    engine.runAndWait()
                print(" SYSTEM: ")
                def run_chrome_incognito():
                    if platform.system() == "Windows":
                        system('start chrome --incognito')
                    if platform.system() == "Linux":
                        system('chromium-browser --incognito > /dev/null 2>&1')
                run_chrome_incognito()
            elif command == "firefox":
                print(" EVA: Uruchamiam program 'Firefox'") # URUCHAMIA FIREFOX
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam program firefox")
                    engine.runAndWait()
                def run_firefox():
                    if platform.system() == "Windows":
                        system('start firefox')
                    if platform.system() == "Linux":
                        system('firefox > /dev/null 2>&1')
                firefox_handler = threading.Thread(target=run_firefox)
                firefox_handler.start()
            elif command == "firefox -i": # URUCHAMIA FIREFOX W TRYBIE INCOGNITO
                def run_firefox_incognito():
                    print(" EVA: Uruchamiam program 'Firefox' w trybie incognito")
                    if engine == pyttsx3.init():
                        engine.say("Uruchamiam program firefox w trybie incognito")
                        engine.runAndWait()
                    if platform.system() == "Windows":
                        system('start firefox -private-window')
                    if platform.system() == "Linux":
                        system('firefox -private-window > /dev/null 2>&1')
                firefox_incognito_handler = threading.Thread(target=run_firefox_incognito)
                firefox_incognito_handler.start()
            elif command == "map": # URUCHAMIA MAPY GOOGLE W TRYBIE INCOGNITO
                def run_google_map():
                    print("EVA: Uruchamiam Mapy Google w trybie incognito")
                    if engine == pyttsx3.init():
                        engine.say("Uruchamiam mapy gogle w trybie incongito")
                        engine.runAndWait()
                    if platform.system() == "Windows":
                        _runBrowserCommand = 'start firefox.exe -private-window www.google.com/maps > nul 2>&1'
                        process = subprocess.Popen(_runBrowserCommand, shell=True, stdout=subprocess.PIPE)
                        process.wait()
                        _returnCode = process.returncode
                        if (_returnCode == 0):
                            pass
                        if (_returnCode == 1):
                            _runBrowserCommand = 'start chrome.exe www.google.com\maps --incognito'
                            process = subprocess.Popen(_runBrowserCommand, shell=True, stdout=subprocess.PIPE)
                            process.wait()
                            _returnCode = process.returncode
                            if (_returnCode == 1):
                                pass
                    if platform.system() == "Linux":
                        system('chromium-browser www.google.com/maps --incognito > /dev/null 2>&1||firefox -private-window www.google.com/maps > /dev/null 2>&1')
                gmap_handler = threading.Thread(target=run_google_map)
                gmap_handler.start()
            elif command == "cmd": # URUCHAMIA INTERPRETERA POLECEŃ SYSTEMU WINDOWS
                print(" EVA: Uruchamiam interpreter poleceń systemu WINDOWS")
                def cmd():
                    system('start cmd')
                print(" SYSTEM: ")
                cmd()
            elif command == "ircs": # URUCHAMIA PROGRAM EVA SAFE IRC SERVER
                print(" EVA: Uruchamiam program 'EVA SAFE IRC SERVER'")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam program ewa, sejwf, i, er, ce, serwer")
                    engine.runAndWait()
                if platform.system() == "Windows":
                    process = subprocess.Popen(
                            'start "EVA SAFE IRC SERVER" cmd /c python3 server_irc.py',
                            stdout=subprocess.PIPE,
                            stderr=None,
                            shell=True
                )
                if platform.system() == "Linux":
                    process = subprocess.Popen(
                            "xfce4-terminal --execute python3 server_irc.py", "exo-open --launch TerminalEmulator python3 server_irc.py", #dodać reszte terminali
                            stdout=subprocess.PIPE,
                            stderr=None,
                            shell=True
                )
            elif command == "ircc": # URUCHAMIA PROGRAM EVA SAFE IRC CLIENT
                print(" EVA: Uruchamiam program 'EVA SAFE IRC CLIENT'")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam program ewa, sejwf, i, er, ce, kli ent")
                    engine.runAndWait()
                if platform.system() == "Windows":
                    process = subprocess.Popen(
                            'start "EVA IRC SAFE CLIENT" cmd /c python3 client_irc.py',
                            stdout=subprocess.PIPE,
                            stderr=None,
                            shell=True
                )
                if platform.system() == "Linux":
                    process = subprocess.Popen(
                            "xfce4-terminal --execute python3 client_irc.py", "exo-open --launch TerminalEmulator python3 client_irc.py",
                            stdout=subprocess.PIPE,
                            stderr=None,
                            shell=True
                )
            elif command == "logout":  # WYLOGOWUJE AKTUALNEGO UŻYTKOWNIKA EVA
                print(" EVA: Wylogowuje...")
                if engine == pyttsx3.init():
                    engine.say("Wylogowuje")
                    engine.runAndWait()
                cls()
                print(" EVA: Wylogowano!")
                system_login_screen.system_load()
            elif command == "Nox" or command == "nox" or command == "exit":  # NOX I EXIT
                exit(cls())
            elif command == "term": # URUCHAMIA TERMINALA SYSTEMU LINUX
                print(" EVA: Uruchamiam terminal systemu LINUX")
                def term():
                    system('xfce4-terminal > /dev/null 2>&1 || exo-open --launch TerminalEmulator > /dev/null 2>&1')
                print(" SYSTEM: ")
                term()
            elif command == "lname": # WYŚWIETLA NAZWĘ HOSTA
                import socket
                hostname=socket.gethostname()
                print(" EVA: Nazwa tego komputera to: " + hostname)
                if engine == pyttsx3.init():
                    engine.say("nazwa tego komputera to")
                    engine.runAndWait()
            elif command == "synth": # AKTYWUJE SYNTEZATOR MOWY EVA
                # Text-to-Speech
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('rate', 170)
                engine.setProperty('volume', 0.5)
                engine.setProperty('voice', 'polish')
                #
                print(" EVA: Od teraz będę używać głosu")
                print(" EVA: jeśli mnie nie słyszysz to nie moja wina")
                print(" EVA: UWAGA! Uruchomiony syntezator mowy spowalnia moje działanie")
                engine.say("Od teraz będę używać głosu,  jeśli mnie nie słyszysz to nie moja wina")
                engine.runAndWait()
            elif command == "desynth": # DEZAKTYWUJE SYNTEZATOR MOWY EVA
                engine = 0 # Text-to-Speech
                print(" EVA: Przestaje mówić. Wpisz polecenie 'synth' aby aktywować mój syntezator mowy")
            elif command == "lip": # WYŚWIETLA LOKALNY ADRES IP
                import socket
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(("8.8.8.8", 80))
                    print(" EVA: Lokalny adres IP to: " + s.getsockname()[0])
                    if engine == pyttsx3.init():
                        engine.say("Lokalny adres aj pi to")
                        engine.runAndWait()
                except OSError:
                    print(" EVA: Nie mogę uzyskać adresu IP")
                    print(" EVA: Sprawdź ustawienia sieci")
                    if engine == pyttsx3.init():
                        engine.say("Nie mogę uzyskać adresu IP")
                        engine.say("Sprawdź ustawienia sieci")
                        engine.runAndWait()
            elif command == "monit": # URUCHAMIA MONITOR POŁĄCZEŃ EVA
                print(" EVA: Uruchamiam monitor połączeń EVA")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam monitor połączeń ewa")
                    engine.runAndWait()
                system('start "MONITOR POŁĄCZEŃ EVA" netstat -a -f 2')
            elif command == "sinfo": # WYŚWIETLA INFORMACJE O SYSTEMIE
                print(" EVA: Zbieram informacje o systemie")
                print(" EVA: Proszę czekać...")
                if engine == pyttsx3.init():
                    engine.say("Zbieram informacje o systemie, proszę czekać")
                    engine.runAndWait()
                time.sleep(1)
                print(" SYSTEM:")
                time.sleep(1)
                system("systeminfo")
            elif command == "pip": # WYŚWIETLA PUBLICZNY ADRES IP
                ip = get('https://api.ipify.org').content.decode('utf8')
                print(" EVA: Publiczny adres IP to: {}".format(ip))
                if engine == pyttsx3.init():
                    engine.say("Publiczny adres aj pi to")
                    engine.runAndWait()
            elif command == "taskm": # URUCHAMIA MENEDŻER ZADAŃ
                print(" EVA: Uruchamiam menedżer zadań")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam menedżer zadań")
                    engine.runAndWait()
                system("start taskmgr")
            elif command == "soundtest": # ODTWARZA PLIK DŹWIĘKOWY sound_test.wav
                print(" EVA: Uruchamiam plik muzyczny sound_test.wav")
                if engine == pyttsx3.init():
                    engine.say("Uruchamiam plik muzyczny sound test wav")
                    engine.runAndWait()
                sound_handler = threading.Thread(target=playsound, args=('eva_sounds/sound_test.wav',))
                sound_handler.start()
            # elif command == "hex":
            #     print("EVA: Uruchamiam program HexChat")
            #     if engine == pyttsx3.init():
            #         engine.say("Uruchamiam program Heks Czat")
            #     if platform.system() == "Linux":
            #         def start_hexchat():
            #             system("hexchat")
            #         hexchat_handler = threading.Thread(target=start_hexchat)
            #         hexchat_handler.start()
            #     if platform.system() == "Windows":
            #         system("")
            elif command == "help" or command == "pomoc" or command == "Pomoc":  # WYŚWIETLA LISTĘ POLECEŃ
                #sound_command(True)
                print("")
                print(" EVA: Lista poleceń")
                if engine == pyttsx3.init():
                        engine.say("Lista poleceń")
                        engine.runAndWait()
                print(" DOTYCZĄCE EVA:")
                print("     synth - Aktywuje syntezator mowy EVA")
                print("     desynth - Dezaktywuje syntezator mowy EVA")
                print("     soundtest - Uruchamia plik muzyczny w celu sprawdzenia działania głosników.")
                print("     microtest - EVA nasłuchuje i powtarza co usłyszała.")
                print("     słuchaj/listen - EVA zaczyna słuchać i wykonuje wypowiedziane polecenie")
                print("     ver - Wyświetla informacje o wersji EVA")
                print("     cls/clear - Czyści terminal EVA")
                print("     exit/nox - Natychmiastowo wyłącza EVA bez zostawiania śladów")
                print(" DOTYCZĄCE UŻYTKOWNIKA:")
                print("     whoami - Wyświetla aktualnie zalogowanego użytkownika programu")
                print("     logout - Wylogowuje aktualnie zalogowanego użytkownika programu")
                print(" DOTYCZĄCE SIECI:")
                print("     lip - Wyświetla lokalny adres IP")
                print("     pip - Wyświetla publiczny adres IP")
                print("     monit - uruchamia Monitor Połączeń EVA (Aktualnie działa tylko w systemie Windows)") #TODO - Sprawdzić czy działa na Linuxach
                print("     ircs - Uruchamia program 'EVA SAFE IRC SERVER'")
                print("     ircc - Uruchamia program 'EVA SAFE IRC CLIENT'")
                print(" DOTYCZĄCE SYSTEMU:")
                print("     lname - Wyświetla nazwę lokalnego hosta")
                print("     sinfo - Wyświela informacje o systemie")
                print("     cmd - Uruchamia interpreter poleceń systemu Windows")
                print("     term - Uruchamia terminal systemu Linux")
                print("     taskm - Uruchamia menedżer zadań (Aktualnie działa tylko w systemie Windows)") #TODO - Dodać obsługę windowsa
                print(" INNE PROGRAMY:")
                print("     note/notatnik - Uruchamia edytor tekstu")
                print("     calc - Uruchamia kalkulator")
                # print("     hex - Uruchamia program HexChat") #TODO - Dodać obsługę windowsa
                print("     chrome - Uruchamia program 'Google Chrome'")
                print("              dodaj parametr '-i' aby uruchomić w trybie incognito")
                print("     firefox - Uruchamia program 'Firefox'")
                print("              dodaj parametr '-i' aby uruchomić w trybie incognito")
                print("     map - Uruchamia mapy google w przeglądarce w trybie incognito") #TODO - Dodać obsługę innych przeglądarek
                print("")
                continue
            elif command == "ver":  # WYŚWIETLA WERSJĘ EVA MAIN CORE
                print("")
                print(" EVA: EVA MAIN CORE")
                print(" EVA: Wersja/Version: 1.0/05.10.2022/LINUX/WINDOWS")
                print("")
                continue
            elif command == "": # USUNĄĆ JEŚLI SPRAWIA PROBLEMY
                print ("\033[A                             \033[A") # USUWA LINIJKĘ TEKSTU TERMINALA WYŚWIETLAJĄCĄ CZAS I DATĘ
                print ("\033[A                             \033[A") # USUWA PUSTĄ LINIJKĘ
                print ("\033[A                             \033[A") # USUWA OSTATNIĄ LINIJKĘ TEKSTU TERMINALA TZN: "(user >|)"
            #elif
            else :  # ELSE
                if is_listening == True: # SPRAWDZA CZY POLECENIE GŁOSOWE JEST POPRAWNE
                    sound_command(False)
                else:
                    time.sleep(0.25)
                    print("")
                    print(" EVA: Przepraszam, nie rozumiem")
                    print(" EVA: proszę powtórzyć")
                    print(" EVA: Wpisz 'help' lub 'pomoc' aby wyświetlić liste poleceń")
                    print("")
                    if engine == pyttsx3.init():
                        engine.say("Przepraszam, nie rozumiem, proszę powtórzyć")
                        engine.runAndWait()
    except TypeError:
        # Dotyczy syntezatora
        print(" EVA: Wystąpił problem z rozpoznawaniem dźwięku (TypeError)")
        engine.say("Wystąpił problem z rozpoznawaniem dźwięku")
        engine.runAndWait()
        evaMainCore(user)
    except KeyboardInterrupt:
        print("")
        print(" EVA: Znikam. Użyto Ctrl + C")
        time.sleep(2)
        exit(cls())

if __name__ == "__main__":
    system_login_screen.system_load()
