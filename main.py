#!/usr/bin/env python3
import argparse
import sys
import os
from core.converter import SupraConverter

def main():
    parser = argparse.ArgumentParser(
        description="Supra-Formatter: L'outil ultime de conversion de listes SSH."
    )
    parser.add_argument("input", help="Fichier d'entrée à convertir")
    parser.add_argument("-o", "--output", help="Fichier de sortie (par défaut: output.txt)", default="output.txt")
    parser.add_argument(
        "-f", "--format", 
        choices=['standard', 'csv', 'gossh'], 
        required=True,
        help="Format cible : 'standard' (user@ip pass), 'csv' (ip,user,pass), ou 'gossh' (ip host=ip ...)"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Fichier '{args.input}' introuvable.")
        sys.exit(1)

    converter = SupraConverter()
    try:
        print(f"[*] Conversion de '{args.input}' vers le format '{args.format}'...")
        count = converter.convert(args.input, args.output, args.format)
        print(f"[+] Terminé ! {count} lignes converties avec succès dans '{args.output}'.")
    except Exception as e:
        print(f"[-] Une erreur est survenue : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
