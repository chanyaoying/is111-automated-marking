# is111-automated-marking
This is a script that will make the lives of IS111 TAs easier by marking the student's Lab Assignments automatically.

I am still working on this project, especially with documenting it properly because this was done impromptu.
For any enquires, feel free to reach out to me at yychan.2019@sis.smu.edu.sg

## Issues and Changes
If you would like to contribute, pull requests are welcome! You can also open an issue and we can discuss any changes.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```
## Usage
This is by no means a comprehensive guide. Please contact me if you need any help.

### Lab directory
For every lab assignment, this directory should be used:

```bash
./labs/labX
```
Where X is the lab number.

### Create testcase.txt
It should be placed in the lab directory, in this format:

```python
# 2.2
print(foo(3, 4) == True)
print(foo(0, 0) == False)
print(foo(-5,-3) == True)

# 2.3
print(bar(4) == [4,6])
print(bar(0) == [])
```

### Run main.py
You will be prompted about whether you want to continue without renaming the displayed files. Remember to configure the settings at the start of main.py.

### Renaming of the student solution .py files
This script will only process .py filenames in this format.

```bash
XXXX-XXXX - JOHN DOE - Feb 4, 2021 534 PM - 2.1
```

 Take note that the number at the end must correspond with the numbers after the '#' sign in testcase.txt.

 ### Report generation
 After the test scripts are run, an excel report will be generated in the lab directory.

