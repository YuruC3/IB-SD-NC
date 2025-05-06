from typing import Optional, Annotated
from datetime import date
from sqlmodel import Field, SQLModel

# Blocked IP table
class logs(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    PROBLEM: Annotated[str, "yeee"]
    SOLUTION: Annotated[str, "Blocked IP"]
    #DATE: Optional[date]


# Running config table
class confBck(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    RUN_CONF: Annotated[str, "Backed up running-config"]
    DATE: Optional[date]
