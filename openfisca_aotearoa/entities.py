# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity


Titled_Property = build_entity(
    key = "titled_property",
    plural = "titled_properties",
    label = u'Titled Property',
    doc = '''
    A Titled property represents a property that is owned by a Person or group of Persons.

    Example usage:
    Check the number of individuals of a specific role: check how many persons co-own the property: `titled_properties.nb_persons(Titled_Property.OWNER)`.
    Calculate a variable applied to each tenant of the group entity: calculate the income of each member of the Property: `tenants_incomes = titled_properties.members('income', period = MONTH); tenants_total_income = titled_properties.sum(tenants_incomes)`.

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
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'owner' in a 'Titled_Property' entity with person.has_role(Titled_Property.owner)).

    For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

Family = build_entity(
    key = "family",
    plural = "families",
    label = u'Family',
    doc = '''
    A Family represents a collection of related persons.

    Example:
    Family entities are required for calculation of working for families entitlements.

    A family can contain a number of roles, such as 'principal_caregiver', 'partner', 'dependant_child' & 'independant_child'.

    For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'principal_caregiver',
            'plural': 'principal_caregivers',
            'label': u'Principal caregivers',
            'doc': u'The one person who is the principal caregiver of a family.'
            },
        {
            'key': 'partner',
            'plural': 'partners',
            'label': u'Partners',
            'doc': u'The one or more persons who are partners of a family principal caregiver.'
            },
        {
            'key': 'dependant_child',
            'plural': 'dependant_children',
            'label': u'Dependant children',
            'doc': u'The one or more persons who are financially dependant children of a family principal caregiver.'
            },
        {
            'key': 'independant_child',
            'plural': 'independant_children',
            'label': u'Independant children',
            'doc': u'The one or more persons who are financially independant children of a family principal caregiver.'
            }
        ]
    )

entities = [Titled_Property, Person, Family]
