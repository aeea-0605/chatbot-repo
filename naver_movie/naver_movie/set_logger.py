import logging


class LogFilter(logging.Filter):
    def filter(self, record):
        if 'Scrapying' in record.getMessage():
            return True


class ConsoleFilter(logging.Filter):
    def filter(self, record):
        allow_texts = ['Pipeline Started.', 'Item to DB inserted.', 'Pipeline Closed.']
        for text in allow_texts:
            if text in record.getMessage():
                return True


def make_f_handler(name, save_path):
    f_handler = logging.FileHandler(filename=f"{save_path}/{name}.log")
    formatter = logging.Formatter(
        'LOG:: %(asctime)s - %(name)s = %(levelname)s - %(message)s'
    )
    f_handler.setFormatter(formatter)

    return f_handler