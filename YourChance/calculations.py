from typing import List

from YourChance.models import Detail, InvestmentView


class Calculations:

    @staticmethod
    def calculate_full_income(self, investment_view: InvestmentView):
        details_cost = self.calculate_details_cost_for_product(investment_view.details)
        income_per_year = self.calculate_income_per_year(details_cost,
                                                         investment_view.products_for_year,
                                                         investment_view.product_cost)
        pure_income_per_year = self.calculate_pure_income_per_year(income_per_year)
        full_income = pure_income_per_year * investment_view.years
        return full_income

    @staticmethod
    def calculate_details_cost_for_product(details: List[Detail]):
        details_prices = []
        for detail in details:
            details_prices.append(detail.cost * detail.quantity)
        return sum(details_prices)

    @staticmethod
    def calculate_income_per_year(details_cost, products_for_year, product_cost):
        details_cost_for_one_year = details_cost * products_for_year
        income_per_year = products_for_year * product_cost - details_cost_for_one_year
        return income_per_year

    @staticmethod
    def calculate_pure_income_per_year(income_per_year):
        NDFL = 0.18  # Общий налог
        VS = 0.015  # Военный сбор
        pure_income_per_year = income_per_year - (income_per_year * NDFL + income_per_year * VS)
        return pure_income_per_year
