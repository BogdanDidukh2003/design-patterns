import CSVLoader


class ImportController:
    def __init__(self, customer_manager, operator_manager):
        self.customer_manager = customer_manager
        self.operator_manager = operator_manager

    def load_data_from_csv(self, filename):
        parsed_csv = CSVLoader.parse_csv(filename)
        operator_headers, operator_datalist = parsed_csv['operator']
        customer_headers, customer_datalist = parsed_csv['customer']
        for operator_data in operator_datalist:
            self.operator_manager.add_operator_from_csv(
                operator_headers, operator_data)
        for customer_data in customer_datalist:
            self.customer_manager.add_customer_from_csv(
                customer_headers, customer_data)
