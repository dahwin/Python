import subprocess
import sys
import os


def install_package(env_name, package_name):
    # Install a package in the virtual environment
    # Use the Python executable inside the virtual environment
    python_executable = os.path.join(env_name, 'Scripts', 'python.exe')
    subprocess.run([python_executable, '-m', 'pip', 'install', package_name], check=True)

# Usage example
env_name = r'dahwin'  # Use raw string for Windows path
package_name = 'httpx'

install_package(env_name, package_name)

print(f"Package '{package_name}' has been installed in the virtual environment '{env_name}'.")
