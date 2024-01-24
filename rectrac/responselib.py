from pydantic import BaseModel
from typing import Any, List, Dict

class Response_Login(BaseModel):
    success: bool
    httpStatus: int
    sessionID: str

class Response_Logout(BaseModel):
    success: bool
    httpStatus: int
    sessionID: str

class Response_SearchTable(BaseModel):
    success: bool
    sessionID: str
    records: List[Dict[str,Any]]

class Response_GetFields(BaseModel):
    success: bool
    sessionID: str
    fields: List[Dict[str,Any]]
