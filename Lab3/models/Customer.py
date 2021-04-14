from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.Person import Person


class Customer(Person):
    __tablename__ = 'customer'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    email = Column(String, ForeignKey('person.email'), nullable=False)
    operator_id = Column(Integer, ForeignKey('operator.id'), nullable=True)
    operator = relationship('Operator', foreign_keys=[operator_id], back_populates='customer')

    def __str__(self) -> str:
        return super().__str__()

    def get_personal_info(self):
        info = super(Customer, self).get_personal_info()
        info['operator_id'] = self.operator_id
        return info

    def validate_header_value(self, header, value):
        value = super().validate_header_value(header, value)
        if header == 'id':
            value = int(value)
        elif header == 'operator_id':
            value = int(value) if value else None
        return value
