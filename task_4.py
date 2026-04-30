class User:
    """
    A class representing a website user.
    """

    def __init__(self, id: int, nick_name: str, first_name: str,
                 last_name: str = '', middle_name: str = '', gender: str = '') -> None:
        """
        Initialize a user with required and optional attributes.

        Args:
            id (int): Unique user ID.
            nick_name (str): User's nickname.
            first_name (str): User's first name.
            last_name (str): User's last name (optional).
            middle_name (str): User's middle name (optional).
            gender (str): User's gender (optional).
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id=None, nick_name=None, first_name=None, last_name=None,
               middle_name=None, gender=None) -> None:
        """
        Update user attributes. Pass None or empty string to skip updating.
        """
        if id is not None:
            self.id = id
        if nick_name is not None and nick_name != '':
            self.nick_name = nick_name
        if first_name is not None and first_name != '':
            self.first_name = first_name
        if last_name is not None and last_name != '':
            self.last_name = last_name
        if middle_name is not None and middle_name != '':
            self.middle_name = middle_name
        if gender is not None and gender != '':
            self.gender = gender

    def __str__(self) -> str:
        """
        Return a string representation of the user.
        """
        # Build full name from non-empty parts
        name_parts = [self.last_name, self.first_name, self.middle_name]
        name = ' '.join(part for part in name_parts if part)

        result = f"ID: {self.id} LOGIN: {self.nick_name} NAME: {name}"

        if self.gender:
            result += f" GENDER: {self.gender}"

        return result

    def __repr__(self) -> str:
        """
        Return a string representation for debugging.
        """
        return self.__str__()


user_1 = User(12, 'alex', 'Алексей')
print(user_1)
user_2 = User(44, 'andru', 'Андрей', 'Петров')
print(user_2)
user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
print(user_3)
user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'M')
print(user_4)
user_5 = User(47, 'ann', 'Анна', gender='F')
print(user_5)
user_4.update(0, '', 'Ваня')
print(user_4)
user_3.update(15, '', 'Никита', '', 'Петрович')
print(user_3)
users = []
users.append(user_2)
users.append(user_4)
users.append(user_5)
users.append(user_1)
users.append(user_3)
print(users)
