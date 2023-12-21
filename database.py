from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:''@localhost/jobs")

conn = engine.connect()


result = conn.execute(text("select * from job_info"))
print(result.fetchall)