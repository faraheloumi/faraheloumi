import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, UniqueConstraint, select, ForeignKey, Boolean, insert
from sqlalchemy.orm import mapper, registry, relationship, declarative_base, Session
from sqlalchemy import text
from sqlalchemy.orm import Mapped

engine = create_engine('mssql+pyodbc://DESKTOP-AED11QE/JenkinsDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
mapper_registry = registry()
user_Jen_table = Table("user_Jen", mapper_registry.metadata,
                        Column('id_user', Integer, primary_key=True),
                        Column('user_name', String(20), nullable=False),
                        Column("password_user", String(20), nullable=False),
                        Column("address_user", String(50), nullable=False),
                        Column("roles", String(20), nullable=False)
                     )
nodes_Jen_table = Table("nodes_Jen", mapper_registry.metadata,
                        Column('node_name', String(50), primary_key=True),
                        Column('computing_power', Integer, nullable=False),
                        Column("Memory", String(255), nullable=False),
                        Column("Storage", String(255), nullable=False),
                        Column("Node_type", String(255), nullable=False),
                        Column("operating_system", String(255), nullable=False),
                        Column("Hardware_and_software_System", String(255), nullable=False),
                        Column("is_offline", Boolean, nullable=False),
                        Column("id_user", Integer, ForeignKey('user.id'), nullable=False)
                     )
class user_Jen:
    def __init__(self, id_user, user_name, password_user, address_user, roles):
        self.id_user = id_user
        self.user_name = user_name
        self.password_user = password_user
        self.address_user = address_user
        self.roles = roles
class nodes_Jen:
    def __init__(self, node_name, computing_power, Memory, Storage, Node_type, operating_system, Hardware_and_software_System, is_offline):
        self.node_name = node_name
        self.computing_power = computing_power
        self.Memory = Memory
        self.Storage = Storage
        self.Node_type = Node_type
        self.operating_system = operating_system
        self.Hardware_and_software_System = Hardware_and_software_System
        self.is_offline = is_offline
user_Jen1 = user_Jen(1, "farah", "farahfarahfarah", "route ...", "java")
nodes_Jen1 = nodes_Jen("master", 1, "N/A", "6,48 GB	", "Permanent_Agent","null","null", 1)
print (user_Jen1)
