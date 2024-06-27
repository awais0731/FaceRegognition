


class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.dlims_distict_list = None
        return cls._instance

    def set_dlims_distict_list(self, dlims_distict_list):
        self.dlims_distict_list = dlims_distict_list

    def get_dlims_distict_list(self):
        return self.dlims_distict_list