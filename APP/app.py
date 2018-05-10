from __init__ import app, api
from controller.V1.Version import VersionController

# Home
api.add_resource(VersionController, '/')
