# 💰 Dutch Salary Calculator

Command-line tool to calculate net salary from gross income in the Netherlands,
including holiday allowance (vakantiegeld).

Part of a structured transition from Process Operator to Data Analyst.

## Features

- Gross to net salary conversion using Dutch tax brackets
- Holiday allowance calculation (8% or 8.33%)
- Breakdown of deductions
- Input validation for salary and allowance percentage

## How to Run
```bash
python salary_calculator.py
```

1. Enter gross yearly salary in €
2. Enter vacation allowance percentage (8 or 8.33 — omit the %)
3. Read the output
4. Choose to repeat or exit

## Tax Constants (2025)

| | Rate |
|---|---|
| Tax bracket low | 36.97% |
| Tax bracket high | 49.50% |
| Bracket limit | € 38,098 |

## Technologies

- Python 3.x
- Standard library only

## Status

✅ Complete
