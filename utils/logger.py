import logger 
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join (LOG_DIR, "log.txt")

os.makedirs (LOG_DIR, exist_ok= True)
logging.basicConfig (
    filename= LOG_FILE
    format= "%(asctime)s - %(levelname)s - %(messages)s",
    level= logging.INFO
)

def log_error(messege):
    logging.info (messege)
