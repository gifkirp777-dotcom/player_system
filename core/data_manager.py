import json
import os

DATA_FILE = "player_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
    return {
        "level":"Рекрут",
        "rank":"E",
        "stats":{
            "Сила тела":0,
            "Интеллект":0,
            "Социум":0,
            "Сила духа":0,
            "Харизма":0,
            "Финансы":0,
            "Власть":0
        },
        "background_charisma":0.0,
        "finance_experience":0.0,
        "logs":[]
    }

def save_data(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data,f)