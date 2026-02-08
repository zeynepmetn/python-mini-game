import os
import sys
import time
import random
from enum import Enum  # current_state == state.PLAYING

global step, x_pos, y_pos, current_state, episode


class State(Enum):
    PLAYING = 1
    DIALOGUE = 2


current_state = State.PLAYING

# position
x_pos = 0
y_pos = 0

# map
episode = 0
width = 10
height = 5

# clock
step = 0
hour = random.randint(10, 23)
min = random.randint(10, 55)

game_maps = {  # # | - _ ¯ ♦ ■ §
    0: {  # Episode 0 EV
        "name": "Harita0", "height": 5, "width": 10,
        "map": [["X", " ", " ", " ", "■", " ", " ", " ", " ", " "],
                [" ", " ", " ", "|", " ", "|", " ", " ", " ", " "],
                [" ", " ", " ", "|", "■", "|", " ", " ", "■", " "],
                [" ", " ", " ", " ", "§", "|", " ", "♦", " ", " "],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
    },
    2: {  # Episode 1 Başlangıç: YER ÜSTÜ BARIŞI
        "name": "Harita1", "height": 15, "width": 25,
        "map": [["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", " ", " ", " ", " ", " ", " "],
                [" ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", "♦", " ", "¶", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", "¯", "¯", "-", "-", "¯", "¯", " ", " ", "¯", "¯", " ", " ", "¯", "¯", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "■"],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", "_", "_", "-", "_", "_", " ", " ", "_", "_", "-", "_", "_", " ", " ", "_", " ", " ", " ", "_", " ", " ", " ", " "],
                [" ", " ", "|", " ", " ", "♦", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", " "],
                [" ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", " "],
                [" ", " ", "|", "♦", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", "♦", " ", "|", " ", " ", " ", " "],
                [" ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|", " ", " ", " ", "§"]]
    },
    1: {  # Episode 2 Gelişme: PARÇALANMA
        "name": "Harita2", "height": 10, "width": 15,
        "map": [["X", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                ["-", "-", "-", "-", "-", "-", "-", "-", "■", "-", "-", "-", "-", "-", "-", "-"],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", "§", " ", " ", " ", " ", " ", " "]]
    },
    4: {  # Episode 0 EV
        "name": "labirent", "height": 13, "width": 17,
        "map": [["X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" ","_","_","_","_","_","_"," ","_","_","_","_"," "," "," "," "," "],
                [" "," "," "," "," "," ","|"," ","|"," ","|"," "," ","|","_","_","_"],
                [" ","_","_","_","_"," ","|"," ","|"," ","|"," "," "," "," ","|"," "],
                [" ","|"," "," ","|"," ","|"," ","|"," "," "," "," "," "," ","|"," "],
                [" ","|"," ","_","|"," ","|"," ","|"," ","_","_","_","_"," ","|"," "],
                [" ","|"," "," ","|"," ","|"," "," "," ","|"," "," ","|"," ","|"," "],
                [" ","|"," "," ","|"," ","|","_","|"," ","|"," "," ","|"," "," "," "],
                [" ","|","_"," ","|"," "," "," ","|"," ","|"," "," "," "," ","|"," "],
                [" "," "," "," "," ","|"," "," "," "," ","|"," "," ","|","_","|"," "],
                [" ","_","_","_","_","|","_","_","_","_","|"," "," ","|"," "," "," "],
                [" "," "," "," "," ","|"," "," "," "," ","|","_","_","|","_"," ","_"],
                [" "," "," "," "," ","|"," "," "," "," "," "," "," "," "," "," ",">"]]
    }
}

characters = {
    "Garry": {"display": """
               ______      __  __
             _|      |_   |  ||  |
           _|   ____   |_ |_█||_█|        
          |   _|  _ |    | |  |
          |  |_  |__|    | |  |
          |_   |_       _| |__|
           _|____|_____|__|   |_
          |_____________________|
         """,
              "tür": "Salyangoz",
              "meslek": "Evcil Hayvan",
              "kişilik": "Uslu, Sadık"
    },
    "Patrick": {"display": """ 
                     ___
                    |   |_
                    |     |_
                    |       |
                    |   _|  |_    
                    |   __  __| 
                    |  | █|| █|
                    |  |_█||_█|
                    | |_      |_
                    |   |_______|
                   _|           |
                  |_____________|
        """,
                "tür": "Deniz Yıldızı",
                "meslek": "İşsiz",
                "kişilik": "Anlama Güçlüğü, Sadık, Saf"
    },
    "Patrick_sleep": {"display": """ 
                     ___
                    |   |_
                    |     |_
                    |       |
                    |   _|  |_    
                    |         | 
                    |  |  ||  |
                    |  |__||__|
                    | |_      |_
                    |   |_______|
                   _|           |
                  |_____________|
        """,
                      "tür": "Deniz Yıldızı",
                      "meslek": "İşsiz",
                      "kişilik": "Anlama Güçlüğü, Sadık, Saf"
    },
    "Plankton": {"display": """ 
                             |        /
                             |_____  /
                            _|     |/
                           |   ____ |
                           |  |    ||
                           |  |  █ ||
                           |  |____||
                           | |_     |
                          /|   |____||
                         / |        ||
                           |_      _|
                             |____|
                             |    |
        """,
                 "tür": "Plankton",
                 "meslek": "Burgerci, Bilim İnsanı",
                 "kişilik": "Zeki, Kurnaz, Hırslı"
    },
    "SpongeBob": {"display": """ 
                 __________________
                |    ___    ___    |
                |  _|   |__|   |_  |
                | |   ██ | ██    | |
                | |_  ██_|_██   _| |
                |   |___|  |___|   |
                |  |____________|  |
                |       |_|_|      |
                |__________________|
        """,
                  "tür": "Sünger",
                  "meslek": "Kızartma Aşçısı",
                  "kişilik": ""
    },
    "SpongeBob_1": {"display": """ 
                 __________________
                |    ___    ___    |
                |  _|   |__|   |_  |
                | |   ██ | ██    | |
                | |_  ██_|_██   _| |
                |   |___|  |___|   |
                |   ____________   |
                |       |_|_|      |
                |__________________|
        """,
                    "tür": "Sünger",
                    "meslek": "Kızartma Aşçısı",
                    "kişilik": ""
    },
    "BMO": {"display": """
           ___________________
          |   ______________  |
          |  |             |  |
          |  |   ▅     ▅   |  |
          |  |    -___-    |  |
          |  |_____________|  |  
         _|   --------   --   |_
        | |    ▅        ╯     | |
        | |   ▉▉▉      .. ▅   | |
        | |    ▉        ╭╮    | |
        |_|  -- --      ╰╯    |_|
          |___________________|
               | |     | |
               |_|     |_|
        """,
            "tür": "Robot",
            "meslek": "Bilim İnsanı",
            "kişilik": "Sinsi, Zeki"
    },

    "Brian":
        """
            ╭━┳━╭━╭━╮╮
            ┃   ┣▅╋▅┫┃
            ┃ ┃ ╰━╰━━━━━━╮
            ╰┳╯         ◢▉◣
             ┃          ▉▉▉▉
             ┃          ◥▉◤
             ┃    ╭━┳━━━━╯
             ┣━━━━━━┫
        """,
}


def stats(name=str):
    if name in characters:
        character = characters[name]
        lines = [
            f"Tür: {character['tür']}",
            f"Meslek: {character['meslek']}",
            f"Kişilik: {character['kişilik']}"
        ]
        max_length = max(len(line) for line in lines)

        # Determine the width and height for the square frame
        size = max(max_length, len(name) + 4)  # Ensure name fits too

        # Print top border
        print("+" + "-" * (size + 2) + "+")

        # Print character name
        print("| " + name.center(size) + " |")

        # Print separator
        print("+" + "-" * (size + 2) + "+")

        # Print character details
        for line in lines:
            print("| " + line.ljust(size) + " |")

        # Print bottom border
        print("+" + "-" * (size + 2) + "+")
    else:
        print(f"Character '{name}' not found.")

# Dialoglara animasyon ekler
def speak(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


# Harita dışındaki sınırları belirler
def draw_map():
    global game_maps, episode
    if episode == 0:
        print(".----------.")
        for row in game_maps[episode]["map"]:
            print("|" + "".join(row) + "|")
        print("'----------'")
    elif episode == 1:
        print(".-------------------------.")
        for row in game_maps[episode]["map"]:
            print("|" + "".join(row) + "|")
        print("'-------------------------'")
    elif episode == 2:
        print(".-------------------------.")
        for row in game_maps[episode]["map"]:
            print("|" + "".join(row) + "|")
        print("'-------------------------'")


# Sınırları aşmadan ve doğru değerde giriş alarak mevcut konumu hareket ettirir
def move_player(width, height, game_map, episode, move_input: str, x: int, y: int):
    global step
    width = game_maps[episode]["width"]
    height = game_maps[episode]["height"]

    """Move the player if the inputs and conditions are valid."""
    if move_input == "w" and y > 0 and game_map[episode]["map"][y - 1][x] not in ["-", "|", "_", "¯"]:
        y -= 1
    elif move_input == "s" and y < height - 1 and game_map[episode]["map"][y + 1][x] not in ["-", "|", "_", "¯"]:
        y += 1
    elif move_input == "a" and x > 0 and game_map[episode]["map"][y][x - 1] not in ["-", "|", "_", "¯"]:
        x -= 1
    elif move_input == "d" and x < width - 1 and game_map[episode]["map"][y][x + 1] not in ["-", "|", "_", "¯"]:
        x += 1
    step += 1
    return episode, x, y, step


# Bulunulan bölümü vurugulayar yazdırır
def title():
    global episode
    print(f"***{game_maps[episode]['name']}***")


# Haritadaki belli bölgelere gelince DİYALOG DURUMUNU aktif eder
def check_position():
    global x_pos, y_pos, episode, current_state

    # EV
    if episode == 0:
        if (x_pos, y_pos) == (8, 2) or (4, 0) or (7, 3) or (4, 2) or (4, 3):
            current_state = State.DIALOGUE
        else:
            current_state = State.PLAYING
        return current_state

    # INDIGO TOWN
    if episode == 2:
        if (x_pos, y_pos) == (18, 13) or (4, 11) or (4, 9) or (3, 13) or (13, 2) or (11,2) or (24, 14):
            current_state = State.DIALOGUE
        else:
            current_state = State.PLAYING
        return current_state




    # BİTİNCE SİL GEREK YOK
def debugger():
    global step, x_pos, y_pos, episode, current_state
    print(f"{current_state} episode:{episode} step:{step} x:{x_pos} y:{y_pos}")


# Terminal temizler
def terminal_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


# Saat ilerletir
def clock():
    global step, hour, min

    if step >= 3:
        min += 5
        if min >= 60:
            min -= 60
            hour += 1

        if hour == 24:
            hour = 0

        step = 0  # Move this line inside the if block
    
    if 0 <= hour < 10 and 0 <= min < 10:
        print("-----------")
        print(f"Saat: 0{hour}.0{min}")
    elif 0 <= hour < 10:
        print("-----------")
        print(f"Saat: 0{hour}.{min}")
    elif 0 <= min < 10:
        print("-----------")
        print(f"Saat: {hour}.0{min}")
    else:
        print("-----------")
        print(f"Saat: {hour}.{min}")
    return step


# Saat ataması yapar
def shuffle_clock():
    global hour, min
    hour = random.randint(10, 55)
    min = random.randint(10, 55)
    return hour, min


# Karakterlerin görüntüsünü yazdırma
def show_display(character):
    stats(character)
    print(characters[character]["display"])
    print("----------------------------------------------")

def change_cursour(choice):
    while True:
        if choice == "w":
            return "^"
        elif choice == "s":
            return "v"
        elif choice == "d":
            return ">"
        elif choice == "a":
            return "<"
        else:
            choice = "o"
            return choice

# Oyunu başlatır
def new_game():
    print("-------------------------------------------------------------------------------------------------------")
    print("                                          xxx")
    print("                         1.Başla\n                         2.Çıkış")
    print("-------------------------------------------------------------------------------------------------------")

    option = input(">>>> ")
    if option == "1":
        episode_0()
    elif option == "2":
        sys.exit()
    terminal_cleaner()

def maze():
    global step, x_pos, y_pos, episode, current_state, krabby_patty_recipe
    episode = 4
    x = x_pos
    y = y_pos
    x_pos = 0
    y_pos = 0

    title()
    while True:
        clock()
        debugger()

        print(".-----------------.")
        for row in game_maps[episode]["map"]:
            print("|" + "".join(row) + "|")
        print("'-----------------'")

        if episode == 4:
            title()
            choice = input("").lower().strip()
            terminal_cleaner()

            game_maps[episode]["map"][y_pos][x_pos] = "."
            episode, x_pos, y_pos, step = move_player(width, height, game_maps, episode, move_input=choice, x=x_pos, y=y_pos)
            game_maps[episode]["map"][y_pos][x_pos] = change_cursour(choice)
            current_state = check_position()


        if episode == 4 and (x_pos, y_pos) == (16, 12): # (16, 12)
            krabby_patty_recipe = True
            episode = 2
            x_pos = x
            y_pos = y
            terminal_cleaner()
            speak("Yengeç Burger tarifi şu an senin ellerinde!")
            time.sleep(0.5)
            speak("Şimdi bu tarifi Plankton'a götürelim!")
            time.sleep(2)
            terminal_cleaner()
            time.sleep(0.5)
            print("   ")
            speak("Plankton'a Yardım Ederek Bay Yengeç'in Karşısında Olmayı Seçtin.")
            print("   ")
            time.sleep(1)
            speak("Gelecek yeniden şekillendi, yeni bir yol çizildi.")
            print("   ")
            time.sleep(2)
            speak("Zaman Makinesi kullanıma yeniden açıldı.")
            print("     ")
            time.sleep(2.5)
            terminal_cleaner()
            return




# Ev'deki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_0():
    global step, x_pos, y_pos, episode, current_state
    mom_dialogue_done = False
    calendar_dialogue_done = False
    preview_dialogue_done = False
    preportal_dialogue_done = False

    while True:
        clock()
        debugger()

        # EPISODE 0 EV
        if current_state == State.PLAYING and episode == 0:
            title()
            draw_map()
            choice = input("").lower().strip()
            terminal_cleaner()

            # Haritada geçilen yerlere '.' ekler, haritadaki mevcut pozisyona X çizer ve değişkenleri günceller
            game_maps[episode]["map"][y_pos][x_pos] = "."
            episode, x_pos, y_pos, step = move_player(width, height, game_maps, episode, move_input=choice,
                                                      x=x_pos, y=y_pos)
            game_maps[episode]["map"][y_pos][x_pos] = change_cursour(choice)
            current_state = check_position()

        # Portal (Break)
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (4, 3):
            speak("Seyehat etmek istediğin zamanı seç.")
            speak(">1) ???")
            speak(">2) ???")
            speak(">3) ???")
            choice = input(">")
            if choice == "1":
                terminal_cleaner()
                print("------------------------")
                speak("Traveling to INDIGO TOWN!")
                speak("bip                 bop")
                speak("        bop")
                speak("  bipbopbipbop")
                time.sleep(1.5)
                speak(f"{random.randint(1, 30)} Mayıs 1984")
                time.sleep(0.5)
                speak("...")
                print("------------------------")
                episode = 1
                x_pos = 0
                y_pos = 0
                current_state = State.PLAYING
                episode_2()
                break

        # Anne
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (7, 3) and not mom_dialogue_done:
            speak("Anneciğin kapıyı tıklıyor")
            time.sleep(1.5)
            speak("Kapıyı açacak mısın?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            mom_dialogue_done = True
            choice = input(">")
            if choice == "1":
                time.sleep(0.5)
                speak("Anneciğin sana bir bardak süt getirmiş")
                time.sleep(0.5)
                speak("Saat geç olduğunu ve yatmanı söylüyor")
                time.sleep(0.5)
                speak("+ Bir adet süt aldın")
                time.sleep(1)

            if choice == "2":
                time.sleep(0.5)
                speak("Anneciğin kapının ardından uyku saatinin geldiğini söylüyor!")
                time.sleep(0.5)
                speak("Biraz sinirlenmiş olmalı!")
                time.sleep(1.3)

            current_state = State.PLAYING
            continue

        # Takvim
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (8, 2) and not calendar_dialogue_done:
            speak("Yatağının yanında bir takvim görüyorsun.")
            speak("Bugünün tarihi 16 Şubat 2014 Cuma")
            speak("Güneş neredeyse batmak üzere")
            print("----------------------------")
            calendar_dialogue_done = True

        # ÖNGÖSTERİM (BİLGİLENDİRME YAZISI)
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (4, 0) and not preview_dialogue_done:
            speak("----------------------------")
            speak("Etkileşime geçebileceğin objeler: ■")
            speak("Ana görev işaretcisi: ¶")
            speak("Zaman makinesi: §")
            speak("Etkileşime geçebileceğin canlılar: ♦")
            print("----------------------------")
            preview_dialogue_done = True

        # PORTAL ÖNÜ (BİLGİLENDİRME YAZISI)
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (4, 2) and not preportal_dialogue_done:
            speak("-Zaman Makinesi-")
            speak("Geçmişteki çeşitli medeniyetlere seyehat etmeni sağlar.")
            speak("Yerini seçebilirsin ancak saat dilimini rastgele oluşturacaktır")
            speak("Geri dönmek için tekrar zaman makinesini (§) kullan")
            print("----------------------------")
            preportal_dialogue_done = True

        current_state = State.PLAYING
        continue


# Bölüm 1'deki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_2():
    global step, x_pos, y_pos, episode, current_state
    garry_dialogues = ["Merhaba", "Sen kimsin?", "Bööö!!", "Çıkış"]
    sponge_bob_dialogues = ["Selam!", "Evini içtiğim için özür dilerim.", "Evin çok lezzetliydi yine olsa yine içerim!", "Çıkış"]
    BMO_dialogues = ["Plankton'la nasıl tanıştınız?",
                     "Plankton’un Yengeç Burger tarifini ele geçirme çabaları hakkında ne düşünüyorsun?",
                     "Bu restorandaki rolün tam olarak nedir?", "Çıkış"]
    plankton_dialogues = ["Yengeç Burger tarifini neden bu kadar çok istiyorsun?",
                          "Bir gün Yengeç Restoran’a karşı kazanma şansın olduğunu gerçekten düşünüyor musun?",
                          " ** Planktona Yengeç Burger Tarifini Ele Geçirmek İçin Yardım Etmeyi Teklif Et **",
                          " ** Plankton'un Planlarını Bay Yengeç'e Anlat ve Plankton'Un Oyununu Boz **"]

    garry_dialogue_done = False
    patrick_dialogue_done = False
    jellyfish_dialogue_done = False
    squidward_dialogue_done = False
    krusty_krab_dialogue_done = False
    sponge_bob_dialogue_done = False
    pineapple_home_dialogue_done = False
    plankton_dialogue_done = False
    chem_bucket_dialogue_done = False
    krabby_patty_recipe = False

    i = 0
    position_y = [14, 13, 12, 11, 14, 13, 12, 11, 10, 10, 10, 10, 10, 14, 14, 14]
    position_x = [2, 2, 2, 2, 6, 6, 6, 6, 2, 3, 4, 5, 6, 3, 4, 5]

    title()

    while True:
        clock()
        debugger()
        game_maps[episode]["map"][14][24] = "§"

        if current_state == State.PLAYING and episode == 2:
            title()
            draw_map()
            choice = input("").lower().strip()
            terminal_cleaner()

            # Haritada geçilen yerlere '.' ekler, haritadaki mevcut pozisyona X çizer ve değişkenleri günceller
            game_maps[episode]["map"][y_pos][x_pos] = "."
            episode, x_pos, y_pos, step = move_player(width, height, game_maps, episode, move_input=choice,
                                                      x=x_pos, y=y_pos)
            game_maps[episode]["map"][y_pos][x_pos] = change_cursour(choice)
            current_state = check_position()


        # PLANKTON
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (13, 2) and not plankton_dialogue_done: # 13,2
            show_display("Plankton")
            time.sleep(2.5)
            speak("İlk defa restoranında farklı bir yüz gören PLankton ne diyeceğini merakla bekliyor gibi görünüyor.")
            print("      ")
            time.sleep(1.3)
            while current_state == State.DIALOGUE:
                for i, row in enumerate(plankton_dialogues, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(plankton_dialogues):
                        answer = plankton_dialogues[choice - 1]
                        if answer == "Çıkış":
                            pass
                        else:
                            plankton_dialogues.pop(choice - 1)
                        # Actions
                        if answer == "Yengeç Burger tarifini neden bu kadar çok istiyorsun?":
                            terminal_cleaner()
                            show_display("Plankton")
                            time.sleep(0.5)
                            speak("Cimri ihtiyar yengeç ile bir zamanlar beraber hayaller kurardık.")
                            time.sleep(0.5)
                            speak("O zamanlar bu burgeri icat ettiğimizde çok büyük bir keşif yaptığımızı fark etmiştik.")
                            time.sleep(0.5)
                            speak("Fakat beni yüzüstü bırakıp kendi başına yola devam edeceğini hiç düşünmemiştim.")
                            time.sleep(0.5)
                            speak("Bu yüzden ondan intikam almalı ve Yengeç Burger tarifi ile tüm kasabayı ele geçirmeliyim!")
                            print("        ")
                            time.sleep(1.3)

                        elif answer == "Bir gün Yengeç Restoran’a karşı kazanma şansın olduğunu gerçekten düşünüyor musun?":
                            terminal_cleaner()
                            show_display("Plankton")
                            time.sleep(0.5)
                            speak("O ihtiyar yengece gününü göstereceğim!!")
                            time.sleep(0.5)
                            speak("Bana yaptıklarını ona ödeteceğim!")
                            time.sleep(0.5)
                            speak("Tek ihtiyacım olan herkesin gözdesi Yengeç Burger'in tarifi!")
                            print("           ")
                            time.sleep(1.3)
                        elif answer == " ** Planktona Yengeç Burger Tarifini Ele Geçirmek İçin Yardım Etmeyi Teklif Et **":
                            terminal_cleaner()
                            show_display("Plankton")
                            time.sleep(0.5)
                            speak("G- Gerçekten bana yardım etmek mi istiyorsun??")
                            time.sleep(0.5)
                            speak("Eğer bunu başarırsan, bütün Bikini Kasabası’nın en güçlü restoranı ben olacağım!")
                            time.sleep(0.5)
                            speak("Herkesin peşinde olduğu o eşsiz tat.")
                            time.sleep(0.5)
                            speak("Eğer tarifi ele geçirebilirsem, 'Yem Kovası' nihayet hak ettiği yere gelecek!")
                            time.sleep(0.5)
                            speak("Düşün, herkes benim kapımda kuyruk olacak. Ve Bay Yengeç... o tarihe karışacak!")
                            time.sleep(2)
                            terminal_cleaner()
                            print("   ")
                            speak("Plankton sana Yengeç Restorana girmek ve gizli tarifi ele geçirmek için bir harita verdi.")
                            time.sleep(0.5)
                            speak("Doğru çıkışı bul ve tarifi ele geçir!!")
                            time.sleep(1)
                            plankton_dialogue_done = True
                            maze()
                            break
                        elif answer == " ** Plankton'un Planlarını Bay Yengeç'e Anlat ve Plankton'Un Oyununu Boz **":
                            terminal_cleaner()
                            time.sleep(0.5)
                            print("   ")
                            speak("Plankton'un Planlarını Bay Yengeç'e Anlatarak Bay Yengeç'in Tarafında Olmayı Seçtin.")
                            print("   ")
                            time.sleep(1)
                            speak("Gelecek yeniden şekillendi, yeni bir yol çizildi.")
                            print("   ")
                            time.sleep(2)
                            speak("Zaman Makinesi kullanıma yeniden açıldı.")
                            print("     ")
                            time.sleep(2.5)
                            plankton_dialogue_done = True
                            break
                        elif answer == "Çıkış":
                            plankton_dialogue_done = False
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # PORTAL
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (24, 14) and not plankton_dialogue_done:
            print("  ")
            speak("Zaman Makinesi Kullanım Dışı.")
            speak("Burada Yapman Gereken Her Şeyi Tamamlamamışsın Gibi Görünüyor.")
            time.sleep(1.3)
            current_state = State.PLAYING

        elif current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (24, 14) and plankton_dialogue_done:
            print("  ")
            speak("Seyehat Edeceğin Yeni Zamanı Seç:")
            speak(">1) ???")
            speak(">2) ???")
            choice = input(">")
            if choice == "1" or "2":
                current_state = State.PLAYING
                episode_3()
                break

        # BMO
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (11, 2):
            speak("Karşında Plankton'un tek ve en yakın arkadaşı.")
            time.sleep(0.5)
            show_display("BMO")
            time.sleep(1)
            while current_state == State.DIALOGUE:
                for i, row in enumerate(BMO_dialogues, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(BMO_dialogues):
                        answer = BMO_dialogues[choice - 1]
                    if answer == "Çıkış":
                        pass
                    else:
                        BMO_dialogues.pop(choice - 1)
                    if answer == "Plankton'la nasıl tanıştınız?":
                        terminal_cleaner()
                        speak("Plankton Bay Yengeç ile yollarını ayırdıktan sonra beni yaptı.")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Plankton’un Yengeç Burger tarifini ele geçirme çabaları hakkında ne düşünüyorsun?":
                        terminal_cleaner()
                        speak("Kesinlikle Plankton'un en büyük destekçisi benim! \nBu konuda ona hep yardımcı oluyorum! \nbip bop")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Bu restorandaki rolün tam olarak nedir?":
                        terminal_cleaner()
                        speak("Plankton'un her daim yanında olmak ve onun yeni planları için ona yardımcı olmak. \nBİP! BOP!")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Çıkış":
                        current_state = State.PLAYING
                else:
                        print()
                        speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # ANANAS EV
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (4, 9) and not pineapple_home_dialogue_done:
            speak("Sünger bobun ananas eviyle karşılaştın.")
            speak("Bir yudum içecek misin?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            choice = input(">")
            if choice.isdigit():
                if choice == "1":
                    terminal_cleaner()
                    pineapple_home_dialogue_done = True
                    speak("Leziz ve buz gibi ananas suyu serinlenmek için birebir!")
                    time.sleep(0.5)
                    speak("Sa- Sanırım biraz fazla içtin. Sünger Bob'un evi nereye kayboldu???")
                    time.sleep(1.3)
                    for a in range(16):
                        game_maps[episode]["map"][position_y[i]][position_x[i]] = " "
                        i += 1

                if choice == "2":
                    terminal_cleaner()
                    speak("Şu an bir ananas suyu leziz olabilirdi.")
                    time.sleep(0.5)
                    speak("Ama Sünger Bob'a kıyamadığın için evini yerinde bırakmaya karar verdin.")
                    time.sleep(1.3)
            else:
                print()
                speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

            current_state = State.PLAYING
            continue

        # SUNGER BOB
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (3, 13) and not sponge_bob_dialogue_done:
            speak("Sünger Bob şaşırmış bir şekilde sana bakıyor.")
            time.sleep(0.5)
            show_display("SpongeBob_1")
            speak("Evini içtiğin için sana biraz sinirli olmalı. Çok üstüne gitme.")
            time.sleep(1.3)
            while current_state == State.DIALOGUE:
                for i, row in enumerate(sponge_bob_dialogues, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(sponge_bob_dialogues):
                        answer = sponge_bob_dialogues[choice - 1]
                        if answer == "Çıkış":
                            pass
                        else:
                            sponge_bob_dialogues.pop(choice - 1)
                        # Actions
                        if answer == "Selam!":
                            terminal_cleaner()
                            show_display("SpongeBob_1")
                            speak("Merhaba, pek hoş bir tanışma olmadı!")
                            time.sleep(1.3)
                        elif answer == "Evini içtiğim için özür dilerim.":
                            terminal_cleaner()
                            show_display("SpongeBob")
                            speak("Neyse, zaten ilk defa başıma gelmiyor..")
                            time.sleep(0.5)
                            speak("Ama sadece bir özür yetmez. Dışarıdaki denizanalarını gördün mü?")
                            speak("Onları toplamaya çıkacağım. Benimle gelmeye ne dersin??")
                            time.sleep(1)
                            speak(">1) Harika! Sana yardım etmek isterim.")
                            speak(">2) Bunu yapmak istediğimden emin değilim.")
                            choice = input(">")
                            if choice == "1":
                                terminal_cleaner()
                                speak("Sünger bob ile denizanaları toplarken çok eğlendiniz.")
                                time.sleep(0.5)
                                speak("Artık sana pek de sinirli değil gibi görünüyor.")
                                time.sleep(1.3)
                                show_display("SpongeBob")
                                speak("Yardım ettiğin için teşekkür ederim.")
                                speak("Teşekkürüm olarak bu yengeç burgeri kabul et!")
                                time.sleep(1.3)
                                speak("Bir yengeç burger aldın!")
                                time.sleep(1.5)
                                sponge_bob_dialogue_done = True
                                break

                            if choice == "2":
                                terminal_cleaner()
                                show_display("SpongeBob_1")
                                speak("Sanırım denizanalarını toplamak için Patrick'i uyandırmaya gideceğim.")
                                time.sleep(1.3)
                                sponge_bob_dialogue_done = True
                                break
                        elif answer == "Evin çok lezzetliydi yine olsa yine içerim!":
                            terminal_cleaner()
                            show_display("SpongeBob_1")
                            time.sleep(0.5)
                            speak("Duymak istediğim yanıtın bu olduğuna emin değilim.")
                            time.sleep(0.5)
                            speak("Dışarıdaki denizanalarını gördün mü?")
                            speak("O denizanalarını toplamaya gideceğim. Eğer yine de bir özür dilemek istersen, bana yardıma gelmeye ne dersin??")
                            time.sleep(1)
                            speak(">1) Harika! Sana yardım etmek isterim.")
                            speak(">2) Bunu yapmak istediğimden emin değilim.")
                            choice = input(">")
                            if choice == "1":
                                terminal_cleaner()
                                speak("Sünger bob ile denizanaları toplarken çok eğlendiniz.")
                                time.sleep(0.5)
                                speak("Artık sana pek de sinirli değil gibi görünüyor.")
                                time.sleep(1.3)
                                show_display("SpongeBob")
                                speak("Yardım ettiğin için teeşekkür ederim.")
                                speak("Teşekkürüm olarak bu yengeç burgeri kabul et!")
                                time.sleep(1.3)
                                speak("Bir yengeç burger aldın!")
                                time.sleep(1.5)
                                sponge_bob_dialogue_done = True
                                break

                            if choice == "2":
                                terminal_cleaner()
                                show_display("SpongeBob_1")
                                speak("Sanırım denizanalarını toplamak için Patrick'i uyandırmaya gideceğim.")
                                time.sleep(1.3)
                                sponge_bob_dialogue_done = True
                                break
                        elif answer == "Çıkış":
                            sponge_bob_dialogue_done = False
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")
                continue

        # PATRİCK
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (18, 13) and not patrick_dialogue_done:
            speak( "**Bikini Kasabası'nın kumlu plajında dolaşırken bir horlama sesi duyuyorsun. \n Patrick bir kayanın altında uyuyor.")
            time.sleep(1.5)
            show_display("Patrick_sleep")
            speak("Onu uyandıracak mısın?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            choice = input(">")
            if choice.isdigit():
                choice = int(choice)

                if choice == "1":
                    terminal_cleaner()
                    show_display("Patrick")
                    time.sleep(0.5)
                    speak("Patrick uyku sersemi sana bakıyor.")
                    speak("Sanırım sinirlenmeden gitsen iyi olur.")
                    time.sleep(1)
                    patrick_dialogue_done = True

                if choice == "2":
                    terminal_cleaner()
                    show_display("Patrick_sleep")
                    time.sleep(0.5)
                    speak("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
                    time.sleep(1.3)
            else:
                print()
                speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

            current_state = State.PLAYING
            continue

        # GARRY
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (5, 11) and not garry_dialogue_done:
            show_display("Garry")
            speak("**Küçücük bir salyangoz kedi ile karşılaştın!")
            time.sleep(1.3)
            while current_state == State.DIALOGUE:
                terminal_cleaner()
                show_display("Garry")
                speak("Garry: meowwwww!")
                for i, row in enumerate(garry_dialogues, 1):
                    print(f"{i}){row}")
                choice = input()
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(garry_dialogues):
                        answer = garry_dialogues[choice - 1]
                        if answer == "Çıkış":
                            pass
                        else:
                            garry_dialogues.pop(choice - 1)
                        # Actions
                        if answer == "Merhaba":
                            time.sleep(0.5)
                            speak("meowwwwww!")
                            time.sleep(0.5)
                        elif answer == "Sen kimsin?":
                            time.sleep(0.5)
                            speak("miuuuuuu!")
                            time.sleep(0.5)
                        elif answer == "Bööö!!":
                            time.sleep(0.5)
                            speak("'Garry kaçtı!'")
                            time.sleep(0.5)
                            terminal_cleaner()
                            current_state = State.PLAYING
                            garry_dialogue_done = True
                            break
                        elif answer == "Çıkış":
                            garry_dialogue_done = False
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")
        else:
            current_state = State.PLAYING

        # DENİZANALARI
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (24, 6) and not jellyfish_dialogue_done:
            speak("Bikini Kasabası'nın eşsiz ve renkli deniz yaşamının önemli bir parçası olan denizanaları burada toplanmış gibiler.")
            speak("Tentaküllerinin parlak görünüşleri seni hemen etkilemesin, zehirli olabilirler onlara dokunmak istemezsin!")
            time.sleep(1)
            jellyfish_dialogue_done = True

        # SQUİDWARD
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (11, 9) and not squidward_dialogue_done:
            speak("Squidward' un evinin önüne geldin.")
            speak("Klarnetinin sesini duyuyorsun.")
            time.sleep(1)
            squidward_dialogue_done = True

        # KRUSTY KRAB
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (5, 6) and not krusty_krab_dialogue_done:
            speak("Bay Yengecin ünlü restoranı 'Yengeç Restoran'ın önünde duruyorsun.")
            speak("Leziz yengeç burgerin kokusu seni iyice acıktırdı.")
            time.sleep(1)
            krusty_krab_dialogue_done = True

        # CHUM BUCKET
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (11, 6) and not chem_bucket_dialogue_done:
            speak("Planktonun müşterisiz restoranı 'Yem Kovası'.")
            time.sleep(0.5)
            speak("Bay Yengeç ile Plankton yolları ayırdıktan sonra Plankton kendine bu restoranı açmış olmalı.")
            time.sleep(1)
            chem_bucket_dialogue_done = True

def episode_3():
    input()

episode_2()