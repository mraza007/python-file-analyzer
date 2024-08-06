# Python File Analyzer Script
A simply utility script which allows you to analyze your python file. It provides simple detailed insights into the structure and composition of Python code, including information about functions, classes, imports, variables, and function calls.

## Usage
1. Clone this repository: `https://github.com/mraza007/python-file-analyzer/`
2. cd into `cd python-file-analyzer` and then simply do `chmod +x index.py`
3. once created an executable simply run `./index.py <python-file>`


## Contributing

Contributions are welcomed. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- This project uses Python's `ast` module for parsing and analyzing Python code.


#### Example Output

```sh
Analysis of ../key.py:
Number of lines: 43

Functions:

Classes:

Imports:
- datetime (line 5)
  Documentation: https://docs.python.org/3/library/datetime.html
- jwt (line 6)
  Documentation: https://docs.python.org/3/library/jwt.html

Variables:
- secret:
  Defined on lines: 9
  Used on lines: 36
- keyId:
  Defined on lines: 15
  Used on lines: 24
- teamId:
  Defined on lines: 16
  Used on lines: 28
- alg:
  Defined on lines: 17
  Used on lines: 23, 36
- time_now:
  Defined on lines: 19
  Used on lines: 30
- datetime:
  Defined on lines:
  Used on lines: 19, 20, 20
- time_expired:
  Defined on lines: 20
  Used on lines: 29
- headers:
  Defined on lines: 22
  Used on lines: 36
- payload:
  Defined on lines: 27
  Used on lines: 36
- int:
  Defined on lines:
  Used on lines: 29, 30
- __name__:
  Defined on lines:
  Used on lines: 34
- token:
  Defined on lines: 36
  Used on lines: 39, 42
- jwt:
  Defined on lines:
  Used on lines: 36
- print:
  Defined on lines:
  Used on lines: 38, 39, 41, 42

Function Calls:
- int: called on lines 29, 30
- print: called on lines 38, 39, 41, 42
```
