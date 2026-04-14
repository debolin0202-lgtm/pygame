#  Pygame Game Project

This is a simple game project built using **Python** and **Pygame**.

---

##  Requirements

* Python **3.12**
* pip (Python package manager)

---

##  Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```bash
.venv\Scripts\activate
```

If activation is blocked, run:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

### 4. Install dependencies

```bash
pip install pygame
```

---

##  Run the Project

```bash
python main.py
```

---

##  Project Structure

```
.
├── main.py        # Main game script
├── font.ttf       # Font file
├── 玩家.ico       # Game icon
├── 圖片/          # Image assets
└── .venv/         # Virtual environment 
```

---

##  Notes

* Make sure you are using **Python 3.12**
* The `.venv` folder should NOT be uploaded to GitHub

---

##  Features

- Displays a game window using Pygame
- Renders a player sprite on the screen
- Moves the sprite automatically across the screen
- Supports closing the game window properly


