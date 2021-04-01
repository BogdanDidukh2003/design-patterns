from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.Person import Person
from models.Customer import Customer


class Operator(Person):
    __tablename__ = 'operator'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    email = Column(String, ForeignKey('person.email'), nullable=False)
    is_available = Column('is_available', Boolean, default=True)
    customer = relationship('Customer', foreign_keys=[Customer.operator_id],
                            uselist=False, back_populates='operator')

    def __str__(self) -> str:
        return super().__str__()

    def get_personal_info(self):
        info = super(Operator, self).get_personal_info()
        info['is_available'] = self.is_available
        return info

    def validate_header_value(self, header, value):
        value = super().validate_header_value(header, value)
        if header == 'id':
            value = int(value)
        elif header == 'is_available':
            value = int(value)
        return value
