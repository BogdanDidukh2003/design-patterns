from flask import make_response, abort
from engine import conversation_controller


def read_one(customer_id):
    customer = conversation_controller.get_customer(customer_id)
    if customer:
        return customer.get_personal_info()
    abort(404, f'Customer with id `{id}` not found')


def read_all():
    data = conversation_controller.get_all_customers()
    data = [customer.get_personal_info() for customer in data]
    return data


def create(customer):
    name = customer.get('name', None)
    email = customer.get('email', None)
    phone_number = customer.get('phone_number', None)
    address = customer.get('address', None)
    operator_id = customer.get('operator_id', None)

    if name and email and phone_number and address:
        customer_id = conversation_controller.add_customer(
            name, email, phone_number, address, operator_id)
        return make_response(
            f'Added customer with id: {customer_id}', 201
        )
    else:
        abort(
            406,
            "Could not add customer",
        )


def update(customer_id, customer):
    return None


def delete(customer_id):
    is_deleted = conversation_controller.remove_customer(customer_id)
    if is_deleted:
        return make_response(
            f'Deleted customer wit id: {customer_id}', 200
        )
    else:
        abort(404, f'Customer with id `{customer_id}` not found')
