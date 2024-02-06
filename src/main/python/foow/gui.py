from exe import create_folders
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading

def show_progress_bar():
    # Create a top-level window for the progress bar
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress Bar")

    # Create a progress bar
    progress = ttk.Progressbar(progress_window, length=300, mode="indeterminate")
    progress.pack(pady=20)

    # Start the progress bar
    progress.start()

    # Setup Environment
    def on_progress_complete():
        # Stop the progress bar
        progress.stop()

        # Destroy the progress window
        progress_window.destroy()

        # Show "Processing Complete" popup
        show_processing_complete_popup()

    # Call create_folders in a separate thread
    progress_window.after(0, lambda: threading.Thread(target=create_folders, args=(on_progress_complete,)).start())

def show_processing_complete_popup():
    messagebox.showinfo("Processing Complete", "The processing is complete!")


def show_selected_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder_label.config(text=f"Selected Folder: {folder_path}")
        print("Selected Folder:", folder_path)

# Create the main window
root = tk.Tk()
root.title("Fish Out of Water")

# Set the initial size of the root window
root.geometry("400x200")

# Create a button to open the file explorer
open_button = tk.Button(root, text="Open File Explorer", command=show_selected_folder)
open_button.pack(pady=20)

# Create a label to display the selected folder path
selected_folder_label = tk.Label(root, text="Selected Folder: None")
selected_folder_label.pack(pady=10)

# Create a button to trigger the pop-up
start_button = tk.Button(root, text="Start", command=show_progress_bar)
start_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
