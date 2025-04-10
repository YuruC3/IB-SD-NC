from typing import Optional, Annotated

from sqlmodel import Field, SQLModel

# NetFlow table structure
class NetFlowTable(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    srcIPAddr: Annotated[int, "Source IP address"]
    destIPAddr: Annotated[int, "Destination IP address"]
    srcPort: Annotated[int, "Source Port"]
    destPort: Annotated[int, "Destination Port"]
    layerThreeProto: Annotated[str, "Layer 3 trotocol such as TCP or UDP"]
    classOfService: Optional[Annotated[int, "Class of Service TOS(bytes)"]] = None
    inpInterface: Annotated[str, "Interface on which packet came"]
    