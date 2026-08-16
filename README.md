#  CLI Code Snippet Vault

A lightweight, pure-Python command-line tool to safely store, manage, and retrieve your most-used code snippets, database commands, and scripts directly from your terminal.

## 🚀 Features
* **Zero Dependencies:** Built entirely with standard Python libraries.
* **Local Storage:** Everything is saved locally in a clean `snippets.json` file.
* **Fast Retrieval:** Search and pull your code instantly without leaving the command line.

## 💻 Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/snippet-vault-cli.git
   cd snippet-vault-cli
   ```

2. **Add a snippet:**
   ```bash
   python vault.py add build-docker "docker build -t my-app ." -d "Builds the docker image"
   ```

3. **List all snippets:**
   ```bash
   python vault.py list
   ```

4. **Retrieve a snippet:**
   ```bash
   python vault.py get build-docker
   ```

5. **Delete a snippet:**
   ```bash
   python vault.py delete build-docker
   ```

## 🛠️ Built With
* Pure Python 3
* `argparse` and `json` standard libraries
