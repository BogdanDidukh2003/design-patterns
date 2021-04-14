from models import Customer, Operator


class ConversationManager:
    def __init__(self, session):
        self.session = session

    def get_conversation(self, customer_id):
        conversation_dict = None
        with self.session() as s:
            customer = s.query(Customer).filter(
                Customer.id == customer_id).one_or_none()
            if customer and customer.operator_id:
                conversation_dict = {
                    'customer_id': customer_id,
                    'operator_id': customer.operator_id,
                }
        return conversation_dict

    def get_all_conversations(self):
        with self.session() as s:
            customers = s.query(Customer).filter(
                Customer.operator_id != None).all()
            conversation_list = [
                {'customer_id': customer.id,
                 'operator_id': customer.operator_id}
                for customer in customers]
        return conversation_list

    def add_conversation(self, customer_id):
        conversation_dict = None
        with self.session() as s:
            customer = s.query(Customer).filter(
                Customer.id == customer_id).one_or_none()
            if customer is None:
                return None
            elif customer.operator_id:
                conversation_dict = {
                    'customer_id': customer_id,
                    'operator_id': customer.operator_id,
                }
            else:
                operator = s.query(Operator).filter(
                    Operator.is_available == 1).first()
                if operator:
                    customer.operator_id = operator.id
                    operator.is_available = False
                    conversation_dict = {
                        'customer_id': customer_id,
                        'operator_id': customer.operator_id,
                    }
                    s.commit()
        return conversation_dict

    def remove_conversation(self, customer_id):
        is_deleted = False
        with self.session() as s:
            customer = s.query(Customer).filter(
                Customer.id == customer_id).one_or_none()
            if customer.operator_id:
                operator = self.session.query(Operator).filter(
                    Operator.id == customer.operator_id).one_or_none()
                if operator:
                    customer.operator_id = None
                    operator.is_available = True
                    is_deleted = True
                    s.commit()
        return is_deleted
