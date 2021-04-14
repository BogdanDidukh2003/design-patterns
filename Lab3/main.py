from flask import render_template
import connexion

# DB_PATH = ':memory:'
DB_PATH = 'C:/Users/Admin/Projects/design-patterns/conversation.db'
host = 'localhost'
port = 5000
is_debug = True

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


def main():
    app.run(host=host, port=port, debug=is_debug)


if __name__ == '__main__':
    main()
