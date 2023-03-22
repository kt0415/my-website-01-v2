from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://19y0ehhumewfocc6ycer:pscale_pw_dJanrVCElOakAlN1LBw1dwMYDrqr1gbSU46vHGTvqPD@ap-south.connect.psdb.cloud/kt17db?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  column_names = result.keys()
  for row in result.all():
    result_dicts.append(dict(zip(column_names, row)))

  print(result_dicts)
