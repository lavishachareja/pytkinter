import tkinter as tk
def greet():
    name = entry.get()
    msg = "Nice to meet you "+name+"!"
    res.config(text=msg)
window = tk.Tk()
window.title("Name Box")
det = tk.Label(text="Hi, Lavisha here",
               fg="white",
               bg="black",
               height=5,
               width=20,
               font=("Arial",15))
ip = tk.Label(text="Your name?",
               font=("Comic Sans MS",10))
entry=tk.Entry()
but = tk.Button(window,text="Tell",command=greet)
res = tk.Label(text="",
               fg="Red",
               height=3,
               width=20,
               font=("Arial",15))
det.pack()
ip.pack()
entry.pack()
but.pack()
res.pack()
window.mainloop()