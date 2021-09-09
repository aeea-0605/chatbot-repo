import configparser


config = configparser.ConfigParser()
config.read("../data.ini")
db_info = config["db"]