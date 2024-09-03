import tkinter as tk

#si function
def cal_si():
    try:
        p = float(principal.get())
        r = float(roi.get())
        t = float(year.get())
        si = (p*r*t)/100
        amt = p + si
        res.config(text=f"Simple Interest: {si:.2f}", bg="#b0fbff")
        res_amt.config(text=f"Amount: {amt:.2f}", bg="#b0fbff")
    except ValueError:
        res.config(text="Enter valid numbers")
        res_amt.config(text="")

#screen
window = tk.Tk()
window.configure(bg="#b0fbff")
window.title("SI calculator")

#principal
principal_label = tk.Label(window, text="Principal Amount (P):", bg="#b0fbff", font=("Times New Roman",14))
principal_label.grid(row=0, column=0, padx=10, pady=10)
principal = tk.Entry(window, font=("Times New Roman",14))
principal.grid(row=0, column=1, padx=10, pady=10)
 
#ROI 
roi_label = tk.Label(window, text="Rate of Interest (in %):", bg="#b0fbff", font=("Times New Roman",14))
roi_label.grid(row=1, column=0, padx=10, pady=10)
roi = tk.Entry(window, font=("Times New Roman",14))
roi.grid(row=1, column=1, padx=10, pady=10)

#time
year_label = tk.Label(window, text="Time Period(in years):", bg="#b0fbff", font=("Times New Roman",14))
year_label.grid(row=2, column=0, padx=10, pady=10)
year = tk.Entry(window, font=("Times New Roman",14))
year.grid(row=2, column=1, padx=10, pady=10)

#cal button
calc_button = tk.Button(window, text="CALCULATE", command=cal_si, bg="black", fg="white", font=("Times New Roman",16,"bold"))
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#result si
res = tk.Label(window, text="Simple Interest:", bg="#b0fbff", font=("Times New Roman",14))
res.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#result amount
res_amt = tk.Label(window, text="Amount:", bg="#b0fbff", font=("Times New Roman",14))
res_amt.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()