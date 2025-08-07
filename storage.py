import json
import os

HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_to_history(query):
    history = load_history()
    if not any(h["query"] == query for h in history):
        history.append({"query": query})
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f)



