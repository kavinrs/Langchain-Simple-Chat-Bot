import logging

# logging.basicConfig(filename="summa.log",level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(levelno)s",filemode="w")

logger=logging.getLogger(__name__)

logger.setLevel(logging.INFO)

f=logging.Formatter("%(asctime)s-%(levelname)s-%(levelno)s")

file=logging.FileHandler("summa.log")

file.setFormatter(f)
logger.addHandler(file)


logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")