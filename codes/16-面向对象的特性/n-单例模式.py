class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            inst = super().__new__(cls)
            cls._instance = inst
        return cls._instance

c1 = AppConfig()
c2 = AppConfig()
print(c1 is c2)