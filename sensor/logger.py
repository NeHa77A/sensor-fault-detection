import logging
import os
from datetime import datetime
from from_root import from_root

LOGS = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path =os.path.join(from_root(),"logs", LOGS)
# for creating a file
os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path,LOGS)

# writing logs
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
