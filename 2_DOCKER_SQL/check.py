from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
connection = engine.connect()
print("Connected successfully!")
connection.close()