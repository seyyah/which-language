import sys
import os

# ==============================================================================
# V1 GÖREV LİSTESİ (V1 TASK LIST)
# 1. Hata mesajlarının tamamı kullanıcı dostu ve Türkçe hale getirilecek.
# 2. 'add' komutunda argüman eksikliği kontrolü sıkılaştırılacak ve Türkçe kılavuz basılacak.
# 3. 'init' komutunda halihazırda dizin varsa dönen hata mesajı netleştirilecek.
# ==============================================================================

def initialize():
    if os.path.exists(".minitodo"):
        return "Hata: Sistem zaten baslatilmis!"
    
    os.mkdir(".minitodo")
    f = open(".minitodo/tasks.dat", "w")
    f.close()
    return "Bos minitodo sistemi '.minitodo/' altinda basariyla olusturuldu."

def add_task(description):
    if not os.path.exists(".minitodo"):
        return "Hata: Sistem henuz baslatilmamis. Once 'init' calistirin."
    
    f = open(".minitodo/tasks.dat", "r")
    content = f.read()
    f.close()
    
    task_id = content.count("\n") + 1
    
    f = open(".minitodo/tasks.dat", "a")
    f.write(str(task_id) + "|" + description + "|PENDING|2026-05-22\n")
    f.close()
    
    return "Gorev #" + str(task_id) + " eklendi: " + description

def show_not_implemented(command_name):
    return "Komut '" + command_name + "' gelecek haftalarda yuklenecektir."

# --- Ana Program ---
if len(sys.argv) < 2:
    print("Kullanim: python solution_v1.py <komut> [argumanlar]")
else:
    command = sys.argv[1]

    if command == "init":
        print(initialize())
        
    elif command == "add":
        if len(sys.argv) < 3:
            print("Kullanim Hasi: Lutfen gorev aciklamasi yazin. Ornek: add 'Sut al'")
        else:
            print(add_task(sys.argv[2]))
            
    elif command == "list" or command == "done" or command == "delete":
        print(show_not_implemented(command))
        
    else:
        print("Hata: Bilinmeyen komut -> " + command)