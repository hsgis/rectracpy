from pydantic import BaseModel
import requests

from .requestlib import Request_OpenSession, Request_Table
from .responselib import Response_Login, Response_Logout, Response_SearchTable, Response_GetFields

class RecTrac(BaseModel):
    BaseHREF: str
    APIKey: str
    username: str

    def requestSuccess(self, request):
        if request.status_code != 200:
            return False
        return True

    def login(self) -> str:
        requestData = Request_OpenSession(APIKey=self.APIKey, username=self.username)
        endUrl = f"{self.BaseHREF}/authenticate/login"
        request = requests.post(endUrl, data=requestData.model_dump())
        if request.status_code != 200:
            raise Exception(f"Could not login: {request.status_code}-{request.text}")
        response = Response_Login(**request.json())
        return response.sessionID

    def endSession(self, sessionId:str) -> Response_Logout:
        endUrl = f"{self.BaseHREF}/authenticate/login"
        request = requests.post(endUrl, data={"SessionID": sessionId})
        if not self.requestSuccess(request):
            raise Exception("Could not endSession: {request.text}")
        response = Response_Logout(**request.json())
        return response

    def searchTable(self, table:str, requestData:Request_Table) -> Response_SearchTable:
        endUrl = f"{self.BaseHREF}/search/get/{table}"
        request = requests.get(endUrl, params=requestData.model_dump_table())
        if not self.requestSuccess(request):
            raise Exception("Could not searchTable: {request.text}")
        response = Response_SearchTable(**request.json())
        return response

    def getTables(self, sessionId:str):
        endUrl = f"{self.BaseHREF}/search/tables"
        request = requests.get(endUrl, params={"SessionId": sessionId})
        if not self.requestSuccess(request):
            raise Exception("Could not getTables: {request.text}")
        return request.json()

    def getFields(self, table:str, sessionId:str):
        endUrl = f"{self.BaseHREF}/search/fields/{table}"
        request = requests.get(endUrl, params={"SessionId": sessionId})
        if not self.requestSuccess(request):
            raise Exception("Could not getFields: {request.text}")
        return Response_GetFields(**request.json())
