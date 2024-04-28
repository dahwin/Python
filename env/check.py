import subprocess
import os
import requests
# Run the 'python --version' command in a subprocess and capture the output
process = subprocess.Popen(["python", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the subprocess to complete
output, error = process.communicate()
output = output.decode()

# Print the output and error
print("Output:", output)

if "3.11" in output:
    print("Python 3.11 is installed")
else:
    print("Python 3.11 is not installed. Installing...")


    filename = "python-3.11.7-amd64.exe"
    url = "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"

    # Check if the file already exists in the current directory
    if not os.path.isfile(filename):
        # File doesn't exist, so download it
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)
            print(f"Download of {filename} completed.")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")
    else:
        print(f"{filename} already exists. Skipping download.")


    # Run the install_python.cmd script using subprocess
    install_process = subprocess.Popen(["install_python.cmd"], shell=True)
    install_process.wait()

    print("Installation complete")






