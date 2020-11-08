import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    # DATABASE_URI = f"{os.getenv('DATABASE')}://" \
    #                f"{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@" \
    #                f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/" \
    #                f"{os.getenv('DB_NAME')} "

    DATABASE_URL = os.getenv('DATABASE_URL')

    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))

    LOG_LEVEL = os.getenv('LOG_LEVEL')
