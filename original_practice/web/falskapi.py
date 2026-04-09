import time
import sys
import random
import pyotp
from colorama import Fore, Style, init

init(autoreset=True)

# Pre-set secret key for the prank
SECRET_KEY = "HL5A5CTWS7PEDEJ7AEVJURGBRE"

def print_slow(text, delay=0.03, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def simulate_progress(message, duration, color=Fore.CYAN):
    print_slow(f"\n{color}{message}...", delay=0.05)
    for i in range(duration):
        progress = int((i + 1) / duration * 100)
        bar = '#' * int((i + 1) / duration * 40)
        remaining = '-' * (40 - len(bar))
        sys.stdout.write(f"{color}[{bar}{remaining}] {progress}%\r{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")

def generate_log_line(prefix):
    actions = [
        "Attempting handshake with server",
        "Establishing encrypted tunnel",
        "Authenticating session token",
        "Bypassing firewall ruleset",
        "Injecting SQL payload",
        "Extracting user data tables",
        "Decrypting sensitive information",
        "Analyzing network traffic",
        "Compiling exploit modules",
        "Executing remote code",
        "Accessing root directory",
        "Scanning for vulnerabilities",
        "Initializing data transfer",
        "Verifying checksums",
        "Cleaning up traces"
    ]
    status = random.choice([f"{Fore.GREEN}SUCCESS{Style.RESET_ALL}", f"{Fore.YELLOW}WARNING{Style.RESET_ALL}", f"{Fore.RED}FAILURE{Style.RESET_ALL}"])
    return f"{Fore.WHITE}[{prefix}] {random.choice(actions)}... {status}{Style.RESET_ALL}"

def main():
    # ASCII Art Header
    print_slow(f"{Fore.RED}███████╗ ██████╗  ██████╗ ██╗      ██████╗  ██████╗ ██╗  ██╗{Style.RESET_ALL}", delay=0.005)
    print_slow(f"{Fore.RED}██╔════╝██╔═══██╗██╔════╝ ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝{Style.RESET_ALL}", delay=0.005)
    print_slow(f"{Fore.RED}██████╗ ██║   ██║██║  ███╗██║     ██║   ██║██║   ██║█████╔╝ {Style.RESET_ALL}", delay=0.005)
    print_slow(f"{Fore.RED}██╔══╝  ██║   ██║██║   ██║██║     ██║   ██║██║   ██║██╔══██╗{Style.RESET_ALL}", delay=0.005)
    print_slow(f"{Fore.RED}██║     ╚██████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║  ██╗{Style.RESET_ALL}", delay=0.005)
    print_slow(f"{Fore.RED}╚═╝      ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝{Style.RESET_ALL}\n", delay=0.005)

    print_slow(f"{Fore.CYAN}Initializing secure connection to Roblox servers...{Style.RESET_ALL}", delay=0.05)
    time.sleep(2)

    # Phase 1: Secret Key Fetching (1 Minute)
    print_slow(f"{Fore.YELLOW}Phase 1: Scanning Roblox Database for Secret Key...{Style.RESET_ALL}", delay=0.05)
    simulate_progress("Fetching Secret Key from DB", 60, color=Fore.YELLOW)
    
    print_slow(f"\n{Fore.GREEN}[!] SECRET KEY FOUND: {SECRET_KEY}{Style.RESET_ALL}", delay=0.05)
    print_slow(f"{Fore.GREEN}[!] MADE BY @diwas{Style.RESET_ALL}", delay=0.05)
    time.sleep(2)

    # Phase 2: Server Hacking (15 Seconds)
    print_slow(f"\n{Fore.MAGENTA}Phase 2: Bypassing Server Security with Secret Key...{Style.RESET_ALL}", delay=0.05)
    for i in range(15):
        print_slow(generate_log_line(f"HACK-{i+1:03d}"), delay=0.01)
        time.sleep(1)

    # Phase 3: OTP Generation
    print_slow(f"\n{Fore.CYAN}Phase 3: Generating Real-Time Bypass Code...{Style.RESET_ALL}", delay=0.05)
    time.sleep(3)

    totp = pyotp.TOTP(SECRET_KEY)
    current_code = totp.now()

    print_slow(f"\n{Fore.YELLOW}========================================{Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}  ROBLOX SERVER BYPASS GRANTED!         {Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}========================================{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}  FULL ACCESS KEY: {Fore.WHITE} {current_code} {Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}========================================{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}  CRACKED BY @diwas                     {Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}========================================{Style.RESET_ALL}\n")

    print_slow(f"{Fore.MAGENTA}Disclaimer: This tool is for educational and entertainment purposes only.{Style.RESET_ALL}", delay=0.03)
    print_slow(f"{Fore.BLUE}Developer Credits: @diwas{Style.RESET_ALL}", delay=0.03)

if __name__ == "__main__":
    main()
