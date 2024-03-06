import hashlib

def hash_file(filepath):
    print("Calculate SHA-256 hash of a file.")
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def compare_files(file1, file2):
    print("Enhanced compare two files using SHA-256 hashes and byte-by-byte comparison.")
    
    #comparing the SHA-256 hashes
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 != hash2:
        return False  # if hash1 not matches with hash2 the it return false and shows that files are not identical
    
    # if hashes are identical then we're performing byte-by-byte comparison
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            b1 = f1.read(1)
            b2 = f2.read(1)
            if b1 != b2:
                return False  # if return false it means there is a difference in byte comparison
            if not b1:
                return True  # if return true, it means there is no difference in both files
