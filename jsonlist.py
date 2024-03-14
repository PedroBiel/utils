"""
CONVIERTE LOS DATOS DE UN FICHERO JSON Y TRANSFIERE LOS DATOS DE LAS CLAVES Y DE LOS VALORES A LISTAS

05/02/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@vamanholding.com
"""

import json

from src.utils.dictjson import DictJson


class JsonList:

    def __init__(self, ruta_json, nombre_json):
        """
        Lee los datos de un fichero json y los pasa a listas.

        :param ruta_json: Ruta donde se leerá el fichero json
        :param nombre_json: Nombre del fichero json
        """

        self.ruta_json = ruta_json  # Referencia relativa desde main.py
        self.nombre_json = nombre_json

    def json_to_dict(self) -> dict:
        """
        Lee un fichero json en la ruta indicada y lo convierte a diccionario.

        :return: d
        """

        self.set_ruta()
        self.set_nombre_json()
        ruta_nombre_json = f'{self.ruta_json}{self.nombre_json}'
        with open(ruta_nombre_json, 'r') as f:
            d = json.load(f)

        return d

    def json_keys_to_list(self) -> list:
        """
        Lee las claves de un fichero json y las guarda en una lista.

        Returns
        -------
        lista_claves
        """

        d = self.json_to_dict()
        lista_claves = list(d.keys())

        return lista_claves

    def json_values_to_list(self) -> list:
        """
        Lee los valores de un fichero json y los guarda en una lista.

        Returns
        -------
        lista_valores
        """

        d = self.json_to_dict()
        lista_valores = list(d.values())

        return lista_valores

    def set_ruta(self):
        """
        Setter de la ruta. Asegura que la ruta termina con '/'
        """

        if self.ruta_json[-1] != '/':
            self.ruta_json = f'{self.ruta_json}/'

    def set_nombre_json(self):
        """
        Setter del nombre del fichero json. Asegura el nombre json tiene la extensión 'json'.
        """

        if self.nombre_json[-5:] != '.json':
            self.nombre_json = f'{self.nombre_json}.json'


if __name__ == '__main__':

    ruta_json = '../../data/'
    nombre_json = 'SM_valores.json'
    json_list = JsonList(ruta_json, nombre_json)
    lista_claves = json_list.json_keys_to_list()
    lista_valores = json_list.json_values_to_list()
    print(lista_claves)
    print(lista_valores)
