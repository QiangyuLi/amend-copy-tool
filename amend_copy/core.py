import os
import shutil

# List of available methods
AMEND_METHODS = ["mtime", "size", "both"]

def list_amend_methods():
    """Return a list of available amend comparison methods."""
    return AMEND_METHODS

def is_file_amended(src_path, dst_path, method="mtime"):
    """Determine if a file should be copied based on the selected method."""
    if not os.path.exists(dst_path):
        return True

    if method == "mtime":
        return os.path.getmtime(src_path) > os.path.getmtime(dst_path)

    elif method == "size":
        return os.path.getsize(src_path) != os.path.getsize(dst_path)

    elif method == "both":
        return (os.path.getmtime(src_path) > os.path.getmtime(dst_path) or
                os.path.getsize(src_path) != os.path.getsize(dst_path))

    else:
        raise ValueError(f"Unsupported amend method: {method}")

def amend_copy(src_folder, dst_folder, method="mtime"):
    """Copy only amended or new files from src to dst."""
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, src_folder)
            dst_file = os.path.join(dst_folder, rel_path)

            if is_file_amended(src_file, dst_file, method):
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src_file, dst_file)
