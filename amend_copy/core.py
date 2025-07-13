import os
import shutil

def is_file_amended(src_path, dst_path):
    """Check if the file is new or modified (based on modified time)."""
    if not os.path.exists(dst_path):
        return True
    return os.path.getmtime(src_path) > os.path.getmtime(dst_path)

def amend_copy(src_folder, dst_folder):
    """Copy only amended or new files from src to dst."""
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, src_folder)
            dst_file = os.path.join(dst_folder, rel_path)

            if is_file_amended(src_file, dst_file):
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src_file, dst_file)
