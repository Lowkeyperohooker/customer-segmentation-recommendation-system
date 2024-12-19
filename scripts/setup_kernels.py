import json
import subprocess
import os
import sys


# Function to execute commands
def execute_command(command, kernel_name, dry_run=False):
    if isinstance(command, dict):  # Handle OS-specific commands
        platform = sys.platform
        if platform.startswith('linux') or platform == 'darwin':  # macOS or Linux
            command = command.get('linux_mac', '')
        elif platform.startswith('win'):  # Windows
            command = command.get('windows', '')
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    if not command:  # Skip if no command is provided for the platform
        print(f"Skipping command for '{kernel_name}': Not applicable on this platform.")
        return

    try:
        if dry_run:
            print(f"[DRY RUN] Would execute: {command}")
        else:
            print(f"Executing: {command}")
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed for kernel '{kernel_name}': {command}")
        raise e


# Main function to set up kernels
def setup_kernels(json_path, dry_run=False):
    try:
        with open(json_path, 'r') as f:
            kernels = json.load(f)

        for kernel in kernels.get('kernels', []):
            print(f"\nSetting up kernel: {kernel['name']} ({kernel['description']})")

            steps = kernel.get('installation_steps', [])
            total_steps = len(steps)
            for idx, step in enumerate(steps, 1):
                print(f"Step {idx}/{total_steps}: {step}")
                execute_command(step, kernel['name'], dry_run)

            print(f"Kernel '{kernel['name']}' setup complete.\n")
            print(f"Notes: {kernel.get('notes', 'No additional notes.')}")
            print(f"Kernel selection command: {kernel.get('select_kernel_command', 'N/A')}")

    except FileNotFoundError:
        print(f"Error: The file {json_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in kernels.json.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    json_path = os.path.join(os.getcwd(), 'config', 'kernels.json')
    dry_run = "--dry-run" in sys.argv

    print(f"Kernel setup starting (dry_run={dry_run})...\n")
    setup_kernels(json_path, dry_run)
