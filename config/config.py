import logging
import sys

from environs import Env

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')

logging.basicConfig(
    # filename='logfile.log',
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s: "
           "%(filename)s: "
           "%(levelname)s: "
           "%(funcName)s(): "
           "%(lineno)d:\t"
           "%(message)s",
)
