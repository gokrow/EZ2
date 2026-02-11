## QuickBZ2 by gokrow.

import bz2
import tkinter as tk
from tkinter import filedialog
import os.path

def compressor():
    files = filedialog.askopenfiles(mode='rb',title="Select files to compress.")
    if not files:
        return
    output_location = filedialog.askdirectory(title="Select directory")

    for f in files:
        filepath = os.path.basename(f.name)
        compfilepath = os.path.join(output_location, filepath + ".bz2")

        with bz2.open(compfilepath, 'wb') as output:
            output.write(f.read())
        print(os.path.basename(f.name) + " was successfully compressed.")

compressor()

root = tk.Tk()
root.withdraw()