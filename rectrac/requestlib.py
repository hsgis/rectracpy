from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict

class Request_OpenSession(BaseModel):
    APIKey: str
    username: str

class Request_CloseSession(BaseModel):
    SessionID: str

class Request_GetTables(BaseModel):
    SessionID: str

class Request_Table(BaseModel):
    SessionID: str
    Fields: str =  "*"
    Count: int = 10
    Filters: Optional[Dict[str, str]] = None

    # @field_validator("Filters")
    # def check_filter(cls, val):
    #     if val:
    #         validFilterByValues = ["eq", "ne", "begins", "lt", "le", "gt", "ge", "contains"]
    #         verificationFilterValues = "_".join(validFilterByValues)
    #         for filter in val:
    #             for k, v in filter.items():
    #                 keySections = k.split("_")
    #                 keyLength = len(keySections)
    #                 if keyLength < 3 or keyLength > 3 or keySections[-1] not in ["filter", "filterby"]:
    #                     raise Exception("Filter keys not formatted correctly.")
    #                 elif keySections[-1] == "filterby" and not v in verificationFilterValues:
    #                         raise Exception("Filter values not formateed correctly")
    #                 elif keySections[-1] == "filter" and v in verificationFilterValues:
    #                         raise Exception("Filter values not formateed correctly")
    #     return val

    def model_dump_table(self):
        returnDict = {}
        for key, val in self.__dict__.items():
            if key == "Filters" and val:
                for k, v in val.items():
                    returnDict[k] = v
            else:
                returnDict[key] = val
        return returnDict
