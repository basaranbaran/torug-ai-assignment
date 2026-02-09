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
The function assumes every dictionary in the list has "status" and "amount" keys. Missing keys would cause a KeyError.

## 2) Proposed Fixes / Improvements
Summary of changes
- 
I introduced a valid_count variable to count only the non-cancelled orders explicitly. The return statement now divides the total by this valid_count. I also added a guard clause to return 0.0 if valid_count is 0, preventing division by zero errors.

### Corrected code
See `correct_task1.py`

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
The code crashes with a TypeError if the list contains non-string types (e.g., None, integers, booleans), as the in operator cannot be used to search for a string inside a non-iterable type like an integer.

Code quality / design issues
- 
Relying on a simple substring check for email validation is poor engineering practice. Standard regular expressions (regex) should be used for robust pattern matching.

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
The original explanation falsely claims the function "safely ignores invalid entries." In reality, the code accepts almost any string containing an "@" symbol as valid and crashes on non-string inputs, failing to ignore invalid data safely.

Rewritten explanation
- 
This function counts the number of valid email addresses in a list using a regular expression (regex). It validates that each email adheres to a standard format (user@domain.extension) and ensures execution safety by handling and ignoring non-string inputs (like None or numbers) via exception handling.

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
The logic is inconsistent: it filters values inside the loop for the sum but uses the raw list length for the count. Both should be calculated based on the same criteria.

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
The original explanation claims the function "calculates the average of valid measurements," but the code actually divides by the total number of items (including invalid ones). The explanation contradicts the code's behavior.

Rewritten explanation
- 
This function calculates the average of valid numerical measurements. It explicitly filters out None values from both the sum and the count, ensuring that the average reflects only the valid data points. It also handles empty or all-None inputs safely by returning 0.0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation contains a mathematical error (incorrect denominator) and lacks safety checks for empty inputs. The proposed fix is required to calculate the true average of valid data.
- Confidence & unknowns: High confidence.
