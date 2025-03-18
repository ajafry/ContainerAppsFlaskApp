"""
This script runs the python_webapp_flask application using a development server.
When this code runs in a container, we use gunicor and not this development server.
"""

from os import environ, getenv
from api_app import app
from dotenv import load_dotenv

_ = load_dotenv()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getenv('SERVER_PORT', 5000), debug=True)