
class ConversationController:
    def __init__(self, customer_manager, operator_manager,
                 conversation_manager):
        self.customer_manager = customer_manager
        self.operator_manager = operator_manager
        self.conversation_manager = conversation_manager

    def get_customer(self, customer_id):
        return self.customer_manager.get_customer(customer_id)

    def get_all_customers(self):
        return self.customer_manager.get_all_customers()

    def add_customer(self, name, email, phone_number, address, operator_id=None):
        return self.customer_manager.add_customer(name, email, phone_number, address, operator_id)

    def update_customer(self, customer_id, name, email, phone_number, address,
                        operator_id=None):
        return self.customer_manager.update_customer(
            customer_id, name, email, phone_number, address, operator_id)

    def remove_customer(self, customer_id):
        return self.customer_manager.remove_customer(customer_id)

    def get_operator(self, operator_id):
        return self.operator_manager.get_operator(operator_id)

    def get_all_operators(self):
        return self.operator_manager.get_all_operators()

    def add_operator(self, name, email, phone_number, address, is_available=True):
        self.operator_manager.add_operator(name, email, phone_number, address, is_available)

    def remove_operator(self, operator_id):
        self.operator_manager.remove_operator(operator_id)

    def add_conversation(self, customer):
        self.conversation_manager.add_conversation(customer)

    def remove_conversation(self, customer):
        self.conversation_manager.remove_conversation(customer)
