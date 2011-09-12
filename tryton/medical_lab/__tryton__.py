# -*- encoding: utf-8 -*-
{
    'name': 'GNU Health: Laboratory',
    'version': '1.0',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'medical',
    ],

    'name_es_ES': 'GNU Health : Laboratorio',
    'translation': ['es_ES.csv'],

    'description': '''

This modules includes lab tests: Values, reports and PoS.


''',

    'description_es_ES': '''

Módulo con la funcionalidad de laboratorio.

''',

    'xml': [
        #'security/ir.model.access.csv',
        'medical_lab_view.xml',
        'medical_lab_report.xml',
        'data/medical_lab_sequences.xml',
        'data/lab_test_data.xml',
        'wizard/create_lab_test.xml',
    ],
}
