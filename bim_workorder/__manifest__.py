# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'WORK ORDER BIM 2.0',
    'version': '13.0.0.1',
    'author': "Ynext",
    'maintainer': 'Ynext',
    'website': 'http://www.ynext.cl',
    'license': 'AGPL-3',
    'category': 'Construction',
    'summary': 'Ordenes de trabajo para BIM',
    'depends': [
        'base_bim_2','hr'
    ],
    'description': """
BIM 2.0
============================
* Orden de Trabajo
        """,
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/bim_workorder_view.xml',
        'views/workorder_timesheet_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'demo': [],
    'test': [],
}
