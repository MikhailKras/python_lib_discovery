from loguru import logger

logger.add(
    "logs/catch_decorator_{time:DD-MM-YY}.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="100 KB",
    compression="zip"
)


def divide(a, b):
    return a / b


@logger.catch
def main():
    divide(1, 0)


main()
