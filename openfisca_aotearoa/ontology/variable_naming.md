# Proposition for handling the naming conventions for variables within OpenFisca Aotearoa

## Legislation/Source Instrument identifier list

 - it = (Income Tax Act 2007)[http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1512301.html]
 - od = (Compensation for Live Organ Donors Act 2016)[http://www.legislation.govt.nz/act/public/2016/0096/latest/DLM4297829.html]
 - rr = (Rates Rebates Act 1973)[http://www.legislation.govt.nz/act/public/1973/0005/latest/whole.html]


## Documentation of thinking process behind naming variables within OpenFisca Aotearoa.

Example: the variable `dependant` from the [Rates Rebates Act 1973](http://www.legislation.govt.nz/act/public/1973/0005/latest/DLM409601.html#DLM409607). 

Obviously the word "dependant" will be utilised in other acts with different definitions. There's a need to give the variable a unique name within the code so that:
 - it's easily read within the code
 - it's use/context is easily understood when searching the docs
 
_There is no right answer._

First proposal was to give each act a tag. So `Rates Rebates Act 1973` becomes `rates_rebates`.
Then we use that tag with the term as a suffix. The reason a suffix is chosen is it makes it easier to type and search in the docs.
We join these with a double underscore so that the variable `dependant` becomes `dependant__rates_rebates`.
This started to be implemented but it was then discovered it made the code unreadable and lead to mistakes. An example of this is `available_tax_loss__income_tax` where `__income_tax` is the Income Tax Act.

In response to this the next proposal is to replace the tag with a two letter identifier. In this situation `available_tax_loss__income_tax` -> `available_tax_loss_it` and
`dependant__rates_rebates` -> `dependant_rr`
The downside to this approach is it introduces another abitary thing to learn for newcomers to the project. 
The upside is it will allow for a unique way of searching within the docs. For example `_rr` would return all variables defined in relation to the `Rates Rebates Act 1973`.

When new acts are referenced within OpenFisca Aotearoa, please add them below with the chosen identifier.
The format of this document could be changed to incorporate a more linked data approach to the list when a format is decided on.

