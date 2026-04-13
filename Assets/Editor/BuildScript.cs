using UnityEditor;
using System.IO;

public class BuildScript
{
    public static void PerformBuild()
    {
        // scenes to include
        string[] scenes = { "Assets/Scenes/SampleScene.unity" };
        
        // output path
        string buildPath = "Builds/Mac/Build.app";

        // directory
        string directory = Path.GetDirectoryName(buildPath);
        if (!Directory.Exists(directory))
        {
            Directory.CreateDirectory(directory);
        }

        // Run the build
        BuildPipeline.BuildPlayer(scenes, buildPath, BuildTarget.StandaloneOSX, BuildOptions.None);
        
        UnityEngine.Debug.Log("Pipeline Check: Build completed successfully at " + buildPath);
    }
}