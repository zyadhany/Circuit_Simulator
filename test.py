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
    header = tk.Frame(root, height=h_head, width=w_head, bg='#DBA159')
    header.grid(row=0, column=0, columnspan=gc_head, rowspan=gr_head, sticky='ew')

    # Add buttons to header
    button1 = tk.Button(header, text="DET")
    button1.pack(side=tk.LEFT, padx=(10, 20), pady=30)
    button2 = tk.Button(header, text="RUN")
    button2.pack(side=tk.LEFT, padx=10, pady=30)

    # Add clear button to header
    clear_button = tk.Button(header, text="RESET", command=clear_content)
    clear_button.pack(side=tk.LEFT, padx=(10, 20), pady=20)

    # Main Content Frame
    content = tk.Frame(root, height=h_content, width=w_content, bg='white')
    content.grid(row=gr_head, column=0, rowspan=gr_content, columnspan=gc_content, sticky='nsew')
    add_button_button = tk.Button(content, text="Add", command=add_frame, anchor='nw')
    add_button_button.pack(anchor='nw', pady=20, padx=10)
    header.pack_propagate(False)
    content.pack_propagate(False)
    return [header, content]

# Declare entry_widgets as a global variable
entry_widgets = []

# Function to add dynamic frame with three Entry widgets
def add_frame():
    def on_entry_click(event, entry_widget):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, tk.END)
            entry_widget.config(fg='black')

    new_frame = tk.Frame(frames[1], bg='lightblue', height=50, width=200)
    new_frame.pack(anchor='nw', pady=10, padx=10)

    # Create a list to store entry widgets
    current_entry_widgets = []

    for _ in range(4):
        entry_var = tk.StringVar()
        entry_widget = tk.Entry(new_frame, textvariable=entry_var, width=5, font=('Arial', 12), bd=3)
        entry_widget.pack(side=tk.RIGHT, pady=5, padx=10)
        current_entry_widgets.append(entry_widget)

        # Bind the function to the Entry widget
        entry_widget.bind("<FocusIn>", lambda event, widget=entry_widget: on_entry_click(event, widget))

    submit_button = tk.Button(new_frame, text="Submit", command=lambda: print([entry.get() for entry in current_entry_widgets]))
    submit_button.pack(side=tk.LEFT, pady=10, padx=10)

    placeholder_text = "ادخلي اسمك هنا"

    # Set the initial placeholder text and color for each entry
    for entry_widget in current_entry_widgets:
        entry_var.set(placeholder_text)
        entry_widget.config(fg='gray')

    # Store the entry widgets in the global list
    entry_widgets.extend(current_entry_widgets)

# Function to clear all content
def clear_content():
    # Clear all frames in the content frame
    for widget in frames[1].winfo_children():
        widget.destroy()

# Create the root window
root = tk.Tk()

# Configure the root window
rootConfig(root)

# Build frames
frames = FrameBuild(root)

# Run the main loop
root.mainloop()