class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Singleton()
        return cls._instance

singleton_instance = Singleton.get_instance()
