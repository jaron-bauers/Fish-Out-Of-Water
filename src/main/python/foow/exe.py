import os
import time

def create_folders(on_complete):
    time.sleep(10)

    # Get the desktop path
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

    # Specify the main folder name
    main_folder_name = 'Results'
    
    # Create the full path to the main folder
    main_folder_path = os.path.join(desktop_path, main_folder_name)

    try:
        # Check if the main folder already exists
        if not os.path.exists(main_folder_path):
            # Create the main folder
            os.makedirs(main_folder_path)
            print(f"Folder '{main_folder_name}' created.")
        else:
            print(f"Folder '{main_folder_name}' already exists.")
            
        # Subfolders to create within the main folder
        subfolders = ['Archived', 'Review', 'Discard']

        for subfolder_name in subfolders:
            # Create the full path to the subfolder
            subfolder_path = os.path.join(main_folder_path, subfolder_name)

            try:
                # Check if the subfolder already exists
                if not os.path.exists(subfolder_path):
                    # Create the subfolder
                    os.makedirs(subfolder_path)
                    print(f"Subfolder '{subfolder_name}' created.")
                else:
                    print(f"Subfolder '{subfolder_name}' already exists.")
            except Exception as e:
                print(f"Error creating subfolder '{subfolder_name}': {e}")

        # Call the on_complete callback function
        on_complete()

    except Exception as e:
        print(f"Error creating main folder '{main_folder_name}': {e}")
        # Call the on_complete callback function even in case of an error
        on_complete()