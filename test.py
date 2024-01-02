import tkinter as tk
import os

current_directory = os.getcwd()

def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def rootConfig(root: tk.Tk):
    root.title("Simulation")
    image_filename = "resource\icon.ico"
    image_path = os.path.join(current_directory, image_filename)
    root.config(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    root.minsize(1280, 720)
    root.maxsize(1280, 720)
    root.attributes('-fullscreen', False)
    root.bind("<F11>", lambda event: toggle_fullscreen(root))
    root.bind("<q>", lambda event: root.quit())
    return root

def FrameBuild(root: tk.Tk):
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()

    # grid geometry
    w_head = int(window_width)
    h_head = int(window_height * 0.1)
    gc_head = 2
    gr_head = 1

    h_content = window_height - h_head
    w_content = int(window_width)

    gc_content = 1
    gr_content = 1

    # Header Frame
    header = tk.Frame(root, height=h_head, width=w_head, bg='#95D7AE')
    header.grid(row=0, column=0, columnspan=gc_head, rowspan=gr_head, sticky='ew')

    # Add buttons to header
    button1 = tk.Button(header, text="DET")
    button1.pack(side=tk.LEFT, padx=(10, 20), pady=50)
    button2 = tk.Button(header, text="RUN")
    button2.pack(side=tk.LEFT, padx=10, pady=30)

    # Main Content Frame
    content = tk.Frame(root, height=h_content, width=w_content, bg='white')
    content.grid(row=gr_head, column=0, rowspan=gr_content, columnspan=gc_content, sticky='nsew')
    add_button_button = tk.Button(content, text="Add ", command=add_button,anchor='ne')
    add_button_button.pack(anchor='ne')
    header.pack_propagate(False)
    content.pack_propagate(False)
    return [header, content]

# Function to add dynamic button
def add_button():
    new_button = tk.Button(frames[1], text="result", command=delete_button)
    new_button.pack(anchor='ne')

# Function to delete the last button
def delete_button():
    # Delete the last button if there are buttons present
    all_buttons = frames[1].pack_slaves()
    if all_buttons:
        last_button = all_buttons[-1]
        last_button.destroy()

# Create the root window
root = tk.Tk()

# Configure the root window
rootConfig(root)

# Build frames
frames = FrameBuild(root)

# Run the main loop
root.mainloop()