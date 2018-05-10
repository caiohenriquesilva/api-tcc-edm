# coding=utf-8
from flask.views import MethodView

class VersionController(MethodView):
    def get(self):
        return "1.0"
