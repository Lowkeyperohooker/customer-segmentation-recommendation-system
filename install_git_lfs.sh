#!/bin/bash

# Check if Git LFS is installed
if ! git lfs --version > /dev/null 2>&1; then
    echo "Git LFS is not installed. Installing now..."
    sudo apt-get update
    sudo apt-get install git-lfs -y
    git lfs install
else
    echo "Git LFS is already installed."
fi

# Initialize Git LFS
echo "Initializing Git LFS..."
git lfs install

# Pull LFS-tracked files (run only if inside a Git repository)
if [ -d ".git" ]; then
    echo "Pulling LFS-tracked files..."
    git lfs pull
    echo "LFS-tracked files pulled successfully."
else
    echo "Not inside a Git repository. Skipping 'git lfs pull'."
fi

# Verify Git LFS installation
if git lfs --version > /dev/null 2>&1; then
    echo "Git LFS setup complete."
else
    echo "Error: Git LFS installation or setup failed."
    exit 1
fi

# Recreate .gitattributes if missing
if [ ! -f .gitattributes ]; then
    echo "Creating .gitattributes file to track CSV files with Git LFS..."
    echo "*.csv filter=lfs diff=lfs merge=lfs -text" > .gitattributes
    git add .gitattributes
    git commit -m "Add .gitattributes to track CSV files with Git LFS"
    git push
else
    echo ".gitattributes file already exists."
fi

# Ensure data.csv is tracked by Git LFS
if git lfs ls-files | grep -q "data.csv"; then
    echo "data.csv is already tracked by Git LFS."
else
    echo "Tracking data.csv with Git LFS..."
    git lfs track "data.csv"
    git add data.csv .gitattributes
    git commit -m "Track data.csv with Git LFS"
    git push
fi

# Force download the LFS-tracked file
echo "Pulling LFS-tracked files..."
git lfs pull

echo "Checking out LFS-tracked files..."
git lfs checkout

# Verify the content of data.csv
if [ -f data.csv ]; then
    echo "data.csv is now ready. Here is a preview:"
    head -n 10 data.csv
else
    echo "Error: data.csv is still missing or not properly downloaded."
    exit 1
fi

echo "Script completed successfully!"



#  code in terminal
# ls
# chmod +x install_git_lfs.sh
#  ./install_git_lfs.sh