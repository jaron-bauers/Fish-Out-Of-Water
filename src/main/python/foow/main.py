import tkinter as tk
from tkinter import ttk
from gui import show_selected_folder, show_process_progress_bar, show_preperation_progress_bar, open_output_folder

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Fish Out of Water")

    # Set the initial size of the root window
    root.geometry("650x350")

    # Create a notebook (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Tab 1: Prepare Images
    prepare_tab = ttk.Frame(notebook)
    notebook.add(prepare_tab, text='Prepare Images')

    # Input folder path Description
    tk.Label(prepare_tab, text="Select Image Folder to Prepare:").grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    prepare_image_folder_path = tk.Text(prepare_tab, height=1, width=40)
    prepare_image_folder_path.grid(row=0, column=1, padx=10, pady=10)

    # Create a button to open the file explorer
    prepare_open_button = tk.Button(prepare_tab, text="Browse", command=lambda: show_selected_folder(prepare_image_folder_path))
    prepare_open_button.grid(row=0, column=2, padx=10, pady=10)

    # Output folder path Description
    tk.Label(prepare_tab, text="Output Destination:").grid(row=1, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    output_destination_tab_1 = tk.Text(prepare_tab, height=1, width=40)
    output_destination_tab_1.grid(row=1, column=1, padx=10, pady=10)

    # Create a button to open the file explorer
    prepare_open_button_2 = tk.Button(prepare_tab, text="Browse", command=lambda: show_selected_folder(output_destination_tab_1))
    prepare_open_button_2.grid(row=1, column=2, padx=10, pady=10)

    # Output folder path Description
    tk.Label(prepare_tab, text="Name Output Folder:").grid(row=2, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    results_folder_tab_1 = tk.Text(prepare_tab, height=1, width=40)
    results_folder_tab_1.grid(row=2, column=1, padx=10, pady=10)

    # Output folder path Description
    tk.Label(prepare_tab, text="Group by This Date:").grid(row=3, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    date = tk.Text(prepare_tab, height=1, width=40)
    date.grid(row=3, column=1, padx=10, pady=10)

    # Create a button to trigger image execution
    prepare_start_button = tk.Button(prepare_tab, text="Start Preperation", command=lambda: show_preperation_progress_bar(root, prepare_image_folder_path.get("1.0", tk.END).strip(), output_destination_tab_1.get("1.0", tk.END).strip(), results_folder_tab_1.get("1.0", tk.END).strip(), date.get("1.0", tk.END).strip()))
    prepare_start_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    # Create a button to open the generated output file
    open_output_folder_button_tab_1 = tk.Button(prepare_tab, text="Open Output Folder", command=lambda: open_output_folder(output_destination_tab_1.get("1.0", tk.END).strip(), results_folder_tab_1.get("1.0", tk.END).strip()))
    open_output_folder_button_tab_1.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    # Tab 2: Process Images (default tab)
    process_tab = ttk.Frame(notebook)
    notebook.add(process_tab, text='Process Images')

    # Output folder path Description
    tk.Label(process_tab, text="Select Image Folder to Process:").grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    process_image_folder_path = tk.Text(process_tab, height=1, width=40)
    process_image_folder_path.grid(row=0, column=1, padx=10, pady=10)

    # Create a button to open the file explorer
    process_open_button = tk.Button(process_tab, text="Browse", command=lambda: show_selected_folder(process_image_folder_path))
    process_open_button.grid(row=0, column=2, padx=10, pady=10)

    # Output folder path Description
    tk.Label(process_tab, text="Output Destination:").grid(row=1, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    output_destination_tab_2 = tk.Text(process_tab, height=1, width=40)
    output_destination_tab_2.grid(row=1, column=1, padx=10, pady=10)

    # Create a button to open the file explorer
    process_open_button_2 = tk.Button(process_tab, text="Browse", command=lambda: show_selected_folder(output_destination_tab_2))
    process_open_button_2.grid(row=1, column=2, padx=10, pady=10)

    # Output folder path Description
    tk.Label(process_tab, text="Name Output Folder:").grid(row=2, column=0, sticky="w", padx=10, pady=10)

    # Create a text box to display the selected folder path
    results_folder_tab_2 = tk.Text(process_tab, height=1, width=40)
    results_folder_tab_2.grid(row=2, column=1, padx=10, pady=10)

    # Create a label to describe the slider
    tk.Label(process_tab, text="Select Confidence Level:").grid(row=3, column=0, sticky="w", padx=10, pady=10)

    # Create a Scale widget (slider)
    confidence_level = tk.Scale(process_tab, from_=1, to=100, orient="horizontal", length=300)
    confidence_level.grid(row=3, column=1, padx=10, pady=10)

    # Create a button to trigger image execution
    process_start_button_tab_2 = tk.Button(process_tab, text="Start Processing", command=lambda: show_process_progress_bar(root, process_image_folder_path.get("1.0", tk.END).strip(), output_destination_tab_2.get("1.0", tk.END).strip(), results_folder_tab_2.get("1.0", tk.END).strip(), confidence_level.get()))
    process_start_button_tab_2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    # Create a button to open the generated output file
    open_output_folder_button_tab_2 = tk.Button(process_tab, text="Open Output Folder", command=lambda: open_output_folder(output_destination_tab_2.get("1.0", tk.END).strip(), results_folder_tab_2.get("1.0", tk.END).strip()))
    open_output_folder_button_tab_2.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    # Tab 3: Train TODO
    train_tab = ttk.Frame(notebook)
    notebook.add(train_tab, text='Train')

    # Add more widgets to the Train tab if needed...

    # Select the default tab as "Process Images"
    notebook.select(process_tab)

    # Run the Tkinter event loop
    root.mainloop()

main()
