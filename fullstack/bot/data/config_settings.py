import configparser

class Config:
    def __init__(self, config_name):
        self.config_name = config_name
        self.config = configparser.ConfigParser()
        self.config.read(self.config_name)
        
    def get(self, section, option):
        return self.config.get(section, option)