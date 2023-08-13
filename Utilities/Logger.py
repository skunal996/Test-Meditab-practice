import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\Kunal -Credence\\Lectures & "
                                      "Notes\\Python\\Projects\\Testing_Meditab\\Logs\\Meditab.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %("
                                       "message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
