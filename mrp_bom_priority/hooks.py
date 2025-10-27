# Copyright 2025 CoopITEasy
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from collections import defaultdict

from odoo.addons.mrp.models.mrp_bom import MrpBom


def post_load_hook():
    def _bom_find_new(
        self, products, picking_type=None, company_id=False, bom_type=False
    ):
        bom_by_product = defaultdict(lambda: self.env["mrp.bom"])
        products = products.filtered(lambda p: p.type != "service")
        if not products:
            return bom_by_product
        domain = self._bom_find_domain(
            products,
            picking_type=picking_type,
            company_id=company_id,
            bom_type=bom_type,
        )

        # Change from the original _bom_find:
        order = "priority DESC, sequence, product_id, id"

        if len(products) == 1:
            bom = self.search(domain, order=order, limit=1)
            if bom:
                bom_by_product[products] = bom
            return bom_by_product

        boms = self.search(domain, order=order)

        products_ids = set(products.ids)
        for bom in boms:
            products_implies = bom.product_id or bom.product_tmpl_id.product_variant_ids
            for product in products_implies:
                if product.id in products_ids and product not in bom_by_product:
                    bom_by_product[product] = bom

        return bom_by_product

    if not hasattr(MrpBom, "_bom_find_original"):
        MrpBom._bom_find_original = MrpBom._bom_find
    MrpBom._bom_find = _bom_find_new
