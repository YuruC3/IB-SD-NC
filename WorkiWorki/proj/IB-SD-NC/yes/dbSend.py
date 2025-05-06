from sqlmodel import Field, Session, create_engine, select, SQLModel
from classesss import *
from typing import Annotated

# DB conf
DB_HOST = "192.168.1.63"
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "221411"
DB_NAME = "Sflow_Data"
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def establilishConnectionToDataBase(inpdbusr: Annotated[str, "Database user."], inpdbpwd: Annotated[str, "password for database user."]):
    # Add at the beggining to setup db connection                      
    engine = create_engine(DATABASE_URL)
    # SQLModel.metadata.create_all(engine)
    return(engine)


def sendToDBModel(inpdict: Annotated[dict, "Dictonary with netflow information."], inpWhatTable: Annotated[str, "Name of class (table name)."]):
    """
    Estabilist database connection, prep statement and put in db.
    """

    # DATABASe

    # Prepare what to send
    if inpWhatTable == "ipBlocks":
        toSend = ipBlocks(BLOCK_IP=inpdict["BLOCK_IP"])
    elif inpWhatTable == "confBck":
        toSend = ipBlocks(RUN_CONF=inpdict["RUN_CONF"])
    else:
        return("No such table")

    TheDB = establilishConnectionToDataBase()

    # Send to DB
    with Session(TheDB) as session:
        session.add(toSend)
        session.commit()  

    
    # Add close connection to DB

    return(0)

                      
# Add at the beggining to setup db connection                      
# engine = create_engine("sqlitmariadb+mariadbconnector://USER:PWD!@127.0.0.1:3306/DB_NAME")
# SQLModel.metadata.create_all(engine)


                    