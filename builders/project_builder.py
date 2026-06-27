from pathlib import Path
import json

class ProjectBuilder:

    def run(self):
        print("="*50)
        print("YouTube Production System v0.4")
        print("="*50)

        title=input("Video Title: ")
        summary=input("Video Summary: ")
        duration=input("Duration (minutes): ")
        project=input("Project Folder (Video001): ")

        root=Path("projects")/project

        folders=[
            "01_project",
            "02_script",
            "03_storyboard",
            "04_images/generated",
            "05_audio",
            "06_video",
            "07_publish"
        ]

        for folder in folders:
            (root/folder).mkdir(parents=True,exist_ok=True)

        project_json={
            "title":title,
            "summary":summary,
            "duration":duration,
            "language":"English",
            "voice":"Indian Female",
            "audience":"Global",
            "style":"Emotional"
        }

        (root/"01_project"/"project.json").write_text(
            json.dumps(project_json,indent=4)
        )

        (root/"02_script"/"script.md").write_text("# Script\n")
        (root/"02_script"/"script_prompt.md").write_text(
            "Generate a script from project.json"
        )
        (root/"03_storyboard"/"storyboard.md").write_text("# Storyboard\n")
        (root/"04_images"/"image_prompts.md").write_text("# Image Prompts\n")
        (root/"05_audio"/"README.md").write_text("Voiceover goes here.")
        (root/"06_video"/"README.md").write_text("Video assets.")
        (root/"07_publish"/"README.md").write_text("Thumbnail, metadata, upload.")

        print("\nProject created successfully!")
        print(root.resolve())
