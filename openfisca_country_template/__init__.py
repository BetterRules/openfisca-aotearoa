# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from . import entities


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(COUNTRY_DIR, 'model.py')
PARAM_FILE = os.path.join(COUNTRY_DIR, 'parameters.xml')

# Our country tax and benefit class, which inherits from the general TaxBenefitSystem class
# The name CountryTaxBenefitSystem must not be changed, as all tools of the OpenFisca ecosystem expect a CountryTaxBenefitSystem class to be exposed in the __init__ module of a country package
class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        # We initialize our tax and benefit system with the general constructor
        super(CountryTaxBenefitSystem, self).__init__(entities.entities)

        # We add to our tax and benefit system all the variables defined in model.py
        self.add_variables_from_file(MODEL_FILE)

        # We add to our tax and benefit system all the legislation parameters defined in parameters.xml
        self.add_legislation_params(PARAM_FILE)
