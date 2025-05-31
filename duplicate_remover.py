import os
import hashlib
#createdbyrahulrachari
def get_file_hash(file_path):
    """Returns the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(directory):
    """Removes duplicate files in the specified directory and its subdirectories."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            
            if file_hash in hashes:
                print(f"Deleting duplicate: {file_path}")
                os.remove(file_path)
            else:
                hashes[file_hash] = file_path

# Set directory_path to the current working directory
directory_path = os.getcwd()
remove_duplicates(directory_path)
