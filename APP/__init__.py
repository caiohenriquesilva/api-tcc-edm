from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_restful import Api


app = Flask(__name__)
CORS(app)
api = Api(app)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'documentacao_api',
            "route": '/documentacao_api.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "basePath": "/api",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

app.config['SWAGGER'] = {
    'title': 'API',
    'uiversion': 2
}

swagger = Swagger(app, config=swagger_config)