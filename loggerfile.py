import logging

class LoggerFile():
    def set_logger(looger_name, log_file, level=logging.DEBUG):
        logger = logging.getLogger(looger_name)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setFormatter(formatter)
        stremhandler = logging.StreamHandler()
        stremhandler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(fileHandler)
        logger.addHandler(stremhandler)



