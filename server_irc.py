#!/usr/bin/env python3
from ipaddress import ip_address
import time
import socket as s
from os import system
import threading
# import queue
import platform
import pyautogui

PORT = 5050
BUFFER = 2048

server_socket_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)
server_is_on = 1

clients = set()
clients_lock = threading.Lock()
# import socket
#     def get_ip():
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.settimeout(0)
#         try:
#             # nie musi byc osiągalny
#             s.connect(('10.254.254.254', 1))
#             IP = s.getsockname()[0]
#         except Exception:
#             IP = '127.0.0.1'
#         finally:
#             s.close()
#         return IP
#     print(get_ip())

# def cls():
#     if platform.system() == "Windows":
#         system('cls')
#     if platform.system() == "Linux":
#        system('clear')
def server_main_loop(host, server_main_thread_status, server_is_on):
    try:
        # # URUCHAMIA WĄTEK SERVER_TERMINAL
        # stop_threads = False
        # server_terminal_handler = threading.Thread(target=server_terminal, args = (lambda : stop_threads, ))
        # server_terminal_handler.start()
        if server_main_thread_status == 1:
            connected = True
            while connected:
                # q.join()
                # print("")
                # print("Funkcja server_load uruchomiona w czasie: " + str(int(time.time())) + " sekundy.")
                client_socket, address = server_socket_tcp.accept()
                with clients_lock:
                    clients.add(client_socket)
                server_main_loop_handler = threading.Thread(target=server_main_loop, args=(host, server_main_thread_status, server_is_on))
                server_main_loop_handler.start()
                
                print("")
                print(f" EVA: Uzyskano połączenie od {address} | inaczej {address[0]}:{address[1]}")
                print(" TERMINAL >| ", sep='            ', end='', flush=True)
                ##############################################
                
                # ODBIERANIE NAZWY UŻYTKOWNIKA
                user_name = client_socket.recv(BUFFER).decode("utf8")
                if user_name == "":
                    print("")
                    print(f" EVA: Połączenie z {address} zostało przerwane")
                    print("          przez klienta podczas próby przydzielenia nicku")
                    print(" EVA: Serwer wciąż działa pod adresem:", host)
                else:
                    print("")
                    print(f" EVA: Przydzielono nick ' {user_name} ' do adresu: {address[0]}:{address[1]}")
                    print(f" EVA: Użytkownik ' {user_name} ' połączony z czatem")
                    print(" TERMINAL >|", end="")
                    
                    # WYSYŁANIE WIADOMOŚĆI POWITALNEJ
                    msg = f" SERWER: Witaj na serwerze, {user_name}!".encode("utf8")
                    client_socket.send(msg)

                    # ODBIERANIE PIERWSZEJ WIADOMOŚCI OD KLIENTA
                    message = client_socket.recv(BUFFER).decode("utf8")
                    if message == "":
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' zamyka aplikacje")
                        print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                        print(" EVA: Serwer wciąż działa pod adresem: ", host)
                        continue
                    if message == "/exit" or message == "/nox":
                        print("")
                        print(f"E VA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                        print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                        print(" EVA: Serwer wciąż działa pod adresem:", host)
                        continue
                    if message == "/cls":
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                    if message == "/logout":
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                        print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                        print(" EVA: Serwer wciąż działa pod adresem: ", host)
                        continue
                    if message == "/help":
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                        next_messages_receiver(client_socket, user_name, host, server_main_thread_status)
                    if message == "/whoami":
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                        next_messages_receiver(client_socket, user_name, host, server_main_thread_status)
                    else:
                        print("")
                        print(f" EVA: Użytkownik ' {user_name} ' wysyła wiadomość: ' ", end="")
                        print(message, "'")
                next_messages_receiver(client_socket, user_name, host, server_main_thread_status)
        else:
            exit()
    except TimeoutError:
        print("")
        print(f" EVA: Serwer nie odpowiada (TimeoutError")
        print(" EVA: Spróbuj ponownie")
        server_socket_tcp.close()
        server_main_loop(host, server_main_thread_status, server_is_on)
    # except OSError:
    #     print("")
    #     print(f"EVA: Podano nieprawidłowy adres (OSError")
    #     print("EVA: Spróbuj podać inny adres")
    #     server_socket_tcp.close()
    #     server_load(host, server_main_thread_status, server_off)
    except KeyboardInterrupt:
        print(" EVA: KeyboardInterrupt")
        print(" EVA: Program EVA SAFE IRC SERVER zatrzymany. Użyto Ctrl + C")
        time.sleep(1)
        exit()
    # finally:
    #         with clients_lock:
    #             clients.remove(client_socket)
                
    #         server_socket_tcp.close()
    # except Exception:
    #     print(Exception)

def next_messages_receiver(client_socket, user_name, host, server_main_thread_status):
    try:
        while True:
            message = client_socket.recv(BUFFER).decode("utf8")
            if message == "":
                print("")
                print(f" EVA: Użytkownik ' {user_name} 'zamyka aplikacje")
                print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                print(" EVA: Serwer wciąż działa pod adresem: ", host)
                server_main_loop(host, server_main_thread_status=1, server_is_on=1)
            if message == "/exit" or message == "/nox":
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                print(" EVA: Serwer wciąż działa pod adresem: ", host)
                server_main_loop(host, server_main_thread_status=1, server_is_on=1)
            if message == "/cls":
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                continue
            if message == "/logout":
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
                print(" EVA: Serwer wciąż działa pod adresem: ", host)
                server_main_loop(host, server_main_thread_status=1, server_is_on=1)
                continue
            if message == "/help":
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                continue
            if message == "/whoami":
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wykonuje polecenie {message}")
                continue
            else:
                print("")
                print(f" EVA: Użytkownik ' {user_name} ' wysyła wiadomość: ' ", end="")
                print(message, "'")
                continue
    except ConnectionResetError:
        print("")
        print(f" EVA: Użytkownik ' {user_name} 'zamyka aplikacje")
        print(f" EVA: Użytkownik ' {user_name} ' rozłączony z serwera")
        print(" EVA: Serwer wciąż działa pod adresem: ", host)
        server_main_loop(host, server_main_thread_status=1, server_is_on=1)
    except TimeoutError:
        print("")
        print(f" EVA: Serwer nie odpowiada (TimeoutError")
        print(" EVA: Spróbuj ponownie")
        server_socket_tcp.close()
        server_main_loop(host, server_main_thread_status, server_is_on)
    # except OSError:
    #     print("")
    #     print(f"EVA: Podano nieprawidłowy adres (OSError")
    #     print("EVA: Spróbuj podać inny adres")
    #     server_socket_tcp.close()
    #     server_load(host, server_main_thread_status, server_off)
    except KeyboardInterrupt:
        print(" EVA: KeyboardInterrupt")
        print(" EVA: Program EVA SAFE IRC SERVER zatrzymany. Użyto Ctrl + C")
        time.sleep(1)
        exit()
    
    # except Exception:
    #     print(Exception)

def get_infos(server_main_thread_status):
    try:
        print("")
        print(" ----------EVA SAFE IRC SERVER----------")
        print("")
        hostname = s.gethostname()
        server_socket_udp = s.socket(s.AF_INET, s.SOCK_DGRAM) # Łączy się przez UDP w celu uzyskania adresu IP
        server_socket_udp.connect(("8.8.8.8", 80))
        print(" EVA: Nazwa tego komputera to: "+ hostname)   
        print(" EVA: Lokalny adres IP to: " + server_socket_udp.getsockname()[0])
        server_socket_udp.close() # Zamyka gniazdo UDP
        
        def get_host():
            try:
                host = input(" EVA: Podaj adres IP pod którym ma działać serwer: ")
                print(" EVA: Proszę czekać...")
                server_socket_tcp.bind((host, PORT))
                server_socket_tcp.listen()
                print(" EVA: Uruchomiono serwer IRC pod adresem: ", host)
                # server_main_loop_handler = threading.Thread(target=server_main_loop, args=(host, server_main_thread_status, server_is_on))
                # server_main_loop_handler.start()
                server_main_loop(host, server_main_thread_status, server_is_on)
            except OSError:
                # Dotyczy błędu spowodowanego nagłym wyłączeniem klienta
                print(f" EVA: Adres jest nieprawidłowy w tym kontekście (OSError)")
                print(" EVA: Użytkownik zamyka aplikacje")
                print(" EVA: Serwer wciąż działa pod adresem: ", host)
                # server_main_loop_handler = threading.Thread(target=server_main_loop, args=(host, server_main_thread_status, server_is_on))
                # server_main_loop_handler.start()
                server_main_loop(host, server_main_thread_status, server_is_on)
        get_host()
    # except EOFError:
    #     print("")
    except TimeoutError:
        print(f" EVA: Serwer nie odpowiada (TimeoutError)")
        print(" EVA: Spróbuj ponownie")
        get_host()
    except s.gaierror:
        print(" EVA: Podano nieprawidłowy adres (socket.gaierror)")
        print(" EVA: Spróbuj ponownie")
        get_host()
    # except OSError:
    #     print(f"EVA: Adres gniazda jest już w użyciu (OSError)")
    #     print("EVA: Spróbuj podać inny adres")
    #     get_host()
    except KeyboardInterrupt:
        print(" EVA: KeyboardInterrupt")
        print(" EVA: Program EVA SAFE IRC SERVER zatrzymany. Użyto Ctrl + C")
        time.sleep(1)
        exit()
        
    # except ConnectionRefusedError:
    # except ConnectionResetError:

# def server_terminal(stop):
#     try:
#         while True:
#             # # OBSŁUGA WĄTKU
           
#             if stop():
#                 break
#             # if stop():
#             #         break
#             # WYSYŁANIE WIADOMOŚCI
#             message_from_server = input(" TERMINAL >| ")
#             if message_from_server == "test":
#                 print("test success 1")
#                 continue
#             #if message == "" - TODO SERWER SIE ZAWIESZA
#             else:
#                 continue
#             # message_as_bytes = str.encode(message_from_server) # SZYFROWANIE stringa
#             # message_as_bytes.decode("utf8") # ROZSZYFROWYWANIE
#             # server_socket_tcp.accept()
#             # server_socket_tcp.send(message_as_bytes) # WYSŁANIE WIADOMOŚCI

if __name__ == "__main__":
    get_infos(server_main_thread_status=1)