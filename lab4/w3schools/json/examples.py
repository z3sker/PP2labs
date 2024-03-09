# Python JSON

# JSON (JavaScript Object Notation) is a lightweight data interchange format.
# JSON in Python

import json

# Example: Convert JSON to Python
# If you have a JSON string, use json.loads() to parse it into a Python dictionary.

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# Converting from Python to JSON

# Example: Convert from Python to JSON
# Use json.dumps() to convert Python objects to JSON strings.

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)

# You can convert Python objects of various types into JSON strings.

# Example: Convert Python objects into JSON strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# JSON Formatting

# Example: Format the JSON result for readability
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Use indent parameter for indentation and separators parameter for changing separators.
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Ordering the Result

# Example: Order the keys in the JSON result
print(json.dumps(x, indent=4, sort_keys=True))
