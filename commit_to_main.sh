#!/bin/bash

# Check if the current branch is 'main'
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "You are currently on branch '$current_branch'. Switching to 'main'..."
    git checkout main
    if [ $? -ne 0 ]; then
        echo "Error: Failed to switch to 'main' branch. Please resolve any issues and try again."
        exit 1
    fi
else
    echo "You are already on the 'main' branch."
fi

# Stage all changes
echo "Staging all changes..."
git add .
if [ $? -ne 0 ]; then
    echo "Error: Failed to stage changes. Please check your repository and try again."
    exit 1
fi

# Commit changes with a provided message or default message
read -p "Enter a commit message (or press Enter to use 'Update from Codespace'): " commit_message
commit_message=${commit_message:-"Update from Codespace"}

echo "Committing changes with message: '$commit_message'..."
git commit -m "$commit_message"
if [ $? -ne 0 ]; then
    echo "Error: Commit failed. Please resolve any issues and try again."
    exit 1
fi

# Push changes to the remote 'main' branch
echo "Pushing changes to 'main' branch..."
git push origin main
if [ $? -ne 0 ]; then
    echo "Error: Push failed. Please resolve any issues and try again."
    exit 1
fi

echo "Changes successfully pushed to the 'main' branch!"

# copy paste to terminal to execute
# chmod +x commit_to_main.sh
# ./commit_to_main.sh