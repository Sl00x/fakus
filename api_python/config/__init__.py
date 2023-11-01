import os
from pathlib import Path
from configparser import ConfigParser

dir = Path(__file__).parent
configuration_dir = dir / '../env.ini'

parser = ConfigParser(os.environ)
parser.read(configuration_dir, encoding="utf8")


class Config():
    @staticmethod
    def read(section, property, default=None):
        return parser.get(section, property) or default
