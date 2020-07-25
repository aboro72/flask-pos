import logging
from time import asctime

from flask import Flask


def debug(datei="server.log"):
    logging.basicConfig(filename=datei,format='%(asctime)s %(message)s',  datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
    logging.error('Error: ')
    logging.critical('Kritischer Fehler!!!!!: ')


