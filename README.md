# 🚀 Tasks CLI — Minimalist Terminal Task Manager

Project URL: [https://github.com/jasurxayitmuradov/Task-Tracker-CLI](https://roadmap.sh/projects/task-tracker)

A fast and simple command-line task manager built for developers who live in the terminal.

* Add, update, delete tasks
* Mark tasks as done or in-progress
* Filter tasks by status
* Lightweight JSON storage
* Fully terminal-based workflow
* Installable with `pip`
* Built for speed and simplicity

---

## 📦 Installation

### Install from PyPI 

```bash
pip install x-tasks
```

### Or install locally (development mode)

```bash
git clone https://github.com/jasurxayitmuradov/Task-Tracker-CLI.git
cd Task-Tracker-CLI
pip install -e .
```

---

## 🧠 Usage

### Add a task

```bash
tasks add "Buy milk"
```

### List all tasks

```bash
tasks list
```

### List by status

```bash
tasks list done
tasks list todo
tasks list in-progress
```

### Update a task

```bash
tasks update 1 "Buy milk and eggs"
```

### Delete a task

```bash
tasks delete 1
```

### Mark task status

```bash
tasks mark-in-progress 1
tasks mark-done 1
```

---

## 📁 Storage

Tasks are stored locally in:

```
~/.tasks/tasks.json
```

This allows access from anywhere in the terminal.

---

## 🛠 Tech Stack

* Python 3.10+
* argparse (CLI parsing)
* JSON (storage)
* setuptools packaging

---

## 🎯 Purpose

This project was built to:

* Practice real-world Python CLI development
* Learn packaging and distribution with pip
* Build production-style project structure
* Improve backend engineering skills

---

## 👨‍💻 Author

Built by a developer who prefers terminal over GUI.
Focused on backend engineering, automation, and AI-powered systems.

---

## ⭐ Future Improvements

* Colored terminal output
* Task priorities
* Due dates & reminders
* Config file support
* Cloud sync (future)

---

## 🧾 License

MIT License — free to use, modify, and distribute.
