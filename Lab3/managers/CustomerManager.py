from models import Customer


class CustomerManager:
    def __init__(self, session):
        self.session = session

    def get_all_customers(self):
        with self.session() as s:
            customer_list = s.query(Customer).all()
        return customer_list

    def get_customer(self, customer_id):
        with self.session() as s:
            customer = s.query(Customer).filter(
                Customer.id == customer_id).one_or_none()
        return customer

    def add_customer(self, name, email, phone_number, address, operator_id=None):
        with self.session() as s:
            customer = Customer()
            customer.name = name
            customer.email = email
            customer.phone_number = phone_number
            customer.address = address
            customer.operator_id = operator_id
            s.add(customer)
            s.flush()
            customer_id = customer.id
            s.commit()
        return customer_id

    def remove_customer(self, customer_id):
        is_deleted = False
        with self.session() as s:
            customer = s.query(Customer).filter(
                Customer.id == customer_id).one_or_none()
            if customer:
                s.delete(customer)
                s.commit()
                is_deleted = True
        return is_deleted

    def add_customer_from_csv(self, customer_headers, customer_data):
        with self.session() as s:
            customer = Customer()
            customer.from_csv(customer_headers, customer_data)
            s.add(customer)
            s.commit()
