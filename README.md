# 📝 To-Do List App (Tkinter + JSON)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Storage](https://img.shields.io/badge/Storage-JSON-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Release](https://img.shields.io/badge/Release-v1.0.0-brightgreen)

A simple and user-friendly desktop To-Do List application built with Python's Tkinter GUI toolkit. It helps users manage daily tasks with the ability to add, delete, and mark them as complete. All data is saved locally using JSON — no external libraries, no database, no internet connection required.

> 🚀 **v1.0.0 is live!** Check out the [latest release](https://github.com/Dinesh8778/to-do-app/releases/tag/v1.0.0).

---

## 🚀 Features

- ✅ Add new tasks
- 📋 View and delete pending tasks
- ✅ Mark tasks as completed
- 📦 View completed tasks separately
- 💾 Auto-saving to JSON files
- 📁 Auto-creation of required backend folder and files on first run
- ❌ Prevents accidental window close without saving

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| GUI | Tkinter |
| Data Storage | JSON |

---

## 📁 Project Structure

```
to-do-app/
├── main.py
├── requirements.txt
├── README.md
└── backend/
    ├── task.json
    └── completed.json
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Dinesh8778/to-do-app.git
cd to-do-app
```

### 2. Run the app

```bash
python main.py
```

✅ On first run, the app automatically creates the `backend/` folder and required `.json` files if they don't already exist.

> No external dependencies are required — the app runs on Python's built-in `tkinter` and `json` modules.

---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Dinesh8778/to-do-app/issues).

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Dinesh Kumar S**
- GitHub: [@Dinesh8778](https://github.com/Dinesh8778)
- LinkedIn: [dinesh-kumar-s-it](https://linkedin.com/in/dinesh-kumar-s-it/)
- Portfolio: [dinesh8778.github.io/portfolio](https://dinesh8778.github.io/portfolio/)
