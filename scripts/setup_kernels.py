import json
import subprocess
import os
import sys

# Function to execute setup commands
def execute_command(command, kernel_name, dry_run=False):
    try:
        if dry_run:
            print(f"[DRY RUN] Would execute: {command}")
        else:
            print(f"Executing: {command}")
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed for kernel '{kernel_name}': {command}")
        raise e


# Main function to load and process kernels
def setup_kernels(json_path, dry_run=False):
    try:
        with open(json_path, 'r') as f:
            kernels = json.load(f)

        # Process each kernel
        for kernel in kernels.get('kernels', []):
            print(f"\nSetting up kernel: {kernel['name']} ({kernel['description']})")

            # Run installation steps
            steps = kernel.get('installation_steps', [])
            total_steps = len(steps)
            for idx, step in enumerate(steps, 1):
                print(f"Step {idx}/{total_steps}: {step}")
                execute_command(step, kernel['name'], dry_run)

            print(f"Kernel '{kernel['name']}' setup complete.")

    except FileNotFoundError:
        print(f"Error: The file {json_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in kernels.json.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Define the path to the JSON configuration
    json_path = os.path.join(os.getcwd(), 'config', 'kernels.json')

    # Check for --dry-run flag
    dry_run = "--dry-run" in sys.argv

    print(f"Kernel setup starting (dry_run={dry_run})...")
    setup_kernels(json_path, dry_run)
