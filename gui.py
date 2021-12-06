from tkinter import Tk, filedialog
from tkinter import ttk
from commands import commands_dictionary


WIDTH = 300
HEIGHT = 200
TITLE = "Mission's Enigma Subtitle Toolkit"


def filedialog_wrapper(func):
    input_filename = filedialog.askopenfilename(title="Select input file")
    if not input_filename:
        return
    output_filename = filedialog.asksaveasfilename(title="Save as")
    if not output_filename:
        return
    encoding = 'utf-8'

    func(input_filename, output_filename, encoding)


root = Tk()
root.title(TITLE)
root.geometry(f"{WIDTH}x{HEIGHT}")

frame = ttk.Frame(root, padding=10)
frame.grid()

for row, (name, func) in enumerate(commands_dictionary.items()):
    ttk.Button(frame, text=name, command=lambda: filedialog_wrapper(func)).grid(column=1, row=row)

root.mainloop()