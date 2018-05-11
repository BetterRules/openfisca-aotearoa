# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity


# Using middle English spelling due to `property` being a Python keyword.
Propertee = build_entity(
    key = "propertee",
    plural = "properties",
    label = u'Property',
    doc = '''
    A Property represents accommodation that is owned by a group of Persons.

    Example usage:
    Check the number of individuals of a specific role: check how many persons co-own the property: `properties.nb_persons(Propertee.OWNER)`.
    Calculate a variable applied to each tenant of the group entity: calculate the income of each member of the Property: `tenants_incomes = properties.members('income', period = MONTH); tenants_total_income = properties.sum(tenants_incomes)`.

    For more information on group entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'owner',
            'plural': 'owners',
            'label': u'Owners',
            'doc': u'The one or more persons who hold title for the property.'
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
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'owner' in a 'Propertee' entity with person.has_role(Propertee.owner)).

    For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

entities = [Propertee, Person]
