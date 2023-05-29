#0x05. Python - Exceptions
In this project, I learned:
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

##Function Prototypes :floppy_disk:

| File                        | Prototype                              |
| --------------------------- | ----------------------------------------------- |
| `0-safe_print_list.py`      | `def safe_print_list(my_list=[], x=0):`     |
| `1-safe_print_integer.py`   | `def safe_print_integer(value):`            |
| `2-safe_print_list_integers.py` | `def safe_print_list_integers(my_list=[], x=0):`    |
| `3-safe_print_division.py`  |	`def safe_print_division(a, b):`            |        
| `4-list_division.py`        | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`      | `def raise_exception():`                    |
| `6-raise_exception_msg.py`  | `def raise_exception_msg(message=""):`      |
| `100-safe_print_integer_err.py` | `def safe_print_integer_err(value):`    |
| `101-safe_function.py`      | `def safe_function(fct, *args):`            |
| `102-magic_calculation.py`  | `def magic_calculation(a, b);`              |
|                             | `void print_python_list(PyObject *p);`      |
| `103-python.c`              | `void print_python_bytes(PyObject *p);`     |
|                             | `void print_python_float(PyObject *p);`     |

##Tasks :page_with_curl:
* **0. Safe list printing**

* Write a function that prints `x` elements of a list on the same line, followed by a new line.
* The parameter `x` represents the number of elements to be printed
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed without importing modules or using `len()`.

* **1. Safe printing of an integers list**

* Write a function that prints an integer in `"{:d}".format()` format.
* The parameter `value` can be any type.
* Returns `True` if `value` was printed correctly (ie. was an integer), False otherwise.
* Do not import modules or use `type()`.

* **2. Print and count integers**

* Write a function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
* The parameter `my_list` can contain any type.
* The parameter `x` represents the number of elements to print - can be bigger than the length of `my_list.`
* Reutnrs the real number of integers printed without importing modules or using `len()`.

* **3. Integers division with debug**

* Write a function that divides two integers and prints the result using `finally:` preceded by `Inside result:`
* The function assumes that the arguments are integers.
* Upon success, returns the value of the division; otherwise - returns None without importing modules.

* **4. Divide a list**

* Write a function that divides two lists element by element.
* Returns a new list of length `list_length` with all divisions.
* The lists `my_list_1` and `my_list_2` can contain any type.
* The parameter `list_length` can be larger than the lengths of either list.
* If an element is not an integer or float, the function prints `wrong type.`
* If the division cannot be done, the result of the division is 0 and the function prints: `division by 0`.
* If either of `my_list_1` or `my_list_2` are too short, the function prints: `out of range` without importing modules.

* **5. Raise exception**

* Write a function that raises a `type exception` without importing modules.

* **6. Raise a message**

* Write a function that raises a `name exception` with a message without importing modules.

* **7. Safe integer print with error message**

* Write a function that prints an integer with type-checking in `"{:d}".format()` format.
* The paramter `value` can be any type.
* Returns `True` if `value` was printed correctly (ie. was an integer).
* Otherwise, prints an `exception` error to `stderr` and returns False without importing modules.

* **8. Safe function**

* Write a function that executes a function safely.
* The function assumes that the parameter `fct` is always a pointer to a function.
* Upon success, returns the result of the function.
* Otherwise, prints an `exception` error to `stderr` and returns `None`.

* **9. ByteCode -> Python #4**

* Write the Python function `def magic_calculation(a, b):` that does exactly as provided by Alx Holberton school

* **10. CPython #2: PyFloatObject**

* Write a C functions that print basic information about Python `lists`, `bytes`, and `float` objects.
