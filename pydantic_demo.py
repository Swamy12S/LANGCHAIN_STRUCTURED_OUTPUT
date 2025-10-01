from pydantic import BaseModel,EmailStr,Field #basemodel ne inherit chestham
from typing import Optional
class student(BaseModel):

    name:str = 'swamy'
    age:Optional[int] = None    # optional 
    email:EmailStr
    cgpa:float =Field(gt=0,lt=10)  # constains

new_student ={'age': '23','email':'abc@gmail.com','cgpa':5}   # endhuloo kuda name evochu 'name':'swamy'

student = student(**new_student)

print(student)