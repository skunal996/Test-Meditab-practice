import configparser

config = configparser.RawConfigParser()
config_file_path = "D:\\Kunal -Credence\\Lectures & Notes\\Python\\Projects\\Testing_Meditab\\Configuration\\config.ini"
config.read(config_file_path)


class ReadConfig:

    @staticmethod
    def get_clinic():
        clinic = config.get('login data', 'Clinic')
        return clinic

    @staticmethod
    def get_user():
        user = config.get('login data', 'Username')
        return user

    @staticmethod
    def get_passwd():
        passwd = config.get('login data', 'Password')
        return passwd
