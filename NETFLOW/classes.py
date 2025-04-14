from typing import Optional, Annotated

from sqlmodel import Field, SQLModel

# NetFlow table structure
class NetFlowTable(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    IPV4_SRC_ADDR: Annotated[str, "Source IP address"]
    IPV4_DST_ADDR: Annotated[str, "Destination IP address"]
    NEXT_HOP: Annotated[str, "Next Hop address"]
    INPUT: Annotated[str, "Interface on which packet came"]
    OUTPUT: Annotated[str, "Interface on which packet went off"]
    IN_PACKETS: Annotated[str, "In packets I guess"]
    IN_OCTETS: Annotated[str, "Out packets I guess"]
    FIRST_SWITCHED: Annotated[str, "Something with how much time it took for packet"]
    LAST_SWITCHED: Annotated[str, "Something with how much time it took for packet"]
    SRC_PORT: Annotated[str, "Source Port"]
    DST_PORT: Annotated[str, "Destination Port"]
    TCP_FLAGS: Annotated[str, "TCP flags (duh)"]
    PROTO: Annotated[str, "Layer 3 trotocol such as TCP or UDP"]
    TOS: Optional[Annotated[istrnt, "Class of Service TOS(bytes)"]]
    SRC_AS: Annotated[str, "Source ASN"]
    DST_AS: Annotated[str, "Destination ASN"]
    SRC_MASK: Annotated[str, "Source networkmask"]
    DST_MASK: Annotated[str, "Source networkmask"]
    DATE: Optional[date]
