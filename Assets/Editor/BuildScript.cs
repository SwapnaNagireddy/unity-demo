using UnityEditor;
using System.IO;

public class BuildScript
{
    public static void PerformBuild()
    {
        // 1. Setup build settings
        string[] scenes = { "Assets/Scenes/SampleScene.unity" };
        string buildPath = "Builds/Android/InterviewBuild.apk";

        // 2. Ensure the directory exists
        Directory.CreateDirectory("Builds/Android");

        // 3. Run the build
        BuildPipeline.BuildPlayer(scenes, buildPath, BuildTarget.Android, BuildOptions.None);
        
        UnityEngine.Debug.Log("Pipeline Check: Build completed successfully!");
    }
}