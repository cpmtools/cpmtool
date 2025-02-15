import os
import sys
import time
import random
import json
import requests
from colorama import Fore, Style, init
import sys
import time
import itertools
#UI functions
def print_colored_text(text, hex_color):
    # Hex rangni RGB ga aylantirish
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # ANSI kodini yaratish
    ansi_code = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(ansi_code)
def success():
    print_colored_text("Tayyor","#FFFFFF")
def loader():
    animation = [Fore.BLACK+"0%  ━━━━━━━━━━━━━━━━━━━━" ,
                 Fore.LIGHTWHITE_EX+"10%  ━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"20%  ━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"30%  ━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"50%  ━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"60%  ━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━",
                 Fore.LIGHTWHITE_EX+"70%  ━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━",
                 Fore.LIGHTWHITE_EX+"80%  ━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━",
                 Fore.LIGHTWHITE_EX+"90%  ━━━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━",
                 Fore.LIGHTWHITE_EX+"100%  ━━━━━━━━━━━━━━━━━━━━",
                 ]
    for i in range(len(animation)):
        sys.stdout.write("\r" + Fore.GREEN + animation[i] + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
#Service functions 
def login(email, password):
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('idToken', None)
    return None  
#add_money
def add_money(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "money": 50000000,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#addcoin
def add_coin(request):
    coin = input(Fore.WHITE+" ➤ "+Fore.RED+"COIN"+Fore.WHITE+" MIQDORINI KIRITING: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": coin,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#get_king
def get_king(request):
    url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"
    url_2 = "https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating4_AppI"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    }
    dd = {
    "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"treasure\" : 2000000000,\"cars\" : 2000000000,\"race_win\" : 999,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"}
    data = {
        "data":"{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\": 2000000000,\"gifts\": 2000000000,\"treasure\": 2000000000,\"cars\": 137,\"race_win\" : 999,\"levels\": 82,\"drift\": 2000000000,\"run\": 2000000000,\"police\": 2000000000,\"block_post\": 2000000000,\"real_estate\": 12,\"fuel\": 2000000000,\"car_trade\": 2000000000,\"car_exchange\": 2000000000,\"burnt_tire\": 2000000000,\"car_fix\": 2000000000,\"car_wash\": 2000000000,\"offroad\": 2000000000,\"passanger_distance\": 2000000000,\"reactions\": 2000000000,\"drift_max\": 2000000000,\"texi\": 2000000000,\"delivery\": 2000000000,\"cargo\": 2000000000,\"push_ups\": 2000000000,\"slicer_cut\":1,\"car_collided\":2000,\"new_type\": 2000}"
    }
    clear_screen()
    a = requests.post(url, headers=headers, json=dd)
    return a.text
#custom_id
def custom_id(request):
    custom_input = input(Fore.WHITE+" ➤  YANGI"+Fore.RED+" ID "+Fore.WHITE+"KIRITING: ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "LocalID": custom_input,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
def get_all(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "content-length": "4686",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    } 
    xx = {"data":"{\"allData\":\"ios7\",\"boughtFsos\":[-1],\"boughtPoliceLights\":[0,9,1,1,3,0,2,1,0,3,1,0],\"boughtPoliceSirens\":[1],\"FriendsID\":[],\"LevelsDoneTime\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"floats\":[169.0,188.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"integers\":[1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,15,0,0,0,0,0,0],\"fcar\":[0],\"favouriteWheels\":[],\"personEquipmentsMale.Gender\":1,\"personEquipmentsMale.bag\":[],\"personEquipmentsMale.beard\":[],\"personEquipmentsMale.cap\":[3,4,5],\"personEquipmentsMale.face\":[0],\"personEquipmentsMale.glasses\":[],\"personEquipmentsMale.gloves\":[],\"personEquipmentsMale.hair\":[3],\"personEquipmentsMale.mask\":[],\"personEquipmentsMale.pants\":[3],\"personEquipmentsMale.shoes\":[0],\"personEquipmentsMale.top\":[0],\"personEquipmentsMale.SelectedEquipments\":[-1,0,-1,3,-1,0,-1,-1,3,0,-1],\"personEquipmentsFemale.Gender\":1,\"personEquipmentsFemale.bag\":[],\"personEquipmentsFemale.beard\":[],\"personEquipmentsFemale.cap\":[],\"personEquipmentsFemale.face\":[],\"personEquipmentsFemale.glasses\":[],\"personEquipmentsFemale.gloves\":[],\"personEquipmentsFemale.hair\":[],\"personEquipmentsFemale.mask\":[],\"personEquipmentsFemale.pants\":[],\"personEquipmentsFemale.shoes\":[],\"personEquipmentsFemale.top\":[],\"personEquipmentsFemale.SelectedEquipments\":[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],\"platesData\":{\"allPlates\":[{\"plateId\":1,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":2,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":3,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":4,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":5,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]},{\"plateId\":6,\"frontCarId\":-1,\"rearCarId\":-1,\"vinyls\":[]}]},\"carIDnStatus\":{\"carGeneratedIDs\":[\"PP046001_0EM520\",\"PP046001_1HZ434\",\"PP046001_2AI601\",\"PP046001_3XE666\",\"PP046001_4UE186\",\"PP046001_5PT234\",\"PP046001_6YX838\",\"PP046001_7LX480\",\"PP046001_8DS116\",\"PP046001_9NX832\",\"PP046001_10WK456\",\"PP046001_11TD028\",\"PP046001_12ND577\",\"PP046001_13DV244\",\"PP046001_14AG741\",\"PP046001_15BS263\",\"\",\"PP046001_17LK238\",\"PP046001_18JF051\",\"PP046001_19KX803\",\"PP046001_20GZ586\",\"PP046001_21UF017\",\"PP046001_22YP130\",\"PP046001_23FN836\",\"PP046001_24HC607\",\"\",\"\",\"PP046001_27RX784\",\"PP046001_28KK142\",\"PP046001_29WE007\",\"PP046001_30PD713\",\"PP046001_31RE817\",\"PP046001_32YY233\",\"\",\"\",\"PP046001_35VU702\",\"\",\"PP046001_37GL131\",\"\",\"PP046001_39TJ356\",\"PP046001_40FW772\",\"PP046001_41EU384\",\"PP046001_42WG860\",\"PP046001_43BS150\",\"PP046001_44WH827\",\"PP046001_45FH475\",\"\",\"PP046001_47UJ768\",\"PP046001_48TV341\",\"PP046001_49JN530\",\"\",\"PP046001_51QD838\",\"\",\"PP046001_53YV825\",\"PP046001_54GJ675\",\"PP046001_55ML516\",\"PP046001_56SJ686\",\"PP046001_57LH242\",\"PP046001_58MP057\",\"PP046001_59AZ262\",\"PP046001_60JU068\",\"PP046001_61SD005\",\"PP046001_62PN525\",\"\",\"\",\"PP046001_65TK146\",\"PP046001_66QD778\",\"\",\"\",\"\",\"PP046001_70ZC458\",\"\",\"\",\"\",\"PP046001_74AX427\",\"\",\"PP046001_76QU426\",\"PP046001_77YK376\",\"\",\"\",\"\",\"PP046001_81GH646\",\"PP046001_82IE441\",\"\",\"\",\"PP046001_85WP652\",\"PP046001_86YN631\",\"PP046001_87CN364\",\"PP046001_88UP157\",\"PP046001_89ZN352\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"_99CE612\",\"PP046001_100ZW228\",\"PP046001_101IA561\",\"PP046001_102UU717\",\"PP046001_103PY155\",\"PP046001_104IX462\",\"PP046001_105MM263\",\"PP046001_106XQ521\",\"PP046001_107AL041\",\"PP046001_108CS818\",\"PP046001_109SP418\",\"PP046001_110UZ317\",\"PP046001_111EI323\",\"PP046001_112UW055\",\"PP046001_113RE516\",\"PP046001_114IU002\",\"PP046001_115RY424\",\"PP046001_116TC480\",\"PP046001_117BK850\",\"PP046001_118LQ005\",\"\",\"PP046001_120BL584\",\"PP046001_121AC887\",\"\",\"PP046001_123LQ316\",\"PP046001_124ND278\",\"PP046001_125TF635\",\"PP046001_126JW025\",\"PP046001_127DT758\",\"PP046001_128FJ077\",\"PP046001_129HK434\",\"PP046001_130XW543\",\"PP046001_131KV244\",\"PP046001_132BD828\",\"PP046001_133HL267\",\"PP046001_134MX336\",\"PP046001_135SE266\",\"PP046001_136PL387\",\"PP046001_137II563\",\"PP046001_138AV428\",\"PP046001_139YP064\",\"PP046001_140EI273\",\"PP046001_141ZW243\",\"PP046001_142MF631\",\"PP046001_143GZ785\",\"PP046001_144XG274\",\"PP046001_145PS766\",\"PP046001_146VP038\",\"PP046001_147XW868\",\"PP046001_148TS261\",\"PP046001_149CC143\",\"PP046001_150LH203\",\"PP046001_151EA023\",\"PP046001_152RE265\",\"PP046001_153WC743\",\"PP046001_154SM847\",\"PP046001_155XR248\",\"PP046001_156CP055\",\"PP046001_157II684\",\"PP046001_158PH630\",\"PP046001_159WR786\",\"PP046001_160TN826\",\"PP046001_161ZB761\",\"PP046001_162AN531\",\"PP046001_163AV585\",\"PP046001_164LX861\",\"PP046001_165YL448\",\"PP046001_166MT276\",\"\",\"PP046001_168IP887\",\"PP046001_169IQ177\",\"PP046001_170EV155\",\"PP046001_171GP661\",\"PP046001_172WP866\",\"\",\"\",\"PP046001_175ZA568\",\"PP046001_176EQ523\",\"PP046001_177VG000\",\"PP046001_178YP367\",\"PP046001_179WS654\",\"PP046001_180GQ561\",\"PP046001_181IH643\",\"PP046001_182FH072\",\"PP046001_183TE720\",\"PP046001_184QM888\",\"PP046001_185JI650\",\"PP046001_186DZ572\",\"PP046001_187QN161\",\"PP046001_188SJ663\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"],\"carStatus\":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},\"flags\":{},\"animations\":[1,2,3,4],\"wheels\":[73,74,79,88,84,87,97,98,101]}"}

    a = requests.post(url, headers=headers, json=xx)
    return a
#Main functions
# Здесь может быть основной код скрипта
while True:
 clear_screen()
 print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
 print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
 print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
 print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
 print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
 print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
 print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
 print_colored_text("│                    CPM AKKAUNTGA KIRISH                     │","#787672")
 print_colored_text("├─────────────────────────────────────────────────────────────┤","#9e9e9e")
 print_colored_text("│              EMAIL VA PAROLNI TO'G'RI KIRITING!             │","#787672")
 print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252"),
 email=input(Fore.LIGHTWHITE_EX+"Email │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#525252")
 password=input(Fore.LIGHTWHITE_EX+"Parol │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#dddddd")
 token = login(email, password)
 time.sleep(2)
 clear_screen()
 print(Fore.LIGHTWHITE_EX+"Akkauntga kirilmoqda! \n")
 loader()
 if not token:
        clear_screen()
        print(Fore.RED+"Kirish xatosi!"+Fore.LIGHTWHITE_EX+"\nQaytadan urinib ko'ring.")
        time.sleep(1.5)
        clear_screen()
 else:
        print(Fore.GREEN+"Akkauntga muvaffaqiyatli kirdingiz! ✅")
        break
clear_screen()
#Service_banner
while True:
    print_colored_text(" ██████╗██████╗ ███╗   ███╗ ████████╗ ██████╗  ██████╗ ██╗", "#ffffff") #1
    print_colored_text("██╔════╝██╔══██╗████╗ ████║ ╚══██╔══╝██╔═══██╗██╔═══██╗██║", "#d9d7d2") #2
    print_colored_text("██║     ██████╔╝██╔████╔██║    ██║   ██║   ██║██║   ██║██║", "#c2c1be") #3
    print_colored_text("██║     ██╔═══╝ ██║╚██╔╝██║    ██║   ██║   ██║██║   ██║██║", "#9e9e9d") #4
    print_colored_text("╚██████╗██║     ██║ ╚═╝ ██║    ██║   ╚██████╔╝╚██████╔╝███████╗", "#787672") #5
    print_colored_text(" ╚═════╝╚═╝     ╚═╝     ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝", "#525252") #6
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#525252")
    print_colored_text("│                          CPM SERVICES                       │","#787672")
    print_colored_text("├──────────────────────────────┬┬─────────────────────────────┤","#9e9e9e")
    print_colored_text("│ [1] ➤ PUL SOLISH            ││   [2] ➤ COIN SOLISH           │","#c2c2be")
    print_colored_text("│ [3] ➤ KING RANK              ││  [4] ➤ ID O'ZGARTIRISH      │","#c2c2be")
    print_colored_text("│ [5] ➤ $ NARSANI OCHISH       ││  [0] ➤ CHIQISH              │","#9e9e9d")
    print_colored_text("├──────────────────────────────┴┴─────────────────────────────┤","#9e9e9e")
    print_colored_text("│                    MASHINALAR OCHILMAYDI!                   │","#787672")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#525252")
    command=input(Fore.WHITE+"[✙]"+Fore.LIGHTBLACK_EX+" ➤  TANLOVINGIZ: ")
    if command.lower() == "0":
        print(Fore.RED + "Dastur tugatildi❗")
        clear_screen()
        break
    if command.lower() == "1":
        add_money(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "2":
        add_coin(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "3":
        get_king(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "4":
        custom_id(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "5":
        get_all(token)
        success()
        time.sleep(2)
        clear_screen()
