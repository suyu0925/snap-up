import os
import configparser
from jd_logger import logger


class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            if config_file == 'config.ini':
                # 如果config.ini不存在，尝试读取config-template.ini
                self._path = os.path.join(os.getcwd(), 'config-template.ini')
                if not os.path.exists(self._path):
                    raise FileNotFoundError("No such file: config.ini")
                else:
                    logger.info('use config-template.ini instead of config.ini')
            else:
                raise FileNotFoundError("No such file: config.ini")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


global_config = Config()
