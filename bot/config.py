import configini
import logging

configini.read('config.ini')


class Config:
    # Discord token needed to connect
    token = configini.String('bot', 'token')

    # Turn on debugging inside terminal
    if configini.Boolean('bot', 'debug', default=False):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Bot reactions strings
    class Reaction:
        correct = configini.String('reaction', 'correct', default='✅')
        wrong = configini.String('reaction', 'wrong', default='❌')
        wrong_message = configini.String('reaction', 'wrong_message', default="{user} ruined it at {number}! Next number is 1.")
