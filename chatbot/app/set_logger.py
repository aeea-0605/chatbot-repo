import logging


class Logger:
    def __init__(self, name, save_path):
        self.name = name
        self.save_path = save_path
        self.logger = self.make_logger()


    def make_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)

        f_handler = logging.FileHandler(filename=f"{self.save_path}/{self.name}.log")
        formatter = logging.Formatter(
            'LOG:: %(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        f_handler.setFormatter(formatter)

        logger.addHandler(f_handler)

        return logger