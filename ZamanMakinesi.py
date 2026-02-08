
# Not: Hikayeselleştirdiğimiz için Bin satırdan fazla print, speak, time.sleep ve sözlüklerdeki
# karakter şekilleri ile haritalar tuttuğu için toplam kod sınırı aştı.

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
width = 25
height = 15

# clock
step = 0
hour = random.randint(10, 23)
min = random.randint(10, 55)

game_maps = {  # # | - _ ¯ ♦ ■ §
    0: {  # Episode 0 EV
        "name": "Ev", "height": 5, "width": 10,
        "map": [["X", " ", " ", " ", "■", " ", " ", " ", " ", " "],
                [" ", " ", " ", "|", " ", "|", " ", " ", " ", " "],
                [" ", " ", " ", "|", "■", "|", " ", " ", "■", " "],
                [" ", " ", " ", "|", "§", "|", " ", "♦", " ", " "],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
    },
    1: {  # Episode 1 Başlangıç: TANITIM
        "name": "Bikini Kasabası", "height": 15, "width": 25,
        "map": [
            ["X", " ", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "♦", "_", "_", "_",
             "_", "_", "_", "_"],
            [" ", "|", "¯", "♦", " ", " ", " ", " ", "¯", "|", "|", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|",
             "-", " ", "-", "|"],
            [" ", "|", "¯", " ", " ", " ", " ", " ", "¯", "|", "|", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|",
             " ", "♦", " ", "|"],
            [" ", "|", "¯", " ", " ", " ", " ", " ", "¯", "|", "|", " ", "♦", " ", "|", " ", " ", " ", " ", " ", "|",
             " ", " ", " ", "|"],
            [" ", "|", "¯", " ", " ", "♦", " ", " ", "¯", "|", "¯", "¯", "■", "¯", "¯", " ", " ", " ", " ", " ", "¯",
             "¯", "■", "¯", "¯"],
            [" ", "¯", "¯", "¯", "¯", "■", "¯", "¯", "¯", "¯", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", "_", "_", "-", "_", "_", " ", " ", "_", "_", "-", "_", "_", " ", " ", "_", " ", " ", " ", "_",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", "♦", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|",
             " ", " ", " ", "§"]]
    },
    2: {  # Episode 2 Gelişime
        "name": "Bikini Kasabası", "height": 15, "width": 25,
        "map": [
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
             "_", "_", " ", " "],
            [" ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", "♦", " ", "¶", " ", "|", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", "♦", " ", "|", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", "¯", "¯", "-", " ", "¯", "¯", " ", " ", "¯", "¯", " ", "¯", "¯", "¯", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", "■"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", "■", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " "],
            [" ", " ", "_", "_", "-", "_", "_", " ", " ", "_", "_", "-", "_", "_", " ", " ", "_", " ", " ", " ", "_",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", "♦", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", "♦", " ", " ", "|", " ", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", "♦", " ", "|",
             " ", " ", " ", " "],
            [" ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|", " ", " ", "|", "_", "_", "_", "|",
             " ", " ", " ", "§"]]
    },
    4: {  # Episode 2 Maze
        "name": "Labirent", "height": 13, "width": 17,
        "map": [["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", "|", " ", "|", " ", "|", " ", " ", "|", "_", "_", "_"],
                [" ", "_", "_", "_", "_", " ", "|", " ", "|", " ", "|", " ", " ", " ", " ", "|", " "],
                [" ", "|", " ", " ", "|", " ", "|", " ", "|", " ", " ", " ", " ", " ", " ", "|", " "],
                [" ", "|", " ", "_", "|", " ", "|", " ", "|", " ", "_", "_", "_", "_", " ", "|", " "],
                [" ", "|", " ", " ", "|", " ", "|", " ", " ", " ", "|", " ", " ", "|", " ", "|", " "],
                [" ", "|", " ", " ", "|", " ", "|", "_", "|", " ", "|", " ", " ", "|", " ", " ", " "],
                [" ", "|", "_", " ", "|", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", "|", " "],
                [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", "|", "_", "|", " "],
                [" ", "_", "_", "_", "_", "|", "_", "_", "_", "_", "|", " ", " ", "|", " ", " ", " "],
                [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", "_", "_", "|", "_", " ", "_"],
                [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "¶"]]
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
    "Patrickk": {"display": """ 
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
    "SüngerBot": {"display": """ 
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
                  "kişilik": "Neşeli, Enerjik, Saf"
                  },
    "SüngerBott": {"display": """ 
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
                    "kişilik": "Neşeli, Enerjik, Saf"
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

    "Brian": {"display": """
            ╭━┳━╭━╭━╮╮
            ┃   ┣▅╋▅┫┃
            ┃ ┃ ╰━╰━━━━━━╮
            ╰┳╯         ◢▉◣
             ┃          ▉▉▉▉
             ┃          ◥▉◤
             ┃    ╭━┳━━━━╯
             ┣━━━━━━┫
        """,
              "tür": "Köpek",
              "meslek": "Sanatçı-Ressam",
              "kişilik": "Sakin, Zeki, Toplumcu, Eşitlikçi"

              },
    "Squidword": {"display": """
            .--'''''''''--.
         .'      .---.      '.
        |    .-----------.    |
       |        .-----.        |
       |       .-.   .-.       |
       |      |   | |   |      |
        |    | .-. | .-. |    |
         '-._| |█| | |█| |_.-'
             | '-' | '-' |
              |___| |___|
           _.-'  |   |  `-._
         .' _.--|     |--._ '.
         ' _...-|     |-..._ '
                |     |
                '.___.'
                  | |
                 _| |_
        """,
                  "tür": "Kalamar",
                  "meslek": "ŞERİF",
                  "kişilik": "Despot, Ketum, Agresif"
                  },
    "Monalisa": {"display": """
     ________________________
    |.----------------------.|
    ||                      ||
    ||                      ||
    ||     .- ```` -.       ||
    ||    |  _.._    `|     ||
    ||   | |      -.   ;    ||
    ||   | |__  __  |   |   ||
    ||   | | e |e   |   |   ||
    ||   | |  |     |   |   ||
    ||   | |   -    |   |   ||
    ||   |  | --   ||   |   ||
    ||   |   `;--- ||   |   ||
    ||   |    |     |   |   ||
    ||   |  .-      |   |   ||
    || --||`        |   |--.||
    ||   ;    .     ;  _.|  ||
    ||    `-.;_    |.-      ||
    ||         ````         ||
    ||______________________||
    '------------------------'
        """
                 },
    "BayYengeç": {"display": """
          ||/   ||/
         |  |  |  |
         |  |  |  |
         |  |  |  |
         |__|  |__|
         |█|   |█|
         |  |__|  |
        /|  |  |  |_
      _/            |
     /     |_______|__ 
    /                 |
    |__               |
       |_____________|
        """,
                "tür": "Yengeç",
                "meslek": "Burgerci",
                "kişilik": "Cimri, Paragöz, Otoriter"
                },
    "News1": {"display": """
.___________________________________________________.
|                                                   |
|          *BİKİNİ KASABASI GAZETESİ*               |
|                           22. Deniz Anası Mevsimi |
|___________________________________________________|
|                                                   |
|   SON DAKİKA!  EŞSİZ BİR BULUŞ                    |
|  Tat kavramını yeniden tanımlayan yeni bir buluş! |
|  Bay Yengeç ve dostu Plankton yeni bir gizli tarif|
|  geliştirdi ve bu Bikini kasabasında bir devrim.  |
|  YARATACAK!                                       |
|                                                   |
|  Haber 1:                                         |
|   YENİ YENGEÇ RESTORANT                           |
|  Bay Yengeç ve ortağı Plankton keşfettikleri eşsiz|
|  formüllerini sergilemek için Bugün yeni restorant|
|  ları Yenton'un açılış sergisine tüm Bikini       |
|  kasabası davetlidir!                             |
|                                                   |
|                                                   |
|  Haber 2:                                         |
|    SÜNGERBOT GÜNÜ KURTARIYOR                      |
|  Süngerbot ÜçgenPantolon yine inanılmaz kızartma  |
|  becerileriyle Yenton restorantının ilk şefi oldu |
|  Üstelik Süngerbot yıllık sadece bir deniz        |
|  incisine anlaştıklarını öğrenen halk Süngerbotun |
|  mütevazıliğini takdir etti!                      |
|                                                   |
|                                                   |
| Haber 3:                                          |
|   KAYIP DENİZ YILDIZI!                            |
|  Bikini kasabasında pembe bir deniz yıldızı,      |
|  son birkaç gündür kayıp. En son Bikini Kasabası  |
|  parkında görüldü. Pembe deniz yıldızı görenler   |
|  derhal Bikini Kasabasına bildirmeleri rica olunur|
|___________________________________________________|
        """
              },
    "News2": {"display": """
.___________________________________________________.
|                                                   |
|          *BİKİNİ KASABASI GAZETESİ*               |
|                           34. Deniz Anası Mevsimi |
|___________________________________________________|
|                                                   |
|                                                   |
|   YENTON'DA ŞOK AYRILIK!                          |
|  Bay Yengeç ve ortağı Plankton restoranlarının    |
|  10. yılında yollarını ayırma kararı aldılar.     |
|  Bunun üzerine Plankton yeni restoranı            |
|  'Yem Kovası'nın açılışını gerçekleştirdi.        |
|                                                   |
|                                                   |
|  Haber 1:                                         |
|   KASABADA YARIŞMA HEYECANI!                      |
|  56. geleneksel denizanası toplama yarışması için |
|  hazırlıklar sürüyor. Geçen yarışmanın kazananı   |
|  Süngerbot'un da yarışmaya katılacağı öğrenildi.  |
|  Büyük bir rekabete sahne olacak bu etkinliğe tüm |
|  kasaba halkından katılım bekleniyor.             |
|                                                   |
|                                                   |
| Haber 2:                                          |
|   ŞERİFE HİZMET MADALYASI                         |
|  Bikini Kasabası'nın gururu Şerif Squidword, dün  |
|  düzenlenen törenle hizmetlerinden dolayı üstün   | 
|  hizmet madalyasına layık görüldü.                |
|                                                   |
|___________________________________________________|
"""
              }
}


# Dialoglara animasyon ekler
def speak(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    time.sleep(1)


# Harita dışındaki sınırları belirler
def draw_map():
    global game_maps, episode
    if episode == 0:
        print("╔══════════╗")
        for row in game_maps[episode]["map"]:
            print("║" + "".join(row) + "║")
        print("╚══════════╝")
    elif episode == 1:
        print("╔═════════════════════════╗")
        for row in game_maps[episode]["map"]:
            print("║" + "".join(row) + "║")
        print("╚═════════════════════════╝")
    elif episode == 2:
        print("╔═════════════════════════╗")
        for row in game_maps[episode]["map"]:
            print("║" + "".join(row) + "║")
        print("╚═════════════════════════╝")


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
    print(f"Mevcut Konum: {game_maps[episode]['name']}")


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

    # TANITIM         # Lab(12,5) Plankton(5,5) Burger(5,6) Patrick(18,3) Portal(24,14) SpongeHome(4, 9)
    if episode == 1:  # Brian(22,5) Atölye(22,3) Squid(17,1) BMO(12,4) Sponge(3,2) News(8,0) PatrickWanted(11, 9)

        if ((x_pos, y_pos) == (17, 1) or (24, 14) or (12, 4) or (12, 5) or
                (5, 5) or (5, 6) or (22, 3) or (22, 5) or (3, 2) or (8, 0) or (11, 9) or (4, 9)):
            current_state = State.DIALOGUE
        else:
            current_state = State.PLAYING
        return current_state

    # GELİŞME
    if episode == 2:
        if (x_pos, y_pos) == (18, 13) or (4, 11) or (4, 9) or (3, 13) or (13, 2) or (11, 2) or (24, 14):
            current_state = State.DIALOGUE
        else:
            current_state = State.PLAYING
        return current_state


# Bugları bulmak için
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

        step = 0

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


# Karakterlerin özellikleri ve görüntüsünü yazdırır
def stats(name=str):
    if name in characters:
        character = characters[name]
        lines = [
            f"Tür: {character['tür']}",
            f"Meslek: {character['meslek']}",
            f"Kişilik: {character['kişilik']}"
        ]
        max_length = max(len(line) for line in lines)

        size = max(max_length, len(name) + 4)

        print("+" + "-" * (size + 2) + "+")

        print("| " + name.center(size) + " |")

        print("+" + "-" * (size + 2) + "+")

        for line in lines:
            print("| " + line.ljust(size) + " |")

        print("+" + "-" * (size + 2) + "+")
    else:
        print(f"Character '{name}' not found.")


# Karakterlerin görüntüsünü yazdırır
def show_display(character):
    stats(character)
    print(characters[character]["display"])
    print("----------------------------------------------")


# Hareket girdisi yanlışsa karakter sembolü değişir
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


# Girilen değerin etrafını çizer(TABELA)
def entrance(name=str):
    print()
    lines = [name]
    max_length = max(len(line) for line in lines)

    size = max(max_length, len(name) + 4)  # Ensure name fits too

    print("+" + "-" * (size + 2) + "+")

    print("| " + name.center(size) + " |")

    print("+" + "-" * (size + 2) + "+")

# Labirent bölümü
def maze():
    global step, x_pos, y_pos, episode, current_state
    episode = 4
    x = x_pos
    y = y_pos
    x_pos = 0
    y_pos = 0

    title()
    while True:  # ╔═║╚══════════╝═╗
        clock()

        print("╔═════════════════╗")
        for row in game_maps[episode]["map"]:
            print("║" + "".join(row) + "║")
        print("╚═════════════════╝")

        if episode == 4:
            title()
            choice = input("").lower().strip()
            terminal_cleaner()

            game_maps[episode]["map"][y_pos][x_pos] = "."
            episode, x_pos, y_pos, step = move_player(width, height, game_maps, episode, move_input=choice, x=x_pos,
                                                      y=y_pos)
            game_maps[episode]["map"][y_pos][x_pos] = change_cursour(choice)
            current_state = check_position()

        if episode == 4 and (x_pos, y_pos) == (16, 12):  # (16, 12)
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


# Başlangıç ekranı
def main():
    while True:
        choice = main_menu()
        if choice == '1':
            start_game()
            break
        elif choice == '2':
            instructions()
        elif choice == '3':
            exit_game()
        else:
            terminal_cleaner()
            print("Geçersiz seçim, lütfen tekrar deneyin.")


# Menüdeki görüntü
def main_menu():
    terminal_cleaner()
    print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                                       ║")
    print("║                                          xxxxxxxxxxxx                                                 ║")
    print("║                                                                                                       ║")
    print("║                                          1. Başla                                                     ║")
    print("║                                          2. Talimatlar                                                ║")
    print("║                                          3. Çıkış                                                     ║")
    print("║                                                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    choice = input("Seçiminizi yapın (1/2/3): ").strip()
    return choice


# Talimatları okutur
def instructions():
    terminal_cleaner()
    print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                          TALİMATLAR                                                   ║")
    print("║                                                                                                       ║")
    print("║    Oyun Talimatları:                                                                                  ║")
    print("║    1. Yapacağınız seçimlere dikkat edin.                                                              ║")
    print("║    2. Seçimler oyunun kaderini belirleyecektir.                                                       ║")
    print("║                                                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    input("Ana menüye dönmek için Enter'a basın.")


# Oyunu başlatır
def start_game():
    terminal_cleaner()
    print("Oyun Başlıyor...")
    episode_0()


# Oyundan çıkar
def exit_game():
    terminal_cleaner()
    print("Oyundan çıkılıyor...")
    exit()


# Ev'deki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_0():
    global step, x_pos, y_pos, episode, current_state
    mom_dialogue_done = False
    calendar_dialogue_done = False
    preview_dialogue_done = False
    preportal_dialogue_done = False

    while True:
        clock()

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
            speak("Gitmek İstediğin Zaman Dilimini Seç!")
            speak(">1) ???")
            speak(">2) ???")
            speak(">3) ???")
            choice = input(">")
            if choice == "1" or "2" or "3":
                terminal_cleaner()
                print("------------------------")
                speak("Bikini Kasabasına Gidiliyor!")
                speak("bip                 bop")
                speak("        bop")
                speak("  bipbopbipbop")
                terminal_cleaner()
                time.sleep(1.5)
                speak(f"{random.randint(1, 30)} Mayıs 1946")
                time.sleep(0.5)
                speak("...")
                print("------------------------")
                episode = 1
                x_pos = 0
                y_pos = 0
                current_state = State.PLAYING
                episode_1()
                break

        # Anne
        if current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) == (7, 3) and not mom_dialogue_done:
            speak("Annen kapıyı tıklatıyor")
            time.sleep(1.5)
            speak("Kapıyı açacak mısın?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            mom_dialogue_done = True
            choice = input(">")
            if choice == "1":
                time.sleep(0.5)
                speak("Annen sana bir bardak süt getirmiş")
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
        if (current_state == State.DIALOGUE and episode == 0 and (x_pos, y_pos) ==
                (4, 2) and not preportal_dialogue_done):
            speak("-Zaman Makinesi-")
            speak("Geçmişteki çeşitli medeniyetlere seyehat etmeni sağlar.")
            speak("Yerini seçebilirsin ancak saat dilimini rastgele oluşturacaktır.")
            speak("Geri dönmek için tekrar zaman makinesini (§) kullan.")
            print("----------------------------")
            preportal_dialogue_done = True
        current_state = State.PLAYING
        continue


# Bölüm 1'deki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_1():
    global step, x_pos, y_pos, episode, current_state
    squidword_dialogues1 = ["Neredeyim?", "Siz kimsiniz?", "**Yardım iste**"]

    plankton_dialogues1 = ["Beni Şerif yolladı. Uzaklardan geliyorum karnım çok aç", "Siz kimsiniz?",
                           "Çok fazla müşteri gelir mi buraya?"]
    plankton_dialogues1_2 = ["Bayım bu yediğim en güzel şey bunun içinde ne var böyle??",
                             "Vay canına bu mükemmel, burger için teşekkürler"]

    bmo_dialogue1 = ["Pardon, ben Plankton ve Yengecin Burgercisini arıyorum nasıl gidebilirim?", "Sen kimsin?",
                     "Çıkış"]
    bmo_dialogue1_2 = ["Bu yer de ne böyle?", "Burada tek başına mı çalışıyorsun", "Sen kimsin?", "Çıkış"]

    brian_dialogue1 = ["Bu Sanat işlerinde para var mı?", "Eserlerinizi görebilir miyim?", "Ne zamandır buradasınız?",
                       "Çık"]
    brian_dialogue1_2 = ["4 yıl mı?? Bu resmen bir delilik !", "Eseri incele"]
    brian_dialogue1_3 = ["Bu eserin adı nedir?", "Bu eserle ne anlatmak istediniz?", "Çık"]
    sponge_dialogue1 = ["Burger dışında başka hangi yemekler popüler?", "Burada çalışmak nasıl bir his?",
                        "Bay Yengeç nasıl bir patron? Onunla çalışmak zor mu?", "Çık"]


    squidward_dialogue_done = False
    plankton_dialogue_done = False
    bmo_dialogue_done = False
    brian_dialogue_done = False
    sponge_dialogue_done = False
    newspaper_done = False
    sponge_home_done = False
    patrick_wanted_done = False
    panel_labratory_done = False
    panel_burger_done = False
    panel_gallery_done = False

    while True:
        clock()

        if current_state == State.PLAYING and episode == 1:
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

        # SQUİDWARD
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (17, 1) and not squidward_dialogue_done):
            show_display("Squidword")
            speak("Squidword: HEY! Evlat sen de kimsin?")
            speak("Squidword: Bu kasabaya dışarıdan yabancılar giremez, yolunu mu kaybettin?")
            print()
            speak("-Merhaba Bayım ben başka bir zaman diliminden geliyorum.")
            print()
            speak("Squidword: Hah Şakacı şey seni?!")
            time.sleep(0.5)
            print()
            while current_state == State.DIALOGUE:
                for i, row in enumerate(squidword_dialogues1, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(squidword_dialogues1):
                        answer = squidword_dialogues1[choice - 1]
                        if answer == "Neredeyim?":
                            terminal_cleaner()
                            show_display("Squidword")
                            time.sleep(1)
                            speak("Squidword: Burayı nasıl bilmezsin burası meşhur Bikini Kasabası.")
                            print()
                            time.sleep(0.5)
                            squidword_dialogues1.pop(choice - 1)

                        elif answer == "Siz kimsiniz?":
                            terminal_cleaner()
                            show_display("Squidword")
                            speak("Squidword: Ben kasabanın şerifi Squidword, kasabanın güvenliği benden sorulur.")
                            print()
                            time.sleep(0.5)
                            squidword_dialogues1.pop(choice-1)

                        elif answer == "**Yardım iste**":
                            terminal_cleaner()
                            show_display("Squidword")
                            speak("-Bana yardımınız etmeniz lazım.")
                            speak("*Karnın guruldar(grrrrrrrr)")
                            speak(" vee yiyecek bir şeyler belki...")
                            print()
                            speak("Squidword: Normalde yabancılar giremez ama sanırım sana yardımcı olabilirim.")
                            time.sleep(0.5)
                            speak("Squidword: Doğruca Plankton ve Yengecin yeni açılan burgercisine git,")
                            speak(" seni benim yolladığımı söyle ve karnını doyur.")
                            speak("Squidword: Burgerci kasabaya doğru giderken sağda kalıyor.")
                            print()
                            time.sleep(0.5)
                            current_state = State.PLAYING
                            squidward_dialogue_done = True
                            pass
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # Burgerci Tabela
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (5, 6) and not panel_burger_done):
            entrance("PLANKTON VE YENGECİN MEŞHUR BURGERCİSİ")
            time.sleep(1)
            speak("-Şerifin Bahsettiği yer burası olmalı.")
            time.sleep(1)
            panel_burger_done = True
            current_state = State.PLAYING

        # Plankton
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (5, 5) and not plankton_dialogue_done):
            show_display("Plankton")
            speak("Plankton: Yengeç Restorana hoşgeldiniz.")
            time.sleep(1)
            print()
            while current_state == State.DIALOGUE:
                for i, row in enumerate(plankton_dialogues1, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(plankton_dialogues1):
                        answer = plankton_dialogues1[choice - 1]
                        if answer == "Siz kimsiniz?":
                            plankton_dialogues1.pop(choice - 1)
                            terminal_cleaner()
                            show_display("Plankton")
                            speak("Plankton: Ben Plankton, kasabanın en iyi burgercisinin Bay Yengeçle birlikte ortağıyım.")
                            print()
                            time.sleep(1)

                        elif answer == "Çok fazla müşteri gelir mi buraya?":
                            plankton_dialogues1.pop(choice - 1)
                            terminal_cleaner()
                            show_display("Plankton")
                            speak("Plankton: Çokta ne kelime? Özel burger tarifimizi bir yiyen her gün yemeden duramaz")
                            speak(" civar kasabalar dahil her yerden müşterimiz eksik olmaz bizim")
                            print()
                            time.sleep(1)

                        elif answer == "Beni Şerif yolladı. Uzaklardan geliyorum karnım çok aç":
                            plankton_dialogues1.pop(choice - 1)
                            terminal_cleaner()
                            show_display("Plankton")
                            # dialoglar
                            speak("Plankton: Ah demek Şerif yolladı. Şerifin misafirlerinin başımızın üstünde yeri vardır")
                            speak("Plankton: Buyur geç içeri")
                            print()
                            time.sleep(1)

                            # BMOYLA KONUŞULDUYSA
                            if bmo_dialogue_done is True:
                                speak("-Ama... Birisi bana geçen hafta burada 4 kişinin zehirlendiğini söyledi.")
                                speak(" Buraya gerçekten güvenebilir miyim?")
                                print()
                                speak("Plankton: NE? Zehirlenmek mi? Buraya gelenler yüzü asık dahi çıkmaz!")
                                speak("Plankton: Kim söyledi sana bu yalanı?")
                                print()
                                speak("-Hemen yan taraftaki Laboratuvarda çalışan görevli söyledi.")
                                print()
                                speak("Plankton: BMO... Onun yanından ayrıldığım için bana kızgın.")
                                speak("Plankton: Laboratuvara geri dönemem için Burgerciyi kötülüyor olmalı.")
                                time.sleep(0.5)
                                speak("Plankton: Merak etme köftelerimiz güvenilir olmasa Şerif seni yollamazdı.")
                                speak("Plankton: Buyur içeri gel.")
                                time.sleep(0.5)

                            print()
                            speak("*İçeri geçilir")
                            speak("+Bir Yenngeç Burger aldın.")
                            print()
                            time.sleep(1)
                            terminal_cleaner()

                            while current_state == State.DIALOGUE:
                                for i, row in enumerate(plankton_dialogues1_2, 1):
                                    print(f"{i}){row}")
                                choice = input(">")
                                if choice.isdigit():
                                    choice = int(choice)
                                    if 1 <= choice <= len(plankton_dialogues1_2):
                                        answer = plankton_dialogues1_2[choice - 1]

                                        if answer == "Bayım bu yediğim en güzel şey bunun içinde ne var böyle??":
                                            plankton_dialogues1_2.pop(choice - 1)
                                            terminal_cleaner()
                                            show_display("Plankton")
                                            print()
                                            speak("Plankton: Demiştim kasabanın en iyi burgerleri, bizimkiler.")
                                            speak("Plankton: İçinde Bay Yengecin özel turşuları ve benim özel labora"
                                                  "tuvarımda geliştirdiğim çok gizli sos var.")
                                            print()
                                            time.sleep(0.5)

                                        elif answer == "Vay canına bu mükemmel, burger için teşekkürler":
                                            terminal_cleaner()
                                            show_display("Plankton")
                                            print()
                                            speak("Plankton: Ne demek istediğin zaman uğrayabilirsin...")
                                            terminal_cleaner()
                                            time.sleep(1)
                                            current_state = State.PLAYING
                                            plankton_dialogue_done = True
                                            pass
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # LAB
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (12, 5) and not panel_labratory_done):
            time.sleep(1)
            entrance("BİKİNİ KASABASI ARAŞTIRMA GELİŞTİRME LABORATUVARI")
            time.sleep(1)
            panel_labratory_done = True
            current_state = State.PLAYING

        # BMO
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (12, 4) and not bmo_dialogue_done):
            show_display("BMO")
            time.sleep(1)
            print()
            while current_state == State.DIALOGUE:

                if plankton_dialogue_done is False:  # PLANKTONA GİDİLDMEDİYSE
                    if len(bmo_dialogue1) == 3:
                        speak("**Laboratuvarın önünde biriyle karşılaştın**")
                    for i, row in enumerate(bmo_dialogue1, 1):
                        print(f"{i}){row}")
                    choice = input(">")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(bmo_dialogue1):
                            answer = bmo_dialogue1[choice - 1]

                            if len(bmo_dialogue1) > 1 and bmo_dialogue_done is False:
                                game_maps[episode]["map"][4][12] = "♦"

                            if answer == "Çıkış":
                                terminal_cleaner()
                                speak("-Gitmeliyim, görüşürüz")
                                time.sleep(1)
                                current_state = State.PLAYING
                                x_pos = 12
                                y_pos = 5
                                game_maps[episode]["map"][5][12] = "v"
                                pass

                            elif answer == "Pardon, ben Plankton ve Yengecin Burgercisini arıyorum nasıl gidebilirim?":
                                bmo_dialogue1.pop(choice - 1)
                                terminal_cleaner()
                                show_display("BMO")

                                speak("BMO: Hıh Burgerciymiş...")
                                speak("BMO: O dandik burgerciye gitmeni önermem geçen gün 4 kişi köftelerden zehirlendi.")
                                print()
                                speak("-Ne? Zehirlendi mi? Bu korkunç ciddi olamazsın.")
                                print()
                                speak("BMO: İster inan ister inanma, ben senin iyiliğin için söylüyorum.")
                                speak("BMO: O aptal burgerci batınca Plankton benim yanıma geri dönücek.(sessizce)")
                                print()
                                speak("-Ne dedin duyamadım?")
                                print()
                                speak("BMO: Hiç.. İşlerim var gitmem gerek!")
                                x_pos = 12
                                y_pos = 5
                                game_maps[episode]["map"][5][12] = "v"
                                game_maps[episode]["map"][4][12] = " "
                                bmo_dialogue_done = True
                                current_state = State.PLAYING

                            elif answer == "Sen kimsin?":
                                bmo_dialogue1.pop(choice - 1)
                                terminal_cleaner()
                                show_display("BMO")
                                speak("BMO: Ben BMO, bu Laboratuvarın sorumlusuyum.")
                                print()
                                time.sleep(1)

                else:  # PLANKTONA GİDİLDİYSE
                    if len(bmo_dialogue1) == 4:
                        speak("**Laboratuvarın önünde biriyle karşılaştın")
                    for i, row in enumerate(bmo_dialogue1_2, 1):
                        print(f"{i}){row}")
                    choice = input(">")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(bmo_dialogue1_2):
                            answer = bmo_dialogue1_2[choice - 1]

                            if answer == "Çıkış":
                                terminal_cleaner()
                                speak("-Gitmeliyim, görüşürüz")
                                time.sleep(1)
                                current_state = State.PLAYING
                                x_pos = 12
                                y_pos = 5
                                game_maps[episode]["map"][5][12] = "v"
                                if bmo_dialogue_done is True:
                                    game_maps[episode]["map"][4][12] = " "
                                else:
                                    game_maps[episode]["map"][4][12] = "♦"
                                pass

                            elif answer == "Sen kimsin?":
                                bmo_dialogue1_2.pop(choice - 1)
                                terminal_cleaner()
                                show_display("BMO")
                                speak("BMO: Ben BMO, bu Laboratuvarın sorumlusuyum")
                                print()
                                time.sleep(1)

                            elif answer == "Burada tek başına mı çalışıyorsun":
                                bmo_dialogue1_2.pop(choice - 1)
                                terminal_cleaner()
                                show_display("BMO")
                                print()
                                speak("BMO: Maalesef Plankton Yengeç ile burgerci açmasaydı beraber çalışıyorduk.")
                                speak("BMO: Ama beni bırakıp gitti, gerçi çok sürmeden geri gelicek...")
                                speak("BMO: O aptal Yengeçte gününü görücek.(sessizce)")
                                print()
                                time.sleep(1)
                                game_maps[episode]["map"][4][22] = " "
                                bmo_dialogue_done = True

                            elif answer == "Bu yer de ne böyle?":
                                bmo_dialogue1_2.pop(choice - 1)
                                terminal_cleaner()
                                show_display("BMO")
                                print()
                                speak("BMO: Burası kasabadaki tek Laboratuvar. Burada bilimsel araştırmalar yapıyorum.")
                                print()
                                time.sleep(1)
                    else:
                        print()
                        speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # Atölye Tabela
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (22, 5) and not panel_gallery_done):
            time.sleep(1)
            entrance("   Brain'ın Sanat Atölyesi   ")
            time.sleep(1)
            panel_gallery_done = True
            current_state = State.PLAYING

        # Brian
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (22, 3) and not brian_dialogue_done):
            show_display("Brian")
            if len(bmo_dialogue1) == 4:
                print()
                speak("Brian: Ah bir sanat sever daha ziyaretime gelmiş, ne harika bir gün...")
                print()
                speak("-Geçerken Atölye dikkatimi çekti demek Brian sizsiniz.")
            print()
            while current_state == State.DIALOGUE:
                for i, row in enumerate(brian_dialogue1, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(brian_dialogue1):
                        answer = brian_dialogue1[choice - 1]

                        if answer == "Çık":
                            terminal_cleaner()
                            speak("-Maalesef gitmeliyim, görüşürüz.")
                            time.sleep(1)
                            current_state = State.PLAYING
                            x_pos = 22
                            y_pos = 4
                            game_maps[episode]["map"][4][22] = "v"
                            if len(bmo_dialogue1) == 4 or 3 or 2:
                                game_maps[episode]["map"][3][22] = "♦"
                            pass

                        elif answer == "Bu Sanat işlerinde para var mı?":
                            brian_dialogue1.pop(choice - 1)
                            terminal_cleaner()
                            show_display("Brian")
                            speak("Brian: Para mı? Ben sanatımı para için değil toplum için icra ediyorum.")
                            speak("Brian: Hem para dediğin nedir ki basit bir "
                                "materyel ben topluma ışık tutmak için sanat yaparım.")
                            speak("Brian: Dünyevi şeyler geçicidir benim topluma "
                                "bırakmak istediğim miras ise ben ölsem dahi kalıcı olur.")
                            print()
                            time.sleep(1)

                        elif answer == "Ne zamandır buradasınız?":
                            brian_dialogue1.pop(choice - 1)
                            terminal_cleaner()
                            show_display("Brian")
                            speak("Brian: Ben kendimi bildim bileli bikini kasabasındayım ve ayrılmak dahi istemiyorum.")
                            speak("Brian: Bu kasabaya aşığım.")
                            print()

                        elif answer == "Eserlerinizi görebilir miyim?":
                            terminal_cleaner()
                            show_display("Brian")
                            speak("Brian: Tabi içeri geçin lütfen.")
                            print()
                            time.sleep(1)
                            speak("*İçeri geçilir ")
                            print()
                            time.sleep(1)
                            brian_dialogue_done = True

                            speak("Brian: 4 yıldır sadece bunun üzerinde çalışıyorum.")
                            print()
                            while current_state == State.DIALOGUE:
                                for i, row in enumerate(brian_dialogue1_2, 1):
                                    print(f"{i}){row}")
                                choice = input(">")
                                if choice.isdigit():
                                    choice = int(choice)
                                    if 1 <= choice <= len(brian_dialogue1_2):
                                        answer = brian_dialogue1_2[choice - 1]

                                        if answer == "4 yıl mı?? Bu resmen bir delilik !":
                                            brian_dialogue1_2.pop(choice - 1)
                                            terminal_cleaner()
                                            show_display("Brian")
                                            print()
                                            speak("Brian: Her sanatçı biraz deli değil midir zaten?")
                                            speak("Brian: Ayrıca bu sanat için ufak bir bedel...")
                                            print()
                                            time.sleep(1)
                                        elif answer == "Eseri incele":
                                            terminal_cleaner()
                                            # Tablo buraya
                                            print(characters["Monalisa"]["display"])
                                            print("----------------------------------")
                                            speak("-Vay canına gerçekten harikaymışşş!")
                                            print()
                                            time.sleep(1)

                                            while current_state == State.DIALOGUE:
                                                for i, row in enumerate(brian_dialogue1_3, 1):
                                                    print(f"{i}){row}")
                                                choice = input(">")
                                                if choice.isdigit():
                                                    choice = int(choice)
                                                    if 1 <= choice <= len(brian_dialogue1_3):
                                                        answer = brian_dialogue1_3[choice - 1]

                                                        if answer == "Bu eserin adı nedir?":
                                                            brian_dialogue1_3.pop(choice - 1)
                                                            terminal_cleaner()
                                                            show_display("Brian")
                                                            print()
                                                            speak(
                                                                "Brian: Buna Madam Lisa adını koydum, kendisi "
                                                                "zihnimde oluşturduğum hayali bir hanımefendi")
                                                            time.sleep(1)
                                                            print()
                                                        elif answer == "Bu eserle ne anlatmak istediniz?":
                                                            brian_dialogue1_3.pop(choice - 1)
                                                            terminal_cleaner()
                                                            show_display("Brian")
                                                            print()
                                                            speak(
                                                                "Brian: Bu tabloyu çizerken, sadece bir kadının"
                                                                " portresini yapmadım")
                                                            speak(
                                                                "Brian: Amacım, insan ruhunun derinliklerindeki"
                                                                " evrensel duyguları yansıtmaktı")
                                                            time.sleep(0.5)
                                                            speak(
                                                                "Brian: Onun gülümsemesi, her bakanın kendi "
                                                                "hikayesini bulacağı bir ayna oldu")
                                                            time.sleep(0.5)
                                                            speak("Brian: Hepimiz farklıyız ama bu gülüşte birleşiyoruz")
                                                            speak(
                                                                "Brian: Sanat, bizi bir araya getirir ve "
                                                                "ortak duygularımızı paylaşmamızı sağlar")
                                                            speak(
                                                                "Brian: İşte bu yüzden bu tablo, sadece bir "
                                                                "yüz değil, insanlığın ta kendisidir")
                                                            time.sleep(1)
                                                            print()
                                                        elif answer == "Çık":
                                                            speak("-Atölye turu için teşekkürler, gitmeliyim")
                                                            current_state = State.PLAYING
                                                            plankton_dialogue_done = True
                                                            pass

                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # SPONGE
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (3, 2) and not sponge_dialogue_done):
            show_display("SüngerBot")
            speak("Restorandaki enfes kokuların geldiği mutfaktasın ve aşçıyla karşılaştın.")
            time.sleep(0.5)
            print()
            while current_state == State.DIALOGUE:
                for i, row in enumerate(sponge_dialogue1, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(sponge_dialogue1):
                        answer = sponge_dialogue1[choice - 1]

                        if len(sponge_dialogue1) == 1:
                            game_maps[episode]["map"][2][3] = " "
                            sponge_dialogue_done = True

                        elif len(squidword_dialogues1) > 1:
                            game_maps[episode]["map"][2][3] = "♦"
                            x_pos = 4
                            y_pos = 2
                            game_maps[episode]["map"][2][4] = ">"

                        if answer == "Burger dışında başka hangi yemekler popüler?":
                            terminal_cleaner()
                            show_display("SüngerBot")
                            speak("SüngerBot: Burger en popüler olanı ama karides kokteyli ve denizanası jölesi de çok seviliyor.")
                            speak("SüngerBot: Ayrıca, patates kızartmalarımız da çok tercih ediliyor.")
                            print()
                            time.sleep(0.5)
                            sponge_dialogue1.pop(choice - 1)

                        elif answer == "Burada çalışmak nasıl bir his?":
                            terminal_cleaner()
                            show_display("SüngerBot")
                            time.sleep(1)
                            speak("SüngerBot: Burada çalışmak harika.")
                            speak(
                                "SüngerBot: Mutfakta çok eğleniyorum ve müşterilerimizi mutlu etmek beni mutlu ediyor.")
                            print()
                            time.sleep(0.5)
                            sponge_dialogue1.pop(choice - 1)

                        elif answer == "Bay Yengeç nasıl bir patron? Onunla çalışmak zor mu?":
                            terminal_cleaner()
                            show_display("SüngerBot")
                            time.sleep(1)
                            speak("SüngerBot: Bay Yengeç oldukça titiz ve parayı çok sever, ama iyi bir patrondur.")
                            speak("SüngerBot: Çalışanlarına değer verir ve restoranın başarılı olması için elinden geleni yapar.")
                            print()
                            time.sleep(0.5)
                            sponge_dialogue1.pop(choice - 1)

                        elif answer == "Çık":
                            terminal_cleaner()
                            time.sleep(0.5)
                            speak("-Gitmeliyim görüşürüz...")
                            current_state = State.PLAYING
                            pass
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # Gazete
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (8, 0) and not newspaper_done):
            print(characters["News1"]["display"])
            print()
            input("Çıkmak için Enter'a basın. ")
            newspaper_done = True
            current_state = State.PLAYING

        # SPONGE EV
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (4, 9) and not sponge_home_done):
            time.sleep(1)
            entrance("   SüngerBot Malikanesi   ")
            time.sleep(1)
            print()
            speak("-Vaaay canınaaaaa")
            speak("-Ananastan bir ev!")
            time.sleep(1)
            terminal_cleaner()
            sponge_home_done = True
            current_state = State.PLAYING

        # Patrick Aranıyor
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (11, 9) and not patrick_wanted_done):
            time.sleep(1)
            entrance("           KAYIP ARANIYOR!           ")
            time.sleep(1)
            print(characters["Patrick"]["display"])
            time.sleep(2)
            terminal_cleaner()
            patrick_wanted_done = True
            current_state = State.PLAYING

        # PORTAL
        if (current_state == State.DIALOGUE and episode == 1 and (x_pos, y_pos) ==
                (24, 14)):
            print("  ")
            speak("Seyehat Edeceğin Yeni Zamanı Seç:")
            speak(">1) ???")
            speak(">2) ???")
            choice = input(">")
            if choice.isdigit():
                if choice == "1" or "2":
                    time.sleep(1)
                    speak("biiiip          boop   ")
                    speak("          boop         ")
                    speak("    boop            bip")
                    print()
                    speak(f"{random.randint(1, 30)} Mayıs 1957")
                    time.sleep(1)
                    current_state = State.PLAYING
                    x_pos = 0
                    y_pos = 0
                    episode = 2
                    game_maps[episode]["map"][0][0] = "X"
                    episode_2()
                    break
            else:
                speak("biip booooooooooop bip bip bip")
        else:
            # State değişimi
            current_state = State.PLAYING


# Bölüm 2'deki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_2():
    global step, x_pos, y_pos, episode, current_state
    garry_dialogues = ["Merhaba", "Sen kimsin?", "Bööö!!", "Çıkış"]
    sponge_bob_dialogues = ["Selam!", "Evini içtiğim için özür dilerim.", "Evin çok lezzetliydi yine olsa yine içerim!",
                            "Çıkış"]
    BMO_dialogues = ["Plankton'la nasıl tanıştınız?",
                     "Plankton’un Yengeç Burger tarifini ele geçirme çabaları hakkında ne düşünüyorsun?",
                     "Bu restorandaki rolün tam olarak nedir?", "Çıkış"]
    plankton_dialogues = ["Yengeç Burger tarifini neden bu kadar çok istiyorsun?",
                          "Bir gün Yengeç Restoran’a karşı kazanma şansın olduğunu gerçekten düşünüyor musun?",
                          " ** Planktona Yengeç Burger Tarifini Ele Geçirmek İçin Yardım Etmeyi Teklif Et **",
                          " ** Plankton'un Planlarını Bay Yengeç'e Anlat ve Plankton'Un Oyununu Boz **"]
    mr_krabs_dialogues = ["Bay Yengeç siz misiniz?", "Plankton ile restoranınızı neden ayırdınız?"]

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
    newspaper_dialogue_done = False
    mr_krabs_dialogue_done = False
    bmo2_dialogue_done = False

    i = 0
    position_y = [14, 13, 12, 11, 14, 13, 12, 11, 10, 10, 10, 10, 10, 14, 14, 14]
    position_x = [2, 2, 2, 2, 6, 6, 6, 6, 2, 3, 4, 5, 6, 3, 4, 5]


    while True:
        clock()
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

        # BayYengeç
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (5, 3) and not mr_krabs_dialogue_done:  # 5,3
            show_display("BayYengeç")
            time.sleep(1)
            speak("Restoran sahibi yengeç bu olmalı.")
            print("      ")
            time.sleep(1.3)
            while current_state == State.DIALOGUE:
                for i, row in enumerate(mr_krabs_dialogues, 1):
                    print(f"{i}){row}")
                choice = input(">")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(mr_krabs_dialogues):
                        answer = mr_krabs_dialogues[choice - 1]

                        # Actions
                        if answer == "Bay Yengeç siz misiniz?":
                            mr_krabs_dialogues.pop(choice - 1)
                            terminal_cleaner()
                            show_display("BayYengeç")
                            time.sleep(0.5)
                            speak("Bay Yengeç: Evet! Kasabanın en zengin yengeci Bay Yengeç!")
                            time.sleep(0.5)
                            speak("Bay Yengeç: Tam karşısında duruyorsun!")
                            print("        ")
                            time.sleep(1.3)
                            mr_krabs_dialogue_done = True

                        elif answer == "Plankton ile restoranınızı neden ayırdınız?":
                            mr_krabs_dialogues.pop(choice - 1)
                            terminal_cleaner()
                            show_display("BayYengeç")
                            time.sleep(0.5)
                            speak("Bay Yengeç: BMO denen o küçük şeytan planktonu hep kıskandı.")
                            time.sleep(0.5)
                            speak("Bay Yengeç: Benden ayrılması için türlü numaralar yaptı.")
                            time.sleep(0.5)
                            speak("Bay Yengeç: Sonunda olan oldu ve ayrıldık.")
                            time.sleep(0.5)
                            speak("Bay Yengeç: Zaten o yanındaki BMO adındaki demir parçası ile çok daha uygunlar!")
                            print("        ")
                            time.sleep(1.3)
                            mr_krabs_dialogue_done = True

                        if len(mr_krabs_dialogues) == 0:
                            current_state = State.PLAYING

                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # PLANKTON ¶
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (
        13, 2) and not plankton_dialogue_done and not mr_krabs_dialogue_done:
            speak("Planktonla konuşabilmek için önce Bay Yengeç'le konuşmalısın!")
            x_pos = 13
            y_pos = 3
            game_maps[episode]["map"][2][13] = "v"
            game_maps[episode]["map"][2][13] = "¶"
            current_state = State.PLAYING
        elif current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (
        13, 2) and not plankton_dialogue_done and mr_krabs_dialogue_done:  # 13,2
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
                            speak("Plankton: Cimri ihtiyar yengeç ile bir zamanlar beraber hayaller kurardık.")
                            time.sleep(0.5)
                            speak(
                                "Plankton: O zamanlar bu burgeri icat ettiğimizde çok büyük bir keşif yaptığımızı fark etmiştik.")
                            time.sleep(0.5)
                            speak("Fakat beni yüzüstü bırakıp kendi başına yola devam edeceğini hiç düşünmemiştim.")
                            time.sleep(0.5)
                            speak(
                                "Plankton: Bu yüzden ondan intikam almalı ve Yengeç Burger tarifi ile tüm kasabayı ele geçirmeliyim!")
                            print("        ")
                            time.sleep(1.3)

                        elif answer == "Bir gün Yengeç Restoran’a karşı kazanma şansın olduğunu gerçekten düşünüyor musun?":
                            terminal_cleaner()
                            show_display("Plankton")
                            time.sleep(0.5)
                            speak("Plankton: O ihtiyar yengece gününü göstereceğim!!")
                            time.sleep(0.5)
                            speak("Plankton: Bana yaptıklarını ona ödeteceğim!")
                            time.sleep(0.5)
                            speak("Plankton: Tek ihtiyacım olan herkesin gözdesi Yengeç Burger'in tarifi!")
                            print("           ")
                            time.sleep(1.3)
                        elif answer == " ** Planktona Yengeç Burger Tarifini Ele Geçirmek İçin Yardım Etmeyi Teklif Et **":
                            terminal_cleaner()
                            show_display("Plankton")
                            time.sleep(0.5)
                            speak("Plankton: G- Gerçekten bana yardım etmek mi istiyorsun??")
                            time.sleep(0.5)
                            speak("Plankton: Eğer bunu başarırsan, bütün Bikini Kasabası’nın en güçlü restoranı ben olacağım!")
                            time.sleep(0.5)
                            speak("Plankton: Herkesin peşinde olduğu o eşsiz tat.")
                            time.sleep(0.5)
                            speak("Plankton: Eğer tarifi ele geçirebilirsem, 'Yem Kovası' nihayet hak ettiği yere gelecek!")
                            time.sleep(0.5)
                            speak("Plankton: Düşün, herkes benim kapımda kuyruk olacak. Ve Bay Yengeç... o tarihe karışacak!")
                            time.sleep(2)
                            terminal_cleaner()
                            print("   ")
                            speak(
                                "Plankton sana Yengeç Restorana girmek ve gizli tarifi ele geçirmek için bir harita verdi.")
                            time.sleep(0.5)
                            speak("Doğru çıkışı bul ve tarifi ele geçir!!")
                            time.sleep(1)
                            plankton_dialogue_done = True
                            krabby_patty_recipe = True
                            maze()
                            break
                        elif answer == " ** Plankton'un Planlarını Bay Yengeç'e Anlat ve Plankton'Un Oyununu Boz **":
                            terminal_cleaner()
                            time.sleep(0.5)
                            print("   ")
                            speak(
                                "Plankton'un Planlarını Bay Yengeç'e Anlatarak Bay Yengeç'in Tarafında Olmayı Seçtin.")
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
                            game_maps[episode]["map"][2][13] = "¶"
                            x_pos = 13
                            y_pos = 3
                            game_maps[episode]["map"][2][13] = "v"
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # PORTAL
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (
        24, 14) and not plankton_dialogue_done:
            print("  ")
            speak("Zaman Makinesi Kullanım Dışı.")
            speak("Burada Yapman Gereken Her Şeyi Tamamlamamışsın Gibi Görünüyor.")
            time.sleep(1.3)
            current_state = State.PLAYING

        elif current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (24, 14) and plankton_dialogue_done:
            print("  ")
            speak("Gerçek Zamana Dönülüyor")
            speak("biiiip          boop   ")
            speak("          boop         ")
            speak("    boop            bip")
            speak(".........")
            current_state = State.PLAYING
            if not krabby_patty_recipe:
                episode_4()
                break
            else:
                episode_3()
                break

        # BMO
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (11, 2) and not bmo2_dialogue_done:
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

                    if answer == "Plankton'la nasıl tanıştınız?":
                        BMO_dialogues.pop(choice - 1)
                        terminal_cleaner()
                        speak("Plankton Bay Yengeç ile yollarını ayırdıktan sonra beni yaptı.")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Plankton’un Yengeç Burger tarifini ele geçirme çabaları hakkında ne düşünüyorsun?":
                        BMO_dialogues.pop(choice - 1)
                        terminal_cleaner()
                        speak(
                            "Kesinlikle Plankton'un en büyük destekçisi benim! \nBu konuda ona hep yardımcı oluyorum! \nbip bop")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Bu restorandaki rolün tam olarak nedir?":
                        BMO_dialogues.pop(choice - 1)
                        terminal_cleaner()
                        speak(
                            "Plankton'un her daim yanında olmak ve onun yeni planları için ona yardımcı olmak. \nBİP! BOP!")
                        show_display("BMO")
                        time.sleep(1.3)
                    elif answer == "Çıkış":
                        current_state = State.PLAYING
                        x_pos = 11
                        y_pos = 3
                        game_maps[episode]["map"][3][11] = "v"
                        game_maps[episode]["map"][2][11] = "♦"
                        if len(BMO_dialogues) == 1:
                            game_maps[episode]["map"][2][11] = " "
                            bmo2_dialogue_done = True
                        pass
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # ANANAS EV
        if (current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) ==
                (4, 9) and not pineapple_home_dialogue_done):
            speak("SüngerBotun ananas eviyle karşılaştın.")
            speak("Bir yudum içecek misin?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            choice_home = input(">")
            if choice_home.isdigit():
                if choice_home == "1":
                    terminal_cleaner()
                    speak("Leziz ve buz gibi ananas suyu serinlenmek için birebir!")
                    time.sleep(0.5)
                    speak("Sa- Sanırım biraz fazla içtin. SüngerBot'un evi nereye kayboldu???")
                    time.sleep(1.3)
                    for a in range(16):
                        if i < 16:
                            game_maps[episode]["map"][position_y[i]][position_x[i]] = " "
                            i += 1
                    pineapple_home_dialogue_done = True

                if choice_home == "2":
                    terminal_cleaner()
                    speak("Şu an bir ananas suyu leziz olabilirdi.")
                    time.sleep(0.5)
                    speak("Ama SüngerBot'a kıyamadığın için evini yerinde bırakmaya karar verdin.")
                    time.sleep(1.3)
                    x_pos = 4
                    y_pos = 8
                    game_maps[episode]["map"][8][4] = "^"
                    game_maps[episode]["map"][9][4] = "■"
            else:
                print()
                speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

            current_state = State.PLAYING


        # SUNGER BOB
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (
        3, 13) and not sponge_bob_dialogue_done:
            speak("SüngerBot şaşırmış bir şekilde sana bakıyor.")
            time.sleep(0.5)
            show_display("SüngerBott")
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
                            show_display("SüngerBott")
                            speak("SüngerBot: Merhaba, pek hoş bir tanışma olmadı!")
                            time.sleep(1.3)
                        elif answer == "Evini içtiğim için özür dilerim.":
                            terminal_cleaner()
                            show_display("SüngerBot")
                            speak("SüngerBot: Neyse, zaten ilk defa başıma gelmiyor..")
                            time.sleep(0.5)
                            speak("SüngerBot: Ama sadece bir özür yetmez. Dışarıdaki denizanalarını gördün mü?")
                            speak("SüngerBot: Onları toplamaya çıkacağım. Benimle gelmeye ne dersin??")
                            time.sleep(1)
                            speak(">1) Harika! Sana yardım etmek isterim.")
                            speak(">2) Bunu yapmak istediğimden emin değilim.")
                            choice = input(">")
                            if choice == "1":
                                terminal_cleaner()
                                speak("SüngerBot ile denizanaları toplarken çok eğlendiniz.")
                                time.sleep(0.5)
                                speak("Artık sana pek de sinirli değil gibi görünüyor.")
                                time.sleep(1.3)
                                show_display("SüngerBot")
                                speak("SüngerBot: Yardım ettiğin için teşekkür ederim.")
                                speak("SüngerBot: Teşekkürüm olarak bu yengeç burgeri kabul et!")
                                time.sleep(1.3)
                                speak("Bir yengeç burger aldın!")
                                time.sleep(1.5)
                                sponge_bob_dialogue_done = True
                                break

                            if choice == "2":
                                terminal_cleaner()
                                show_display("SüngerBott")
                                speak("SüngerBot: Sanırım denizanalarını toplamak için Patrick'i uyandırmaya gideceğim.")
                                time.sleep(1.3)
                                sponge_bob_dialogue_done = True
                                break
                        elif answer == "Evin çok lezzetliydi yine olsa yine içerim!":
                            terminal_cleaner()
                            show_display("SüngerBott")
                            time.sleep(0.5)
                            speak("SüngerBot: Duymak istediğim yanıtın bu olduğuna emin değilim.")
                            time.sleep(0.5)
                            speak("SüngerBot: Dışarıdaki denizanalarını gördün mü?")
                            speak(
                                "SüngerBot: O denizanalarını toplamaya gideceğim. Eğer yine de bir özür dilemek istersen, \nbana yardıma gelmeye ne dersin??")
                            time.sleep(1)
                            speak(">1) Harika! Sana yardım etmek isterim.")
                            speak(">2) Bunu yapmak istediğimden emin değilim.")
                            choice = input(">")
                            if choice == "1":
                                terminal_cleaner()
                                speak("SüngerBot ile denizanaları toplarken çok eğlendiniz.")
                                time.sleep(0.5)
                                speak("Artık sana pek de sinirli değil gibi görünüyor.")
                                time.sleep(1.3)
                                show_display("SüngerBot")
                                speak("SüngerBot: Yardım ettiğin için teeşekkür ederim.")
                                speak("SüngerBot: Teşekkürüm olarak bu yengeç burgeri kabul et!")
                                time.sleep(1.3)
                                speak("Bir yengeç burger aldın!")
                                time.sleep(1.5)
                                sponge_bob_dialogue_done = True
                                break

                            if choice == "2":
                                terminal_cleaner()
                                show_display("SüngerBott")
                                speak("SüngerBot: Sanırım denizanalarını toplamak için Patrick'i uyandırmaya gideceğim.")
                                time.sleep(1.3)
                                sponge_bob_dialogue_done = True
                                break
                        elif answer == "Çıkış":
                            sponge_bob_dialogue_done = False
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

        # PATRİCK
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (
        18, 13) and not patrick_dialogue_done:
            speak(
                "**Bikini Kasabası'nın kumlu plajında dolaşırken bir horlama sesi duyuyorsun. \n Patrick bir kayanın altında uyuyor.")
            time.sleep(1.5)
            show_display("Patrickk")
            speak("Onu uyandıracak mısın?")
            time.sleep(1)
            speak(">1) Evet")
            speak(">2) Hayır")
            choice = input(">")
            if choice.isdigit():

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
                    show_display("Patrickk")
                    time.sleep(0.5)
                    speak("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
                    time.sleep(1.3)
                    patrick_dialogue_done = True
            else:
                print()
                speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")

            current_state = State.PLAYING
            continue

        # GARRY
        if current_state == State.DIALOGUE and episode == 2 and (x_pos, y_pos) == (5, 11) and not garry_dialogue_done:
            show_display("Garry")
            if len(garry_dialogues) == 4:
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
                            speak("Garry: meowwwwww!")
                            time.sleep(0.5)
                        elif answer == "Sen kimsin?":
                            time.sleep(0.5)
                            speak("Garry: miuuuuuu!")
                            time.sleep(0.5)
                        elif answer == "Bööö!!":
                            time.sleep(0.5)
                            print()
                            speak("'Garry kaçtı!'")
                            time.sleep(0.5)
                            terminal_cleaner()
                            current_state = State.PLAYING
                            garry_dialogue_done = True
                            break
                        elif answer == "Çıkış":
                            game_maps[episode]["map"][11][5] = "♦"
                            x_pos = 5
                            y_pos = 10
                            game_maps[episode]["map"][10][5] = "^"
                            current_state = State.PLAYING
                else:
                    print()
                    speak("*****Geçersiz giriş. Lütfen bir sayı seçin*****")
        else:
            current_state = State.PLAYING

        # DENİZANALARI
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (
        24, 6) and not jellyfish_dialogue_done:
            speak(
                "Bikini Kasabası'nın eşsiz ve renkli deniz yaşamının önemli bir parçası olan denizanaları burada toplanmış gibiler.")
            speak(
                "Tentaküllerinin parlak görünüşleri seni hemen etkilemesin, zehirli olabilirler onlara dokunmak istemezsin!")
            time.sleep(1)
            jellyfish_dialogue_done = True

        # SQUİDWORD
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (
        11, 9) and not squidward_dialogue_done:
            speak("Şerif Squidword'un evi burası olmalı.")
            time.sleep(1)
            squidward_dialogue_done = True

        # KRUSTY KRAB
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (
        5, 6) and not krusty_krab_dialogue_done:
            speak("Bay Yengecin ünlü restoranı 'Yengeç Restoran'ın önünde duruyorsun.")
            speak("Leziz yengeç burgerin kokusu seni iyice acıktırdı.")
            time.sleep(1)
            krusty_krab_dialogue_done = True

        # CHUM BUCKET
        if current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (
        12, 6) and not chem_bucket_dialogue_done:
            speak("Planktonun müşterisiz restoranı 'Yem Kovası'.")
            time.sleep(0.5)
            speak("Bay Yengeç ile Plankton yolları ayırdıktan sonra Plankton kendine bu restoranı açmış olmalı.")
            time.sleep(1)
            chem_bucket_dialogue_done = True

        # NEWSPAPER
        if (current_state == State.PLAYING and episode == 2 and (x_pos, y_pos) == (
        14, 0) and not newspaper_dialogue_done):
            print(characters["News2"]["display"])
            print()
            input("Çıkmak için Enter'a basın. ")
            newspaper_dialogue_done = True


# Bölüm 3'teki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_3():
    time.sleep(1)
    speak("Seçimlerin Bikini Kasabası ve halkının geleceğini şekillendirdi.")
    time.sleep(1)
    speak("İşte Yaşanan Alternatif Gelecek ve Sonuçları...")
    time.sleep(2)
    terminal_cleaner()

    # Plankton
    time.sleep(1)
    print(characters["Plankton"]["display"])
    entrance("                              Plankton                              ")
    speak("-Plankton çaldığı formülle burgerlerini fahiş fiyattan sattı")
    speak(" Kazandığı parayı da BMO ile kötü emelleri için kullandılar.")
    print()
    time.sleep(1)
    speak("-Halkı köleleştiren Planktonun zulmü yıllar boyu Bikini Kasabasında hüküm sürdü.")
    speak(" BMO ile Plankton bolluk ve refah içinde yıllarca yaşadılar.")
    time.sleep(2)
    terminal_cleaner()

    # Bay Yengeç Buraya
    print(characters["BayYengeç"]["display"])
    entrance("                            Bay Yengeç                            ")
    speak("-Formülü Planktona kaptıran Bay Yengeç işini ve tüm servetini kaybetti.")
    time.sleep(2)
    terminal_cleaner()

    # BMO
    print(characters["BMO"]["display"])
    entrance("                                BMO                                ")
    speak("-BMO sonunda çok sevdiği Planktonun tek dostu oldu.")
    speak("-İstediğini elde etti ve uzun yıllar beraber yaşadılar.")
    time.sleep(2)
    terminal_cleaner()

    # Sponge
    print(characters["SüngerBot"]["display"])
    entrance("                              SüngerBot                              ")
    speak("-Planktonun kazanmasıyla işinden olan SüngerBot dilenci olup sokaklara düştü.")
    time.sleep(2)
    terminal_cleaner()

    # Patrick
    print(characters["Patrick"]["display"])
    entrance("                              Patrick                              ")
    speak("-Arkadaşını çok seven Patrick, SüngerBot'un peşinden gitti ve o da dilenci oldu.")
    time.sleep(2)
    terminal_cleaner()

    # Garry
    print(characters["Garry"]["display"])
    entrance("                              Garry                              ")
    speak("-Garry'nin masraflarını karşılayamayan SüngerBot onu Squidworde emanet etti.")
    time.sleep(2)
    terminal_cleaner()

    # Brian
    print(characters["Brian"]["display"])
    entrance("                              Brian                              ")
    speak("-Brian Planktonun hüküm sürdüğü kasaba da fakirlikten eserlerini satmak zorunda kaldı.")
    time.sleep(1)
    print()
    speak(" 4 senedir üzerinde çalıştığı Madam Lisa Tablosunu 5 deniz kabuğuna aşağı kasabadan")
    speak(" Vatoz Henriye sattı.")
    print()
    time.sleep(2)
    terminal_cleaner()

    # MonaLisa
    print(characters["Monalisa"]["display"])
    speak("-Tablonun daha sonra bazı koleksiyonerler tarafından rağbet "
          "görmesiyle değeri 5 milyon deniz kabuğuna kadar çıktı.")
    time.sleep(2)
    terminal_cleaner()

    # Squid
    print(characters["Squidword"]["display"])
    entrance("                              Squidword                              ")
    speak("-İşini kaybeden Squidword civar kasabalardan Deniz Kabarcığı Kasabasına taşındı.")
    speak(" Garryi de yanında götürdü.")
    speak(" Orada da Şeriflik görevine devam etti ve başarılı oldu.")
    time.sleep(2)
    terminal_cleaner()

    # Son
    speak("Ve son...")
    time.sleep(3)


# Bölüm 4'teki diyalog geçişlerini yapar ve fonksiyonları çağırır
def episode_4():
    time.sleep(1)
    speak("Seçimlerin Bikini Kasabası ve halkının geleceğini şekillendirdi.")
    time.sleep(1)
    speak("İşte Yaşanan Alternatif Gelecek ve Sonuçları...")
    time.sleep(2)
    terminal_cleaner()

    time.sleep(1)
    print(characters["Plankton"]["display"])
    entrance("                              Plankton                              ")
    speak("-Plankton'un tüm planları açığa çıktı.")
    speak(" Formülü ele geçiremeyen Plankton ve BMO'nun Yem Kovası Restoranı iflas etti.")
    time.sleep(2)
    terminal_cleaner()

    # BMO
    print(characters["BMO"]["display"])
    entrance("                                BMO                                ")
    speak("-Halk tarafından kötü planları öğrenilen Plankton ve BMO Kaya Dibi'ne sürgün edildi.")
    time.sleep(2)
    terminal_cleaner()

    # Bay Yengeç Buraya
    print(characters["BayYengeç"]["display"])
    entrance("                            Bay Yengeç                            ")
    speak(
        "-İşlerini büyüten Bay Yengeç restoran zinciri kurdu ve diğer kasabalarda da faaliyet göstermeye başladı.")
    time.sleep(2)
    terminal_cleaner()

    # Sponge
    print(characters["SüngerBot"]["display"])
    entrance("                              SüngerBot                              ")
    speak("-İşini her zaman severek yapan SüngerBot Bay Yengeç tarafından ödüllendirildi.")
    speak(" Yılın çalışanı seçildi ve terfi aldı.")
    time.sleep(2)
    terminal_cleaner()

    # Patrick
    print(characters["Patrick"]["display"])
    entrance("                              Patrick                              ")
    speak("-Patrick eski aylak hayatına devam etti.")
    time.sleep(2)
    terminal_cleaner()

    # Garry
    print(characters["Garry"]["display"])
    entrance("                              Garry                              ")
    speak("-Sahibi SüngerBot ile sakin ve mutlu bir hayat sürdü.")
    speak(" meow")
    time.sleep(2)
    terminal_cleaner()

    # Brian
    print(characters["Brian"]["display"])
    entrance("                              Brian                              ")
    speak(
        "-Sanatı sonunda değer görmeye başlayan Brian, Madam Lisa tablosunu binlerce deniz incisi teklifi gelmesine rağmen satmadı.")
    time.sleep(1)
    print()
    speak(" Çeşitli yerlerde resim sergileri düzenleyen Brian'ın ünü tüm su altı dünyasına yayıldı.")
    time.sleep(2)
    terminal_cleaner()

    # Squidword
    print(characters["Squidword"]["display"])
    entrance("                              Squidword                              ")
    speak("-Squidword kasabanın güvenliğini arttırmak için Plankton’un planlarının engellenmesinden ilham alarak")
    speak(" Deniz Güvenlik Birimi'ni kurarak kasaba güvenliğini arttırdı.")
    time.sleep(2)
    terminal_cleaner()

    # Son
    speak("Ve son...")
    time.sleep(3)


main()
