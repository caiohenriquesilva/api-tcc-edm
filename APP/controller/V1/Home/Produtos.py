# coding=utf-8
from flask.views import MethodView
from model.Home.Produtos import Produtos
from model.ControllerError import ControllerError

class ProdutosController(MethodView):
    def get(self):
        """
        Lista de produtos da Home
        Está chamada retorna os produtos que irá aparecer na home
        ---
        tags:
            - Home
        """

        try:
            produtos = Produtos()
            ret = produtos.getProdutosHome()
            ret['sucesso'] = True
            return ret, 200

        except ControllerError.MySQLError as e:
            msg = ControllerError().MySQL(e)
            return msg, 500

        except Exception as e:
            msg = ControllerError().default(e)
            return msg, 500

        finally:
            produtos.destroy()
        
