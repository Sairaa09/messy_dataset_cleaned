# Cleaned Messy Dataset (100 Entries)

## Overview
This dataset contains 100 entries from a messy source, which included inconsistent formatting, redundant columns, invalid entries, and missing values. The cleaning process standardized the data, making it ready for analysis while preserving important information.

## Cleaning Steps
1. Removed redundant or empty columns: `AGE` (duplicate of `age`) and `Extra Column` (empty/redundant).  
2. Standardized column names: lowercase, no spaces, no parentheses.  
3. Converted `UNKNOWN`, `ERROR`, and blank values to `NaN`.  
4. Converted `income` column to numeric by removing currency symbols and commas.  
5. Attempted to clean `date_joined` column, but values were inconsistent. Many entries became missing, so the column was dropped.  
6. Cleaned categorical columns (`name`, `gender`) with title case and filled missing values as "Unknown".  
7. Cleaned `phone_number` to keep only digits and `+`, filling missing values with "Unknown".  
8. Converted `email` to lowercase.  
9. Kept `age` NaN values as-is to avoid losing potentially important information.

## Columns
- `name` (string)  
- `gender` (string)  
- `age` (numeric, NaN preserved)  
- `phone_number` (string)  
- `email` (string)  
- `income` (numeric)

## Summary
- Redundant columns removed.  
- Numeric and categorical columns standardized.  
- Dataset ready for analysis while preserving key information.

