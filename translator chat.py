import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        source_text = source_text_box.get("1.0", tk.END).strip()
        src_lang = src_lang_combo.get()
        dest_lang = dest_lang_combo.get()

        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        if src_lang not in LANGUAGES.values() or dest_lang not in LANGUAGES.values():
            messagebox.showwarning("Language Error", "Please select valid source and destination languages.")
            return

        translator = Translator()
        translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
        
        dest_text_box.delete("1.0", tk.END)
        dest_text_box.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Google Translator with Tkinter")

# Source language combobox
src_lang_label = ttk.Label(root, text="Source Language:")
src_lang_label.grid(row=0, column=0, padx=10, pady=10)
src_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
src_lang_combo.grid(row=0, column=1, padx=10, pady=10)
src_lang_combo.current(0)

# Destination language combobox
dest_lang_label = ttk.Label(root, text="Destination Language:")
dest_lang_label.grid(row=1, column=0, padx=10, pady=10)
dest_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
dest_lang_combo.grid(row=1, column=1, padx=10, pady=10)
dest_lang_combo.current(1)

# Source text box
source_text_label = ttk.Label(root, text="Source Text:")
source_text_label.grid(row=2, column=0, padx=10, pady=10)
source_text_box = tk.Text(root, height=10, width=50)
source_text_box.grid(row=2, column=1, padx=10, pady=10)

# Destination text box
dest_text_label = ttk.Label(root, text="Translated Text:")
dest_text_label.grid(row=3, column=0, padx=10, pady=10)
dest_text_box = tk.Text(root, height=10, width=50)
dest_text_box.grid(row=3, column=1, padx=10, pady=10)

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()