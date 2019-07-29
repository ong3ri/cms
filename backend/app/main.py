import os

from app import create_app

app = create_app(os.getenv('S_FLASK_CONFIG', 'default'))

if __name__ == '__main__':
    app.run()
