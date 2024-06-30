import tkinter as tk
window = tk.Tk()
window.geometry("600x250")
window.title("DIRECTIONS!")
frame = tk.Frame(window,bg="lightblue",padx=20,pady=20)
def n():
    msg="NORTH"
    op.config(text=msg)
def w():
    msg="WEST"
    op.config(text=msg)
def s():
    msg="SOUTH"
    op.config(text=msg)
def e():
    msg="EAST"
    op.config(text=msg)
def ne():
    msg="NORTH-EAST"
    op.config(text=msg)
def se():
    msg="SOUTH-EAST"
    op.config(text=msg)
def sw():
    msg="SOUTH-WEST"
    op.config(text=msg)
def nw():
    msg="NORTH-WEST"
    op.config(text=msg)    
buttondes={"bg":"#002157","fg":"white","font":("Arial", 12, "bold"), "relief": "raised", "bd": 3}
tk.Button(frame,text="7",padx=20,pady=10,command=w,**buttondes).grid(row=1,column=0,padx=20,pady=10)
tk.Button(frame,text="1",padx=20,pady=10,command=n,**buttondes).grid(row=0,column=1,padx=20,pady=10)
tk.Button(frame,text="2",padx=20,pady=10,command=ne,**buttondes).grid(row=0,column=2,padx=20,pady=10)
tk.Button(frame,text="4",padx=20,pady=10,command=se,**buttondes).grid(row=2,column=2,padx=20,pady=10)
tk.Button(frame,text="6",padx=20,pady=10,command=sw,**buttondes).grid(row=2,column=0,padx=20,pady=10)
tk.Button(frame,text="8",padx=20,pady=10,command=nw,**buttondes).grid(row=0,column=0,padx=20,pady=10)
tk.Button(frame,text="5",padx=20,pady=10,command=s,**buttondes).grid(row=2,column=1,padx=20,pady=10)
tk.Button(frame,text="3",padx=20,pady=10,command=e,**buttondes).grid(row=1,column=2,padx=20,pady=10)
op = tk.Label(frame,text="",font=("Comic Sans MS",20), width=20,relief="sunken", bd=3, bg="white",fg="#002157")
op.grid(row=1,column=1)
frame.pack(expand=True, fill=tk.BOTH)
window.mainloop()