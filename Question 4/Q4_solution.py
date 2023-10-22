## Question 4
import os
import shutil
import sys
from datetime import datetime


def backup_files(source_directory, final_directory):
    ## Checking if specified source directory exists
    try:
        if not os.path.exists(source_directory):
            raise FileNotFoundError(f"Source Directory '{source_directory}' does not exist.")
            
        ## Creating destination directory if it doesn't exist already
        ## Specify exist_ok to True to let the existing directory remain unaltered.
        os.makedirs(final_directory, exist_ok=True)

        ## Iterate through the files in source directory
        for filename in os.listdir(source_directory):
            ## Append the filenames to the source and final directory paths
            source_directory_file_path = os.path.join(source_directory,filename)
            final_directory_file_path = os.path.join(final_directory,filename)

            ## Appending the current time in Year, month, day, hour, minute 
            ## and second format onto source file if it exists already in final directory
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            ## Use while statement to check the presence of the existing file with same name as in source directory
            while os.path.exists(final_directory_file_path):
                head, tail = os.path.splitext(filename)
                filename = "f{head}_{timestamp}{extension}"
                final_directory_file_path = os.path.join(final_directory,filename)


                ## Copy the files from source to final directory using copy2 module
                shutil.copy2(source_directory_file_path,final_directory_file_path)
                print(f"Copied:{filename}")
            print("Back Successfully Completed")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")      
        
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Inputs incorrect. Specify inputs in the following format")
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)