from django.db import models
from django import forms


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Project:
    def __init__(self, name, platform, terms, price):
        self.name = name
        self.platform = platform
        self.terms = terms
        self.price = price
