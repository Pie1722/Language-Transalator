import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Language options and codes
LANGUAGES = {
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Bengali': 'bn',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Punjabi': 'pa',
    'Urdu': 'ur'
}

# Function to translate
def translate_text():
    text = input_text.get("1.0", "end-1c")
    lang = lang_combo.get()
    
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    if lang not in LANGUAGES:
        messagebox.showwarning("Language Error", "Please select a target language.")
        return

    try:
        translator = Translator()
        translated = translator.translate(text, src='en', dest=LANGUAGES[lang])
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Create main window
root = tk.Tk()
root.title("Multilingual Translator")
root.geometry("550x480")
root.resizable(False, False)

# Title
tk.Label(root, text="English to Indian Languages Translator", font=("Arial", 16, "bold")).pack(pady=10)

# Input text
tk.Label(root, text="Enter English Text:", font=("Arial", 12)).pack(anchor='w', padx=20)
input_text = tk.Text(root, height=5, width=60, font=("Arial", 11))
input_text.pack(padx=20, pady=5)

# Language selector
tk.Label(root, text="Select Language:", font=("Arial", 12)).pack(anchor='w', padx=20)
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.keys()), font=("Arial", 11), state="readonly", width=20)
lang_combo.pack(padx=20, pady=5)
lang_combo.set("Hindi")  # Default

# Translate button
tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Output text
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(anchor='w', padx=20)
output_text = tk.Text(root, height=5, width=60, font=("Arial", 11))
output_text.pack(padx=20, pady=5)

# Start GUI
root.mainloop()
