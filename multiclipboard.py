import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"  # kaydedilen verilerin tutulduğu dosya

def saveData(filepath, data):  # json dosyasına verileri kaydetme
    with open(filepath, "w") as f:  # dosyayı aç ve yaz w=write
        json.dump(data, f)

def loadData(filepath):  # json dosyasından verileri oku
    try:    # alttaki durumu dener olmaz ise expecte geçer
        with open(filepath, "r") as f:  # dosyayı aç ve oku r=read
            data = json.load(f)
            return data
    except: # dosya yoksa boş liste döndür
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadData(SAVED_DATA)  # json dosyasından verileri oku

    if command == "save":
        key = input("Key: ")
        data[key] = clipboard.paste() # clipboard.paste() clipboard'ın içeriğini alır
        saveData(SAVED_DATA, data) # json dosyasına verileri kaydet
        print("Saved")
    elif command == "load":
        key = input("Key: ")
        if key in data: # veri varsa
            clipboard.copy(data[key]) # clipboard'a verileri kopyala
            print("Loaded")        
        else:
            print("Key not found")

    elif command == "list":
        print(data) # verileri listele
    else:
        print("Invalid command")    
else:
    print("Please pass one command")
