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


def load_job(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs where id = {id}"))
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if (len(rows) == 0):
      return None
    else:
      return row


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    
    conn.execute(query, {
            'job_id': job_id,
            'full_name': data['name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })
                 # job_id=job_id,
                 # full_name=data['name'],
                 # email=data['email'],
                 # linkedin_url=data['linkedin_url'],
                 # education=data['education'],
                 # work_experience=data['work_experience'],
                 # resume_url=data['resume_url'])
                 
