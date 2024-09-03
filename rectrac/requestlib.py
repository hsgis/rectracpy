from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict, Union

from datetime import datetime

class Request_OpenSession(BaseModel):
    APIKey: str
    username: str

class Request_Table(BaseModel):
    SessionID: str
    Fields: str =  "*"
    Count: int = 10
    Filters: List[Dict[str, Union[datetime, str]]]

    @field_validator("Filters", mode="before")
    def check_filter(cls, val):
        if val:
            # for filter in val: #list
            for i in range(len(val)):
                for k, v in val[i].items(): #dict
                    if isinstance(v, bool):
                        val[i][k] = str(v).upper()
                    elif isinstance(v, datetime):
                        val[i][k] = datetime.strftime(v, "%m/%d/%Y %H:%M:%S.%f")
        return val

    def is_valid_filterby(self, filterby: str):
        if filterby in ["eq", "ne", "begins", "lt", "le", "gt", "ge", "contains"]:
            return True
        else:
            return False

    def is_valid_filterbys(self, filterByList:List[str]) -> bool:
        isValidFilterBy = [self.is_valid_filterby(i) for i in filterByList]
        if False in isValidFilterBy:
            return False
        else:
            return True

    def is_valid_endkey(self, endkey:str) -> bool:
        if endkey == "filter" or endkey == "filterby":
            return True
        else:
            return False

    def is_valid_endkeys(self, endKeyList:List[str]) -> bool:
        isValidFilterBy = [self.is_valid_endkey(i) for i in endKeyList]
        if False in isValidFilterBy:
            return False
        else:
            return True


    def validate_filter(self, inDict: Dict):
        endKeys = [i.split("_")[2] for i in inDict.keys()]
        filterBy = [v for k,v in inDict.items() if k.endswith("filterby")]
        validEndKeys = self.is_valid_endkeys(endKeys)
        validFilterBy = self.is_valid_filterbys(filterBy) if filterBy else None
        if validEndKeys:
            if validFilterBy == None or validFilterBy:
                return True
            else:
                return False
        else:
            return False

    def handle_filter(self, filterValue):
        returnDict = {}
        for filter in filterValue:
            isValid = self.validate_filter(filter)
            if isValid:
                returnDict.update(filter)
            else:
                raise Exception(f"Invalid filters for request: {filter}")
        return returnDict

    def model_dump_table(self):
        returnDict = {}
        for key, val in self.__dict__.items():
            if key == "Filters" and val:
                filterDict = self.handle_filter(val)
                returnDict.update(filterDict)
            else:
                returnDict[key] = val
        return returnDict
