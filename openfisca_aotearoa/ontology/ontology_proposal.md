# Proposed approach to handle ontology learnings from OpenFisca Aotearoa work

The OpenFisca project will result in the handling of ontology related aspects with respects New Zealand legislation. Recording the decisions around this for the purpose of providing a resource for any future authoritive ontology considerations. Archives New Zealand has already developed a ontology that covers NZ legislation that is not yet publically linkable.

The following is a discussion starter, proposed is a YAML linked data model based on the Dublin Core that is translatable to RDF.
Inspired by the [following work](https://douroucouli.wordpress.com/2015/08/27/a-lightweight-ontology-registry-system/).


```
- id: rates_rebates
  title: Rates Rebates Act 1973
  source: http://www.legislation.govt.nz/act/public/1973/0005/latest/DLM409601.html
  type: Act
- id: rates_rebates__dependant
  title: Dependant
  source: http://www.legislation.govt.nz/act/public/1973/0005/latest/DLM409601.html#DLM409607
  type: Interpretation
  related: rates_rebates
```
