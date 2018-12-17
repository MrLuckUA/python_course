class Contact:
    def __init__(self, first_name: str, second_name: str, phone_number: str):
        self._first_name = first_name
        self._second_name = second_name
        self._phone_number = phone_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def second_name(self):
        return self._second_name

    @property
    def phone_number(self):
        return self._phone_number

    @first_name.setter
    def first_name(self, name: str):
        self._first_name = name

    @second_name.setter
    def second_name(self, surname: str):
        self._second_name = surname

    @phone_number.setter
    def phone_number(self, number: str):
        self._phone_number = number
