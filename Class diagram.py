import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, UniqueConstraint, select, ForeignKey
from sqlalchemy.orm import mapper , registry , relationship
#from sqlalchemy.orm import map_imperatively
from sqlalchemy import text
from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column
engine = create_engine('mssql+pyodbc://DESKTOP-AED11QE/JenkinsDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
mapper_registry = registry()
#Jenkinsdata = MetaData()
Build_Jen_table = Table("Build_Jen", mapper_registry.metadata,
                        Column('Build_number', Integer, primary_key=True),
                        Column('start_date_build', String(10), nullable=False),
                        Column("end_date_build", String(10), nullable=False),
                        Column("version_number", Integer, nullable=False),
                        Column("execution_status", String(50), nullable=False),
                        Column("output_console", String(255), nullable=False),
                        Column('id_job', Integer, ForeignKey('job.id'), nullable=False),
                     )

Job_Jen_table = Table("Job_Jen", mapper_registry.metadata,
                        Column('id_job', Integer, primary_key=True),
                        Column('job_name', String(50), nullable=False),
                        Column("latest_success", String(10), nullable=False),
                        Column("latest_failure", String(10), nullable=False),
                        Column("parameters_job", String(255), nullable=False),
                        Column("address_job", String(50), nullable=False),
                     )

class Build_Jen:
    def __init__(self, Build_number, start_date_build, end_date_build, version_number, execution_status, output_console):
        self.Build_number = Build_number
        self.start_date_build = start_date_build
        self.end_date_build = end_date_build
        self.version_number = version_number
        self.execution_status = execution_status
        self.output_console = output_console

    def fromdict(self, data):
        self.Build_number = data.get('Build_number')
        self.start_date_build = data.get('start_date_build')
        self.end_date_build = data.get('end_date_build')
        self.version_number = data.get('version_number')
        self.execution_status = data.get('execution_status')
        self.output_console = data.get('output_console')
class Job_Jen:
    def __init__(self, id_job, job_name, latest_success, latest_failure, parameters_job, address_job):
        self.id_job = id_job
        self.job_name = job_name
        self.latest_success = latest_success
        self.latest_failure = latest_failure
        self.parameters_job = parameters_job
        self.address_job = address_job

    def fromdict(self, data):
        self.id_job = data.get('id_job')
        self.job_name = data.get('job_name')
        self.latest_failure= data.get('latest_failure')
        self.latest_success = data.get('latest_success')
        self.parameters_job = data.get('parameters_job')
        self.address_job = data.get('address_job')

Build_Jen1 = Build_Jen(67, "10-07-2023", "10-07-2023", 10, "SUCCESS", "Démarré par l'utilisateur Farah Elloumi Running as SYSTEM Building in workspace C:ProgramData\Jenkins\.jenkins\workspace\MonPrem [MonPrem] $ cmd /c call C:\Windows\TEMP\jenkins1168184064063655989.batC:\ProgramData\Jenkins\.jenkins\workspace\MonPrem>echo test test C:\ProgramData\Jenkins\.jenkins\workspace\MonPrem>exit 0 Finished: SUCCESS")
Build_Jen1.fromdict({"Build_number": 67, "start_date_build": "10-07-2023", "end_date_build": "10-07-2023", "version_number": 10, "execution_status":"SUCCESS", "output_console":"Démarré par l'utilisateur Farah Elloumi Running as SYSTEM Building in workspace C:ProgramData\Jenkins\.jenkins\workspace\MonPrem [MonPrem] $ cmd /c call C:\Windows\TEMP\jenkins1168184064063655989.batC:\ProgramData\Jenkins\.jenkins\workspace\MonPrem>echo test test C:\ProgramData\Jenkins\.jenkins\workspace\MonPrem>exit 0 Finished: SUCCESS"})
print(f"Build_Jen1={Build_Jen1.__dict__}")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

stmt = select(Build_Jen_table).\
            where(Build_Jen_table.c.start_date_build == '10-07-2023')

results = session.execute(stmt).fetchall()
print(results)
print(stmt)