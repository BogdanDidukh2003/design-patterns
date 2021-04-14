from flask import make_response, abort
from engine import conversation_controller


def read_one(customer_id):
    conversation = conversation_controller.get_conversation(customer_id)
    if conversation:
        return conversation
    abort(404, f'Conversation with customer `{customer_id}` not found')


def read_all():
    data = conversation_controller.get_all_conversations()
    return data


def create(conversation):
    customer_id = conversation.get('customer_id', None)

    if customer_id:
        conversation = conversation_controller.add_conversation(customer_id)
        if conversation is not None:
            customer_id = conversation['customer_id']
            operator_id = conversation['operator_id']
            return make_response(
                'Added conversation between customer `{}` and operator `{}`'.format(
                    customer_id, operator_id
                ), 201
            )
    abort(406, "Could not add conversation")


def delete(customer_id):
    is_deleted = conversation_controller.remove_conversation(customer_id)
    if is_deleted:
        return make_response(
            f'Deleted conversation with customer: {customer_id}', 200
        )
    else:
        abort(404, f'Conversation with customer `{customer_id}` not found')
