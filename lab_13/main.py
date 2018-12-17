#!/usr/bin/env/python3
# -*- coding: utf8 -*-

from abc import ABC, abstractmethod


class Worker(ABC):

    def __init__(self, id, second_name, salary):
        self._id = id
        self._second_name = second_name
        self._salary = salary
        super().__init__()

    @abstractmethod
    def salary_with_tax(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Vasya(Worker):
    def salary_with_tax(self):
        return self.get_salary() - self.get_salary() * 0.32

    def get_salary(self):
        return self._salary


a = Vasya(123, 'Pupkin', 1000)
print(a.get_salary())
print(a.salary_with_tax())
