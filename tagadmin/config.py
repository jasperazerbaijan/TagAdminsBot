import os


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("3588368", None))
    API_HASH = os.environ.get("3d64c47cfe8d1cb0fc2cc06f5512298e", None)
    TG_BOT_TOKEN = os.environ.get("1696209895:AAFshFqsclUgRbeQxtpCb4Yvj15mgi2wT58", None)
    OWNER_ID = int(os.environ.get("94008646", None))
    TMP_DIR = os.environ.get("TMP_DIR", "./TEMP/")
    CHANNEL = os.environ.get("CHANNEL", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")
    CONTACT_OWNER = os.environ.get("CONTACT_OWNER", None)
    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    ENV = os.environ.get("ENV", True)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
