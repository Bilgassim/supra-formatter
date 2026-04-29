import re
import os

class SupraConverter:
    """Cœur de la logique de conversion pour Supra-Formatter."""
    
    FORMATS = {
        'standard': '{user}@{host} {password}',
        'csv': '{host},{user},{password}',
        'gossh': '{host} host={host} user={user} password={password}'
    }

    @staticmethod
    def detect_format(line):
        """Détecte le format d'une ligne donnée."""
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
        """Extrait host, user, password selon le format."""
        line = line.strip()
        try:
            if fmt == 'gossh':
                host = re.search(r'host=([^\s]+)', line).group(1)
                user = re.search(r'user=([^\s]+)', line).group(1)
                password = re.search(r'password=([^\s]+)', line).group(1)
                return {'host': host, 'user': user, 'password': password}
            
            if fmt == 'csv':
                parts = line.split(',')
                return {'host': parts[0], 'user': parts[1], 'password': parts[2]}
            
            if fmt == 'standard':
                parts = line.split()
                creds = parts[0]
                password = parts[1]
                user, host = creds.split('@')
                return {'host': host, 'user': user, 'password': password}
        except Exception:
            return None
        return None

    def convert(self, input_file, output_file, target_format):
        """Convertit le fichier d'entrée vers le format cible."""
        if target_format not in self.FORMATS:
            raise ValueError(f"Format cible non supporté: {target_format}")

        # Création automatique du dossier de destination s'il n'existe pas
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        count = 0
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
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
