from sqlmodel import Field, Session, create_engine, select
from classes import *


def establilishConnectionToDataBase(inpdbusr: Annotated[str, "Database user."], inpdbpwd: Annotated[str, "password for database user."]):
    # Add at the beggining to setup db connection                      
    engine = create_engine(f"sqlitmariadb+mariadbconnector://{inpdbusr}:{}@127.0.0.1:3306/DB_NAME")
    SQLModel.metadata.create_all(engine)


def sendToDBModel(inpdict: Annotated[dict, "Dictonary with netflow information."]):
    """
    Estabilist database connection, prep statement and put in db.
    """

    # DATABASe

    # Prepare what to send
    toSend = NetFlowTable(srcIPAddr=X1, destIPAddr=X2, srcPort=X3, \
                        destPort=X4, layerThreeProto=X5, \
                        classOfService=X6, inpInterface=X7)
                      
# Add at the beggining to setup db connection                      
engine = create_engine("sqlitmariadb+mariadbconnector://USER:PWD!@127.0.0.1:3306/DB_NAME")
SQLModel.metadata.create_all(engine)


# Send to DB
with Session(engine) as session:
    session.add(toSend)
    session.commit()                      