# coding=utf-8
from model.MySql import MySql, MySqlr
import re


class Produtos:

    def __init__(self):
        self.mysqlr = MySqlr()
        self.curr = self.mysqlr.open()
        self.curr_produtos_top = self.mysqlr.open()
        self.curr_produtos_home = self.mysqlr.open()
        # self.mysql = MySql()
        # self.cur = self.mysql.open()

    def getProdutosHome(self):
        self.curr_produtos_home.execute("""
            SELECT
                sh.produto_codigo,
                p.produto_nome,
                sm.nome,
                p.produto_descricao,
                p.video_link,
                p.preco,
                p.preco_antigo,
                p.tmp_avaliacao_numero,
                p.tmp_avaliacao_nota,
                p.disponibilidade,
                p.menu,
                p.preco_prime,
                p.preco_antigo_prime,
                pd.desconto,
                pf.nome AS fabricante,
                p.disponibilidade
            FROM kb_001_site_home sh
            INNER JOIN kb_produtos p ON p.codigo = sh.produto_codigo
            INNER JOIN kb_site_menu sm ON sm.codigo = SUBSTRING_INDEX(SUBSTRING_INDEX(p.menu,'`:`',-2),'`:`',1)
            INNER JOIN kb_produtos_descontos pd ON pd.codigo = p.desconto
            INNER JOIN kb_produtos_fabricantes pf ON pf.codigo = p.fabricante
            ORDER BY sh.codigo ASC LIMIT 33
            ;
            """)

        ret = []
        for row in self.curr_produtos_home:
            codigo = row['produto_codigo']
            desconto = row['desconto']
            
            preco_desconto = 0
            if (desconto > 0):
                preco_desconto = (1 - (desconto / 100)) * float(row['preco'])
                preco_desconto_prime = (1 - (desconto / 100)) * float(row['preco_prime'])

            self.curr.execute("""SELECT filename_m, filename_g FROM kb_produtos_imagens WHERE codigo_produto = %s AND principal = 1""", (codigo))
            foto = self.curr.fetchone()

            ret.append({
                'codigo'                : codigo,
                'img'                   : self.__urlImagem(codigo, foto['filename_m']),
                'nome'                  : row['produto_nome'],
                'alt'                   : codigo,
                'link_descricao'        : self.__urlDescricao(codigo, row['produto_nome']),
                'preco'                 : float(row['preco']),
                'preco_prime'           : float(row['preco_prime']),
                'preco_desconto'        : float(preco_desconto),
                'preco_desconto_prime'  : float(preco_desconto_prime),
                'avaliacao_numero'      : row['tmp_avaliacao_numero'],
                'avaliacao_nota'        : row['tmp_avaliacao_nota'],
                'fabricante'            : row['fabricante'],
                'disponibilidade'       : True if row['disponibilidade'] == 1 else False
            })

        return {'produtos': ret}

    def getTopProdutos(self, limit):
        self.curr_produtos_top.execute("""
            SELECT
                p.codigo,
                p.produto_nome,
                sm.nome,
                p.produto_descricao,
                p.video_link,
                p.preco,
                p.preco_antigo,
                p.tmp_avaliacao_numero,
                p.tmp_avaliacao_nota,
                p.disponibilidade,
                p.menu,
                p.fabricante,
                p.preco_prime,
                p.preco_antigo_prime,
                pd.desconto
            FROM kb_produtos p 
            INNER JOIN kb_site_menu sm ON sm.codigo = SUBSTRING_INDEX(SUBSTRING_INDEX(p.menu,'`:`',-2),'`:`',1)
            INNER JOIN kb_produtos_descontos pd ON pd.codigo = p.desconto
            ORDER BY p.tmp_ranking ASC 
            LIMIT %s
            """ % (limit))
        
        ret = []
        for row in self.curr_produtos_top:
            codigo = row['codigo']
            desconto = row['desconto']
            preco_desconto = 0
            if (desconto > 0):
                preco_desconto = (1 - (desconto / 100)) * float(row['preco'])

            self.curr.execute("""SELECT filename_m, filename_g FROM kb_produtos_imagens WHERE codigo_produto = %s AND principal = 1""", (codigo))
            foto = self.curr.fetchone()

            ret.append({
                'codigo': codigo,
                'img': self.__urlImagem(codigo, foto['filename_m']),
                'nome': row['produto_nome'],
                'alt': codigo,
                'link_descricao': self.__urlDescricao(codigo, row['produto_nome']),
                'preco': float(row['preco']),
                'preco_desconto': float(preco_desconto),
                'preco_prime': float(row['preco_prime']),
                'avaliacao_numero': row['tmp_avaliacao_numero'],
                'avaliacao_nota': row['tmp_avaliacao_nota']
            })

        return {'produtos': ret}

    def __urlImagem(self, codigo, filename):
        codigo = str(codigo)
        filename = str(filename)
        url = 'https://images' + \
            codigo[-1] + '.kabum.com.br/produtos/fotos/' + \
            codigo + '/' + filename

        return url

    def __urlDescricao(self, codigo, nome):
        return '/produto/' + str(codigo) + '/' + self.__amigavel(nome)
        # return 'https://www.kabum.com.br/produto/' + str(codigo)

    def __amigavel(self, nome):
        num = re.sub(r'[^A-Za-z0-9\-\_]', "-", nome)
        num = re.sub(r'\-{2,}', "-", num)

        return num.lower()

    def destroy(self):
        self.curr.close()
        self.curr_produtos_top.close()
        self.curr_produtos_home.close()
        self.mysqlr.close()
        # self.cur.close()
        # self.mysql.close()
