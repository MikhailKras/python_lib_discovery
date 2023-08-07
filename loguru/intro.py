from loguru import logger

logger.add(
    "logs/intro.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="100 KB",
    compression="zip"
)
for _ in range(1000):
    logger.debug('This is debug')
    logger.info('This is info')
    logger.error('This is error')
