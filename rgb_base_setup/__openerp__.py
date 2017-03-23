# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Base Setup
#   Copyright 2017 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'RGB Base Setup',
    'version': '8.0.1.0.0',
    'depends': ['contacts',
                'note',
                'calendar',
                'document',
                # server-tools
                'admin_technical_features',
                'mass_editing',
                'password_security',
                'disable_openerp_online',
                # web
                'web_dialog_size',
                'web_searchbar_full_width',
                'web_export_view',
                'web_hide_db_manager_link',
                'web_search_with_and',
                'web_sheet_full_width',
                # partner-contact
                'base_location_geonames_import',
                ],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'RGB',

    'summary': 'Default base modules',

    'description': """
RGB Base Setup
==============

Installs the base modules for a basic setup.
    """,

    'data': [
    ],

    'demo': [
    ],
    'installable': True,
    'application': False,
}
