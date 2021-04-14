from flask import make_response, abort
from engine import conversation_controller


def read_one(customer_id):
    customer = conversation_controller.get_customer(customer_id)
    if customer:
        return customer
    abort(404, f'Customer with id `{id}` not found')


def read_all():
    data = conversation_controller.get_all_customers()
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
    name = customer.get('name', None)
    email = customer.get('email', None)
    phone_number = customer.get('phone_number', None)
    address = customer.get('address', None)
    operator_id = customer.get('operator_id', None)

    updated_customer = None
    if name and email and phone_number and address:
        updated_customer = conversation_controller.update_customer(
            customer_id, name, email, phone_number, address, operator_id)

    if updated_customer:
        return updated_customer
    else:
        abort(404, f'Customer with id `{customer_id}` not found')


def delete(customer_id):
    is_deleted = conversation_controller.remove_customer(customer_id)
    if is_deleted:
        return make_response(
            f'Deleted customer wit id: {customer_id}', 200
        )
    else:
        abort(404, f'Customer with id `{customer_id}` not found')
