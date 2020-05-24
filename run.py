from app.app import app
from settings import config_by_name


app.config.from_object(config_by_name['dev'])
if __name__ == '__main__':
    app.run()