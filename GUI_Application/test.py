import tkinter as tk

root = tk.Tk()
root.title("Default Size in Grid Layout")

# Creating labels in different rows and columns
label1 = tk.Label(root, text="Row 0 - Label 1", bg="red")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Row 1 - Label 2", bg="green")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Row 2 - Label 3", bg="blue")
label3.grid(row=2, column=0)

label4 = tk.Label(root, text="Column 1 - Label 4", bg="yellow")
label4.grid(row=0, column=1)

label5 = tk.Label(root, text="Column 2 - Label 5", bg="orange")
label5.grid(row=0, column=2)

root.mainloop()
