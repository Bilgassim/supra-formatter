import re
import os

class SupraConverter:
    """
    Cœur de la logique de conversion pour Supra-Formatter.
    Gère la détection, le parsing et le formatage des identifiants SSH.
    """
    
    # Formats de sortie supportés
    FORMATS = {
        'standard': '{user}@{host} {password}',
        'csv': '{host},{user},{password}',
        'gossh': '{host} host={host} user={user} password={password}'
    }

    @staticmethod
    def detect_format(line):
        """
        Détecte automatiquement le format d'une ligne de texte.
        
        Args:
            line (str): La ligne brute à analyser.
            
        Returns:
            str: 'gossh', 'csv', 'standard' ou None si inconnu.
        """
        line = line.strip()
        if 'host=' in line and 'user=' in line:
            return 'gossh'
        if ',' in line and len(line.split(',')) >= 3:
            return 'csv'
        if '@' in line and ' ' in line:
            return 'standard'
        return None

    @staticmethod
    def parse_line(line, fmt):
        """
        Extrait les données (host, user, password) d'une ligne selon son format.
        
        Args:
            line (str): La ligne à parser.
            fmt (str): Le format identifié de la ligne.
            
        Returns:
            dict: Un dictionnaire contenant 'host', 'user' et 'password' ou None.
        """
        line = line.strip()
        try:
            if fmt == 'gossh':
                # Extraction par Regex pour GoSSH
                host = re.search(r'host=([^\s]+)', line).group(1)
                user = re.search(r'user=([^\s]+)', line).group(1)
                password = re.search(r'password=([^\s]+)', line).group(1)
                return {'host': host, 'user': user, 'password': password}
            
            if fmt == 'csv':
                # Split simple pour CSV
                parts = line.split(',')
                return {'host': parts[0], 'user': parts[1], 'password': parts[2]}
            
            if fmt == 'standard':
                # Extraction pour le format user@ip password
                parts = line.split()
                creds = parts[0]
                password = parts[1]
                user, host = creds.split('@')
                return {'host': host, 'user': user, 'password': password}
        except (AttributeError, ValueError, IndexError):
            # Erreur de parsing sur cette ligne spécifique
            return None
        return None

    def convert(self, input_file, output_file, target_format):
        """
        Lit un fichier, détecte le format de chaque ligne et écrit le résultat
        dans le format cible.
        
        Args:
            input_file (str): Chemin du fichier source.
            output_file (str): Chemin du fichier de destination.
            target_format (str): Format souhaité ('standard', 'csv', 'gossh').
            
        Returns:
            int: Le nombre de lignes converties avec succès.
        """
        if target_format not in self.FORMATS:
            raise ValueError(f"Format cible non supporté: {target_format}")

        # Création récursive du dossier parent si nécessaire
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        count = 0
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if not line.strip(): continue
                
                detected = self.detect_format(line)
                if not detected:
                    continue
                
                data = self.parse_line(line, detected)
                if data:
                    formatted = self.FORMATS[target_format].format(**data)
                    outfile.write(formatted + '\n')
                    count += 1
        return count
