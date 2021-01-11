class ConfigFile():
    def __init__(self):
        self.LAPTOP = False
        self.DESKTOP = False
        self.AMHOME = False
        self.CSVPATH = ""
        self.DOCUMENTS = ""
        self.DEFAULT_DB = ""
        self.OSDPATH = ""
        self.JSDATABASE = ""
        self.JSON_DATABASE = ""
        self.LIBREPORT = 2002
        self.TESTDBNAME = "QuizDB"

    def __str__(self):
        return str(self.__dict__)
