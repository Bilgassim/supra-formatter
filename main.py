#!/usr/bin/env python3
import argparse
import sys
import os
import re
from core.converter import SupraConverter

# Tentative d'import de readline pour l'auto-complétion (Linux/macOS)
try:
    import readline
    readline.parse_and_bind("tab: complete")
    # Configuration pour compléter les noms de fichiers
    readline.set_completer_delims(' \t\n=')
except ImportError:
    # Readline n'est pas disponible sur toutes les plateformes (ex: Windows sans extension)
    pass

# Style de la bannière : Art ASCII en raw string + Couleurs
BANNER_COLOR = "\033[36m"
BANNER_RESET = "\033[0m"
BANNER_ART = r"""
  ____  _   _ ____  ____      _    
 / ___|| | | |  _ \|  _ \    / \   
 \___ \| | | | |_) | |_) |  / _ \  
  ___) | |_| |  __/|  _ <  / ___ \ 
 |____/ \___/|_|   |_| \_\/_/   \_\
"""

INFO_TEXT = "\033[90m [+] version 1.2.0 | Advanced Interactive Mega-Formatter\n [+] author: Bilgassim | Bilgassim/supra-formatter\033[0m"

BANNER = BANNER_COLOR + BANNER_ART + BANNER_RESET + INFO_TEXT

def interactive_mode():
    """Lance le menu interactif pour guider l'utilisateur."""
    print("\n\033[33m--- Mode Interactif (Tab pour compléter les chemins) ---\033[0m")
    
    # 1. Demander le fichier d'entrée (avec support auto-completion)
    try:
        input_file = input("[?] Chemin du fichier source : ").strip()
    except EOFError:
        return

    if not os.path.exists(input_file):
        print(f"\033[31m[-] Erreur: Le fichier '{input_file}' n'existe pas.\033[0m")
        return

    # 2. Choisir le format de sortie
    print("\n[!] Choisissez le format de sortie souhaité :")
    print("  1. Standard (user@ip password)")
    print("  2. CSV      (ip,user,password)")
    print("  3. GoSSH    (ip host=ip user=user password=pass)")
    
    choice = input("\n[?] Votre choix (1-3) : ").strip()
    
    formats_map = {
        '1': 'standard',
        '2': 'csv',
        '3': 'gossh'
    }
    
    target_format = formats_map.get(choice)
    if not target_format:
        print("\033[31m[-] Erreur: Choix invalide.\033[0m")
        return

    # 3. Demander le fichier de sortie
    default_output = f"output_{target_format}.txt"
    output_file = input(f"[?] Nom du fichier de sortie (Défaut: {default_output}) : ").strip()
    if not output_file:
        output_file = default_output

    # 4. Exécuter la conversion
    run_conversion(input_file, output_file, target_format)

def run_conversion(input_file, output_file, target_format):
    """Logique commune de conversion."""
    converter = SupraConverter()
    try:
        print(f"\n[*] Conversion de '{input_file}' vers '{target_format}'...")
        count = converter.convert(input_file, output_file, target_format)
        print(f"\033[32m[+] Succès ! {count} lignes converties dans '{output_file}'.\033[0m")
    except Exception as e:
        print(f"\033[31m[-] Erreur lors de la conversion : {e}\033[0m")

def main():
    print(BANNER)
    
    if len(sys.argv) == 1:
        interactive_mode()
        return

    parser = argparse.ArgumentParser(
        description="Supra-Formatter: L'outil ultime de conversion de listes SSH."
    )
    parser.add_argument("input", help="Fichier d'entrée à convertir")
    parser.add_argument("-o", "--output", help="Fichier de sortie", default="output.txt")
    parser.add_argument(
        "-f", "--format", 
        choices=['standard', 'csv', 'gossh'], 
        help="Format cible : 'standard', 'csv', ou 'gossh'"
    )

    args = parser.parse_args()
    
    if not args.format:
        print("\033[31m[-] Erreur: Le flag -f est requis en mode commande.\033[0m")
        return

    if not os.path.exists(args.input):
        print(f"\033[31m[-] Error: Fichier '{args.input}' introuvable.\033[0m")
        sys.exit(1)

    run_conversion(args.input, args.output, args.format)

if __name__ == "__main__":
    main()
