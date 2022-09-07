# Halflap
Halflap is a simple, easy-to-use, easy-to-enhance RPC library that uses RabbitMQ and JSON-serializable payloads.
## Usage
Import `task` from the halflap module and decorate a top-level function. Assign a unique channel to the task. The args and kwargs of the function must be JSON-serializable:
```python3
from halflap import task

@task(channel="greetings")
def say_hello(name: str = "World"):
    print(f"Hello {name}!")
    # do more stuff...
```
Invoke the decorated function followed by `.rpc(...)` to enqueue the task, to be handled by a random worker also running the same codebase:
```python3
say_hello.rpc("from somewhere")
# prints "Hello from somewhere!" on whatever machine handles the task first
```
Or, the function *can* be invoked normally, bypassing the RPC feature, executing locally and immediately:
```python3
say_hello("you")
# prints "Hello you!" right now
```
## Notes
- You must have RabbitMQ installed and running somewhere, and all of the workers must be able to connect to it.
- Functions decorated as tasks must be top-level functions. Halflap doesn't work with, for example, class methods. This was intentional. We want to keep the code simple enough to read, understand, and modify.
- All of the arguments and keyword arguments must be JSON-serializable types. Halflap doesn't work with functions that take, for example, another function or class as an argument. You can use lookup tables to work around this in many cases.
- Decorated functions shouldn't return anything--the return values have nowhere to go.
- As a best-practice, write task functions that are idempotent. You should be able to call a task with the same arguments any number of times without changing the result.
- Halflap doesn't handle retries, timeouts, dead-letter queuing, scheduling, or any other fancy features. We want to provide a very simple module that can be expanded upon by the developer.