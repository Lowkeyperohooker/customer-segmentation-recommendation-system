import json
import subprocess
import sys

def install_requirements(requirements_file):
    try:
        # Open the JSON file
        with open(requirements_file, 'r') as file:
            data = json.load(file)
        
        # Install core dependencies
        if "dependencies" in data:
            print("Installing core dependencies...")
            dependencies = [
                f"{pkg}{version}" 
                for pkg, version in data["dependencies"].items()
            ]
            subprocess.check_call([sys.executable, "-m", "pip", "install", *dependencies])
            print("Core dependencies installed successfully!")
        
        # Install development dependencies
        if "devDependencies" in data:
            print("Installing development dependencies...")
            dev_dependencies = [
                f"{pkg}{version}" 
                for pkg, version in data["devDependencies"].items()
            ]
            subprocess.check_call([sys.executable, "-m", "pip", "install", *dev_dependencies])
            print("Development dependencies installed successfully!")

    except FileNotFoundError:
        print(f"Error: The file {requirements_file} was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in requirements.json.")
    except subprocess.CalledProcessError as e:
        print(f"Error: A subprocess error occurred while installing dependencies: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    requirements_file = "requirements.json"  # Path to your requirements.json file
    install_requirements(requirements_file)
