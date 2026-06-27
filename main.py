from pathlib import Path

print("="*50)
print("YouTube Production System")
print("="*50)

title=input("Video Title: ")
summary=input("Video Summary: ")
duration=input("Duration (minutes): ")
folder=input("Output Folder Name (e.g. Video001): ")

out=Path("output")/folder
(out/"images").mkdir(parents=True, exist_ok=True)

for f in ["README.md","script.md","storyboard.md","image_prompts.md","thumbnail.md","metadata.md","production_checklist.md"]:
    (out/f).touch()

for i in range(1,13):
    (out/"images"/f"Scene{i:02}.png").touch()

(out/"README.md").write_text(f"# {folder}\n\n## Title\n{title}\n\n## Summary\n{summary}\n\n## Duration\n{duration} minutes\n")
print("Project created:", out.resolve())
