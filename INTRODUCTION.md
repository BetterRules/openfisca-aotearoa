# OpenFisca Aotearoa Contributors Introduction

## Writing the Legislation Wiki

Guide to writing legislation as code for Aotearoa New Zealand. This documentation is to be considered an introduction to OpenFisca and a style guide for OpenFisca Aotearoa. For technical documentation on OpenFisca please refer to the [Open Fisca Docs](http://openfisca.org/doc/)

### Meta considerations

The goal of the project is foremost an accurate computational representation of Aotearoa's legislation. For programmers this can require losing some "best practice" habits in achieving optimal outcomes with respect to the legislation. This wiki's goal is give clarity and a sense of consistency to contributors contributing to OpenFisca Aotearoa. 

Your first consideration when approaching this project is that it will never be finished, precisely because our legislative environment doesn't look like it'll stop making changes any time soon. As such there will be multiple ongoing legislative changes and breaking changes as term use changes. This makes good practice around change tracking essential. It's also envisaged that OpenFisca is deployed per use rather than in a centralise manner. This frees the project to grow, adapt and moves the responsibility of accurate/up-to-date deployments along with decisions to upgrade on those deploying the instances. 

The second consideration is that OpenFisca Aotearoa is more of a platform than a product and it sits on the OpenFisca Core which is the underlying computational engine. As a platform it has a very open folder structure and any organisation of file names and terminology is up to those working on the project.

### Guide to Ontology

Naming things is of course considered the hardest thing in programming. With legislation the standardisation of terms and their definitions within individual pieces of law is common practice. Within the Aotearoa legislative environment it's also common to reference other terms "as defined by the [Another Act]". However individual terms are widely used in different ways and even redefined from their natural english meaning for the purpose of an individual act.

Here's a simple example from current Aotearoa legislation:

Within the [Student Allowances Regulations 1998](http://www.legislation.govt.nz/regulation/public/1998/0277/latest/DLM259355.html) we find the phrase: 

    > does not include a person who is legally married but who does not have a spouse

A dictionary definition of the word spouse is:
    > [Someone's spouse is the person they are married to.](https://www.collinsdictionary.com/dictionary/english/spouse)

This immediately creates a conundrum of how could this statement ever be true. The trick to solving this is that the same act also redefines what the common understanding is of the word "spouse" with the following definition:
    > spouse, in relation to an applicant, means a person who is legally married to that applicant if—
    > (a) both of them are of or over 24; or
    > (b) one or both of them are younger than 24 and at least 1 of them has a supported child 

Technically the act has been drafted to discriminate against young married childless couples and it's this redefinition of the word spouse that we need to grapple with.

Within OpenFisca the only limit to the ontology is that two terms cannot have the same name. Therefore when naming a term it's important to consider how it'll be perceived throughout the entire OpenFisca project. In the above example we therefore might therefore name the term "spouse" as

`spouse_as_defined_by_student_allowances`
or
`spouse_as_defined_by_Student_Allowances_Regulations_1998`
or
`spouse_as_defined_by_student_allowances_regulations_1998`

### Getting Started

Review the [Key Concepts](http://openfisca.org/doc/key-concepts.html) on the OpenFisca documentation site. Also take note of [Variables](http://openfisca.org/doc/variables.html), [Parameters](http://openfisca.org/doc/parameters.html) and [Entities](http://openfisca.org/doc/coding-the-legislation/50_entities.html).

### Referencing Legislation

New Zealand legislation is referencable on [legislation.govt.nz] (http://www.legislation.govt.nz/).
Open Fisca allows for direct referencing of parameters and variables. 
When creating a parameter or variable include a reference as you believe most appropriate. Some examples of how that can be done with respects to the "age of majority" defined in the Age of Majority Act 1970.

The following links to the whole act, being a smaller document this could be considered the best approach.
```yaml
description: Age of majority (in years)
reference: http://www.legislation.govt.nz/act/public/1970/0137/latest/whole.html#DLM396495
values:
  1970-12-02:
    value: 20.0
```
Options include:

1. A link direct to the appropriate section of the whole act (as in the above example)[http://www.legislation.govt.nz/act/public/1970/0137/latest/whole.html#DLM396495](http://www.legislation.govt.nz/act/public/1970/0137/latest/whole.html#DLM396495)

2. A link direct to just the appropriate section (preferred for sections in large pieces of legislation)[http://www.legislation.govt.nz/act/public/1970/0137/latest/DLM396495.html](http://www.legislation.govt.nz/act/public/1970/0137/latest/DLM396495.html)

3. A link to the whole piece of legislation (case of last resort) [http://www.legislation.govt.nz/act/public/1970/0137/latest/whole.html](http://www.legislation.govt.nz/act/public/1970/0137/latest/whole.html)

### Time Periods


### Parameters

For a technical understanding of parameters please reference [docs.openfisca.org](http://openfisca.org/doc/parameters.html)
When inputting parameters it's a good idea to ignore the basic programmer instincts of removing "duplicate code". In the cases that an Act has been reenacted and the parameter in question didn't change,  reiterate the value for each year it's reenacted regardless of it's value changing. This gives readers of the code a more complete understanding of the parameter's history. 

### Variables

For a technical understanding of variables please reference [docs.openfisca.org](http://openfisca.org/doc/variables.html)
Variables allow for formulas, when writing for formulas be aware all calculations are vectorial as [explained in the docs](http://openfisca.org/doc/coding-the-legislation/25_vectorial_computing.html).

### Testing

Start every formula with a test and work to build up the test case libraries with unique situations as they come to the fore. The opportunity to add new test cases to OpenFisca Aotearoa adds to the human orientated nature of the project. It allows for an increasingly nuanced response to the various circumstances faced by the people the project is designed to serve. The tests also add real world scenarios that researchers can include in their work when modelling the impacts various proposed scenarios might create.
