# -*- coding: utf-8 -*-

# This file defines a reform.
# A reform is a set of modifications to be applied to a reference tax and benefit system to carry out experiments.
# See https://doc.openfisca.fr/reforms.html


# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *


class modify_social_security_taxation(Reform):
    # A reform always defines an `apply` method that builds the reformed tax and benefit system from the reference one.
    # See https://doc.openfisca.fr/coding-the-legislation/reforms.html#writing-a-reform
    def apply(self):
        # Our reform modifies the `social_security_contribution` parameter, which is a scale.
        # This parameter is declared in `taxes.xml` using a `<BAREME>` XML element, the French name for "scale".
        #
        # See https://doc.openfisca.fr/coding-the-legislation/legislation_parameters.html
        self.modify_legislation_json(modifier_function=self.modify_brackets)

    def modify_brackets(self, reference_legislation_json_copy):
        # This function takes an argument `reference_legislation_json_copy` which is a JSON-like representation
        # of the XML element. It can be modified and must be returned.

        # Access the right legislation node:
        scale = reference_legislation_json_copy['children']['taxes']['children']['social_security_contribution']
        brackets = scale['brackets']

        # Add 0.1 to the rates of the second bracket, keeping the same thresholds:
        for rate in brackets[1]['rate']:
            rate['value'] += 0.1

        # Remove the first bracket:
        del brackets[0]

        # Add a new bracket with a higher tax rate for rich people:
        brackets.append({
            'rate': [{'start': '2017-01-01', 'value': 0.4}],
            'threshold': [{'start': '2017-01-01', 'value': 40000}]
            })

        return reference_legislation_json_copy
