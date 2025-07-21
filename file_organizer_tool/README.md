# 📁 File Organizer Tool

A Python utility that automatically organizes files in a directory by categorizing them based on their file types.

## 🌟 Key Features

- Organizes files into category-based folders
- Supports multiple file types and categories
- Handles duplicate filenames automatically
- Simple command-line interface
- No external dependencies required

## 📂 Supported Categories

- Images (.jpg, .png, .gif, etc.)
- Documents (.pdf, .doc, .txt, etc.)
- Audio (.mp3, .wav, .flac, etc.)
- Video (.mp4, .avi, .mkv, etc.)
- Archives (.zip, .rar, .7z, etc.)
- Code (.py, .java, .cpp, etc.)
- Executables (.exe, .msi, .bat, etc.)
- Others (unrecognized types)

## 🚀 Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Choose from the menu options:
   - Organize a directory (1)
   - View supported file types (2)
   - Exit (3)

3. When organizing, provide the full path to the directory you want to organize.

## 📁 Project Structure

```
file_organizer_tool/
├── main.py            # App entry point for user input
├── organizer.py       # Core logic for organizing files
├── file_types.py      # Configuration of file type categories
└── README.md          # Documentation
```

## ⚙️ How It Works

1. Creates category folders if they don't exist
2. Scans all files in the specified directory
3. Categorizes each file based on its extension
4. Moves files to appropriate category folders
5. Handles duplicate filenames by adding numerical suffixes

## 🔒 Safety Features

- Preserves original files (moves instead of copies)
- Handles duplicate filenames safely
- Skips directories during organization
- Validates directory existence

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies
- Works on Windows, macOS, and Linux
