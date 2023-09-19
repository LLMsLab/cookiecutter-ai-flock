# How-to-Guides

## Checking and Installing Essential Bash Tools on Ubuntu

### Introduction

When configuring a new Ubuntu system – be it a server or a workstation –
ensuring that all requisite tools and commands are available is crucial,
especially for tasks involving scripting, development, or data management. This
guide outlines a systematic methodology for ensuring all essential Bash tools
are in place.

### 1. Attempt Direct Installation

Often, the name of the command is identical to the name of the package it
belongs to. Given this, a direct installation attempt for each tool can swiftly
ensure that a large portion of them are installed. Execute the following:

```bash
PACKAGES="make tree grep sed awk cut sort uniq wc tr paste split cat \
head tail find xargs tee parallel curl wget jq htop tmux \
screen git ncdu tldr csvkit rename terraform perl vim join \
pandoc lsof ripgrep more less zip unzip tar gzip \
gunzip bzip2 xz rsync dd fdupes top ps pgrep pkill at"

for package in $PACKAGES; do
    sudo apt install -y $package
done
```

This step, while not exhaustive, will help in getting the common tools up and
running promptly.

### 2. Verify Tool Availability

After attempting a direct installation, it's prudent to check which tools are
actually present. This can be achieved through the script below:

```bash
for package in $PACKAGES; do
    if command -v $package > /dev/null 2>&1; then
        echo "$package is installed."
    else
        echo "$package is NOT installed."
    fi
done
```

This script inspects the availability of each tool by trying to invoke it. If a
tool is accessible, the script confirms its installation; otherwise, it flags it
as missing.

### 3. Addressing Missing Tools

For the tools reported as missing:

1. Try running the tool with the `--version` flag, for instance, `pdftotext
   --version`. 
2. Ubuntu is generally helpful and will suggest the apt package that contains
   the missing tool, if it's available.
3. Proceed with the suggested `sudo apt install [package-name]` command to get
   the tool installed.

An example:

```
Command 'pdftotext' not found, but can be installed with:
sudo apt install poppler-utils
```

Follow the system's advice (`sudo apt install poppler-utils` in this case) to
install the necessary tool.

**Note**: While Ubuntu typically suggests packages for recognized tools, this
might not be the case for all. In such scenarios, a manual lookup on package
repositories or web resources might be necessary.