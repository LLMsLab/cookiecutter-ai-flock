import json
import platform
import os
import subprocess
import shutil
from cookiecutter.main import cookiecutter

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
    os_type = '{{ cookiecutter.os_type }}'
    project_slug = '{{ cookiecutter.project_slug }}'
    
    # Specify the correct path to your cookiecutter template directory
    username = os.getenv('USERNAME')
    target_directory = os.path.join("C:", "Users", username, "OneDrive - New York Life", "Documents", "Projects")
    source_filename = os.path.join(template_dir, f'READMEs\\README_{os_type.lower()}.md')
    
    # Use the _output_dir variable to get the path to the generated project
    target_directory = '{{ cookiecutter._output_dir }}'
    target_filename = os.path.join(target_directory, 'README.md')
    print(target_directory)
    print(target_filename)
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    shutil.copy(source_filename, target_filename)

if __name__ == "__main__":
    # Ensure the script is executable
    ensure_script_executable()

    # Modify the VS Code settings
    modify_vscode_settings()

    # Copy the OS-specific README.md file
    copy_os_specific_readme()
