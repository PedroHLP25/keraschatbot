import os
import json

# Obter o caminho absoluto do diretório atual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Definir o caminho completo do arquivo intents.json
intents_file = os.path.join(dir_path, 'intents.json')

# Carregar o arquivo intents.json em um objeto JSON
with open(intents_file, 'r', encoding='utf-8') as f:
    intents = json.load(f)