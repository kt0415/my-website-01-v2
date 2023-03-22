from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECT_STR']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  column_names = result.keys()
  for row in result.all():
    jobs.append(dict(zip(column_names, row)))
  return jobs
