from sqlalchemy import Column, Integer, String
from models.Base import Base


class Person(Base):
    __tablename__ = 'person'

    email = Column('email', String, primary_key=True)
    name = Column('name', String)
    phone_number = Column('phone_number', String, unique=True)
    address = Column('address', String)

    def __str__(self) -> str:
        return self.get_personal_info().__str__()

    def get_personal_info(self):
        info = {
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
        }
        if hasattr(self, 'id'):
            info['id'] = self.id
        return info

    def from_csv(self, headers: str, values: str, sep=','):
        headers_list = headers.split(sep)
        values_list = values.split(sep)
        assert len(headers_list) == len(values_list)
        for header, value in zip(headers_list, values_list):
            if hasattr(self, header):
                value = self.validate_header_value(header, value)
                setattr(self, header, value)

    def validate_header_value(self, header, value):
        return value
