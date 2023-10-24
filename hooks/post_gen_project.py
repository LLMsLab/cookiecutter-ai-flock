import json
import platform
import os
import subprocess
import shutil

def modify_vscode_settings():
    """
    Modify the VS Code settings file to set the correct Python
    interpreter path based on the OS.

    This function reads the .vscode/settings.json file, modifies the
    python.defaultInterpreterPath setting based on the user's operating
    system, and then writes the modified settings back to the file.
    """
    print(f"Current working directory: {os.getcwd()}") 
    # Define the path to the settings.json file
    settings_path = os.path.join('.vscode', 'settings.json')
    print(f"Settings path: {settings_path}")

    # Open and read the settings.json file
    with open(settings_path, 'r', encoding='utf-8') as f:
        print(f"File contents: {f.read()}")  # This line is for debugging
        f.seek(0)  # Reset file pointer to the beginning
        settings = json.load(f)

    # Check the operating system
    if platform.system() == 'Windows':
        # Get the username from the environment
        username = os.environ.get('USERNAME')
        if username:
            # Set the correct Python interpreter path for Windows
            settings["python.defaultInterpreterPath"] = f"C:\\Users\\{username}\\Anaconda3\\envs\\{{cookiecutter.environment_name}}\\python.exe"
        else:
            # Print a warning if the username could not be obtained
            print("Could not obtain username from environment. You may need to manually update the settings.json file.")
    else:
        # Set the correct Python interpreter path for MacOS
        settings["python.defaultInterpreterPath"] = "/anaconda/envs/{{cookiecutter.environment_name}}/bin/python"

    # Open and write the modified settings to the settings.json file
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=4)

def ensure_script_executable():
    """
    Ensure that this script is executable.

    This function uses the subprocess module to run a chmod command that
    sets the executable permission on this script file.
    """

    # Check if the operating system is Unix-like
    if platform.system() in ["Linux", "Darwin"]:  # Darwin is the OS name for MacOS
        # Get the absolute path to this script file
        script_path = os.path.abspath(__file__)

        # Run the chmod command to set the executable permission
        subprocess.run(["chmod", "+x", script_path])

def copy_os_specific_readme():
    """
    Copy the correct README.md file to the project root based on the OS.
    """
    # Get the username from the environment
    username = os.environ.get('USERNAME')
    if not username:
        print("Could not obtain username from environment. You may need to manually copy the README file.")
        return  # Exit the function if the username could not be obtained
    
    # Construct the base directory path
    base_dir = f'C:\\Users\\{username}\\.cookiecutters\\cookiecutter-rag'

    # Determine the operating system
    os_type = 'windows' if platform.system() == 'Windows' else 'macos'

    # Define the paths to the source and destination README.md files
    src_readme_path = os.path.join(base_dir, 'os_specific_files', f'README_{os_type}.md')
    
    # Get the current working directory
    cwd = os.getcwd()
    
    # The destination directory is the current working directory
    dest_readme_path = os.path.join(cwd, 'README.md')

    print(f"Src README: {src_readme_path}")  # Debugging line
    print(f"Dest README: {dest_readme_path}")  # Debugging line

    # Ensure the source README file exists before attempting to copy
    if not os.path.exists(src_readme_path):
        print(f"Source file does not exist: {src_readme_path}")
        return  # Exit the function if the file does not exist

    # Ensure the destination directory exists
    os.makedirs(cwd, exist_ok=True)

    # Copy the appropriate README.md file to the project root
    shutil.copy(src_readme_path, dest_readme_path)

    # Now read the contents of the README file, substitute the placeholders,
    # and write it back to the file.
    with open(dest_readme_path, 'r') as file:
        file_contents = file.read()

    # Substitute placeholders
    file_contents = file_contents.replace('{{cookiecutter.project_name}}', '{{cookiecutter.project_name}}')
    file_contents = file_contents.replace('{{cookiecutter.description}}', '{{cookiecutter.description}}')

    # Write the modified contents back to the file
    with open(dest_readme_path, 'w') as file:
        file.write(file_contents)
    
if __name__ == "__main__":
    # Ensure the script is executable
    ensure_script_executable()

    # Modify the VS Code settings
    modify_vscode_settings()

    # Copy the OS-specific README.md file
    copy_os_specific_readme()
