import pyautogui
import random
import time
import threading
import keyboard
from pynput import mouse

# ==============================
# GLOBAL STATE VARIABLES
# ==============================

running = True          # Controls full process (for kill hotkey)
bot_active = True       # Controls whether automation is currently active
last_user_activity = time.time()   # Timestamp of last mouse/keyboard activity
INACTIVITY_TIMEOUT = 10  # Seconds before bot resumes after user inactivity


# ==============================
# HOTKEY TO TERMINATE PROCESS
# ==============================

def kill_process():
    """
    Triggered when user presses CTRL + SPACE + L
    Completely stops the script.
    """
    global running
    print("Kill hotkey pressed. Exiting process...")
    running = False


keyboard.add_hotkey('ctrl+space+l', kill_process)


# ==============================
# USER ACTIVITY DETECTION
# ==============================

def on_user_activity(event=None):
    """
    Called whenever keyboard or mouse activity is detected.
    Stops bot and updates last activity timestamp.
    """
    global bot_active, last_user_activity
    last_user_activity = time.time()
    if bot_active:
        print("User activity detected -> Bot paused.")
        bot_active = False


# Detect keyboard activity
keyboard.on_press(on_user_activity)

# Detect mouse movement
mouse_listener = mouse.Listener(on_move=lambda x, y: on_user_activity())
mouse_listener.start()


# ==============================
# AUTO RESUME CHECK THREAD
# ==============================

def inactivity_watcher():
    """
    Background thread that checks user inactivity.
    If no activity for INACTIVITY_TIMEOUT seconds,
    bot resumes automatically.
    """
    global bot_active

    while running:
        if not bot_active:
            if time.time() - last_user_activity > INACTIVITY_TIMEOUT:
                print("No user activity detected. Resuming bot...")
                bot_active = True
        time.sleep(1)


watcher_thread = threading.Thread(target=inactivity_watcher, daemon=True)
watcher_thread.start()


# ==============================
# RANDOM MOUSE MOVEMENT FUNCTION
# ==============================

def random_mouse_move():
    """
    Moves mouse to a random position on screen
    with smooth animation.
    """
    screen_width, screen_height = pyautogui.size()

    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)

    duration = random.uniform(0.5, 2.5)

    pyautogui.moveTo(random_x, random_y, duration, pyautogui.easeInOutQuad)


# ==============================
# MAIN AUTOMATION LOOP
# ==============================

if __name__ == '__main__':

    # Small startup delay
    time.sleep(2 + random.random() * 1.3)

    while running:

        # If bot paused due to user activity → wait
        if not bot_active:
            time.sleep(0.5)
            continue

        t1 = int((random.random() * 100) % 7)

        if t1 == 0:
            pyautogui.keyDown("alt")
            for _ in range(random.randint(1, 4)):
                pyautogui.press("tab")
                time.sleep(0.1)
            pyautogui.keyUp("alt")

        elif t1 == 1:
            pyautogui.keyDown("ctrl")
            for _ in range(random.randint(1, 4)):
                pyautogui.press("tab")
                time.sleep(0.1)
            pyautogui.keyUp("ctrl")

        elif t1 == 2:
            pyautogui.press("pageup")

        elif t1 == 3:
            pyautogui.press("pagedown")

        elif t1 == 4:
            for _ in range(random.randint(1, 10)):
                pyautogui.press("down")
                time.sleep(0.1)

        elif t1 == 5:
            for _ in range(random.randint(1, 10)):
                pyautogui.press("up")
                time.sleep(0.1)

        else:
            # NEW: Fully random mouse movement
            random_mouse_move()

        # Random sleep between actions
        time.sleep(random.uniform(1.3, 2.6))

    print("Process terminated cleanly.")