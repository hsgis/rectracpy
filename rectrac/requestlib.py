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

    @field_validator("Filters")
    def check_filter(cls, val):
        if val:
            for filter in val: #list
                for k, v in filter.items(): #dict
                    if isinstance(v, datetime):
                        filter[k] = datetime.strftime(v, "%m/%d/%Y %H:%M:%S.%f")
        return val

    def is_valid_filterby(self, filterby: str):
        if filterby in ["eq", "ne", "begins", "lt", "le", "gt", "ge", "contains"]:
            return True
        else:
            return False

    def validate_filter(self, inDict: Dict):
        endKeys = [i.split("_")[2] for i in inDict.keys()]
        filterBy = [v for k,v in inDict.items() if k.endswith("filterby")]
        if endKeys == ["filter", "filterby"] and self.is_valid_filterby(filterBy[0]):
            return True
        elif endKeys == ["filter"]:
            return True
        else:
            return False


    def handle_filter(self, filterValue):
        returnDict = {}
        for filter in filterValue:
            isValid = self.validate_filter(filter)
            if isValid:
                returnDict.update(filter)
            else:
                raise Exception(f"Invalid filter for request: {filter}")
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
