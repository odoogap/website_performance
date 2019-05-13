# -*- coding: utf-8 -*-

from odoo import models
from collections import OrderedDict

from odoo.addons.base.ir.ir_qweb.assetsbundle import AssetsBundle


class AssetsBundleDefer(AssetsBundle):

    def to_node(self, css=True, js=True, debug=False, async_load=False, **kw):
        response = []
        if debug != 'assets' and js and self.javascripts:
            attr = OrderedDict([
                ["defer", "defer"],
                ["type", "text/javascript"],
                ["src", self.js().url],
            ])
            response.append(("script", attr, None))
            return response

        response = super(AssetsBundleDefer, self).to_node(css, js, debug, async_load, **kw)
        return response


class QWeb(models.AbstractModel):
    _inherit = 'ir.qweb'

    def get_asset_bundle(self, xmlid, files, remains=None, env=None):
        return AssetsBundleDefer(xmlid, files, remains=remains, env=env)
