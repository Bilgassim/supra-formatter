#!/usr/bin/env python3
import argparse
import sys
import os
from core.converter import SupraConverter

BANNER = r"""
\033[36m
  ____  _   _ ____  ____      _    
 / ___|| | | |  _ \|  _ \    / \   
 \___ \| | | | |_) | |_) |  / _ \  
  ___) | |_| |  __/|  _ <  / ___ \ 
 |____/ \___/|_|   |_| \_\/_/   \_\
\033[0m
 \033[90m[+] version 1.1.0 | Interactive Mega-Formatter\033[0m
 \033[90m[+] author: Bilgassim | Bilgassim/supra-formatter\033[0m
"""

def interactive_mode():
    """Lance le menu interactif pour guider l'utilisateur."""
    print("\n\033[33m--- Mode Interactif ---\033[0m")
    
    # 1. Demander le fichier d'entrée
    input_file = input("[?] Chemin du fichier source (ex: list.txt) : ").strip()
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
    
    # Si aucun argument n'est passé, on lance le mode interactif
    if len(sys.argv) == 1:
        interactive_mode()
        return

    # Sinon, on utilise le mode commande classique (pour les scripts/automation)
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
