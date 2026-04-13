import subprocess
import os
import sys

def run_build():
    # Retrieve the path we set in TeamCity Parameters
    unity_path = os.getenv("UNITY_PATH")

    print(f"🛠 Starting Production Unity Build on Agent...")

    # If Unity isn't there, we fail the build immediatelyyy
    if not unity_path or not os.path.exists(unity_path):
        print(f"ERROR: UNITY_PATH is missing or invalid: {unity_path}")
        print("Please check TeamCity Agent Parameters.")
        sys.exit(1) 

    # build command
    build_command = [
        unity_path,
        "-batchmode",
        "-projectPath", os.getcwd(),
        "-executeMethod", "BuildScript.PerformBuild",
        "-quit",
        "-nographics",
        "-logFile", "unity_build_log.txt"
    ]

    try:
        print(f"Launching Unity from: {unity_path}")
        subprocess.run(build_command, check=True)
        print("Real Unity Build Finished Successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Unity Build Failed with exit code {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_build()