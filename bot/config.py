import configini
import logging

configini.read('config.ini')


class Config:
    token = configini.String('bot', 'token')

    if configini.Boolean('bot', 'debug', default=False):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    class Reaction:
        correct = configini.String('reaction', 'correct', default='✅')
        wrong = configini.String('reaction', 'wrong', default='❌')
        wrong_message = configini.String('reaction', 'wrong_message', default="{user} ruined it at {number}! Next number is 1.")
