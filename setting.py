from tkinter import *
import os
import shutil
import sys

def check_state():
    value = check_var.get()
    print(f"Check button value: {value}")
    
    # Overwrite the value of setting.setting
    with open("setting.setting", "w") as file:
        file.write(f"PAS:{value}")
    current_script = sys.argv[0]
    if value ==1:
    # Get the path to the startup folder
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        # Create the destination path
        destination_path = os.path.join(startup_folder, os.path.basename(current_script))

        # Copy the script to the startup folder
        shutil.copy(current_script, destination_path)
    else:
        try:
            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

            # Create the destination path
            destination_path = os.path.join(startup_folder, os.path.basename(current_script))

            # Copy the script to the startup folder
            os.remove(destination_path)
        except:
            pass
    window.destroy()
# Create the main application window
window = Tk()

# Create a variable to store the check button's state
check_var = IntVar()

# Read the value of setting.setting and set the initial state of the check button accordingly
# Assuming setting.setting contains the value in the format "PAS:{VALUE}"
with open("setting.setting", "r") as file:
    value = file.read().strip()
    if value.startswith("PAS:"):
        check_var.set(int(value[4:]))

# Create the check button and associate it with the variable
check_button = Checkbutton(window, text="Auto-start", variable=check_var)
check_button.pack()

# Create a button to check the state of the check button
state_button = Button(window, text="Check State", command=check_state)
state_button.pack()

# Start the main event loop
window.mainloop()