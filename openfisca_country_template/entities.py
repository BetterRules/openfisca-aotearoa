# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.

from openfisca_core.entities import build_entity

Household = build_entity(
    key = "household",
    plural = "households",
    label = u'Household',
    doc = '''
    A group entity.
    Contains multiple natural persons with specific roles.
    From zero to two parents with 'first_parent' and 'second_parent' subroles.
    And an unlimited number of children.
    ''',
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
            'plural': 'children',
            'label': u'Child',
            }
        ]
    )


Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'Person',
    doc = '''
    The minimal legal entity on which a legislation might be applied.
    Represents a natural person.
    ''',
    is_person = True,
    )


entities = [Household, Person]
