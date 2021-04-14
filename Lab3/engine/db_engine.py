from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from controllers import ConversationController
from managers import (
    CustomerManager,
    OperatorManager,
    ConversationManager,
)
from models import Base

# DB_PATH = ':memory:'
DB_PATH = 'C:/Users/Admin/Projects/design-patterns/conversation.db'

engine = create_engine('sqlite:///' + DB_PATH)  # ,echo=True) for debugging
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

session = scoped_session(sessionmaker(bind=engine))

customer_manager = CustomerManager(session)
operator_manager = OperatorManager(session)
conversation_manager = ConversationManager(session)
conversation_controller = ConversationController(
    customer_manager=customer_manager,
    operator_manager=operator_manager,
    conversation_manager=conversation_manager,
)
