from models import Operator


class OperatorManager:
    def __init__(self, session):
        self.session = session

    def get_all_operators(self):
        with self.session() as s:
            operator_list = [
                operator.get_personal_info()
                for operator in s.query(Operator).all()
            ]
        return operator_list

    def get_operator(self, operator_id):
        with self.session() as s:
            operator = s.query(Operator).filter(
                Operator.id == operator_id).one_or_none()
            if operator:
                operator = operator.get_personal_info()
        return operator

    def add_operator(self, name, email, phone_number, address, is_available=True):
        with self.session() as s:
            operator = Operator()
            operator.name = name
            operator.email = email
            operator.phone_number = phone_number
            operator.address = address
            operator.is_available = is_available
            s.add(operator)
            s.flush()
            operator_id = operator.id
            s.commit()
        return operator_id

    def update_operator(self, operator_id, name, email, phone_number,
                        address, is_available=None):
        operator_dict = None
        is_removed = self.remove_operator(operator_id)
        if is_removed:
            with self.session() as s:
                operator = Operator()
                operator.id = operator_id
                operator.name = name
                operator.email = email
                operator.phone_number = phone_number
                operator.address = address
                if is_available is not None:
                    operator.is_available = is_available
                s.add(operator)
                s.flush()
                operator_dict = operator.get_personal_info()
                s.commit()
        return operator_dict

    def remove_operator(self, operator_id):
        is_deleted = False
        with self.session() as s:
            operator = s.query(Operator).filter(
                Operator.id == operator_id).one_or_none()
            if operator:
                s.delete(operator)
                s.commit()
                is_deleted = True
        return is_deleted

    def add_operator_from_csv(self, operator_headers, operator_data):
        with self.session() as s:
            operator = Operator()
            operator.from_csv(operator_headers, operator_data)
            s.add(operator)
            s.commit()
