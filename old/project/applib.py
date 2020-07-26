import logging
import pymysql
from time import asctime

from flask import Flask


# Debug
def debug(datei="server.log"):
    logging.basicConfig(filename=datei,format='%(asctime)s %(message)s',  datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
    logging.error('Error: ')
    logging.critical('Kritischer Fehler!!!!!: ')


# SQL Allgemein
def AnmeldungSQL(ip, db_nutzer, db_paswort):
    #    ip = input("Bitte Server IP eingeben: ")
    #    db_nutzer = input("Datenbanknutzer eingeben: ")
    #    db_paswort = input("Passwort eingeben: ")
    global db
    db = pymysql.connect(ip, db_nutzer, db_paswort)


def AbmeldungSQL():
    db.close()
    print("Verbindung wurde zu Datenbank beendet!")


def AuswahlDB(db):
    db.select_db(db=db)