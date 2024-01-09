from pydantic import BaseModel
import requests

from .requestlib import Request_GetTables, Request_OpenSession, Request_CloseSession, Request_Table
from .responselib import Response_Login, Response_Logout, Response_SearchTable

class RecTrac(BaseModel):
    BaseHREF: str
    APIKey: str
    username: str

    def login(self) -> str:
        requestData = Request_OpenSession(APIKey=self.APIKey, username=self.username)
        endUrl = f"{self.BaseHREF}/authenticate/login"
        request = requests.post(endUrl, data=requestData.model_dump())
        print(request.text)
        if request.status_code != 200:
            raise Exception(f"Could not login: {request.status_code}-{request.text}")
        response = Response_Login(**request.json())
        return response.sessionID

    def endSession(self, requestData:Request_CloseSession) -> Response_Logout:
        endUrl = f"{self.BaseHREF}/authenticate/login"
        request = requests.post(endUrl, json=requestData.model_dump_json())
        response = Response_Logout(**request.json())
        return response

    def searchTable(self, table:str, requestData:Request_Table) -> Response_SearchTable:
        endUrl = f"{self.BaseHREF}/search/get/{table}"
        request = requests.get(endUrl, params=requestData.model_dump_table())
        print(requestData.model_dump())
        print("here:", request.text)
        response = Response_SearchTable(**request.json())
        return response

    def getTables(self, requestData:Request_GetTables):
        endUrl = f"{self.BaseHREF}/search/tables"
        request = requests.get(endUrl, params=requestData.model_dump())
        print(request.text)
