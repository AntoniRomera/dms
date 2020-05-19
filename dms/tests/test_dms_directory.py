# -*- coding: utf-8 -*-

###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import base64
import logging
import unittest
import collections

from odoo import _
from odoo.tests import common

from odoo.tests import common

from odoo.addons.muk_dms.tests import dms_case

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class DirectoryTestCase(dms_case.DMSTestCase):
    
    def setUp(self):
        super(DirectoryTestCase, self).setUp()
        
    def tearDown(self):
        super(DirectoryTestCase, self).tearDown()
    
    def test_create_directory(self):
        settings = self.browse_ref("muk_dms.settings_demo").sudo()
        root_directory = self.env['muk_dms.directory'].sudo().create({
            'name': "RootTestDir",
            'is_root_directory': True,
            'settings': settings.id})
        self.assertTrue(root_directory.settings.id == settings.id)
        sub_directory = self.env['muk_dms.directory'].sudo().create({
            'name': "SubTestDir",
            'is_root_directory': False,
            'parent_directory': root_directory.id})
        self.assertTrue(sub_directory.settings.id == settings.id)
        self.assertTrue(root_directory.count_directories == 1)