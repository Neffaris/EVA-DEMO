def system_load():
    import time
    import main_core
    import os
    import threading
    import platform
    from os import system
    
    def cls():
        system('cls||clear')

    #  SYSTEM LOGOWANIA
    print("")
    print("")
    print(" ----------EVA MAIN CORE TERMINAL----------")
    print("")
    if platform.system() == "Windows":
        os.system("title EVA MAIN CORE TERMINAL")
    if platform.system() == "Linux":
        os.system('echo "\033]0;EVA MAIN CORE TERMINAL\a"')

    login_success = 1
    while login_success == 1:
        import stdiomask

        login = stdiomask.getpass(prompt=' EVA: Podaj login i zatwierdź ENTER: ')
        password = stdiomask.getpass(prompt=' EVA: Podaj hasło dostępu i kliknij ENTER: ')
        time.sleep(0.5)
        if login == "lumos" and password == "maxima":
            user = "Admin"
            print(" EVA: Prosze czekać...")
            cls()
            print("")
            print(" EVA: Witaj", user, ":)")
            time.sleep(0.1)
            print(" EVA: Co mogę dla ciebie zrobić? :)")
            print(" EVA: Wpisz 'help' lub 'pomoc' aby wyświetlić liste poleceń")
            print("")
            main_core.eva_main_core(user)

        if login == "nox" or login == "exit":
            cls()
            time.sleep(0.5)
            exit()
        else:
            cls()
            print("")
            print("----------EVA MAIN CORE----------")
            print("")
            print(" EVA: ! Błędny login lub hasło !")
            print(" EVA: Spróbuj ponownie")
            time.sleep(0.5)
            continue
            # engine.say("Błędny login lub hasło, Spróbuj ponownie")
            # engine.runAndWait()
