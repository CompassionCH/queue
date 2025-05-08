# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from openupgradelib import openupgrade

from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    # Remove cron garbage collector
    env = api.Environment(cr, SUPERUSER_ID, {})
    openupgrade.delete_records_safely_by_xml_id(
        env,
        ["queue_job.ir_cron_queue_job_garbage_collector"],
    )
