from django.db import models


class User:
    def __int__(self, username, email):
        self.username = username
        self.email = email


class Project:
    def __init__(self, name, platform, terms, price):
        self.name = name
        self.platform = platform
        self.terms = terms
        self.price = price


class Detail:
    def __int__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity


class InvestmentView:
    def __init__(self, details, products_for_year, product_cost, years):
        self.details = details
        self.products_for_year = products_for_year
        self.product_cost = product_cost
        self.years = years
