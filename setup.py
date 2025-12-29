import os

folders = [
    'config',
    'models',
    'services',
    'data'  
]

files = {
    '__init__.py': ['config', 'models', 'services'],
    'settings.py': ['config'],
    'database.py': ['models'],
    'models.py': ['models'],
    'book_service.py': ['services'],
    'report_service.py': ['services'],
    'requirements.txt': ['.'],
    'main.py': ['.']
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder created: {folder}")

for file, locations in files.items():
    for location in locations:
        path = os.path.join(location, file) if location != '.' else file
        with open(path, 'w') as f:
            if file == '__init__.py':
                f.write('# Package initialization\n')
        print(f"File created: {path}")