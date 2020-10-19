"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first, last, email, password):
            self.first = first
            self.last = last
            self.email = email
            self.password = password 

    def __repr__(self):
        return f'<Customer: {self.first}, {self.last}, {self.email}, {self.password}>'

def read_customer_types_from_file(filepath):

    customers_dict = {}

    with open(filepath) as file:
        for line in file:
            first, last, email, password = line.rstrip().split('|')
    
            customers_dict[email] = Customer(first, last, email, password)

    return customers_dict

def get_by_email(email):
    return customers_dict[email]

customers_dict = read_customer_types_from_file('customers.txt')