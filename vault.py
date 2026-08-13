import json
import os
import argparse

VAULT_FILE = 'snippets.json'

def load_snippets():
    """Loads snippets from the JSON file."""
    if not os.path.exists(VAULT_FILE):
        return {}
    try:
        with open(VAULT_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_snippets(data):
    """Saves the dictionary of snippets back to the JSON file."""
    with open(VAULT_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_snippet(name, code, description=""):
    """Adds a new snippet to the vault."""
    data = load_snippets()
    data[name] = {
        "code": code,
        "description": description
    }
    save_snippets(data)
    print(f"✅ Snippet '{name}' saved successfully!")

def list_snippets():
    """Lists all available snippets."""
    data = load_snippets()
    if not data:
        print("📭 Your vault is empty.")
        return
    
    print("📚 Your Saved Snippets:")
    for name, details in data.items():
        desc = details.get('description', '')
        print(f"  - {name}" + (f" ({desc})" if desc else ""))

def get_snippet(name):
    """Retrieves and prints a specific snippet."""
    data = load_snippets()
    if name in data:
        print(f"\n--- {name} ---\n{data[name]['code']}\n")
    else:
        print(f"❌ Snippet '{name}' not found.")

def delete_snippet(name):
    """Deletes a snippet from the vault."""
    data = load_snippets()
    if name in data:
        del data[name]
        save_snippets(data)
        print(f"🗑️ Snippet '{name}' deleted successfully.")
    else:
        print(f"❌ Snippet '{name}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A local CLI vault for your code snippets.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command to add a snippet
    parser_add = subparsers.add_parser("add", help="Add a new snippet")
    parser_add.add_argument("name", type=str, help="A short, memorable name for the snippet")
    parser_add.add_argument("code", type=str, help="The actual code or command to save")
    parser_add.add_argument("-d", "--desc", type=str, default="", help="An optional description")

    # Command to list all snippets
    parser_list = subparsers.add_parser("list", help="List all saved snippets")

    # Command to get a snippet
    parser_get = subparsers.add_parser("get", help="Retrieve a snippet by name")
    parser_get.add_argument("name", type=str, help="The name of the snippet to retrieve")

    # Command to delete a snippet
    parser_delete = subparsers.add_parser("delete", help="Delete a snippet by name")
    parser_delete.add_argument("name", type=str, help="The name of the snippet to delete")

    args = parser.parse_args()

    # Route the command to the correct function
    if args.command == "add":
        add_snippet(args.name, args.code, args.desc)
    elif args.command == "list":
        list_snippets()
    elif args.command == "get":
        get_snippet(args.name)
    elif args.command == "delete":
        delete_snippet(args.name)
    else:
        parser.print_help()