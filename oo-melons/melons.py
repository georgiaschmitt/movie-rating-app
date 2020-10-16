"""Classes for melon orders."""
import random
from datetime import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty

    def get_base_price(self):
        """ Caculate base price based on splurge pricing """
        return random.randint(5,9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price() * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order, needs to pass inspection and exempt from tax"""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.order_type = 'government'
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed == 'passed':
            self.passed_inspection = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
