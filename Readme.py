import sys
import time
import os

# --- Konfigurasi Warna (ANSI Escape Codes) ---
# Biar terminalnya warna-warni tanpa perlu install library tambahan
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- ASCII Art Payung (Sesuai Cerita) ---
UMBRELLA_ART = f"""
{Colors.CYAN}
      .-^-.
     /     \\      {Colors.WARNING}WARNING: DATA CORRUPTED{Colors.CYAN}
    |   |   |     {Colors.GREEN}System Integrity: 45%{Colors.CYAN}
   '---------'
        |
        |
      __|_{Colors.ENDC}
"""

def clear_screen():
    """Membersihkan layar terminal (support Windows & Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.04, color=Colors.GREEN):
    """Membuat efek mengetik satu per satu"""
    sys.stdout.write(color) # Set warna
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(Colors.ENDC) # Reset warna
    print() # Pindah baris

def loading_animation():
    """Efek loading sederhana"""
    print(f"{Colors.BLUE}[*] Establishing secure connection...", end="")
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f" {Colors.GREEN}Connected.{Colors.ENDC}\n")
    time.sleep(0.5)

def main():
    clear_screen()
    loading_animation()
    
    # Tampilkan Banner
    print(UMBRELLA_ART)
    time.sleep(1)

    # --- Bagian Cerita (Story) ---
    print(f"{Colors.HEADER}{Colors.BOLD}[ INCOMING MESSAGE FROM: CAMPUS ADMIN ]{Colors.ENDC}")
    print("-" * 50)
    
    story_lines = [
        "Sebuah kampus tampak asri...",
        "Dipenuhi dengan keindahan dari payung-payung warna warni.",
        "",
        "Namun, ada masalah...",
        f"{Colors.WARNING}Prana{Colors.GREEN}, seorang mahasiswa di kampus tersebut...",
        "Telah kehilangan datanya.",
        "",
        f"{Colors.CYAN}Bisakah kamu mencari data tersebut?{Colors.ENDC}"
    ]

    for line in story_lines:
        if line == "":
            print() # Baris kosong
            time.sleep(0.5)
        else:
            typing_effect(line)
            time.sleep(0.3) # Jeda antar baris

    print("-" * 50)
    print(f"\n{Colors.FAIL}[!] HINT:{Colors.ENDC} Jangan lupa cek 'payung' yang tersembunyi.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}[!] Connection Terminated.{Colors.ENDC}")
        sys.exit()