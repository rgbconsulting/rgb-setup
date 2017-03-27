# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Base Accounting
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
    'name': 'RGB Base Accounting',
    'version': '8.0.1.0.0',
    'depends': ['account_accountant',
                # account-financial-tools
                'account_balance_line',
                'account_fiscal_position_vat_check',
                'account_invoice_tax_required',
                'account_move_line_no_default_search',
                'account_tax_chart_interval',
                # account-invoicing
                'account_group_invoice_lines',
                'account_invoice_period_usability',
                'account_invoice_supplier_number_info',
                'account_invoice_supplier_ref_unique',
                'account_invoice_zero_autopay',
                'account_journal_report_xls',
                'invoice_fiscal_position_update',
                #account-payment
                'account_due_list',
                #account-financial-reporting
                'account_financial_report_webkit_xls',
                #account-invoicing
                'account_payment_term_extension',
                #bank-statement-import
                'base_bank_account_number_unique',
                ],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'RGB',

    'summary': 'Installs Accounting modules',

    'description': """
RGB Base Accounting Modules
===========================


Installs accounting modules.
    """,

    'data': [
    ],

    'demo': [
    ],
    'installable': True,
    'application': False,
}
