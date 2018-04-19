# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity


# to be renamed, currently experimenting with structure
_Property = build_entity(
    key = "_property",
    plural = "_properties",
    label = u'_Property',
    doc = '''
    _Property is an example of a group entity.
    A group entity contains one or more individual·s.
    Each individual in a group entity has a role (e.g. rate payer, owner, resident). Some roles can only be held by a limited number of individuals (e.g. a 'first_parent' can only be held by one individual), while others can have an unlimited number of individuals (e.g. 'children').

    Example:
    _Property variables (e.g. _property rates') are usually defined for a group entity such as '_Property'.

    Usage:
    Check the number of individuals of a specific role (e.g. check if there is a 'rate_payer'  _property.nb_persons(_Property.RATE_PAYER)).
    Calculate a variable applied to each individual of the group entity (e.g. calculate the 'salary' of each member of the 'Property' with salaries = _property.members('salary', period = MONTH); sum_salaries = _property.sum(salaries)).

    For more information, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'owner',
            'plural': 'owners',
            'label': u'Owners',
            'max': 2,
            'subroles': ['rate_payer'],
            'doc': u'The one or more persons who hold title for the property.'
            },
        {
            'key': 'tenant',
            'plural': 'tenants',
            'label': u'Tenant',
            'doc': u'One or more persons who live at the property.'
            }
        ]
    )

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'Person',
    doc = '''
    A Person represents an individual, the minimal legal entity on which a legislation might be applied.

    Example:
    The 'salary' and 'income_tax' variables are usually defined for the entity 'Person'.

    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent' in a 'Property' entity with person.has_role(Property.FIRST_PARENT)).

    For more information, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

entities = [_Property, Person]
