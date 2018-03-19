# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

{
    'name': 'Registro',
    'version': '1.0',
    'author': 'Bryan Oviedo',
    'category': 'Nueva',
    'summary': 'Ejemplo de un módulo de Odoo',
    'website': '',
    'description': """
Es un módulo de ejemplo
======================
Con este modulo haremos nuestra primera aplicación en Odoo.

Nota: Necesita Ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale'],
    'update_xml': [
        'registro_view.xml',
    ],
    'installable': True,
    'active': False,
}