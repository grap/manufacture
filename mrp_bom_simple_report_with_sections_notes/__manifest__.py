# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Quentin Dupont (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "MRP BoM Simple Report With Sections and Notes",
    "summary": "Print simple report for your Bill of Materials with Sections and Notes",
    "version": "16.0.1.0.0",
    "category": "Manufacturing",
    "author": "GRAP, Odoo Community Association (OCA)",
    "maintainers": ["quentinDupont"],
    "website": "https://github.com/OCA/manufacture",
    "license": "AGPL-3",
    "depends": [
        "mrp_bom_widget_section_and_note_one2many",
    ],
    "assets": {
        "web.report_assets_common": [
            "/mrp_bom_simple_report_with_sections_notes/"
            "static/src/scss/mrp_bom_simple_report.scss"
        ],
    },
    "data": [
        "report/report_simple_bom.xml",
        "report/ir_actions_report.xml",
    ],
    "installable": True,
}
