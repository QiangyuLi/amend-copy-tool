import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from amend_copy.core import amend_copy, list_amend_methods

def select_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

def start_copy(src_entry, dst_entry, method_var):
    src = src_entry.get()
    dst = dst_entry.get()
    method = method_var.get()
    
    if not src or not dst:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return
    try:
        amend_copy(src, dst, method=method)
        messagebox.showinfo("Success", f"Amend copy completed using method: {method}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Amend Copy Tool")
    root.geometry("580x180")

    tk.Label(root, text="Source Folder:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    src_entry = tk.Entry(root, width=50)
    src_entry.grid(row=0, column=1, padx=5)
    tk.Button(root, text="Browse", command=lambda: select_folder(src_entry)).grid(row=0, column=2)

    tk.Label(root, text="Destination Folder:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=1, column=1, padx=5)
    tk.Button(root, text="Browse", command=lambda: select_folder(dst_entry)).grid(row=1, column=2)

    tk.Label(root, text="Amend Method:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    method_var = tk.StringVar()
    method_dropdown = ttk.Combobox(root, textvariable=method_var, values=list_amend_methods(), state="readonly", width=47)
    method_dropdown.grid(row=2, column=1, padx=5)
    method_dropdown.current(0)  # Default to first method

    tk.Button(root, text="Start Amend Copy", command=lambda: start_copy(src_entry, dst_entry, method_var)).grid(row=3, column=1, pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()
