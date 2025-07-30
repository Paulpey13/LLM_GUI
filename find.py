import os
from pathlib import Path

# Répertoire à explorer
base_path = Path('.').resolve()

# Récupérer tous les fichiers, y compris les cachés
files_with_mtime = []

for path in base_path.rglob('*'):
    if path.is_file():
        try:
            mtime = path.stat().st_mtime
            files_with_mtime.append((path, mtime))
        except (PermissionError, FileNotFoundError):
            continue  # ignore les fichiers inaccessibles

# Tri par date de modification (plus récent d'abord)
files_sorted = sorted(files_with_mtime, key=lambda x: x[1], reverse=True)

# Écriture dans un .txt
with open('fichiers_modifies_ordre.txt', 'w', encoding='utf-8') as f:
    for file, _ in files_sorted:
        f.write(f"{file}\n")
