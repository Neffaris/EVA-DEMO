import socket
import socket as s
import time
from os import system
import threading

PORT = 5050
BUFFER = 2048

def cls():
    import platform
    if platform.system() == "Windows":
        system('cls')
    if platform.system() == "Linux":
       system('clear')

def client_load():
    try:
        client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

        print("")
        print(" ----------EVA SAFE IRC CLIENT----------")
        print("")
        host = input(" EVA: Podaj adres IP serwera IRC: ")
        print(" EVA: Proszę czekać...")
        client_socket.connect((host, PORT))
        user_name = input(" EVA: Podaj nick: ").encode("utf8")
        client_socket.send(user_name)
        # ODBIERANIE WIADOMOSCI POWITALNIEJ
        print(client_socket.recv(BUFFER).decode("utf8"))
        print(" EVA: Wpisz ' /help ' aby wyświetlić listę poleceń")

        while True:
            # # ODBIERANIE WIADOMOŚCI SERWERA
            # def server_messages_receiver():
            #     print(client_socket.recv(buffer).decode("utf8"))
            # server_messages_receiver_handler = threading.Thread(target=server_messages_receiver)
            # server_messages_receiver_handler.start()
            
            # WYSYLANIE WIADOMOSCI
            print(user_name.decode("utf8"), end="")
            message = input(" > ")
            message_as_bytes = str.encode(message)
            message_as_bytes.decode("utf8")
            client_socket.send(message_as_bytes)
            if message == "/nox" or message == "/exit":
                client_socket.close()
                exit()
            if message == "/cls":
                cls()
                print(" EVA: Wpisz ' /help ' aby wyświetlić listę poleceń")
                continue
            if message == "/logout":
                client_socket.close()
                print(" EVA: Wylogowano z serwera")
                client_load_again()
            if message == "/whoami":
                print(" EVA: Twój nick to:", user_name.decode("utf8"))
                continue
            if message == "/help":
                print("")
                print(" ----------LISTA POLECEŃ----------")
                print(" /help - wyświetla listę poleceń")
                print(" /cls - czyści ekran czatu")
                print(" /whoami - wyświetla twój nick")
                print(" /logout - wylogowuje z serwera IRC")
                print(" /exit lub /nox - wyłącza program EVA IRC CLIENT bez pozostawiania śladów")
                continue
            else:
                continue  
    except KeyboardInterrupt:
            cls()
            print(" EVA: KeyboardInterrupt")
            print(" EVA: Program EVA SAFE IRC SERVER zatrzymany. Użyto Ctrl + C")
            time.sleep(1)
            client_load_again(exit()) # !!!
    except socket.gaierror:
            print(" EVA: Nie można połączyć się z serwerem (socket.gaierror)")
            print(" EVA: Spróbuj ponownie")
            client_load_again()
    except OSError: 
            print(" EVA: Nie można połączyć się z serwerem (OSEError)")
            print(" EVA: Spróbuj ponownie")
            client_load_again()

def client_load_again():
    try:
        client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        host = input(" EVA: Podaj adres IP serwera IRC: ")
        client_socket.connect((host, PORT))
        user_name = input(" EVA: Podaj nick: ").encode("utf8")
        client_socket.send(user_name)

        while True:
            print(user_name.decode("utf8"), end="")
            message = input(" > ")
            message_as_bytes = str.encode(message)
            message_as_bytes.decode("utf8")
            client_socket.send(message_as_bytes)
            if message == "/cls":
                cls()
                print(" EVA: Wpisz ' /help ' aby wyświetlić listę poleceń")
                continue
            if message == "/exit" or message == "/nox":
                cls()
                exit()
            if message == "/logout":
                client_load()
            if message == "/whoami":
                print("")
                print(" EVA: Aktualnie zalogowano jako:", user_name.decode("utf8"))
                print("")
                continue
            if message == "/help":
                print("")
                print(" ----------Lista poleceń programu EVA SAFE IRC CLIENT----------")
                print(" /help - wyświetla listę poleceń")
                print(" /cls - czyści ekran czatu")
                print(" /whoami - wyświetla twój nick")
                print(" /logout - wylogowuje z serwera IRC")
                print(" /exit lub /nox - przerywa połączenie i wyłącza program EVA SAFE IRC CLIENT bez pozostawiania śladów")
                print("")
                continue
            else:
                continue
    except KeyboardInterrupt:
        cls()
        print(" EVA: Program EVA SAFE IRC SERVER zatrzymany. Użyto Ctrl + C")
        time.sleep(1)
        exit()
    except socket.gaierror:
        print(" EVA: Nie można połączyć się z serwerem (socket.gaierror)")
        print(" EVA: Spróbuj ponownie")
        client_load_again()
    except OSError: 
            print(" EVA: Nie można połączyć się z serwerem (OSEError)")
            print(" EVA: Spróbuj ponownie")
            client_load_again()


# ConnectionResetError
client_load()
