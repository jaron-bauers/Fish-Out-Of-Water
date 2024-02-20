
def prepare_images(on_complete, selected_folder_path, output_destination, results_folder, date):
    # Sorting Images by Inputted Date Execution

    # VALIDATION
    print("Path to Images: ", selected_folder_path)
    print("Path to Generated Folders: ", output_destination)
    print("Output Folder Name: ", results_folder)
    print("Date to Group by: ", date)

    # get rid of progress bar
    on_complete()
