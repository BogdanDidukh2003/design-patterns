from models import Customer


class CustomerManager:
    def __init__(self, session):
        self.session = session

    def get_all_customers(self):
        return self.session.query(Customer).all()

    def get_customer(self, customer_id):
        return self.session.query(Customer).filter(
            Customer.id == customer_id).one_or_none()

    def add_customer(self, name, email, phone_number, address, operator_id=None):
        customer = Customer()
        customer.name = name
        customer.email = email
        customer.phone_number = phone_number
        customer.address = address
        customer.operator_id = operator_id
        self.session.add(customer)

    def remove_customer(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            self.session.delete(customer)

    def add_customer_from_csv(self, customer_headers, customer_data):
        customer = Customer()
        customer.from_csv(customer_headers, customer_data)
        self.session.add(customer)
