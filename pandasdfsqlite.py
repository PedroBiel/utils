# -*- coding: utf-8 -*-
"""
Transfiere datos de pandas DataFrame a SQLite

Created on Tue Mar 21 16:39:29 2020

__author__ = Pedro Biel

__version__ = 0.0.1

__email__ = structural.eng.biel@gmail.com
"""


import sqlite3


class PandasDFSQLite:

    def __init__(self, ruta_nombre: str, df: object, tabla: str):
        """Transfers data from a pandas DataFrame to a SQLite data base."""

        self.ruta_nombre = ruta_nombre  # Ruta y nombre de la base de datos a guardar.
        self.df = df  # DataFrame a convertir.
        self.tabla = tabla  # Tabla de la base de datos.

    def df_to_sql(self) -> object:
        """
        Crea una base de datos SQLite con los datos de pandas DataFrame y la guarda en la ruta especificada.

        :return: SQLite data base
        """

        conn = sqlite3.connect(self.ruta_nombre)
        self.df.to_sql(
                self.tabla,
                conn,
                if_exists='replace',
                index=False
                )
