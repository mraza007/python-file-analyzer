# Python File Analyzer Script
A simply utility script which allows you to analyze your python file. It provides simple detailed insights into the structure and composition of Python code, including information about functions, classes, imports, variables, and function calls.

## Usage
### Windows
1. Clone this repository: `https://github.
com/mraza007/python-file-analyzer/`
2. Go into the directory where you cloned, hold Shift and right click.
3. Open a PowerShell/command line window from there and type in ` python .\index.py [.py file]`
### Linux
1. Clone this repository: `https://github.com/mraza007/python-file-analyzer/`
2. `cd` into `python-file-analyzer` and then simply do `chmod +x index.py`
3. once created an executable simply run `./index.py [.py file]`

## Contributing

Contributions are welcomed. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- This project uses Python's `ast` module for parsing and analyzing Python code.


#### Example Output

```sh
Analysis of ./test.py:
Filesize: 1.5 KiB
Number of lines: 48

Functions:
- generate_random_numbers(count, min_val, max_val) -> Unknown (line 4)
  Docstring: Generates...
- calculate_average(numbers) -> Unknown (line 8)
  Docstring: Calculates...
- calculate_histogram(numbers, bins) -> Unknown (line 12)
  Docstring: Calculates...
- print_histogram(histogram, min_val, bin_width) -> Unknown (line 24)
  Docstring: Prints...
- main() -> Unknown (line 32)
  No docstring found

Classes:

Imports:
- random (line 1)
  Documentation: https://docs.python.org/3/library/random.html
- statistics (line 2)
  Documentation: https://docs.python.org/3/library/statistics.html

Variables:
- random:
  Defined on lines:
  Used on lines: 6
- min_val:
  Defined on lines: 14, 44
  Used on lines: 6, 15, 19, 22, 28, 45
- max_val:
  Defined on lines: 14
  Used on lines: 6, 15
- _:
  Defined on lines: 6
  Used on lines:
- range:
  Defined on lines:
  Used on lines: 6
- count:
  Defined on lines: 27
  Used on lines: 6, 30
- numbers:
  Defined on lines:
  Used on lines: 10, 10, 14, 14, 18
- statistics:
  Defined on lines:
  Used on lines: 10
- min:
  Defined on lines:
  Used on lines: 14, 19
- max:
  Defined on lines:
  Used on lines: 14
- bin_width:
  Defined on lines: 15, 44
  Used on lines: 19, 22, 28, 29, 45
- bins:
  Defined on lines: 36
  Used on lines: 15, 16, 19, 44
- histogram:
  Defined on lines: 16, 44
  Used on lines: 20, 22, 27, 45
- number:
  Defined on lines: 18
  Used on lines: 19
- bin_index:
  Defined on lines: 19
  Used on lines: 20
- int:
  Defined on lines:
  Used on lines: 19
- print:
  Defined on lines:
  Used on lines: 26, 30, 41, 42
- i:
  Defined on lines: 27
  Used on lines: 28
- enumerate:
  Defined on lines:
  Used on lines: 27
- bin_start:
  Defined on lines: 28
  Used on lines: 29, 30
- bin_end:
  Defined on lines: 29
  Used on lines: 30
- num_count:
  Defined on lines: 33
  Used on lines: 38, 41
- min_value:
  Defined on lines: 34
  Used on lines: 38
- max_value:
  Defined on lines: 35
  Used on lines: 38
- random_numbers:
  Defined on lines: 38
  Used on lines: 39, 44
- generate_random_numbers:
  Defined on lines:
  Used on lines: 38
- average:
  Defined on lines: 39
  Used on lines: 42
- calculate_average:
  Defined on lines:
  Used on lines: 39
- calculate_histogram:
  Defined on lines:
  Used on lines: 44
- print_histogram:
  Defined on lines:
  Used on lines: 45
- __name__:
  Defined on lines:
  Used on lines: 47
- main:
  Defined on lines:
  Used on lines: 48

Function Calls:
- range: called on lines 6
- min: called on lines 14, 19
- max: called on lines 14
- int: called on lines 19
- print: called on lines 26, 30, 41, 42
- enumerate: called on lines 27
- generate_random_numbers: called on lines 38
- calculate_average: called on lines 39
- calculate_histogram: called on lines 44
- print_histogram: called on lines 45
- main: called on lines 48
```
