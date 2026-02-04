import os
import shutil

# --- Setup Project Folder ---
PROJECT_DIR = os.path.abspath(input("📁 Enter the main project folder (will be created if it doesn't exist): ").strip())
os.makedirs(PROJECT_DIR, exist_ok=True)
print(f"✅ Working in main folder: {PROJECT_DIR}")

# --- Logging Function ---
def log_action(action):
    try:
        with open(os.path.join(PROJECT_DIR, "history.log"), 'a') as log_file:
            log_file.write(action + "\n")
    except Exception as e:
        print(f"❌ Logging error: {e}")

# ================== FILE OPERATIONS ==================
def create_file(filename):
    file_path = os.path.join(PROJECT_DIR, filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure folder exists
    try:
        with open(file_path, 'x') as f:
            print(f"✅ File '{filename}' created!")
            log_action(f"Created file: {filename}")
    except FileExistsError:
        print(f"⚠️ File '{filename}' already exists.")
    except Exception as e:
        print(f"❌ Error: {e}")

def read_file(filename):
    file_path = os.path.join(PROJECT_DIR, filename)
    if not os.path.isfile(file_path):
        print(f"⚠️ '{filename}' is not a file or does not exist.")
        return
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            print(f"\n📖 Content of '{filename}':\n{'-'*30}\n{content}\n{'-'*30}")
    except Exception as e:
        print(f"❌ Error: {e}")

def edit_file(filenames):
    files = [f.strip() for f in filenames.split(',')]
    content_to_add = input("✍️ Enter text to add: ")
    for filename in files:
        file_path = os.path.join(PROJECT_DIR, filename)
        if not os.path.isfile(file_path):
            print(f"⚠️ File '{filename}' not found.")
            continue
        try:
            with open(file_path, 'a') as f:
                f.write(content_to_add + "\n")
            print(f"✅ Content added to '{filename}'.")
            log_action(f"Edited file: {filename}")
        except Exception as e:
            print(f"❌ Error: {e}")

def delete_file(filenames):
    files = [f.strip() for f in filenames.split(',')]
    for filename in files:
        file_path = os.path.join(PROJECT_DIR, filename)
        try:
            os.remove(file_path)
            print(f"🗑️ File '{filename}' deleted.")
            log_action(f"Deleted file: {filename}")
        except FileNotFoundError:
            print(f"⚠️ File '{filename}' not found.")
        except Exception as e:
            print(f"❌ Error: {e}")

def copy_file(filename, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copy(os.path.join(PROJECT_DIR, filename), dest_folder)
        print(f"📄 File '{filename}' copied to '{dest_folder}'.")
        log_action(f"Copied file '{filename}' to '{dest_folder}'")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def move_file(filename, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(os.path.join(PROJECT_DIR, filename), dest_folder)
        print(f"📂 File '{filename}' moved to '{dest_folder}'.")
        log_action(f"Moved file '{filename}' to '{dest_folder}'")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def search_files(keyword):
    matches = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        for fname in files:
            file_path = os.path.join(root, fname)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    if keyword.lower() in f.read().lower():
                        rel_path = os.path.relpath(file_path, PROJECT_DIR)
                        matches.append(rel_path)
            except Exception:
                continue
    if matches:
        print(f"🔎 Files containing '{keyword}':")
        for m in matches:
            print(f"   {m}")
    else:
        print(f"⚠️ No files found containing '{keyword}'.")

def view_all_files():
    print(f"\n📂 All files in '{PROJECT_DIR}' (including subfolders):")
    found = False
    for root, dirs, files in os.walk(PROJECT_DIR):
        for f in files:
            rel_path = os.path.relpath(os.path.join(root, f), PROJECT_DIR)
            print(f"   📄 {rel_path}")
            found = True
    if not found:
        print("   (No files found)")

# ================== FOLDER OPERATIONS ==================
def create_folder(folder_name):
    folder_path = os.path.join(PROJECT_DIR, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"✅ Folder '{folder_name}' created!")
        log_action(f"Created folder: {folder_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_all_folders():
    print(f"\n📂 All folders in '{PROJECT_DIR}':")
    found = False
    for root, dirs, files in os.walk(PROJECT_DIR):
        for d in dirs:
            rel_path = os.path.relpath(os.path.join(root, d), PROJECT_DIR)
            print(f"   📁 {rel_path}")
            found = True
    if not found:
        print("   (No folders found)")

def delete_folder(folders):
    folders = [f.strip() for f in folders.split(',')]
    for folder_name in folders:
        folder_path = os.path.join(PROJECT_DIR, folder_name)
        try:
            shutil.rmtree(folder_path)
            print(f"🗑️ Folder '{folder_name}' deleted.")
            log_action(f"Deleted folder: {folder_name}")
        except FileNotFoundError:
            print(f"⚠️ Folder '{folder_name}' not found.")
        except Exception as e:
            print(f"❌ Error: {e}")

def copy_folder(folder_name, dest_folder):
    src_path = os.path.join(PROJECT_DIR, folder_name)
    dest_path = os.path.abspath(dest_folder)
    try:
        shutil.copytree(src_path, os.path.join(dest_path, folder_name))
        print(f"📂 Folder '{folder_name}' copied to '{dest_path}'.")
        log_action(f"Copied folder '{folder_name}' to '{dest_path}'")
    except FileNotFoundError:
        print(f"⚠️ Folder '{folder_name}' not found.")
    except FileExistsError:
        print(f"⚠️ Destination already has folder '{folder_name}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def move_folder(folder_name, dest_folder):
    src_path = os.path.join(PROJECT_DIR, folder_name)
    dest_path = os.path.abspath(dest_folder)
    try:
        shutil.move(src_path, dest_path)
        print(f"📂 Folder '{folder_name}' moved to '{dest_path}'.")
        log_action(f"Moved folder '{folder_name}' to '{dest_path}'")
    except FileNotFoundError:
        print(f"⚠️ Folder '{folder_name}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def search_folders(keyword):
    matches = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        for d in dirs:
            if keyword.lower() in d.lower():
                rel_path = os.path.relpath(os.path.join(root, d), PROJECT_DIR)
                matches.append(rel_path)
    if matches:
        print(f"🔎 Folders containing '{keyword}':")
        for m in matches:
            print(f"   {m}")
    else:
        print(f"⚠️ No folders found containing '{keyword}'.")

# ================== MAIN MENU ==================
def main():
    while True:
        print("\n=== FILE & FOLDER MANAGEMENT APP ===")
        print("1️⃣  Folder Operations")
        print("2️⃣  File Operations")
        print("3️⃣  Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            while True:
                print("\n--- FOLDER OPERATIONS ---")
                print("1️⃣  Create folder")
                print("2️⃣  View all folders")
                print("3️⃣  Delete folder (comma-separated)")
                print("4️⃣  Copy folder")
                print("5️⃣  Move folder")
                print("6️⃣  Search folders")
                print("7️⃣  Back")
                sub = input("Enter choice (1-7): ").strip()

                if sub == '1':
                    create_folder(input("Folder name to create: ").strip())
                elif sub == '2':
                    view_all_folders()
                elif sub == '3':
                    delete_folder(input("Folder(s) to delete (comma-separated): ").strip())
                elif sub == '4':
                    copy_folder(input("Folder to copy: ").strip(), input("Destination folder path: ").strip())
                elif sub == '5':
                    move_folder(input("Folder to move: ").strip(), input("Destination folder path: ").strip())
                elif sub == '6':
                    search_folders(input("Keyword to search in folder names: ").strip())
                elif sub == '7':
                    break
                else:
                    print("❌ Invalid input.")

        elif choice == '2':
            while True:
                print("\n--- FILE OPERATIONS ---")
                print("1️⃣  Create file")
                print("2️⃣  Read file")
                print("3️⃣  Edit file (comma-separated)")
                print("4️⃣  Delete file (comma-separated)")
                print("5️⃣  Copy file")
                print("6️⃣  Move file")
                print("7️⃣  Search files by content")
                print("8️⃣  View all files")
                print("9️⃣  Back")
                sub = input("Enter choice (1-9): ").strip()

                if sub == '1':
                    create_file(input("File name to create (can include subfolders): ").strip())
                elif sub == '2':
                    read_file(input("File name to read (relative path from project folder): ").strip())
                elif sub == '3':
                    edit_file(input("File(s) to edit (comma-separated, relative paths allowed): ").strip())
                elif sub == '4':
                    delete_file(input("File(s) to delete (comma-separated, relative paths allowed): ").strip())
                elif sub == '5':
                    copy_file(input("File to copy: ").strip(), input("Destination folder path: ").strip())
                elif sub == '6':
                    move_file(input("File to move: ").strip(), input("Destination folder path: ").strip())
                elif sub == '7':
                    search_files(input("Keyword to search inside files: ").strip())
                elif sub == '8':
                    view_all_files()
                elif sub == '9':
                    break
                else:
                    print("❌ Invalid input.")

        elif choice == '3':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid input.")

if __name__ == "__main__":
    main()
