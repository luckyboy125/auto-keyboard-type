# Activity Automation Bot (`sticky.py`)

A lightweight Python script that simulates random keyboard and mouse activity.
It includes smart pause/resume based on real user input, desktop notifications,
and a global kill hotkey.

---

## Features

- **Random activity simulation**
  - `Alt + Tab` window switching
  - `Ctrl + Tab` tab switching
  - `PageUp` / `PageDown`
  - `Up` / `Down` arrow scrolling
  - Smooth random mouse movement across the screen
- **Human‑like timing**
  - Randomized actions and delays to avoid repetitive patterns
- **Smart auto‑pause on user activity**
  - Pauses as soon as it detects:
    - Mouse movement
    - Any keyboard key press
  - Console message: `User activity detected -> Bot paused.`
- **Auto‑resume after inactivity**
  - If there is **no user activity for 15 seconds** (`INACTIVITY_TIMEOUT`),
    the bot resumes automatically.
  - Console message: `No user activity detected. Resuming bot...`
- **Global kill hotkey**
  - Press **`Ctrl + Space + L`** to terminate the script cleanly.
  - Console message: `Kill hotkey pressed. Exiting process...`
- **Desktop notifications**
  - Shows notification when:
    - Automation starts
    - Automation stops (including via kill hotkey)
  - Uses `plyer` when available, otherwise falls back to console output.

---

## Requirements

- **OS**: Windows
- **Python**: 3.10+ recommended
- **Packages**:

```bash
pip install pyautogui keyboard pynput plyer
```

> For the global hotkey and keyboard hooks (`keyboard` module), running the
> terminal **as Administrator** is often required on Windows.

---

## How It Works

- **Global state**
  - `running`: controls the main loop and is set to `False` by the kill hotkey.
  - `bot_active`: indicates whether automation is currently allowed to run.
  - `last_user_activity`: timestamp of last mouse/keyboard event.
  - `INACTIVITY_TIMEOUT`: seconds since last activity before auto‑resume
    (default: `15`).

- **Notifications**
  - `show_notification(title, message, timeout=5)`:
    - Uses `plyer.notification.notify(...)` if available.
    - Otherwise prints a `[NOTIFY]` line to the console.
  - Called when:
    - The bot starts (`"Automation started."`)
    - The bot stops (`"Automation stopped."`)

- **User activity detection**
  - `keyboard.on_press(on_user_activity)` listens for any key press.
  - `pynput.mouse.Listener(on_move=...)` listens for mouse movement.
  - Any activity:
    - Updates `last_user_activity`.
    - Sets `bot_active = False` (pauses bot).

- **Inactivity watcher**
  - A daemon thread runs `inactivity_watcher()`:
    - Every second it checks if `bot_active` is `False` and
      `time.time() - last_user_activity > INACTIVITY_TIMEOUT`.
    - If so, it prints `No user activity detected. Resuming bot...` and
      sets `bot_active = True`.

- **Random actions**
  - In the main loop, while `running` is `True` and `bot_active` is `True`,
    it chooses a random action:
    - `Alt + Tab` / `Ctrl + Tab` with random number of presses
    - `PageUp` / `PageDown`
    - Multiple `Up` or `Down` key presses with short delays
    - Smooth random mouse move using `pyautogui.moveTo` with easing
  - Between actions it sleeps for a random interval
    (currently between ~1.3 and 2.6 seconds).

- **Kill hotkey**
  - `keyboard.add_hotkey('ctrl+space+l', kill_process)`:
    - Sets `running = False`
    - Prints a message
    - Triggers the “Automation stopped” notification

---

## Usage

From a terminal in the project directory:

```bash
cd D:\workplace\smart-contract\python-pra
python sticky.py
```

- Let it run in the background.
- Use your PC normally. The bot:
  - Pauses while you are active.
  - Resumes a short time after you stop.
- To stop it, press **`Ctrl + Space + L`**.

If `keyboard` fails to initialize (e.g. due to permissions), you may need to:

- Run PowerShell / CMD as **Administrator**, or
- Adjust the code to catch exceptions around `keyboard.add_hotkey` and
  `keyboard.on_press` and run without global hotkeys.

---

## Building as an EXE (optional)

You can bundle the script into a standalone Windows executable using PyInstaller.

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole sticky.py
```

- `--onefile`: produces a single `.exe` file.
- `--noconsole`: hides the console window (runs in background).

The resulting file will be in the `dist/` directory:

- `dist/sticky.exe`

---

## Notes, Use Cases, and Disclaimer

- **Typical use cases**
  - Prevent system idle timeout or screen lock
  - Keep remote desktop / VPN sessions active
  - Simulate light, non‑intrusive user activity

- **Antivirus**
  - Because it uses keyboard and mouse hooks, some antivirus tools may flag or
    sandbox it. This is common for automation utilities.

- **Disclaimer**
  - This script is intended for **legitimate** automation only.
  - Always comply with your organization’s policies and local regulations.
