# Proposed approach to handle ontology learnings from OpenFisca Aotearoa work

The OpenFisca project will result in the identification of ontology related aspects to New Zealand legislation. These should be recorded for the purpose of providing a useful resource that could be utilised in any future authoritive ontology considerations.

The following is a discussion starter, proposed is a YAML linked data model based on the Dublin Core that is translatable to RDF.
Inspired by the [following work](https://douroucouli.wordpress.com/2015/08/27/a-lightweight-ontology-registry-system/).


```
- id: rr
  title: Rates Rebates Act 1973
  source: http://www.legislation.govt.nz/act/public/1973/0005/latest/DLM409601.html
  type: Act
- id: dependant_rr
  title: Dependant
  source: http://www.legislation.govt.nz/act/public/1973/0005/latest/DLM409601.html#DLM409607
  type: Interpretation
  related: rr
```
