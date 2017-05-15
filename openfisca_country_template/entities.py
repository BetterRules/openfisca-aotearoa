# -*- coding: utf-8 -*-

from openfisca_core.entities import build_entity

# You can define here the entities you need in your legislation.

Household = build_entity(
    key = "household",
    plural = "households",
    label = u'Household',
    roles = [
        {
            'key': 'parent',
            'plural': 'parents',
            'label': u'Parents',
            'max': 2,
            'subroles': ['first_parent', 'second_parent']
            },
        {
            'key': 'child',
            'plural': 'child',
            'label': u'Child',
            }
        ]
    )


Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'Person',
    is_person = True,
    )

entities = [Household, Person]
