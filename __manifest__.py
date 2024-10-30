{
    'name': 'Custom CRM',
    'version': '1.0',
    'summary': 'A short summary of the module',
    'description': """
        Application To manage freelancer communication with client.
    """,
    'author': 'zain alabidin ali',
    #'website': 'https://yourwebsite.com',
    'category': '',
    'depends': [
        'base',
        'mail',
        'calendar',
        'contacts'
        ],  # List of dependencies
    'data': [
        # List of XML/CSV files for data import, views, security rules, etc.
        #'views/my_module_view.xml',
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/base_menu.xml',
        'views/client_view.xml',
        'views/invoice_view.xml',
        'views/tag_view.xml',
        'views/interaction_view.xml',
        'data/email_templates.xml',
        'reports/invoice_report.xml',

    ],
    'demo': [
        # Demo data files
        #'demo/demo_data.xml',
    ],
    'installable': True,  # Can be installed
    'application': True,  # If set to True, this will make the module appear in the apps list
    #'auto_install': False,  # If set to True, this module will be installed automatically if all dependencies are met
    'license': 'LGPL-3',  # License of the module
    # 'assets': {
    #     'web.assets_backend': [
    #         'web/static/src/legacy/js/widgets/colorpicker.js'
    #     ],
    # }
}
