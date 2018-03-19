# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _


class registro_modelo(osv.osv):
	_name = 'registro.modelo'
	_description = 'Formulario de Atletas'
	_columns = {
	     # Campo oblidatorio para buscar , readonly = True
	     'name' : fields.char('Nombre' , size=256, required=True, help='Este es el nombre'),
	     'pais' : fields.char('Nombre' , size=256, required=True),
	     'oro' : fields.integer('Oro' , size=256, required=True),
	     'plata' : fields.char('Plata' , size=256, required=True),
       # Campo para activar el registro es necesario
         'active': fields.boolean('Activo'),
	}
	_defaults = {
       'state' : 'draft',
       'active' : 'true',
	}


registro_modelo()