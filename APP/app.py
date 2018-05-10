from __init__ import app, api
from controller.Version import VersionController

# Home
api.add_resource(VersionController, '/version')
