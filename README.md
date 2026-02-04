# File & Folder Management App

A Python console application to **manage files and folders easily**.  
It provides a menu-based interface to create, edit, delete, copy, move, and search files and folders.

---

## Features
- ✅ Create, read, edit, delete, copy, and move files  
- ✅ Create, view, delete, copy, and move folders  
- ✅ Search files and folders by keyword  
- ✅ Logs all actions in `history.log`  
- ✅ User-friendly terminal interface  
- ✅ Supports multiple files/folders at once (comma-separated)  

---

## How to Run

1. Clone the repository or download the project:  

git clone https://github.com/YOUR_USERNAME/FileFolderManager.git
cd FileFolderManager


2. Run the program:  

    python file_folder_manager.py


or on Mac/Linux:  

    python3 file_folder_manager.py


3. When prompted:  

📁 Enter the main project folder (will be created if it doesn't exist):


- Enter a folder name (created in the same location as the script), e.g.:  
    MyFiles  

- Or a full folder path:  
Windows: C:\Users\UserName\Documents\MyFiles  
Mac/Linux: /Users/username/Documents/MyFiles  

- Press Enter. The program will show:  
✅ Working in main folder: /path/to/your/folder  

---

## Main Menu

=== FILE & FOLDER MANAGEMENT APP ===
1️⃣ Folder Operations
2️⃣ File Operations
3️⃣ Exit


- Type `1` for Folder Operations  
- Type `2` for File Operations  
- Type `3` to exit  

---

## Folder Operations (Option 1)

--- FOLDER OPERATIONS ---
1️⃣ Create folder
2️⃣ View all folders
3️⃣ Delete folder (comma-separated)
4️⃣ Copy folder
5️⃣ Move folder
6️⃣ Search folders
7️⃣ Back


- Create folder: Type folder name → creates it in main folder  
- View all folders: Lists all folders  
- Delete folder: Type names separated by commas → deletes them  
- Copy/Move folder: Type folder name and destination path  
- Search folders: Type keyword → lists matching folders  
- Back: Return to main menu  

---

## File Operations (Option 2)

--- FILE OPERATIONS ---
1️⃣ Create file
2️⃣ Read file
3️⃣ Edit file (comma-separated)
4️⃣ Delete file (comma-separated)
5️⃣ Copy file
6️⃣ Move file
7️⃣ Search files by content
8️⃣ View all files
9️⃣ Back


- Create file: Type filename → creates it  
- Read file: Type filename → shows content  
- Edit file: Type filenames (comma-separated) → append text  
- Delete file: Type filenames → removes them  
- Copy/Move file: Type filename and destination path  
- Search files: Type keyword → shows matching files  
- View all files: Lists all files in the folder  
- Back: Return to main menu  

---

## Exiting the Program

- From main menu, type `3` → program exits:  
👋 Exiting program...

---

## Notes

- All files/folders are managed inside the folder you choose at the start.  
- All actions are automatically logged in `history.log`.  
- You can manage multiple files/folders using comma-separated names.  
- Works on Windows, Mac, and Linux.  

---
