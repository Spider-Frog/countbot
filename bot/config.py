import configini
import logging

configini.read('config.ini')


class Config:
    token = configini.String('bot', 'token')
    if configini.Boolean('bot', 'debug', default=False):
        logging.basicConfig(level=logging.DEBUG)

    class Messages:
        wrong_number = configini.String('messages', 'wrong_number', default="Wrong number! start again...")
