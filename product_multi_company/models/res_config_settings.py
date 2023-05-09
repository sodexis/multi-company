# Copyright 2023 Sodexis
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sync_template_product_companies = fields.Boolean(
        config_parameter="product_multi_company.sync_template_product_companies",
    )
