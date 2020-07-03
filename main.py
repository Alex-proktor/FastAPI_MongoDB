from fastapi import FastAPI
from pydantic import BaseModel

from models import Users

app = FastAPI()


class Item(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int


@app.get("/users")
async def read_users(name: str = None,
                     email: str = None,
                     age: int = None,
                     company: str = None,
                     join_date: str = None,
                     job_title: str = None,
                     gender: str = None,
                     salary: int = None):
    us = Users()
    user = await us.get(name=name,
                        email=email,
                        age=age,
                        company=company,
                        join_date=join_date,
                        job_title=job_title,
                        gender=gender,
                        salary=salary)
    return user
