import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with fitz.open(file_path) as pdf:
            text = ""
            for page_num in range(len(pdf)):
                page = pdf[page_num]
                text += page.get_text()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)

root = tk.Tk()
root.title("Document Reader")

upload_button = tk.Button(root, text="Upload Document", command=upload_file)
upload_button.pack(pady=20)

text_box = tk.Text(root, height=20, width=80)
text_box.pack(padx=20, pady=10)

root.mainloop()
