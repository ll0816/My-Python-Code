# !/usr/bin/python
# -*- coding: utf-8 -*-
# class
# Liu L.
# 12-06-15
# source: http://intermediatepythonista.com/classes-and-objects

class Account(object):

    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def del_account(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance

    def __getattr__(self, name):
        return "Sorry. I don't see any attribute called {}".format(name)

    @staticmethod
    def type():
        return "Current Account"

    @classmethod
    def from_dict(cls, **kwargs):
        params = kwargs
        return cls(params.get("name"), params.get("balance"))

if __name__ == "__main__":

    Liu = Account("Liu", 10)
    print "Liu's account type is", Liu.type()
    x = Account.from_dict(name = "Liu", balance = 100)
    print "x's balance is", x.inquiry()
    print x.number