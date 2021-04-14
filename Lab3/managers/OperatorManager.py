from models import Operator


class OperatorManager:
    def __init__(self, session):
        self.session = session

    def get_all_operators(self):
        return self.session.query(Operator).all()

    def get_operator(self, operator_id):
        return self.session.query(Operator).filter(
            Operator.id == operator_id).one_or_none()

    def add_operator(self, name, email, phone_number, address, is_available=True):
        operator = Operator()
        operator.name = name
        operator.email = email
        operator.phone_number = phone_number
        operator.address = address
        operator.is_available = is_available
        self.session.add(operator)

    def remove_operator(self, operator_id):
        operator = self.get_operator(operator_id)
        if operator:
            self.session.delete(operator)

    def add_operator_from_csv(self, operator_headers, operator_data):
        operator = Operator()
        operator.from_csv(operator_headers, operator_data)
        self.session.add(operator)
