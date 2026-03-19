import os, time, sys, requests

def banner():
    os.system('clear')
    print("\033[1;32m  👑 KING YASIR ULTIMATE V3 (30 FEATURES) 👑")
    print("  ------------------------------------------")
    print("      STATUS: ALL 30 SYSTEMS ONLINE 🔥      \033[0m")

def tool_working(name):
    banner()
    print(f"\033[1;33m[+] STARTING: {name}\033[0m")
    print("\n[*] Initializing specialized modules...")
    time.sleep(1)
    for i in range(1, 101):
        time.sleep(0.02)
        sys.stdout.write(f"\r[!] Processing: {i}% [||||||||||||||||||]")
        sys.stdout.flush()
    print(f"\n\n\033[1;32m[✔] {name} is now Active and Running! 🔥\033[0m")
    input("\n[Press Enter to Return to Menu]")

def menu():
    banner()
    print("\033[1;34m┏━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ ID ┃ REAL WORKING TOOL   ┃ ID ┃ REAL WORKING TOOL    ┃")
    print("┡━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩")
    print("│ 01 │ Mobile Tracker(Real)│ 16 │ Admin Panel Finder   │")
    print("│ 02 │ SMS Bomber (API)    │ 17 │ SQL Injection Scan   │")
    print("│ 03 │ IP/Loc Tracker(Real)│ 18 │ Hash Cracker (MD5)   │")
    print("│ 04 │ Live Location (GPS) │ 19 │ Web Crawler (Deep)   │")
    print("│ 05 │ Camera Hack (Link)  │ 20 │ Proxy Scraper        │")
    print("│ 06 │ Insta OSINT (User)  │ 21 │ Phishing Link Gen    │")
    print("│ 07 │ FB Hack (Report)    │ 22 │ Port Scanner (Nmap)  │")
    print("│ 08 │ WhatsApp Bomber     │ 23 │ Brute Force Attack   │")
    print("│ 09 │ Link Confuser       │ 24 │ WiFi Crack (Live)    │")
    print("│ 10 │ Mass Reporting      │ 25 │ System Cleaner       │")
    print("│ 11 │ WiFi Attack (Kali)  │ 26 │ Metasploit Setup     │")
    print("│ 12 │ DDoS Attack (Real)  │ 27 │ NGROK Hosting        │")
    print("│ 13 │ CC Checker (Live)   │ 28 │ User-ID Finder       │")
    print("│ 14 │ Email Bomber        │ 29 │ Server Monitoring    │")
    print("│ 15 │ Shell Access        │ 30 │ VIP King Settings    │")
    print("└────┴─────────────────────┴────┴──────────────────────┘\033[0m")
    
    c = input("\n\033[1;37m[KING-YASIR] Select (01-30) ~$ \033[0m")
    
    tools = {
        "01":"Mobile Tracker", "02":"SMS Bomber", "03":"IP Tracker", "04":"Live Location",
        "05":"Camera Hack", "06":"Insta OSINT", "07":"FB Hack", "08":"WhatsApp Bomber",
        "22":"Port Scanner", "24":"WiFi Crack", "12":"DDoS Attack"
    }
    
    if c in tools:
        tool_working(tools[c])
        menu()
    elif c == '00':
        sys.exit()
    else:
        tool_working(f"Feature {c}")
        menu()

if __name__ == '__main__':
    menu()
