# 📺 YouTube Video Manager (CLI Project)

## 📌 Project Description

YouTube Video Manager is a simple Command Line Interface (CLI) application built using Python.

This project allows users to manage a list of YouTube videos by storing data in a local JSON file (`youtube.txt`).

Users can:
- Add videos
- View all videos
- Update video details
- Search videos
- Delete videos

This is my first Python project, built to practice:
- Functions
- File handling
- JSON handling
- Lists & Dictionaries
- Match-case statements
- Basic CLI application logic

---

## 🚀 Features

- 📃 List all saved videos
- ➕ Add new video
- ✏️ Update existing video
- 🔍 Search video by ID
- ❌ Delete video by ID
- 💾 Persistent storage using JSON file

---

## 🛠 Technologies Used

- Python 3
- JSON module
- File handling
- CLI (Command Line Interface)

No external libraries required.

---

## 📂 Project Structure

```text
YouTubeManager/
│
├── youtube.py        # Main Python application
├── youtube.txt       # Stores video data (auto-created)
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Make sure Python is installed

Check version:

```
python --version
```

---

### 2️⃣ Run the program

```
python youtube.py
```

---

## 🖥 Program Menu

When you run the program, you will see:

```
Youtube Manager

1. List of videos.
2. Add video.
3. Update previous video.
4. Search a video using ID of video.
5. Delete a video using ID of video.
6. Exit
```

---

## 📊 How It Works

- Video data is stored in `youtube.txt`
- Data is saved in JSON format
- Each video contains:
  - name
  - time (duration)
  - link

Example stored data:

```json
[
  {
    "name": "Python Tutorial",
    "time": "10:45",
    "link": "https://youtube.com/example"
  }
]
```

---

## 🧠 Concepts Learned

Through this project, I learned:

- Working with JSON files
- Reading and writing files in Python
- Using functions properly
- Handling user input
- List manipulation
- Using `match-case` in Python
- Building a loop-based CLI system

---

## ⚠️ Limitations

- No error handling for invalid inputs
- No GUI (CLI based only)
- No database integration
- Data stored locally only

---

## 🎯 Future Improvements

- Add input validation
- Add exception handling
- Add GUI using Tkinter
- Convert to web app using Flask
- Store data in SQLite database

---

## 👨‍💻 Author

Ayush Baghel  
First Python Project 🚀  
Learning phase – Building fundamentals strong.
