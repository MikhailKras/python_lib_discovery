import datetime
import gzip
import logging.handlers
import shutil


def namer(name):
    now = datetime.datetime.now()
    return f'{name}_{now.strftime("%d-%m-%y_%H-%M")}.gz'


def rotator(source, dest):
    with open(source, 'rb') as file_in:
        with gzip.open(dest, 'wb') as file_out:
            shutil.copyfileobj(file_in, file_out)


handler = logging.handlers.RotatingFileHandler('logs/rotating.log', maxBytes=512, backupCount=5)
f = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(f)
handler.namer, handler.rotator = namer, rotator
logger = logging.getLogger(__name__)
logger.addHandler(handler)
for i in range(1000):
    logger.warning(f'number {i}')
