import logging

logging.basicConfig(
    filename="log.log",
    encoding="utf8",
    format='%(asctime)s#%(name)s#%(levelname)s#%(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger("Monitor")
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
logging.debug('Debug')  # will not print anything
logging.error('error')  # will not print anything
logging.critical('critical')  # will not print anything