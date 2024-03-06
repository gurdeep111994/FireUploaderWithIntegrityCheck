from utils.firebase_utils import upload_large_file
from datetime import datetime

from utils.log_config import setup_logging
setup_logging()

import logging
logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")
    file_path = 'filesToUpload/recs_small_dict.pkl'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_blob_name = f'uploads/recs_small_dict_{timestamp}.pkl'
    upload_large_file(file_path, destination_blob_name)
    logger.info("File upload and comparison process done")

if __name__ == "__main__":
    main()
