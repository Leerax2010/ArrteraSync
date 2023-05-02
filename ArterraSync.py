import shutil
import SaveDirectories as sdi
import os
import Settings
import time
import keyboard
import threading

def backup():
    print("Backup processing...")
    process = 0
    cof = 100 / (len(sdi.directories))
    for i in sdi.directories:
        if os.path.exists(i[1]):
            shutil.rmtree(i[1])
        shutil.copytree(i[0], i[1])
        process += cof
        if(Settings.show_info == True):
            print(str(int(process)) + '% ' + f"copy {i[0]} to {i[1]} is done.")
        else:
            print(str(int(process)) + '%')
        if run_backup.is_set():
            print('Backup interrupted by user')
            break
    print("Backup is done!")

def handle_input():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
            run_backup.set()
            break
        time.sleep(0.1)

# Создаем объекты Event для управления потоками
run_backup = threading.Event()

# Запускаем потоки
backup_thread = threading.Thread(target=backup)
input_thread = threading.Thread(target=handle_input)
backup_thread.start()
input_thread.start()

# Ожидаем завершения работы потоков
backup_thread.join()
input_thread.join()
