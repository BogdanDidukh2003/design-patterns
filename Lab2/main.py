from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controllers import ConversationController, ImportController
from managers import (
    CustomerManager,
    OperatorManager,
    ConversationManager,
)
from models import Base
from views import AppView

# DB_PATH = ':memory:'
DB_PATH = 'C:/Users/Admin/Projects/design-patterns/conversation.db'


def main():
    print('\t\tMVC LAB\n')
    engine = create_engine('sqlite:///' + DB_PATH)  # ,echo=True) for debugging
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # ------- INIT -------
        customer_manager = CustomerManager(session)
        operator_manager = OperatorManager(session)
        conversation_manager = ConversationManager(session)
        conversation_controller = ConversationController(
            customer_manager=customer_manager,
            operator_manager=operator_manager,
            conversation_manager=conversation_manager,
        )
        AppView(conversation_controller)
        # ----- INIT END -----
        import_controller = ImportController(
            customer_manager=customer_manager,
            operator_manager=operator_manager,
        )
        # import_controller.load_data_from_csv('generated_data.csv')
        # session.commit()

        print('\n\t--- OPERATORS ---')
        for operator in conversation_controller.get_all_operators()[:5]:
            print(operator)
        print('\n\t--- CUSTOMERS ---')
        for customer in conversation_controller.get_all_customers()[:5]:
            print(customer)


if __name__ == '__main__':
    main()
