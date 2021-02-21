# is111-automated-marking
This is a script that will make the lives of IS111 TAs easier by marking the Lab Assignments automatically.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```
## Usage
### Lab directory
For every lab assignment, this directory should be used:

```bash
./labs/labX
```

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

