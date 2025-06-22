import logging

def setup_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Optional: Simpan ke file log
    fh = logging.FileHandler('bot.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger