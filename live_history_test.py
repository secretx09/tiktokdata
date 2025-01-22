import tkinter as tk
from tkinter import ttk

live_his = "TikTok_Data_1735588272\\Tiktok\\TikTok Live\\Watch Live History.txt"

def create_popup():
    popup = tk.Tk()
    popup.title("Live History")

    notebook = ttk.Notebook(popup)
    notebook.pack(fill='both', expand=True)

    with open(live_his, "r", encoding='utf-8') as live_history_file:
        live_history_data = live_history_file.read()

    comments = live_history_data.strip().split('\n')

    comments_frame = ttk.Frame(notebook)
    notebook.add(comments_frame, text='Comments')

    comments_text = tk.Text(comments_frame, wrap='word')
    comments_text.pack(fill='both', expand=True)
    comments_text.insert(tk.END, '\n'.join(comments))
    comments_text.config(state=tk.DISABLED)

    popup.mainloop()

create_popup()