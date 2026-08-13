import json
import os
import argparse

# The file where our snippets will be stored
VAULT_FILE = 'snippets.json'

def load_snippets():
    """Loads snippets from the JSON file. Returns an empty dict if the file is missing or empty."""
    if not os.path.exists(VAULT_FILE):
        return {}
    
    try:
        with open(VAULT_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If the file exists but is empty or corrupted, return a fresh dictionary
        return {}

def save_snippets(data):
    """Saves the dictionary of snippets back to the JSON file."""
    with open(VAULT_FILE, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # A quick local test to ensure our data layer works
    print("Initializing Snippet Vault Data Layer...")
    
    # Try loading (should load an empty dict initially)
    current_data = load_snippets()
    print(f"Currently storing {len(current_data)} snippets.")