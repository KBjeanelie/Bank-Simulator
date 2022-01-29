from __future__ import annotations


class Account:
    def __init__(self):
        self.bank_code: int
        self.branch_code: int
        self.account_number: int
        self.tax: int | float
        self.customer_id: int

    def bank_code(self) -> int:
        """
            get the value of bank code
        :return: int
        """
        return self.bank_code

    def branch_code(self) -> int:
        """
            get the value of branch code
        :return: int
        """
        return self.branch_code

    def deposit(self, sum_add: float | int) -> bool:
        """
            allow the money deposit
            Return True if all is good
        :param sum_add: amount to deposit on account bank
        :return:True | False
        """

    def withdraw_money(self, sum_remove: float | int) -> bool:
        """
            Allow the withdrawing money in a current account bank on abject
            Return True if all is good
            We remove also a tax for this methode
        :param sum_remove: amount of withdrawing
        :return: True | False
        """

    def get_account_number(self):
        """
            get the all value of account bank number
        :return: str
        """
