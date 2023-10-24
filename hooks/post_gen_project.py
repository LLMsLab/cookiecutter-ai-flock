# import json
# import platform
# import os
# import subprocess
# import shutil
# import logging
# from cookiecutter.main import cookiecutter
# from pathlib import Path

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)

# def modify_vscode_settings(cookiecutter_env_name):
#     """
#     Modify the VS Code settings file to set the correct Python
#     interpreter path based on the OS.
#     """
#     logging.info(f"Current working directory: {os.getcwd()}") 
#     # Define the path to the settings.json file
#     settings_path = os.path.join('.vscode', 'settings.json')
#     logging.info(f"Settings path: {settings_path}")

#     # Open and read the settings.json file
#     try:
#         with open(settings_path, 'r', encoding='utf-8') as f:
#             settings = json.load(f)
#     except FileNotFoundError:
#         logging.error(f"File not found: {settings_path}")
#         return

#     # Check the operating system
#     if platform.system() == 'Windows':
#         # Get the username from the environment
#         username = os.environ.get('USERNAME')
#         if username:
#             # Set the correct Python interpreter path for Windows
#             settings["python.defaultInterpreterPath"] = f"C:\\Users\\{username}\\Anaconda3\\envs\\{cookiecutter_env_name}\\python.exe"
#         else:
#             # Log a warning if the username could not be obtained
#             logging.warning("Could not obtain username from environment. You may need to manually update the settings.json file.")
#     else:
#         # Set the correct Python interpreter path for MacOS
#         settings["python.defaultInterpreterPath"] = f"/anaconda/envs/{cookiecutter_env_name}/bin/python"

#     # Open and write the modified settings to the settings.json file
#     with open(settings_path, 'w') as f:
#         json.dump(settings, f, indent=4)

# def ensure_script_executable():
#     """
#     Ensure that this script is executable.
#     """
#     # Check if the operating system is Unix-like
#     if platform.system() in ["Linux", "Darwin"]:
#         # Get the absolute path to this script file
#         script_path = os.path.abspath(__file__)

#         # Run the chmod command to set the executable permission
#         subprocess.run(["chmod", "+x", script_path])

# def copy_os_specific_readme(template_dir, output_dir):
#     os_type = '{{ cookiecutter.os_type }}'
#     project_slug = '{{ cookiecutter.project_slug }}'
    
#     # Use the pathlib module to handle paths
#     source_filename = Path(template_dir) / 'READMEs' / f'README_{os_type.lower()}.md'
    
#     # Use the _output_dir variable to get the path to the generated project
#     target_directory = output_dir
#     target_filename = Path(target_directory) / 'README.md'
#     logging.info(f"Target directory: {target_directory}")
#     logging.info(f"Target filename: {target_filename}")
    
#     # Ensure the target directory exists
#     os.makedirs(target_directory, exist_ok=True)
    
#     shutil.copy(str(source_filename), str(target_filename))

# if __name__ == "__main__":
#     # Ensure the script is executable
#     ensure_script_executable()

#     # Modify the VS Code settings
#     cookiecutter_env_name = '{{ cookiecutter.environment_name }}'
#     modify_vscode_settings(cookiecutter_env_name)
