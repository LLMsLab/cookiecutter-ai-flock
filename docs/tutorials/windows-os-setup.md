# Setting Up a Python Environment on Windows OS

Welcome to the setup guide for creating a Python environment on a
Windows OS machine without admin rights and behind a firewall. This
guide will walk you through all the prerequisites and steps required to
set up a Python development environment, ensuring you can work
seamlessly even with limited permissions on your Windows machine.

In the following sections, you will find instructions on installing
essential tools like Visual Studio Code, Anaconda, and Git Bash without
requiring administrative privileges. We'll also provide guidance on
configuring your environment behind a firewall, ensuring a smooth setup
process for your project.

Follow these steps carefully to get your Python environment up and
running, and you'll be well-equipped to dive into your project. Let's
get started!

## Instructions

!!! note

    Before you can get started with this project, you'll need to
    have the following software installed on your Windows machine.

### Prerequisites

**Visual Studio Code (VS Code):**

- Download and install VS Code by following the instructions on the
  official website: [VS Code
  Download](https://code.visualstudio.com/download)
- During the installation process, choose an installation location
  within a directory where you have write permissions, typically
  within your user directory, `C:/Users/[Username]/`. You should not
  encounter any admin rights issues during the installation of VS
  Code.

**Anaconda Distribution:**

- Download the Anaconda Distribution for Windows from the official
  website: [Anaconda
  Download](https://www.anaconda.com/products/distribution)
- Follow these steps to install Anaconda without admin rights:
    - During the Anaconda installation process, when you reach the
      "Advanced Options" section, select the "Install for me only"
      option.
    - Choose a directory location where you have write permissions
      (e.g., your user directory) for the installation.
    - Complete the installation process.

**Git Bash:**

- Download and install Git Bash, which provides a Unix-like
  command-line environment for Windows: [Git Bash
  Download](https://git-scm.com/downloads)
- During the installation, choose an installation location within a
  directory where you have write permissions (e.g., your user
  directory). You should not encounter any admin rights issues when
  installing Git Bash.

Once you have installed these prerequisites, you'll be ready to set up
and run this project on your Windows machine, even without admin
rights.

## Install Recommended VS Code Extensions

To ensure a consistent development environment and take advantage of
tools and configurations tailored for this project, it's advisable to
install the extensions specified in the `.vscode/extensions.json` file.

Follow the steps below:

1. **Start by opening the project in Visual Studio Code.**
2. Access the Extensions panel:
    - Click the square icon on the sidebar
    - Or press `Ctrl+Shift+X`
3. Once in the Extensions panel:
    - Type `@recommended` in the search bar. This filters and displays
      the list of recommended extensions for the project.
4. **Install the extensions:** For every listed recommended extension,
   press the `Install` button to incorporate it into your VS Code.

## Enable the Usage of Conda Commands from the Git Bash Terminal in VS Code

Follow the steps below to get started:

### 1. Identify Anaconda Installation Path

- Open the `Anaconda Prompt` from the Start menu.
- Type the command below and press `Enter`:
  
  ```bash title="Anaconda Prompt"
  conda info
  ```

- Look for the line starting with `base environment :`. This displays
  the path to your Anaconda installation.

### 2. Activate Conda in Git Bash

- Start `VS Code`.
- Open a new terminal, making sure it's `Git Bash`.
- Run the following command, substituting the path with your specific
  Anaconda installation path:

  ```bash title="Bash"
  . C:/Users/[Username]/Anaconda3/etc/profile.d/conda.sh
  ```

### 3. Automate Conda Activation

To ensure Conda activates automatically every time you launch the
integrated Git Bash terminal in VS Code:

#### Determine `.bashrc` and `.bash_profile` location

In the integrated Git Bash terminal of VS Code, run:

```bash title="Bash"
echo $HOME
```

!!! note

    `.bashrc` and `.bash_profile` might be hidden. Turn on the 'view
    hidden files' option in File Explorer.

#### If these files are absent in your home directory:

!!! info

    In Windows OS, the home directory for a user is typically located at
    `C:/Users/[Username]/`, where `[Username]` is the name of the user
    account. When using tools that are Unix-based or Unix-like (e.g., Git
    Bash), the concept of the "home" directory often maps to this path.

    When you're in Git Bash, for instance, referencing `~` (the tilde
    symbol) will typically point to this directory. So if you run a command
    like `cd ~` in Git Bash, it would take you to `C:/Users/[Username]/`.

##### a. Open the integrated Git Bash terminal in VS Code

You can do this by selecting the Git Bash option from the terminal
dropdown in VS Code or by setting it as the default terminal.

##### b. Create the `.bashrc` File

Enter this command to generate a `.bashrc` file in your home directory:

```bash title="Bash"
touch ~/.bashrc
```

This `touch` command produces an empty `.bashrc` file if it's missing.

##### c. Create the `.bash_profile` File

To create the `.bash_profile` file, use:

```bash title="Bash"
touch ~/.bash_profile
```

##### d. Edit the `.bash_profile` File

To edit the file using VS Code's built-in editor, run:

```bash title="Bash"
code ~/.bash_profile
```

Once opened in VS Code, incorporate these lines:

```bash title="Bash"
if [ -f ~/.bashrc ]; then
  source ~/.bashrc
fi
```

Save and close the file.

##### e. Edit the `.bashrc` File

To edit the `.bashrc` file in VS Code, use:

```bash title="Bash"
code ~/.bashrc
```

Then, append:

```bash title="Bash"
. C:/Users/[Username]/Anaconda3/etc/profile.d/conda.sh
```

Remember to replace `[Username]` with your actual username. Save and
close the file once done.

##### f. Apply the Changes

Apply your changes by either restarting the integrated Git Bash terminal
in VS Code or by sourcing the `.bash_profile` file:

```bash title="Bash"
source ~/.bash_profile
```

Every time you initiate a new Bash session within VS Code, the `.bashrc`
file gets sourced automatically due to the `.bash_profile`
configuration. This setup loads the Conda configuration in `.bashrc`,
enabling the use of Conda commands.

### 4. Verify Conda Activation

- Shut and reopen the Git Bash terminal in `VS Code`.
- Enter `conda activate` and hit `Enter`. If `(base)` appears in the
  terminal, the base Conda environment is active.

With these steps complete, you can now utilize Conda commands from the
Git Bash terminal in VS Code on Windows. Whenever you launch a new
Git Bash terminal in VS Code, Conda activates automatically,
streamlining your Conda environment and package management tasks.

## Install Linux Tools on Git Bash

When you lack admin rights on a Windows machine, system-wide software
installations become tricky. Yet, for your local environment, like Git
Bash, there's a way. For instance, to install the `make` tool, follow
the steps below.

### What is `make`?

`make` is a utility controlling the creation of executables and other
non-source program files.

### Steps to Add `make` to Git Bash

#### 1. Download the Tool

Head over to
[ezwinports](https://sourceforge.net/projects/ezwinports/files/) and get
`make-4.4.1-without-guile-w32-bin.zip`.

!!! note "Reference"

    **Reference**: Check this
    [article](https://www.pascallandau.com/blog/setting-up-git-bash-mingw-msys2-on-windows/)
    for a more comprehensive setup guide.

#### 2. Extract the Download

Unpack the contents to, say,
`C:\Users\[Username]\Tools\make-4.4.1-without-guile-w32-bin`.

#### 3. Update the `$PATH` in Git Bash

Run the following commands:

```bash title="Bash"
echo 'export PATH=$PATH:C:\\Users\\[Username]\\Tools\\make-4.4.1-without-guile-w32-bin\\bin' >> ~/.bashrc
source ~/.bashrc
```

This is how your `.bashrc` profile should now appear:

```bash title="Bash"
. C:/Users/[Username]/Anaconda3/etc/profile.d/conda.sh
export PATH=$PATH:C:\\Users\\[Username]\\Tools\\make-4.4.1-without-guile-w32-bin\\bin
```

#### 4. Verify Installation

At this point, you should be able to run `make` commands from Git Bash.

!!! note

    Tools added this way are localized to your Git Bash environment for
    your user profile. They won't be accessible in other command-line
    interfaces unless their paths receive similar adjustments.
  
    Some tools might come with dependencies. Make it a habit to peruse
    documentation or README files to guarantee all requisite components
    are in place.

## Install Poetry for Dependency Management

Here are the steps to install Poetry in the NYL Windows machine
without admin access and firewall.

##### Disconnect VPN

Disconnect your VPN is it is connected.

##### Update Conda

Open the Anaconda PowerShell Prompt and update your Conda installation:

```bash title="Anaconda Prompt"
conda update conda
```

##### Install Poetry for Package Management

Following the Poetry's docs, let's install Poetry with `pipx`. First
install `pipx`:

```bash title="Anaconda Prompt"
pip install pipx
```

Install Poetry using `pipx`:

```bash title="Anaconda Prompt"
pipx install poetry
```

Output:

```bash title="Anaconda Prompt"
installed package poetry 1.6.1, installed using Python 3.9.18

These apps are now globally available

- poetry.exe

⚠️ Note: 'C:\\Users\\[Username]\\.local\\bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is
updated. Run pipx ensurepath to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).

done! ✨ 🌟 ✨
```

It looks like Poetry was installed successfully using Pipx, but the
`.local/bin`folder where the poetry executable is installed is not in
your PATH environment variable.

Since you don't have admin access to modify the PATH globally, you need
to update it just for your user account.

Since we are using `.bashrc` and `.bash_profile` files for our shell
configuration on Windows, here is how you can automatically add Poetry's
path to our `PATH`. Add the following line to your `.bash_profile`:

```bash title="Bash"
export PATH=$PATH:C:\\Users\\[Username]\\.local\\bin
```

Your `.bashrc` must looks like this:

```bash title="Bash"
# Add Anaconda to PATH
# Sourcing this script initializes Conda and adds it to the PATH
# This gives access to Conda, Python and any packages installed in the default Conda env
# This give access to Conda command from Git Bash integrated in VS Code
. C:/Users/[Username]/Anaconda3/etc/profile.d/conda.sh
# Add Make to PATH
# This adds the Make (GNU make) bin folder containing make.exe to the PATH
# Now Make can be run from any directory in the Git Bash terminal integrated in VS Code
export PATH=$PATH:C:\\Users\\[Username]\\Tools\\make-4.4.1-without-guile-w32-bin\\bin
# Add Poetry to PATH
# Poetry is used for Python dependency and package management
# It was installed using Pipx into the ~/.local/bin folder
# Adding this folder to PATH makes the poetry command globally available
# Now Make can be run from any directory in the Git Bash terminal integrated in VS Code
export PATH=$PATH:C:\\Users\\[Username]\\.local\\bin
# General notes:
# - Use single quotes for Windows paths
# - Escape spaces and special characters in paths
# - Export PATH additions to make commands globally available
# - Source scripts like conda.sh to initialize environments
# - Restart shell or run source ~/.bashrc after making changes
```

Now, restart your Git Bash terminal integrated in VS Code or run `source
~/.bashrc` and validate the Poetry command is available:

```bash title="Bash"
$ poetry --version
Poetry (version 1.6.1)
(base) 
```

Notice that the Conda `base` environment must be activated to validate
that `conda`, `make` and, `poetry` commands are available on Git Bash:

```bash title="Bash"
[Username]@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ conda activate
(base) 
[Username]@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ conda --version
conda 23.9.0
(base) 
[Username]@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ make --version
GNU Make 4.4.1
Built for Windows32
Copyright (C) 1988-2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
(base) 
[Username]@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ poetry --version
Poetry (version 1.6.1)
(base) 
```
