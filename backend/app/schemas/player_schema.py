from pydantic import BaseModel

class PlayerBase(BaseModel):
    full_name: str
    first_name: str
    last_name: str
    is_active: bool

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        from_attributes = True
