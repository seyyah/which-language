"""
mini-notes v0 — Basitlestirilmis implementasyon
Ogrenci: Yağmur Anise KARACA (251478022)
Kapsam: Sadece init ve create komutlari.
Yasaklar: Dongu (for/while) ve Liste ([]) kullanilmadi.
"""
"""

V2 GÖREV LİSTESİ:
1. 'list' komutunu ekle: Tüm notları döngü kullanarak alt alta listele.
2. 'search' komutunu ekle: Kullanıcının girdiği kelimeyi not başlıklarında ara.
3. 'filter' komutunu ekle: Seçilen önceliğe (Düşük/Orta/Yüksek) göre notları süz.

"""

import sys
import os

def list_notes():
    """Tüm notları döngü ile ekrana yazdırır."""
    if not os.path.exists(".mininotes/notes.dat"):
        return "Kayıtlı not bulunamadı."
    
    f = open(".mininotes/notes.dat", "r")
    for line in f:
        # Format: id|baslik|icerik|oncelik|tarih
        parcalar = line.strip().split("|")
        print(f"[{parcalar[0]}] {parcalar[1]} - Öncelik: {parcalar[3]}")
    f.close()
    return ""

def search_notes(kelime):
    """Notlar içinde arama yapar."""
    f = open(".mininotes/notes.dat", "r")
    bulundu = False
    for line in f:
        if kelime.lower() in line.lower():
            parcalar = line.strip().split("|")
            print(f"Eşleşme Bulundu: [{parcalar[0]}] {parcalar[1]}")
            bulundu = True
    f.close()
    if not bulundu:
        print(f"'{kelime}' içeren bir not bulunamadı.")

def filter_notes(seviye):
    """Önceliğe göre filtreleme yapar."""
    f = open(".mininotes/notes.dat", "r")
    bulundu = False
    for line in f:
        parcalar = line.strip().split("|")
        if parcalar[3].lower() == seviye.lower():
            print(f"[{parcalar[0]}] {parcalar[1]}")
            bulundu = True
    f.close()
    if not bulundu:
        print(f"{seviye} önceliğinde not bulunamadı.")
        
def initialize():
    """Not defteri klasörünü ve dosyasını oluşturur."""
    if os.path.exists(".mininotes"):
        return "Hata: Uygulama zaten başlatılmış."
    
    os.mkdir(".mininotes")
    f = open(".mininotes/notes.dat", "w")
    f.close()
    return "Not defteri başarıyla oluşturuldu."

def create_note(title, content, priority="Orta"):
    # GÖREV 3: Boş giriş kontrolü
    if title == "" or content == "":
        return "Hata: Not başlığı veya içeriği boş bırakılamaz!"

    if not os.path.exists(".mininotes"):
        return "Hata: Önce uygulamayı başlatmalısınız (init komutu)."
    
    f = open(".mininotes/notes.dat", "r")
    data = f.read()
    f.close()
    
    note_id = data.count("\n") + 1
    
    # GÖREV 2: Öncelik bilgisi dosyaya kaydediliyor
    f = open(".mininotes/notes.dat", "a")
    f.write(str(note_id) + "|" + title + "|" + content + "|" + priority + "|2026-03-17\n")
    f.close()
    
    return "Not başarıyla kaydedildi. ID: " + str(note_id) + " [Öncelik: " + priority + "]"

def show_not_implemented(command):
    return "'" + command + "' komutu ilerleyen haftalarda eklenecektir."

# --- Ana Program ---
if len(sys.argv) < 2:
    print("Kullanım: python mininote.py <komut> [argümanlar]")
else:
    cmd = sys.argv[1]
    
    if cmd == "init":
        print(initialize())
    elif cmd == "create":
        # Create komutu için 4 veya 5 argüman (opsiyonel öncelik dahil)
        if len(sys.argv) < 4:
            print("Kullanım: python mininote.py create \"Başlık\" \"İçerik\" [Öncelik]")
        else:
            prio = "Orta"
            if len(sys.argv) == 5:
                prio = sys.argv[4]
            print(create_note(sys.argv[2], sys.argv[3], prio))
    else:
        # Diğer komutlar (list, search, delete) henüz aktif değil
        if cmd in ["list", "search", "delete"]:
            print(show_not_implemented(cmd))
        else:
            print("Bilinmeyen komut: " + cmd)
