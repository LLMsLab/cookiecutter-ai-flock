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

    This function determines the user's operating system, and then
    copies the appropriate README.md file from the os_specific_files
    directory to the root of the generated project.
    """

    # Determine the operating system
    os_type = 'windows' if platform.system() == 'Windows' else 'macos'

    # Get the absolute path to the current working directory
    cwd = os.path.abspath(os.getcwd())

    # Define the paths to the source and destination README.md files
    src_readme_path = os.path.join(cwd, '..', 'os_specific_files', f'README_{os_type}.md')
    dest_readme_path = os.path.join(cwd, '{{cookiecutter.project_slug}}', 'README.md')

    print(f"Src README: {src_readme_path}")  # Debugging line
    print(f"Dest README: {dest_readme_path}")  # Debugging line
    
    # Ensure the source README file exists before attempting to copy
    if not os.path.exists(src_readme_path):
        print(f"Source file does not exist: {src_readme_path}")
        return  # Exit the function if the file does not exist

    # Copy the appropriate README.md file to the project root
    shutil.copy(src_readme_path, dest_readme_path)

if __name__ == "__main__":
    # Ensure the script is executable
    ensure_script_executable()

    # Modify the VS Code settings
    modify_vscode_settings()

    # Copy the OS-specific README.md file
    copy_os_specific_readme()
