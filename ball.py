from tkinter import messagebox,ttk,Checkbutton, IntVar
from tkinter import *
import psutil,time,subprocess,os,sys,threading,webbrowser,clipboard,pystray
from engine import engine_ud,setting,free_space,tool
from pystray import MenuItem
from PIL import Image
def exit_clicked(icon,item):
            icon.notify('Program Exited')
            icon.stop()
            exit(0)

def bar():

            
    menu = (
            MenuItem('Open', lambda: tk.attributes('-alpha', 1) ),
            MenuItem('exit', lambda icon, item: exit_clicked(icon, item))
            )
    image = Image.open('creeper.png')
    icon = pystray.Icon("A-Speed ball", image, "A-Speed ball", menu)
    icon.run()


def menu_about():
        def copy_mail(event):
            clipboard.copy("rddff236ss@hotmail.com")
            messagebox.showinfo("Email Copied","Email is copied")
        tk2 = Tk()
        tk2.geometry('600x600')
        label_about = Label(tk2,text="Copyright (C) Andy Chan 2023-2024\nYou can use the source code for personal use\n")
        label_about.pack()
        label_github = Label(tk2,text="My Github Account",cursor="hand2")
        label_github.pack()
        label_github.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://github.com/Rddff123"))
        label_github = Label(tk2,text="My Email:rddff236ss@hotmail.com",cursor="hand2")
        label_github.pack()
        label_github.bind("<Button-1>", copy_mail)
        mainloop()
def menu_open_setting():
    def check_status():
        comfirm = messagebox.askokcancel("Warning","The program will modify registry, are you sure to do so?")
        # Get the current directory of the Python script
        if comfirm:
            script_directory = os.path.dirname(os.path.realpath(__file__))

                # Set the file path to the current Python script
            script_file_path = os.path.join(script_directory, os.path.basename(__file__))
            setting.add_to_startup(script_file_path,check_var_1.get())
    setting_window = Toplevel(tk)  # Create a Toplevel widget instead of a new Tk instance
    check_var_1 = IntVar()
    setting_window.geometry('400x300')
    checkbutton1 = Checkbutton(setting_window, text='Start program on system startup', variable=check_var_1)
    checkbutton1.pack()

    button = Button(setting_window, text='Check Status', command=check_status)
    button.pack()

    setting_window.mainloop()
def free_temp_space():
    threading.Thread(target=free_space.clean_space).start()
def toolbox():
    def do_selection():
        var_1 = check_var_1.get()
        var_2 = check_var_2.get()
        tool.DisableSearchBoxSuggestions(var_1)
        tool.TraditionalRightClickMenu(var_2)
    toolbox_window = Toplevel(tk)  # Create a Toplevel widget instead of a new Tk instance
    check_var_1 = IntVar()
    check_var_2 = IntVar()

    toolbox_window.title("Toolbox")
    toolbox_window.geometry('600x600')
    label_about = Label(toolbox_window,text="Toolbox for Windows 10 & 11 only!\n",foreground="red",font=("Arial", 16))
    label_about.pack()

    checkbutton1 = Checkbutton(toolbox_window, text='[10&11]Disable SearchBox Internet Suggestions', variable=check_var_1)
    checkbutton1.pack()  
    checkbutton2 = Checkbutton(toolbox_window, text='[11]Traditional Right Click Menu', variable=check_var_2)
    checkbutton2.pack()
    button_comfirm = Button(toolbox_window, text='Clean temp space', command=do_selection)
    button_comfirm.pack()
    toolbox_window.mainloop()
def GUI():
    global tk
    tk = Tk()
    tk.wm_attributes("-topmost", 1)
    tk.overrideredirect(True)
    menu2 = Menu(tearoff=0)
    def hide():
        tk.attributes('-alpha', 0)
    def update_updownload():
        engines = engine_ud()
        for speed in engines.updownload():
            label_bl.config(text=speed[0])
            label_br.config(text=speed[1])
            
    menu2.add_command(label="Free up spaces",command=free_temp_space) 
    menu2.add_command(label="Toolbox",command=toolbox)       
    menu2.add_command(label="Setting",command=menu_open_setting) 
    menu2.add_command(label="About",command=menu_about)
    menu2.add_command(label="Hide",command=hide)
    menu2.add_command(label="Exit",command=exit_clicked)
    
    
    def menu_start(event):
        menu2.post(event.x_root, event.y_root)
    def on_canvas_press(event):
        # Store the initial position of the mouse
        canvas.start_x = event.x
        canvas.start_y = event.y

    def on_canvas_motion(event):
        # Calculate the distance moved by the mouse
        dx = event.x - canvas.start_x
        dy = event.y - canvas.start_y
        # Move the window according to the mouse movement
        tk.geometry(f"+{tk.winfo_x() + dx}+{tk.winfo_y() + dy}")
    def update_information():
        engines = engine_ud()
        for things in engines.update_CPUMEM():
            label_tl.config(text=things[0])
            label_tr.config(text=things[1])        
            
            
    canvas = Canvas(width=200, height=50, bg='white', highlightthickness=0)
    canvas.pack()
    canvas.bind("<ButtonPress-1>", on_canvas_press)
    canvas.bind("<B1-Motion>", on_canvas_motion)
    canvas.bind("<Button-3>", menu_start)

    def change_image(images):
        global photo
        photo = PhotoImage(file=images)
                # Define the desired width and height for the resized image
        desired_width = 50
        desired_height = 50
         
        photo = photo.subsample(photo.width() // desired_width, photo.height() // desired_height)
        image_item = canvas.create_image(0, 0, anchor='nw', image=photo)
    change_image('creeper.png')
    #canvas  = Canvas(tk, width=desired_width, height=desired_height)
    #canvas.place(x=0,y=0,width=50,height=50)
    canvas.bind("<ButtonPress-1>", on_canvas_press)
    canvas.bind("<B1-Motion>", on_canvas_motion)
    label_tl = Label(text="CPU:Loading")
    label_tl.place(x=50, y=0, width=75, height=25)
 
    label_tr = Label(text="Mem:Loading")
    label_tr.place(x=125, y=0, width=75, height=25)
 
    label_bl = Label(text="U:Loading")
    label_bl.place(x=50, y=25, width=75, height=25)
 
    label_br = Label(text="D:Loading")
    label_br.place(x=125, y=25, width=75, height=25)
    
    label_tl.bind("<ButtonPress-1>", on_canvas_press)
    label_tl.bind("<B1-Motion>", on_canvas_motion)
    label_tr.bind("<ButtonPress-1>", on_canvas_press)
    label_tr.bind("<B1-Motion>", on_canvas_motion)
    label_bl.bind("<ButtonPress-1>", on_canvas_press)
    label_bl.bind("<B1-Motion>", on_canvas_motion)
    label_br.bind("<ButtonPress-1>", on_canvas_press)
    label_br.bind("<B1-Motion>", on_canvas_motion)

    # Start updating the CPU usage
    threading.Thread(target=update_information).start()
    threading.Thread(target=update_updownload).start()
    threading.Thread(target=bar).start()    
    tk.mainloop()
GUI()
