import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title("Scrollbar Example")
root.geometry("400x300")

# Add a Text widget for demonstration
text = tk.Text(root, wrap="none")
text.pack(side="left", fill="both", expand=True)

# Add a vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=text.yview)
vsb.pack(side="right", fill="y")
text.configure(yscrollcommand=vsb.set)

# Add a horizontal scrollbar
hsb = ttk.Scrollbar(root, orient="horizontal", command=text.xview)
hsb.pack(side="bottom", fill="x")
text.configure(xscrollcommand=hsb.set)

# Insert some text into the Text widget
for i in range(30):
    text.insert("end", f"Line {i}\n")

root.mainloop()
