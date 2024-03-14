"""
1. Transfiere los datos de un diccionario a un fichero json y lo guarda en la ruta indicada.

2. Lee un fichero json en la ruta indicada y lo transfiere a un diccionario.

18/01/2024

__author__ = Pedro Biel

__version__ = 0.0.1

__email__ = structural.eng.biel@gmail.com

versión 0.0.1 : se sutituye with open(fichero_json, 'r') por with open(fichero_json, encoding='utf-8') para asegurar la codificación correcta
"""


import json


class DictJson:

    def __init__(self, d: dict, ruta: str, nombre_json: str):
        """
        Lee los datos de un diccionario y los pasa a un fichero json.

        :param d: Diccionario
        :param ruta: Ruta donde se guadará el fichero json
        :param nombre_json: Nombre del fichero json
        """

        self.d = d
        self.ruta = ruta
        self.nombre_json = nombre_json

    def dict_to_json(self):
        """
        Crea un fichero json con los datos del diccionario y lo guarda en la ruta indicada.

        :return: fichero json
        """

        self.set_ruta()
        self.set_nombre_json()
        ruta_nombre_json = f'{self.ruta}{self.nombre_json}'
        with open(ruta_nombre_json, 'w') as f:
            json.dump(self.d, f)

    def json_to_dict(self) -> dict:
        """
        Lee un fichero json en la ruta indicada y lo convierte a diccionario.

        :return: d
        """

        self.set_ruta()
        self.set_nombre_json()
        ruta_nombre_json = f'{self.ruta}{self.nombre_json}'
        # with open(ruta_nombre_json, 'r') as f:
        with open(ruta_nombre_json, encoding='utf-8') as f:
            d = json.load(f)

        return d

    def set_ruta(self):
        """
        Setter de la ruta. Asegura que la ruta termina con '/'
        """

        if self.ruta[-1] != '/':
            self.ruta = f'{self.ruta}/'

    def set_nombre_json(self):
        """
        Setter del nombre del fichero json. Asegura el nombre json tiene la extensión 'json'.
        """

        if self.nombre_json[-5:] != '.json':
            self.nombre_json = f'{self.nombre_json}.json'


class JsonDict:

    def __init__(self, ruta: str, nombre_json: str):
        """
        Lee los datos de un fichero json y los pasa a un diccionario.

        :param ruta: Ruta donde se leerá el fichero json
        :param nombre_json: Nombre del fichero json
        """

        self.ruta = ruta
        self.nombre_json = nombre_json

    def json_to_dict(self) -> dict:
        """
        Lee un fichero json en la ruta indicada y lo convierte a diccionario.

        :return: d
        """

        DictJson.set_ruta(self)
        DictJson.set_nombre_json(self)
        ruta_nombre_json = f'{self.ruta}{self.nombre_json}'
        with open(ruta_nombre_json, encoding='utf-8') as f:
            d = json.load(f)

        return d


if __name__ == '__main__':

    d = {
        'clave1': [1, 2, 3],
        'clave2': ['a', 'b', 'c', 'ÁÉÍÓÚáéíóú']
    }

    # Ruta no contiene '/' al final y nombre de fichero json no contiene extensión '.json'
    ruta1 = '../../pruebas/data'
    nombre_json1 = 'prueba1'
    dict_json = DictJson(d, ruta1, nombre_json1)
    dict_json.dict_to_json()

    # Ruta contiene '/' al final y nombre de fichero json contiene extensión '.json'
    ruta2 = '../../pruebas/data/'
    nombre_json2 = 'prueba2.json'
    dict_json = DictJson(d, ruta2, nombre_json2)
    dict_json.dict_to_json()

    # Lee fichero json y lo convierte a diccionario
    ruta3 = '../../pruebas/data/'
    nombre_json3 = 'prueba3.json'
    dict_json = JsonDict(ruta3, nombre_json3)
    d = dict_json.json_to_dict()
    print(f'Diccionario: {d} -> {type(d)}')
