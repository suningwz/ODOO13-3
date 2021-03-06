from odoo import api, fields, models


class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('folder', 'Folder')])

    @api.model
    def postprocess(self, model, node, view_id, in_tree_view, model_fields):
        if node.tag == 'folder':
            in_tree_view = True
        return super().postprocess(model, node, view_id, in_tree_view, model_fields)
