from models import Customer, Operator


class ConversationManager:
    def __init__(self, session):
        self.session = session

    def add_conversation(self, customer):
        operator = self.session.query(Operator).filter(
            Operator.is_available == 1).one_or_none()
        print(operator)
        if operator:
            customer.operator_id = operator.id
            operator.is_available = False

    def remove_conversation(self, customer):
        if customer.operator_id:
            operator = self.session.query(Operator).filter(
                Operator.id == customer.operator_id).one_or_none()
            if operator:
                customer.operator_id = None
                operator.is_available = True
