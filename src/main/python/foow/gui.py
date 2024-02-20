import os
import threading
import tkinter as tk
from processing import execution
from preperation import prepare_images
from tkinter import ttk, filedialog, messagebox


def show_process_progress_bar(root, selected_folder, output_destination, results_folder, confidence_level):
    # Validate that all fields are filled out and pathing/naming are available
    if validate_user_inputs_tab_2(selected_folder, output_destination, results_folder):
        # Exit out and do not start processing
        return 

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
        messagebox.showinfo("Processing Complete", "The processing is complete!")

    # Call create_folders in a separate thread
    progress_window.after(0, lambda: threading.Thread(target=execution, args=(on_progress_complete, selected_folder, output_destination, results_folder, confidence_level)).start())


def show_preperation_progress_bar(root, selected_folder, output_destination, results_folder, date):
    # Validate that all fields are filled out and pathing/naming are available
    if validate_user_inputs_tab_1(selected_folder, output_destination, results_folder, date):
        # Exit out and do not start processing
        return 

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
        messagebox.showinfo("Processing Complete", "The processing is complete!")

    # Call create_folders in a separate thread
    progress_window.after(0, lambda: threading.Thread(target=prepare_images, args=(on_progress_complete, selected_folder, output_destination, results_folder, date)).start())


def show_selected_folder(selected_folder):
    # File explorer pop up
    folder_path = filedialog.askdirectory()

    if folder_path:
        # Clear the existing content in the Text widget
        selected_folder.delete(1.0, tk.END)
        # Insert the selected folder path into the Text widget
        selected_folder.insert(tk.END, folder_path)

def validate_user_inputs_tab_2(selected_folder, output_destination, results_folder):
    # Initialize Variables
    output_path = os.path.join(output_destination, results_folder)

    # Store all input errors to Display at the end if any exist
    input_error_messages = []

    # Check if User did not select an image folder
    if not selected_folder:
        input_error_messages.append("Please Select an Image Folder to Process")
    
    # Check if User did not select an output_destination
    if not output_destination:
        input_error_messages.append("Please Select an Output Destination")

    # Check if a name was entered for results folder
    if not results_folder:
        input_error_messages.append("Please Name your Output Folder")
    else:
        # Check if this folder already exists
        if os.path.exists(output_path):
            input_error_messages.append(f"The Output Folder Path: '{output_path}' already exists")

    # Display error messages if any
    if input_error_messages:
        messagebox.showerror("User Input Error", "\n".join(input_error_messages))

        # User Input Errors Found
        return True
    
    # No User Input Errors
    return False


def validate_user_inputs_tab_1(selected_folder, output_destination, results_folder, date):
    # Initialize Variables
    output_path = os.path.join(output_destination, results_folder)

    # Store all input errors to Display at the end if any exist
    input_error_messages = []

    # Check if User did not select an image folder
    if not selected_folder:
        input_error_messages.append("Please Select an Image Folder to Process")
    
    # Check if User did not select an output_destination
    if not output_destination:
        input_error_messages.append("Please Select an Output Destination")

    # Check if a name was entered for results folder
    if not results_folder:
        input_error_messages.append("Please Name your Output Folder")
    else:
        # Check if this folder already exists
        if os.path.exists(output_path):
            input_error_messages.append(f"The Output Folder Path: '{output_path}' already exists")

    # Check if User did not input a date
    if not date:
        input_error_messages.append("Please Select a Date to Group by")

    # Display error messages if any
    if input_error_messages:
        messagebox.showerror("User Input Error", "\n".join(input_error_messages))

        # User Input Errors Found
        return True
    
    # No User Input Errors
    return False


def open_output_folder(output_destination, output_folder_name):
    # Create the full path to the results folder
    output_path = os.path.join(output_destination, output_folder_name)

    # Check to make sure output folder was generated
    if not os.path.exists(output_path):
        messagebox.showerror("Error", "Output Folder Not Yet Generated!")
        return
    
    # Open the Folder
    os.startfile(output_path)