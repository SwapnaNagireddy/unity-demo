import subprocess
import os
import sys

# 1. Path to your Unity Editor (Verify this path on your Mac!)
# Usually: /Applications/Unity/Hub/Editor/<VERSION>/Unity.app/Contents/MacOS/Unity
UNITY_EXE = "/Applications/Unity/Hub/Editor/6000.4.2f1/Unity.app/Contents/MacOS/Unity"

def run_build():
    print("Starting Automated Unity Build...")
    
    # These are the 'Batch Mode' commands that run Unity without a window
    build_command = [
        UNITY_EXE,
        "-batchmode",
        "-projectPath", os.getcwd(),
        "-executeMethod", "BuildScript.PerformBuild",
        "-quit",
        "-nographics",
        "-logFile", "unity_build_log.txt"
    ]

    try:
        # This triggers the process
        process = subprocess.run(build_command, check=True)
        print("Build Pipeline Finished Successfully!")
    except subprocess.CalledProcessError:
        print("Build Failed! Check unity_build_log.txt for details.")
        sys.exit(1)

if __name__ == "__main__":
    run_build()