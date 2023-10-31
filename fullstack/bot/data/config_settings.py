import configparser
import os
from pathlib import Path

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file, encoding='utf-8')
        
    def get_token(self):
        return self.config.get('settings', 'bot_token')
    
    def set_token(self, token):
        self.config.set('settings', 'bot_token', str(token))
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        
config = Config(r'fullstack\bot\config.ini')

