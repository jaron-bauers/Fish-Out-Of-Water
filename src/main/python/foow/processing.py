import os


def create_folders(output_destination, results_folder_name):
    folder_paths = []

    # Create the full path to the results folder
    results_folder_name = os.path.join(output_destination, results_folder_name)

    os.makedirs(results_folder_name)

    # Append path to Array
    folder_paths.append(results_folder_name.replace('\\', '/'))
        
    # Subfolders to create within the main folder
    subfolders = ['Archived', 'Review', 'Discard']

    for subfolder_name in subfolders:
        # Create the full path to the subfolder
        subfolder_path = os.path.join(results_folder_name, subfolder_name)

        # Create the subfolder
        os.makedirs(subfolder_path)

        # Append path to Array
        folder_paths.append(subfolder_path.replace('\\', '/'))

    return folder_paths


def execution(on_complete, selected_folder_path, output_destination, results_folder, confidence_level):
    # creates the needed folders to store images and returns their path in an array
    folder_paths = create_folders(output_destination, results_folder)

    # VALIDATION
    print("Path to Images: ", selected_folder_path)
    print("Path to Generated Folders: ", folder_paths)
    print("Confidence Level: ", confidence_level)

    # rest of execution will go here

    # get rid of progress bar
    on_complete()
