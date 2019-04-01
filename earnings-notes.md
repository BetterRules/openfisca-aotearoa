Finish with https://docs.google.com/viewerng/viewer?url=https://trello-attachments.s3.amazonaws.com/5c64cd8f31d6a7671bbdd586/5c9c0562c31df90b6e29b29a/63cb87efc4a315cb963a6ac8e7b52904/Earnings_Rule_Statements_v0.2.docx

Earnings upfront - AC Act 2001, s6
- `earnings_as_employee`:
  - (a + b) - c
  - a = `have_paye_income_payments` (Income Tax Act s RD 3)
  - b = `earnings_as_private_domestic_worker` (AC Act 2001, s 13) 
  - c = exclusions section AC Act 2001, 9 & 10
    - `payments_to_spouse`
    - `income_tested_benefit`
    - `veterans_pension`
    - `new_zealand_super`
    - `schedular_payment`
    - `parental_leave_payment`
    - `student_allowance`

- `earnings_shareholder_employee`:
  - = a + b
  - a = `paye_income_payments_from_company_where_person_is_shareholder_and_employee` (Income Tax Act s RD 3)
  - b = `all_income_other_than_paye_of_person_who_is_shareholder_employee` (AC Act 2001, s 15b) 
    - this seems like a loophole, mike to follow up

OR
  - = a + b
  - a = `reasonable_renumeration_as_employee_for_a_given_tax_year` (AC Act 2001, s 15(s)(a)(i)) 
  - b = `reasonable_renumeration_as_director_of_company_for_a_given_tax_year`(AC Act 2001, s 15(s)(a)(ii))


- `earnings_self_employed`:
  - = a - b
  - a = `income_from_personal_exersions` (AC Act 2001, s 15(s)(b)) 
    = a - c - d
    - c = `earnings_as_employee`
    - d = `earnings_shareholder_employee`
  - b = `self_employed_deductions`
  

Earnings after
- `earnings_as_employee_for_abatement`: (AC ACt 2001, Sch 1, cls 49, 51)
  - = a + b + c
  - a = `earnings_as_employee`
  - b = `overseas_income_payment`
  - c = `organ_donor_compensation_payment`

- `earnings_self_employed_for_abatement`: (AC Act 2001, Sch 1, cls 49, 50, 51)
  - = a + b + c
  - a = `earnings_self_employed`
  - b = `overseas_income_payment`
  - c = `organ_donor_compensation_payment`

  OR if `earnings_self_employed` cannot be readily ascertained
  - = a + b + c
  - a = `estimated_earnings_for_abatement`
  - b = `overseas_income_payment`
  - c = `organ_donor_compensation_payment`


- `income_as_shareholder_employee_for_abatement`:  (AC ACt 2001, Sch 1, cls 49, 50, 51)
    - a = `earnings_shareholder_employee`
    - c = `overseas_income_payment`
    - d = `organ_donor_compensation_payment`