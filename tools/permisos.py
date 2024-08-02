import os
import stat

def check_file_permissions(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                print(f"File: {file_path}")
                print(f"  Readable: {bool(file_stat.st_mode & stat.S_IRUSR)}")
                print(f"  Writable: {bool(file_stat.st_mode & stat.S_IWUSR)}")
                print(f"  Executable: {bool(file_stat.st_mode & stat.S_IXUSR)}")
            except Exception as e:
                print(f"Error checking {file_path}: {e}")

# Usa la ruta a tu carpeta de assets
assets_path = r"C:\Workspace\Economic_Analysis\assets"
check_file_permissions(assets_path)