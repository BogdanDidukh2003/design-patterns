from flask import make_response, abort
from engine import conversation_controller


def read_one(operator_id):
    operator = conversation_controller.get_operator(operator_id)
    if operator:
        return operator
    abort(404, f'Operator with id `{id}` not found')


def read_all():
    data = conversation_controller.get_all_operators()
    return data


def create(operator):
    name = operator.get('name', None)
    email = operator.get('email', None)
    phone_number = operator.get('phone_number', None)
    address = operator.get('address', None)
    is_available = operator.get('is_available', True)

    if name and email and phone_number and address:
        operator_id = conversation_controller.add_operator(
            name, email, phone_number, address, is_available)
        return make_response(
            f'Added operator with id: {operator_id}', 201
        )
    else:
        abort(
            406,
            "Could not add operator",
        )


def update(operator_id, operator):
    name = operator.get('name', None)
    email = operator.get('email', None)
    phone_number = operator.get('phone_number', None)
    address = operator.get('address', None)
    is_available = operator.get('is_available', None)

    updated_operator = None
    if name and email and phone_number and address:
        updated_operator = conversation_controller.update_operator(
            operator_id, name, email, phone_number, address, is_available)

    if updated_operator:
        return updated_operator
    else:
        abort(404, f'Operator with id `{operator_id}` not found')


def delete(operator_id):
    is_deleted = conversation_controller.remove_operator(operator_id)
    if is_deleted:
        return make_response(
            f'Deleted operator wit id: {operator_id}', 200
        )
    else:
        abort(404, f'Operator with id `{operator_id}` not found')
