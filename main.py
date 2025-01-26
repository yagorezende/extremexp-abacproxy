import os
from dotenv import load_dotenv

load_dotenv()

from api import app


if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_APP_HOST'),
        port=int(os.getenv('FLASK_APP_PORT')),
        debug=os.getenv('FLASK_APP_DEBUG'),
        threaded=True
    )
