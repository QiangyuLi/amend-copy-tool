import tkinter as tk
from tkinter import filedialog, messagebox
from amend_copy.core import amend_copy

def select_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

def start_copy(src_entry, dst_entry):
    src = src_entry.get()
    dst = dst_entry.get()
    if not src or not dst:
        messagebox.showerror("Error", "Please select both folders.")
        return
    try:
        amend_copy(src, dst)
        messagebox.showinfo("Success", "Amend copy completed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Amend Copy Tool")

    tk.Label(root, text="Source Folder:").grid(row=0, column=0, sticky="e")
    src_entry = tk.Entry(root, width=50)
    src_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=lambda: select_folder(src_entry)).grid(row=0, column=2)

    tk.Label(root, text="Destination Folder:").grid(row=1, column=0, sticky="e")
    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=1, column=1)
    tk.Button(root, text="Browse", command=lambda: select_folder(dst_entry)).grid(row=1, column=2)

    tk.Button(root, text="Start Amend Copy", command=lambda: start_copy(src_entry, dst_entry)).grid(row=2, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
