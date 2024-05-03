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

        def add_user(self, user):
            if isinstance(user, User):
                self._users.append(user)
            else:
                raise ValueError('Invalid user type')

        def remove_user(self, user_id):
            for user in self._users:
                if user.get_id() == user_id:
                    self._users.remove(user)
                    return
            raise ValueError('User not found')


# Меню для взаимодействия с системой

def main_menu():
    while True:
        print("Выберите действие:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Просмотреть список пользователей")
        print("4. Выход")



