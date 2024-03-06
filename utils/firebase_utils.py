from firebase_admin import credentials, storage, initialize_app
import os
from config import settings
import time
from utils.file_utils import compare_files

import logging
logger = logging.getLogger(__name__)

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
initialize_app(cred, {'storageBucket': settings.STORAGE_BUCKET})

def upload_large_file(file_path, destination_blob_name):
    try:
        start_time = time.time()
        
        bucket = storage.bucket()
        blob = bucket.blob(destination_blob_name)
        
        blob.chunk_size = 5 * 1024 * 1024  # 5MB
        
        logger.info("File upload started")
        print("Starting upload...")
        blob.upload_from_filename(file_path, timeout=300)
        
        elapsed_time = time.time() - start_time

        uploadTime = f"File {file_path} uploaded to {destination_blob_name} in {elapsed_time:.2f} seconds."
        logger.info(uploadTime)
        print(uploadTime)
    except Exception as e:
        errorMessage = f"Failed to upload {file_path}. Error: {e}"
        logger.error(errorMessage)
        print(errorMessage)
        return
    
    # After uploading file then we're downloading the file for comparison
    try:
        print("Starting download for comparison...")
        downloaded_file_path = f"downloaded_{os.path.basename(file_path)}"
        blob.download_to_filename(downloaded_file_path)
        print(f"Downloaded file for comparison to {downloaded_file_path}")
        
        if compare_files(file_path, downloaded_file_path):
            print("Verification successful: The uploaded file matches the original file.")
        else:
            print("Verification failed: The uploaded file does not match the original file.")
    except Exception as e:
        print(f"Failed to download {destination_blob_name} for comparison. Error: {e}")
