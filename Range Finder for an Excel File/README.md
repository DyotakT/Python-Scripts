# Range Finder for an Excel File

## Finding the ranges in a list of numbers in an Excel sheet

For example, lets find the ranges in this table of numbers - 

| |
| ------ |
| 1 |
| 2 |
| 3 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |

Output would be:
| From | To |
| ------ | ------ |
| 1 | 3 |
| 5 | 10 |

Usage:
```
python index.py FILENAME THRESHOLD
```

Where,
| Argument | Input | Notes |
| ----------- | ----- | ------|
| FILENAME | file name :P | Just put the filename here, no need to add the file extension |
| THRESHOLD | any number | The difference to be included in the range; suppose you want the two numbers which are 20 counts away to be included in the range, you'd then put 20 as THRESHOLD |

Example usage command:
```
python index.py Book1 20
```

**Please ensure the values are only numbers, contains no alphabets and are sorted in ascending order.**

Python version used:
* Python 3.8.10

Packages used:
* openpyxl 3.0.7
* alive-progress 1.6.2
