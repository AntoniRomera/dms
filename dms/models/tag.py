# Copyright 2020 RGB Consulting
# Copyright 2017-2019 MuK IT GmbH
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Tag(models.Model):
    _name = 'dms.tag'
    _description = 'Document Tag'

    name = fields.Char(string='Name', required=True, translate=True)
    active = fields.Boolean(
        default=True,
        help="The active field allows you "
             "to hide the tag without removing it.",
    )
    category_id = fields.Many2one(
        comodel_name='dms.category',
        context="{'dms_category_show_path': True}",
        string='Category',
        ondelete='set null',
        oldname='category',
    )
    color = fields.Integer(string='Color Index', default=10)
    directory_ids = fields.Many2many(
        comodel_name='dms.directory',
        relation='dms_directory_tag_rel',
        column1='tid',
        column2='did',
        string='Directories',
        readonly=True,
        oldname='directories'
    )
    file_ids = fields.Many2many(
        comodel_name='dms.file',
        relation='dms_file_tag_rel',
        column1='tid',
        column2='fid',
        string='Files',
        readonly=True,
        oldname='files'
    )
    count_directories = fields.Integer(
        compute='_compute_count_directories', string='Count Directories'
    )
    count_files = fields.Integer(
        compute='_compute_count_files', string='Count Files'
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name, category)', 'Tag name already exists!'),
    ]

    @api.depends('directories')
    def _compute_count_directories(self):
        for rec in self:
            rec.count_directories = len(rec.directories)

    @api.depends('files')
    def _compute_count_files(self):
        for rec in self:
            rec.count_files = len(rec.files)
