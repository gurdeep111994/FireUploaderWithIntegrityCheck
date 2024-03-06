import logging
import os

def setup_logging():
    print("loaded setup logging function")
    log_dir = 'logs'
    log_file = 'app.log'
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=os.path.join(log_dir, log_file),
                        filemode='a')
