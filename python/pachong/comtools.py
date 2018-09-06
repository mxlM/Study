#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import inspect
import sys
import logging


def initLog_file():
    # create logger
    logger = None
    logger = logging.getLogger("longbo.log")
    logger.setLevel(logging.DEBUG)
    # logfilename =  ("./log/" + getCurrentDay() + ".log")
    logfilename = "./log/longbo.log"
    fh = logging.FileHandler(logfilename)
    # create console handler and set level to debug
    fh.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # add formatter to ch
    fh.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(fh)
    return logger


logger = initLog_file()


def whoami():
    return inspect.stack()[1][3]


def whosdaddy():
    return inspect.stack()[2][3]


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


def now():
    # 2010-01-01 00:00:00
    return unicode(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def printException():
    errmsg = " ".join(
        (str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(whosdaddy()), str(sys.exc_info()[2].tb_lineno)))
    print errmsg
    logger.error(errmsg)
    print now(), errmsg


def printInfo(info, _lineno=lineno(), level="info"):
    print now(), info
    try:
        try:
            logmsg = "called:[{0}] line:[{1}] info: {2}".format(whosdaddy(), _lineno, info)
        except:
            logmsg = u"called:[{0}]:line:[{1}] info: {2} -- unicode error".format(whosdaddy(), _lineno, info)

        logger.info(logmsg)
    except:
        print info
