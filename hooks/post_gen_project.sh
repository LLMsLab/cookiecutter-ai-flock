#!/bin/bash

# Redirect output to a file
exec > >(tee -a script_output.log) 2>&1

# Assign values from Cookiecutter variables
os_type="{{ cookiecutter.os_type }}"
project_slug="{{ cookiecutter.project_slug }}"
project_name="{{ cookiecutter.project_name }}"
description="{{ cookiecutter.description }}"
target_directory="{{ cookiecutter._output_dir }}"
username=$(echo "$USERPROFILE" | awk -F'\\' '{print $NF}')
template_dir="C:/Users/$username/.cookiecutters/cookiecutter-rag"

# Construct the source and target filenames
source_filename="$template_dir/READMEs/README_${os_type,,}.md"
target_filename="$target_directory/$project_slug/README.md"

# Print the directories and filenames for debugging
echo "Target Directory: $target_directory"
echo "Source Filename: $source_filename"
echo "Target Filename: $target_filename"

# Ensure the target directory exists
mkdir -p "$target_directory/$project_slug"

# Check if the source file exists and is readable
if [[ -r "$source_filename" ]]; then
    # Copy the file content
    cat "$source_filename" > "$target_filename"
else
    echo "Source file $source_filename not found or not readable"
    exit 1
fi

# Replace the placeholders with the actual project name and description
# Replace the placeholders with the actual project name and description
sed -i.bak -e "s/{{cookiecutter.project_name}}/$project_name/g" -e "s/{{cookiecutter.description}}/$description/g" "$target_filename"
"$target_filename" > temp.md && mv temp.md "$target_filename"

