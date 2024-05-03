class User:

    def __init__(self, id, name, access_level="user"):
        self._id = id
        self._name = name
        self._access_level = access_level

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    class Admin("User"):

        def __init__(self, id, name):
            super().__init__(id, name, "admin")
            self._users = []
