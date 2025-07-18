import os
import shutil

def estimate_time(content: str):
    words = len(content.split())
    if words < 300:
        return "1–2 days"
    elif words < 600:
        return "2–3 days"
    return "4+ days"

def zip_project(base_path: str):
    if not os.path.exists(base_path):
        print(f"❌ Cannot zip: Folder '{base_path}' does not exist.")
        return

    shutil.make_archive(base_path, 'zip',
        root_dir=os.path.dirname(base_path),
        base_dir=os.path.basename(base_path)
    )
    print(f"📦 Project zipped at: {base_path}.zip")
