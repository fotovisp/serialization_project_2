from pydantic import BaseModel
from typing import List


class Person(BaseModel):
    name: str
    age: int

person = Person(name="John", age=42)
js = person.model_dump_json(indent=4)
print(js)

with open("person.json", "w") as f:
    f.write(js)

