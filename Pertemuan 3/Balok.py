import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    L = pj * lb
    
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_Volume():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    V = 2 * (pj + lb)
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)
    
def hitung():
    hitung_luas()
    hitung_Volume()
    
# Creat tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulaor Luas dan Volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
panjang = Label(frame, text="panjang:")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar = Label(frame, text="Lebar  :")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume:")
Volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas 
txtluas = Entry(frame)
txtluas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
