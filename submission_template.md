# AI Code Review Assignment (Python)

## Candidate
- Name: Baran Başaran
- Approximate time spent: 1.5 hour

---

# Task 1 — Average Order Value

## 1) Code Review Findings
Critical bugs: 
- 
The initial purpose is sound at adding the sum of the non-cancelled orders still, it takes the number of orders as the denominator and does not. This has cancelled orders in the number therefore artificially low value of average. Also, error handling has not been implemented in the code as it throws the ZeroDivisionError in case the orders list is empty.

Edge cases & risks
- 
The code does not have error processing of empty lists. When all orders are in the orders list, we have the length of the orders list equal to 0 and that results in a ZeroDivisionError resulting in the crash of the program.

Code quality / design issues
- 
The code does not have error processing of empty lists. When all orders are in the orders list, we have the length of the orders list equal to 0 and that results in a ZeroDivisionError resulting in the crash of the program.

## 2) Proposed Fixes / Improvements
Summary of changes
- 
I introduced a valid_count variable to count only the non-cancelled orders explicitly. The return statement now divides the total by this valid_count. I also added a guard clause to return 0.0 if valid_count is 0, preventing division by zero errors.

### Corrected code
See `correct_task1.py`

 ### Testing Considerations
Empty List: [] -> Should return 0.0.

All Cancelled: Only List to "cancelled" orders -> Should return 0.0.

Mixed Status: List with both "completed" and "cancelled" -> Should calculate average of only completed ones.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

Issues in original explanation
- 
I added a validcount variable to achieve a count only of the non-cancelled orders made. This validcount is the one which is divided by the return statement. I also added a guard clause to give 0.0 in case of 0.0 valid count so that the division by 0 errors can be avoided.

Rewritten explanation
- 
This is a calculation that determines the mean value of orders by the total value of the noncancelled orders and dividing this total by the number of such orders in particular. It is mathematically accurate because it does not include cancelled orders in the sum as well as in the count. Also, it treats hard cases (like lists of long/empty lists or lists of only cancelled orders) with returns of 0.0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original code contains a critical logical error (incorrect denominator including cancelled orders) and a runtime error risk (division by zero). It cannot be approved for production without the proposed fixes.
- Confidence & unknowns: High confidence

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
Critical bugs
- 
The original logic if "@" in email is severely insufficient for validation. It incorrectly accepts strings like "not_an_email@", "@domain", or even " @ " as valid emails, leading to a high number of false positives.

Edge cases & risks
- 
A TypeError occurs on code crashing when the list contains some other type other than a string (e.g. None, integer, a boolean) because the in operator cannot be applied to find a string within a non-iterative type such as an integer.

Code quality / design issues
- 
The implementation of a simple substring check to validate email addresses is bad engineering practice. Normal strong regular expressions (regex) should be used to do strong pattern matching.

## 2) Proposed Fixes / Improvements
Summary of changes
- 
I replaced the simple check with the re (regex) module for robust validation.

* Regex Pattern: I implemented r'^[\w\.-]+@[\w\.-]+\.\w+$' to ensure the email follows the standard structure: [User]@[Domain].[Extension].

* Type Safety: I wrapped the check in a try-except TypeError block. This allows the function to safely ignore non-string inputs (like None or 123) without crashing, adhering to the requirement of counting only valid entries.


### Corrected code
See `correct_task2.py`


### Testing Considerations
1. Invalid formats: Strings like "user@", "@domain.com", "plain text" -> Should be ignored.

2. Non-string types: Lists containing None, integers, booleans -> Should be ignored safely.

3. Valid emails: Standard formats like "user.name@sub.domain.co.uk" -> Should be counted.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

Issues in original explanation
- 
The original explanation falsely claims the function "safely ignores invalid entries." In reality, the code credentials for almost any string with an "@" symbol in them as valid, and crashes as non-strings, this time not ignoring invalid data safely.


Rewritten explanation
- 
This function is used to count the no. of valid email addresses from a list using regular expression (regex). It is used to validate that each email is in a standard form (user@domain.extension) and provides for the execution safety by processing and ignoring nonsensitive inputs to methods (such as None or numbers) using the exception handling.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original code is fundamentally flawed, allowing invalid data to pass as valid and crashing on mixed input types. The proposed regex solution is necessary for correctness and stability.
- Confidence & unknowns: High confidence.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
Critical bugs
- 
The function correctly adds up only the valid numbers (total), but it divides this sum by len(values). Since len(values) includes None (missing) values, the denominator is larger than it should be, causing the calculated average to be artificially low (incorrect).


Edge cases & risks
- 
If the input list is empty [] or contains only None values [None, None], the function will likely cause a ZeroDivisionError or return an incorrect result because it doesn't check if there are any valid numbers before dividing.

Code quality / design issues
- 
The logic is inconsistent in that it filters values within the loop that will be added to the sum, but uses the raw number of elements in the list as the number of elements that will be added to the sum. Both should be calculated on the same criteria.
## 2) Proposed Fixes / Improvements
Summary of changes
- 
I introduced a valid_count variable to track the number of valid measurements manually. Inside the loop, whenever a value is not None, I increment this counter. I also added a check if valid_count == 0 to return 0.0 immediately, preventing division by zero errors for empty or all-None lists.

### Corrected code
See `correct_task3.py`

### Testing Considerations
1. Mixed List: [10, None, 20] -> Should return 15.0 (Calculation: 30 / 2).

2. All None: [None, None] -> Should return 0.0 without crashing.

3. Empty List: [] -> Should return 0.0.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

Issues in original explanation
- 
The original explanation says "calculates the average of valid measurements", but from the code it appears that what it is actually doing is dividing by the total number of things (including invalid ones). The explanation disagrees with the behavior of the code.

Rewritten explanation
- 
This function is used to sum up the average of solid numbers. On the other hand, it explicitly excludes values of None from the sum as well as the count so it makes sure an average is calculated only over valid data values. It also conveys safely an input which is empty or all None as just 0.0.
## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation contains a mathematical error (incorrect denominator) and lacks safety checks for empty inputs. The proposed fix is required to calculate the true average of valid data.
- Confidence & unknowns: High confidence.
