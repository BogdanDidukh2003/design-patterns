import random
import string

databases = ['operator', 'customer']
names = [
    'Mark', 'Amber', 'Todd', 'Anita', 'Sandy',
    'John', 'Fred', 'Jason', 'Keyser', 'Lily',
    'Anna', 'Mike', 'Luke', 'Andrea', 'Lisa',
    'Stephen', 'James', 'Albert', 'Emma', 'Lia',
]


def generate_random_csv(filename='generated_data.csv', num_entries_per_db=500):
    operator_headers = 'name,phone_number,email,address,id,is_available\n'
    data_list = []
    is_available = '1'
    for id in range(1, num_entries_per_db + 1):
        name = random.choice(names)
        phone = ''.join(random.choices(string.digits, k=8))
        email = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                       k=random.randint(4, 8))) + '@gmail.com'
        address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        data_list.append(','.join([name, phone, email, address, str(id), is_available]) + '\n')
    with open(filename, 'w') as file:
        file.write('operator\n')
        file.write(operator_headers)
        file.writelines(data_list)

    data_list = []
    customer_headers = 'name,phone_number,email,address,id,operator_id\n'
    operator_id = ''
    for id in range(1, num_entries_per_db + 1):
        name = random.choice(names)
        phone = ''.join(random.choices(string.digits, k=8))
        email = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                       k=random.randint(4, 8))) + '@gmail.com'
        address = ''.join(random.choices(string.ascii_lowercase,
                                         k=random.randint(4, 12))).title()
        data_list.append(','.join([name, phone, email, address, str(id), operator_id]) + '\n')
    with open(filename, 'a') as file:
        file.write('customer\n')
        file.write(customer_headers)
        file.writelines(data_list)


def parse_csv(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines if line.endswith('\n')]

    operator_table_idx = lines.index('operator')
    operator_headers = lines[operator_table_idx + 1]
    customer_table_idx = lines.index('customer')
    customer_headers = lines[customer_table_idx + 1]
    operator_list = lines[operator_table_idx + 2: customer_table_idx]
    customer_list = lines[customer_table_idx + 2:]

    return {
        'operator': (operator_headers, operator_list),
        'customer': (customer_headers, customer_list)
    }
