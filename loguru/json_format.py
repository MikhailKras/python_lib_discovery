from loguru import logger

logger.add(
    "logs/json_format_{time:DD-MM-YY}.json",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="100 KB",
    compression="zip",
    serialize=True
)

logger.info("This is info")

def divide(a, b):
    return a / b


@logger.catch
def main():
    divide(1, 0)


main()