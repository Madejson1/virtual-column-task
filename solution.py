import pandas as pd
import re

# I changed 'pandas' to 'pd' in the function parameters
def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    pattern = r"[A-Za-z_]+" # only characters and underscores for column names

    # In the task it is said that column labels must consist only of letters and underscores - to be sure I am also validating the column names of the input dataframe.
    if not all(re.fullmatch(pattern, column) for column in df.columns):
        return pd.DataFrame([])

    parts = re.split(r"\s*([+\-*])\s*", role.strip()) # Regex expression is used to find the operator in 'role', even if it is surrounded by whitespace.

    # Safety check in case 'role' is something like 'a+b+c'
    if len(parts) != 3:
        return pd.DataFrame([])

    first_column, operator, second_column = parts # Because the operator is inside a capturing group () in the Regex expression, re.split() returns three elements split by the operator (with it also being included).

    # Check column names from the 'role'
    if not (re.fullmatch(pattern, first_column) and re.fullmatch(pattern, second_column) and re.fullmatch(pattern, new_column)):
        return pd.DataFrame([])

    # Check if column names from the 'role' correspond to the input df
    if first_column not in df.columns or second_column not in df.columns:
        return pd.DataFrame([])

    df = df.copy()
    if operator == "+":
        df[new_column] = df[first_column] + df[second_column]
    elif operator == "-":
        df[new_column] = df[first_column] - df[second_column]
    elif operator == "*":
        df[new_column] = df[first_column] * df[second_column]
    else:
        return pd.DataFrame([])

    return df