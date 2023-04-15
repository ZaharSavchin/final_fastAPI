from pydantic import BaseModel


class BackCallBaseModel(BaseModel):
    contacts: str
    message: str


class BackCallCreateModel(BackCallBaseModel):
    pass


class BackCallUpdateModel(BackCallBaseModel):
    pass


class BackCallModel(BackCallBaseModel):
    id: int

    class Config:
        orm_mode = True