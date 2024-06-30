import tkinter as tk
from textblob import TextBlob
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from spellchecker import SpellChecker

spell = SpellChecker()

def check_spell():
    word = ip.get().strip()
    if word:
        corrected_words = get_suggestions(word)
        display_results(corrected_words)

def get_suggestions(word):
    return spell.candidates(word)

def get_definition(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "No definition found."

def display_results(words):
    results = []
    for word in words:
        definition = get_definition(word)
        results.append(f"Word: {word}\nDefinition: {definition}")
    
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    for result in results:
        label = tk.Label(result_frame, text=result, font=("Comic Sans MS", 15), bg="#b5fffb", fg="navy", justify="left", anchor="w", wraplength=650)
        label.pack(anchor="w", padx=10, pady=5)

window = tk.Tk()
window.title("Spell-Def Buzz")
window.geometry("700x500")
window.config(background="#b5fffb")

heading = tk.Label(window, text="Spelling Checker", font=("Comic Sans MS", 30, "bold"), bg="#b5fffb", fg="navy")
heading.pack(padx=50, pady=50)

ip = tk.Entry(window, justify="center", width=30, font=("Comic Sans MS", 20), bg="white", border=2)
ip.pack(pady=20)
ip.focus()

button = tk.Button(window, text="CHECK", font=("Comic Sans MS", 20), bg="navy", fg="white", command=check_spell)
button.pack()

# Create a canvas and a scrollbar
canvas = tk.Canvas(window, bg="#b5fffb")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
result_frame = tk.Frame(canvas, bg="#b5fffb")
canvas.create_window((0, 0), window=result_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

result_frame.bind("<Configure>", on_frame_configure)

window.mainloop()
