import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\davud\PycharmProjects\demoQA\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common', 'baseURL')
        return url


