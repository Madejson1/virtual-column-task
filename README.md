
# Virtual Column Task

Function `add_virtual_column` creates a new column in a pandas DataFrame based on a rule like:

label_one + label_two

Supported operators:
- +
- -
- *

Column names must contain only letters and underscores.

If the rule or column names are invalid, the function returns an empty DataFrame.

Additional validation rules for proper processing are also included.

## Running tests

python test_virtual_column.py
