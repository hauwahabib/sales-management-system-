# sales-management-system-
A Python-based menu-driven application for managing employee sales data and calculating commissions.

## Features
- Employee data management (name, ID, properties sold)
- Automated commission calculation (£500 per property)
- Employee ranking using bubble sort algorithm
- Weekly performance awards (15% bonus for top performer)
- 7 menu options for comprehensive sales analytics

## Functionality
1. Display ranked employee list
2. Calculate individual sales commissions
3. Calculate total weekly commission
4. Show total properties sold
5. Determine employee of the week
6. Calculate bonus amount
7. Exit/continue menu

## Technologies Used
- Python 3
- Lists and data structures
- Functions and algorithms
- User input validation

## How to Run
```bash
python MENU.py
```

## Test Plan
Comprehensive testing covered:
- Input validation
- Ranking algorithm accuracy
- Commission calculations
- Menu navigation
- Employee of the week determination

## Sample Output
```
How many employees are there? : 3

Enter employee name: John
Enter employee's ID number: 101
Enter number of properties sold: 10

[Menu displays with 7 options...]
```

## Future Improvements
- Add error handling for invalid inputs
- Replace bubble sort with Python's built-in sort() for efficiency
- Add data persistence (save to file)
- Create graphical user interface
