# AI Code Review Assignment (Python)

## Candidate
- Name: Baran Başaran
- Approximate time spent: 1.5 hour

---

# Task 1 — Average Order Value

## 1) Code Review Findings
Critical bugs: 
- 
The original function is correct at adding the amount of non-cancelled orders but it uses len(orders) as the denominator and doesn't. This includes cancelled orders in the number so gives an artificially low average value. Additionally, there is no error handling in the code, as it throws a ZeroDivisionError in case the orders list is empty.

Edge cases & risks
- 
The code lacks error handling for empty lists. If the orders list is empty, len(orders) becomes 0, causing a ZeroDivisionError which crashes the program.

Code quality / design issues
- 
he function assumes every dictionary in the list has "status" and "amount" keys. Missing keys would cause a KeyError.

## 2) Proposed Fixes / Improvements
Summary of changes
- 
I introduced a valid_count variable to count only the non-cancelled orders explicitly. The return statement now divides the total by this valid_count. I also added a guard clause to return 0.0 if valid_count is 0, preventing division by zero errors.

### Corrected code
    correct_task1.py

 ### Testing Considerations
Empty List: [] -> Should return 0.0.

All Cancelled: List with only "cancelled" orders -> Should return 0.0.

Mixed Status: List with both "completed" and "cancelled" -> Should calculate average of only completed ones.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

Issues in original explanation
- 
The original explanation is misleading. It claims the function "correctly excludes cancelled orders," but while it excludes them from the sum, it fails to exclude them from the count (denominator), making the calculation mathematically incorrect.

Rewritten explanation
- 
This function calculates the average order value by summing the amounts of non-cancelled orders and dividing by the count of those specific valid orders. It ensures mathematical accuracy by excluding cancelled orders from both the sum and the count. Additionally, it handles edge cases such as empty lists or lists containing only cancelled orders by returning 0.0.

## 4) Final Judgment
- Decision: Approve
- Justification: The original code contains a critical logical error (incorrect denominator including cancelled orders) and a runtime error risk (division by zero). It cannot be approved for production without the proposed fixes.
- Confidence & unknowns: High confidence

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
