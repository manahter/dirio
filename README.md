# Dirio - Python Independent Class Process
[![Dirio](https://img.shields.io/badge/version-0.1.1-orange?&style=flat&llogoColor=white)](https://github.com/manahter/dirio)
[![Dirio](https://img.shields.io/github/license/manahter/dirio)](https://github.com/manahter/dirio/blob/main/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/manahter/dirio)

## Features
* Inherit Class independently from running script.
* Uses serialization method with JSON
* You do not wait in classes like Socket

## Usage

```python
# Import module
from dirio import Dirio


# Inherit class
# args mut be tuple. Don't forget to put a comma -> args=(xx, )
try_cls = Dirio(target=TryClass, args=("arg1",), kwargs={"key1": "val1"})
# PARAMETERS:
#   target      : class : Target Class
#   args        : tuple : Arguments for Target Class
#   kwargs      : dict  : Keyword Arguments for Target Class
#   tempdir     : str   : Temporary directory path. If it is empty, system temp path is used.
#   keeperiod   : float : !!! Not activated. Do not use.
#   looperiod   : float : Independent Class renewal frequency. 
#                         Default: .05
#                         Smaller value, more CPU
#                         Bigger  value, delayed processing
#   worker      : bool  : You don't use. The class itself uses



# Standard, Call your method, 
# First time return value is None
try_cls.yourmethod("arg1", key="value")
#-> Returned: None

# In the next call, the return value is that of the previous one.
try_cls.yourmethod("arg1", key="value")
#-> Returned: "result_of_previous_call_returned"

# If you want to return the value of the method you are calling;
# Notice; dr_code=True used
call_code = try_cls.yourmethod("arg1", key="value", dr_code=True)
#-> call_code -> 12

# Give the result of call code 12
try_cls.yourmethod("arg1", key="value", dr_code=call_code)
#-> Returned: None

# If None, the method operation is not yet run or finished.
# We can call again and again
try_cls.yourmethod("arg1", key="value", dr_code=call_code)
#-> Returned: "result_of_previous_call_returned"

# We can wait as long as we want the answer to arrive
# dr_wait=3.4 -> Wait 3.4 second
try_cls.yourmethod("arg1", key="value", dr_wait=3.4)
#-> Returned: "result_of_previous_call_returned"
# if the operation is not over
#-> Returned: None

# Wait until the reply comes
# dr_wait=-1 -> until the operation is over
try_cls.yourmethod("arg1", key="value", dr_wait=-1)
#-> Returned: "result_of_previous_call_returned"

# Terminate the Dirio Process. 
# Make sure to use this at the end of the script.
try_cls.dr_terminate()
```

NOTE : Sorry, my English is poor. I use translation.