import logging
import logging.handlers
import os

LOG_FOLDER = 'logs'
def initiate_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
   
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(asctime)s\t%(levelname)-7s\t%(name)-25s\t%(message)s', datefmt='%m-%d %H:%M:%S')
    ch_formatter.default_msec_format = '%s.%03d'
    ch.setFormatter(ch_formatter)

    INFO_FILENAME = os.path.join(LOG_FOLDER, 'info.log')
    fh_info = logging.handlers.TimedRotatingFileHandler(filename=INFO_FILENAME, when='midnight', interval=1, backupCount=2, utc=True)
    fh_info.setLevel(logging.INFO)
    fh_info_formatter = logging.Formatter('%(asctime)s\t%(levelname)-7s\t%(name)-25s\t%(message)s', datefmt='%m-%d %H:%M:%S')
    fh_info_formatter.default_msec_format = '%s.%03d'
    fh_info.setFormatter(fh_info_formatter)

    DEBUG_FILENAME = os.path.join(LOG_FOLDER, 'debug.log')
    fh_debug = logging.handlers.TimedRotatingFileHandler(filename=DEBUG_FILENAME, when='midnight', interval=1, backupCount=2, utc=True)
    fh_debug.setLevel(logging.DEBUG)
    fh_debug_formatter = logging.Formatter('%(asctime)s\t%(levelname)-7s\t%(name)-25s\t%(message)s', datefmt='%m-%d %H:%M:%S')
    fh_debug_formatter.default_msec_format = '%s.%03d'
    fh_debug.setFormatter(fh_debug_formatter)
    
    logger.addHandler(ch)
    logger.addHandler(fh_info)
    logger.addHandler(fh_debug)