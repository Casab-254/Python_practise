import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from docx import Document

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.lower().endswith('.pdf'):
            extract_pdf_text(file_path)
        elif file_path.lower().endswith('.docx'):
            extract_docx_text(file_path)
        elif file_path.lower().endswith('.txt'):
            extract_txt_text(file_path)

def extract_pdf_text(file_path):
    with fitz.open(file_path) as pdf:
        text = ""
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text += page.get_text()
        display_text(text)

def extract_docx_text(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    display_text(text)

def extract_txt_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    display_text(text)

def display_text(text):
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)

root = tk.Tk()
root.title("Document Reader")

upload_button = tk.Button(root, text="Upload Document", command=upload_file)
upload_button.pack(pady=20)

text_box = tk.Text(root, height=20, width=80)
text_box.pack(padx=20, pady=10)

root.mainloop()
