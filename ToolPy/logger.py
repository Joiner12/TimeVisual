# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:25:14 2022

@author: W-H
"""

import logging
import random


class Logger:

    Logger = None

    def __init__(self,
                 logging_service="chongbuluo",
                 enable_notifications=False):
        # Logger setup
        self.Logger = logging.getLogger(f"{logging_service}_logger")
        self.Logger.setLevel(logging.DEBUG)
        self.Logger.propagate = False
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # default is "logs/chongbuluo_log.log"
        fh = logging.FileHandler(f"{logging_service}.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.Logger.addHandler(fh)

        if enable_notifications:
            # logging to console
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            self.Logger.addHandler(ch)

    def log(self, message, level="info", notification=True):

        if level == "info":
            self.Logger.info(message)
        elif level == "warning":
            self.Logger.warning(message)
        elif level == "error":
            self.Logger.error(message)
        elif level == "debug":
            self.Logger.debug(message)

    def info(self, message, notification=True):
        self.log(message, "info", notification)

    def warning(self, message, notification=True):
        self.log(message, "warning", notification)

    def error(self, message, notification=True):
        self.log(message, "error", notification)

    def debug(self, message, notification=False):
        self.log(message, "debug", notification)


if __name__ == "__main__":
    test_logger = Logger()
    log_level = ['info', 'warning', 'error', 'debug']
    for i in range(10):
        test_logger.log("message", level=log_level[random.randint(0, 3)])
