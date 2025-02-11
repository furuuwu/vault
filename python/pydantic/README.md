# Pydantic stuff

```shell
pipenv install "pydantic<3.0.0"
pipenv install "mypy<2.0.0"

# to run the examples in the jupyter notebook
pipenv install "notebook<8.0.0" ipykernel
```

* <https://docs.pydantic.dev/latest/>
* <https://github.com/python/mypy>

## Type hinting, mypy

* Python is a dynamically typed language, and types aren’t known until runtime.
* Type annotations or hints in Python

  were introduced in v3.5. It's an additional syntax that notifies you, the developer, of the expected type of a variable. They are not used by the Python language at runtime, and they do not modify or affect the behavior of your program in any way.

  ```python
  # examples

  text: str = "John"

  def count_users(users: list[str]) -> int:
      return len(users)
  
  from typing import Union
  x: Union(str, int) # string or integer

  x: str | int # same thing

  def get_filename_from_conf(**kwargs) -> Optional[str]:
      file_name = smt.get('file_path')  # Returns None if 'file_name' is not present.
      return file_path
  ```
  
  Here, `Optional[str]` is equivalent to `Union[str, None]`, indicating that the function might return None.

  The typing module contains several types, including the following:

  * List: for variables that should be of the list type
  * Dict: for dictionaries
  * Sequence: for any type of sequence of values
  * Callable: for callables, such as functions
  * Iterator: indicates that a function or variable accepts an iterator object (an object that implements the iterator protocol and can be used in a for loop)
  * Optional: used for handling optional values and None values in an explicit and developer-friendly way.
  * Union: allows you to define a union of possible types, such as integers and strings. Modern Python uses the pipe operator (|).
  * self: is used to indicate that the value will be an instance of a certain class, useful in Pydantic model validators
  * New: allows developers to define completely new types based on existing types.

  <https://docs.python.org/3/library/typing.html>

  ```python
  from typing import List

  def square_numbers(numbers: List[int]) -> List[int]:
    return [number ** 2 for number in numbers]

  # Example usage
  input_numbers = [1, 2, 3, 4, 5]
  squared_numbers = square_numbers(input_numbers)
  print(squared_numbers) # Output: [1, 4, 9, 16, 25]
  ```

  ```python
  # Literal - restricts the possible values of a variable to a few admissible states
  from typing import Literal

  account_type: Literal["personal", "business"]
  account_type = "name" # gives an error when using a type checker
  ```

  ```python
  from datetime import datetime

  def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")
  
  now = datetime.now()
  print(format_datetime(now))
  ```

  ```python
  # list of dictionaries
  def get_users(id: int) -> list[dict]:
    return [
      {"id": 1, "name": "Alice"},
      {"id": 2, "name": "Bob"},
      {"id": 3, "name": "Charlie"},
    ]
  ```

* using a type checker - eg. Mypy

  Type hints can also be defined as a formalism - a formal solution to statically (before runtime) indicate the type of a value to a type checker

  ```shell
  # by default, no type-checking
  mypy 1_bad.py # this passes

  # report an error for any function that is missing type annotations
  mypy --disallow-untyped-defs 1_bad.py
  """
  output:

  :1: error: Function is missing a type annotation  [no-untyped-def]
  Found 1 error in 1 file (checked 1 source file)
  """

  mypy --disallow-untyped-defs 1_corrected.py
  """
  output:

  Success: no issues found in 1 source file
  """

  # --strict Mode. This mode includes --disallow-untyped-defs and other strict checks
  mypy --strict 2_bad.py
  """
  output:

  :4: error: Incompatible types in assignment (expression has type "Literal['name']", variable has type "Literal['personal', 'business']")  [assignment]
  Found 1 error in 1 file (checked 1 source file)
  """
  ```

  the number in the output is the line where the error occurs

  using a `mypy.ini` configuration file

  ```text
  [mypy]
  # disallow_untyped_defs = true
  strict = true
  ```

  ```shell
  mypy 1_bad.py
  ```

## Pydantic

Pydantic

* a modern Python library that enforces type hints at runtime, provides customizable and user-friendly errors when data is invalid, and allows definition of data structures using Python type annotations.
* unlike some other libraries that provide similar functionality (such as [`dataclasses`](https://docs.python.org/3/library/dataclasses.html)), Pydantic provides a base model (aptly named `BaseModel`) that enables the parsing and validation functionality through inheritance.

```python
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
  id: int
  username: str
  email: str
  dob: datetime

try:
  u = User(
    id="one",
    username="freethrow",
    email="email@gmail.com",
    dob=datetime(1975, 5, 13),
  )
  print(u)
except Exception as e:
  print(e)
```

See `pydantic.ipynb`

resources:

* [Coding Crash Courses - Pydantic V2](https://www.youtube.com/watch?v=7aBRk_JP-qY)
