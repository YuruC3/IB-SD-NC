from typing import Optional, Annotated
from datetime import date
from sqlmodel import Field, SQLModel



# NetFlow table structure
class data(SQLModel, table=True):
    ID: int | None = Field(default=None, primary_key=True)
    IPV4_SRC_ADDR: Annotated[str, "Source IP address"]
    IPV4_DST_ADDR: Annotated[str, "Destination IP address"]
    SRC_PORT: Annotated[str, "Source Port"]
    DST_PORT: Annotated[str, "Destination Port"]
    PROTO: Annotated[str, "Layer 3 trotocol such as TCP or UDP"]
    DATE: Optional[date]






#
#
#
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▓▓▓▒▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▓▒▓▓▓▒▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▒▓▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▓▓▓▒▒▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▓▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▓▓▓▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▒▓▓▓▓▓▓▒▒▓▒▒▓▓▒▒▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▒▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▓▓▓▒▒▒▒▒▒▒▒▓▓▒▓▓▓▒▓▓▓▓▒▓▒▒▒▒▒▓▓▓▓▒▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▓▓▓▒▒▒▒▒▒▒▓▓▓▒▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▒▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▓▓▓▓▒▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▓▒▒▒▒▒▒▓▓▒▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▒▓▓▒
# ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▒▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▓▓▓▒▒▒▒▒▒▓▓▒▓▓▒▒▓▒▒▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▓▓▓▓▒
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▓▓▓▓▓▓▒▒▒▓▓▒▓▓▓▓▒▒▒▒▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▓▓▓▓▒
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓▓▓▓▓▓▒
# ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▓▒▒▒▓▓▒▓▓▓▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▓▓▓▓▓▒▒
# ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓▓▓▒▒▒▓▓▒▓▓▓▒▒▒▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▒▒
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▓▒▓▓▓▒▒▒▓▓▓▓▓▒▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓███▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▒▓▓██▓▓▓▒▒▓▓▓▒▒▒
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒▓▓▓▓▒▒▒▓▓▒▒▓▓▓▒▒▒▓▓▓█▓▓▓▓▓▓▒▓▓▓▓▓▓█▓▓▓▓▓▒▒▓
# ▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▒▓▓██▓▓▓▓█▓▓▓██▓▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▓▒▒▒▓▓▒▒▒▒▓▓▓▓▓█▓▓▓███▓█▓▓██▓▓███▓▓▓▒▒▒▓
# ▓▓█▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓██▓▓██▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▓▓▒▒▒▒▓▓▓▓▓▓▓█▓▒▓███████████▓▓▓██▓▓▓▒▒▒▓
# ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓█▓▓▒▓▓▓▓▓████████████▓▓██▓▓█▓▓▓▓▓▒▓▓▓▒▒▒▒▒▓▓▒▓▓▒▒▒▒▒▒▓▓▓▓▓▒▓▓███████████▓▒▓██▓▓▒▒▒▓▓
# ▒▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▒▓▓▒▒▒▓▓▓██████████████▓▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓█▓▓█▓▓▓▓▒▒▓▓▓▓▓▒▒▓▓▓
# ▒▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▒▓▒▒▒▒▒▒▒▒▓▓███▓▓█▓▓███▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓█▓▓█▓▒▓▓▓▓▓▒▒▓▓▓▓
# ▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓██▓▓▓██▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▒▒▓▓▓▓▓▒▓▓▓▓▓
# ▒▒▓▓▓█▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓█▓▓▓▓▓█████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▒▒▓▓▓▓▓
# ▒▓▓▓▓█▓▓▓▓▓▓▒▒▒▒▒▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▒▒▒▓▓▓▓▒▓▓▓▓▓▓▓
# ▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
# ▒▒▓▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▒▒▓▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓
# ▒▓▓▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓
# ▒▓▓▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▒▒▒▒▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓
# ▒▓▓▒▓▓▓▓▓▓▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓
# ▒▒▒▓▓▓▒▓▓▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
# ▒▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓
# ▒▓▓▒▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▓▒▒▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▓▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓



