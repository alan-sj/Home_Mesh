from sqlalchemy import create_engine, text

DATABASE_URL= "mysql+pymysql://root:2801@127.0.0.1:3306/devdb"

engine= create_engine(DATABASE_URL)

def test_db():
    with engine.connect() as conn:
        result=conn.execute(text("Desc users"))
        print(result.fetchall())
    return {"db_status":"connected"}