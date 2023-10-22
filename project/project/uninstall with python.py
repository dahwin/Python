import subprocess

# Run the Control Panel and the "uninstall a program" utility
subprocess.run(["control.exe", "/name", "Microsoft.ProgramsAndFeatures"])

# Wait for the utility to open
time.sleep(5)

# Simulate pressing the "Enter" key to select Firefox from the list of programs
subprocess.run(["powershell.exe", "Send-Keys", "-Keys", "Enter"])

# Wait for the uninstallation process to start
time.sleep(5)

# Simulate pressing the "Enter" key to confirm the uninstallation
subprocess.run(["powershell.exe", "Send-Keys", "-Keys", "Enter"])

# Wait for the uninstallation to complete
time.sleep(60)
# import win32api
#
# win32api.ShellExecute(
#     0,
#     "runas",
#     "msiexec.exe",
#     "/x {product code} /quiet",
#     None,
#     1
# )
