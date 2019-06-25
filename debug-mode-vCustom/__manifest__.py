{
    'name': 'On/Off Debug',
    'description': 'Fastest way to turn On/Off debug mode',
    'summary': 'Click to turn on/off Debug, Assets Debug mode',
    'author': 'Vinh Huynh',
    'data':[
        'views/debug_mode_template.xml',
    ],
    'depends':['web'],

    'application': True,
    'installable': True,

    'qweb': [
        'static/src/xml/icon_templates.xml'
    ],

}