from pydantic import BaseModel


class HelloPage(BaseModel):
    name: str = "Hello"