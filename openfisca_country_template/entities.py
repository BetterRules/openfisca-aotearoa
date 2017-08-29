# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
import textwrap

from openfisca_core.entities import build_entity

Household = build_entity(
    key = "household",
    plural = "households",
    label = u'Household',
    doc = textwrap.dedent('''
    A group entity.
    Contains multiple natural persons with specific roles.
    From zero to two parents with 'first_parent' and 'second_parent' subroles.
    And an unlimited number of children.

    Example: 
    Housing variables like 'housing_tax' are usually defined for an entity 'Household'.

    Usage: 
    Access a role or a subrole like 'first_parent' with: Household.FIRST_PARENT
    Calculate a variable applied to a 'Person' like 'salary' on the whole 'Household' with: simulation.household.members('salary', period = MONTH) 

    For more information, see: https://doc.openfisca.fr/coding-the-legislation/50_entities.html
    '''),
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
    doc = textwrap.dedent('''
    The minimal legal entity on which a legislation might be applied.
    Represents a natural person.

    Example: 
    'salary' and 'income_tax' variables are usually defined for the entity 'Person'.

    Usage: 
    Calculate a variable applied to a 'Person' like 'salary' on a specific month with: person('salary', "2017-05")

    For more information, see: https://doc.openfisca.fr/coding-the-legislation/50_entities.html
    '''),
    is_person = True,
    )


entities = [Household, Person]
