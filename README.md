# 🖱️ Activity Automation Bot

A lightweight Python automation tool that simulates random keyboard and
mouse activity.\
Includes smart pause/resume logic based on real user interaction and a
global kill hotkey.

------------------------------------------------------------------------

## 🚀 Features

### ✅ Random Activity Simulation

The bot performs random actions such as: - ALT + TAB switching - CTRL +
TAB switching - Page Up / Page Down - Arrow key scrolling - Random mouse
movement across the screen

All actions use randomized timing and behavior to avoid repetitive
patterns.

------------------------------------------------------------------------

### ✅ Smart Auto-Pause on User Activity

If the user: - Moves the mouse\
- Presses any keyboard key

The bot immediately pauses.

Console message: User activity detected -\> Bot paused.

------------------------------------------------------------------------

### ✅ Auto-Resume After Inactivity

If there is **no user activity for 10 seconds**, the bot automatically
resumes.

Console message: No user activity detected. Resuming bot...

The inactivity timeout is configurable:

INACTIVITY_TIMEOUT = 10

------------------------------------------------------------------------

### ✅ Global Kill Hotkey

Press:

CTRL + SPACE + L

This will completely terminate the process.

Console message: Kill hotkey pressed. Exiting process... Process
terminated cleanly.

------------------------------------------------------------------------

## 📦 Requirements

Install dependencies before running:

pip install pyautogui keyboard pynput

------------------------------------------------------------------------

## 🛠 Build as EXE

Install PyInstaller:

pip install pyinstaller

Build:

pyinstaller --onefile --noconsole your_script.py

Options Explained: - --onefile → Single executable file - --noconsole →
Runs silently in background

The final executable will be located in:

dist/your_script.exe

------------------------------------------------------------------------

## ⚠️ Important Notes

### Antivirus Warning

Since the application hooks keyboard input and monitors mouse movement,
some antivirus software may flag it as suspicious. This is common
behavior for automation tools.

------------------------------------------------------------------------

### Administrator Privileges

For global hotkeys to work reliably on Windows, you may need to run the
executable as Administrator.

------------------------------------------------------------------------

## 🧠 How It Works

### Background Watcher Thread

A daemon thread constantly checks: Current Time - Last User Activity
Time

If greater than inactivity timeout → bot resumes.

------------------------------------------------------------------------

### Activity Detection Hooks

-   keyboard.on_press() → Detects keyboard input\
-   pynput.mouse.Listener() → Detects mouse movement

These update the last_user_activity timestamp and pause automation.

------------------------------------------------------------------------

### Random Mouse Movement

The bot: - Detects screen resolution - Moves to a random (x, y)
coordinate - Uses smooth easing animation

------------------------------------------------------------------------

## 🔧 Customization

You can modify: - INACTIVITY_TIMEOUT - Mouse movement duration - Action
delay timing - Kill hotkey combination

------------------------------------------------------------------------

## 📌 Use Cases

-   Prevent system idle timeout\
-   Prevent screen lock\
-   Keep remote sessions active\
-   Simulate light activity

------------------------------------------------------------------------

## 🔒 Disclaimer

This software is intended for legitimate automation purposes only.\
Ensure compliance with company policies and local regulations before
use.
