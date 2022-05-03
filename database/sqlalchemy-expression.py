from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo=False)

print(engine.table_names())

meta = MetaData()

students = Table("students", meta,
                 Column('id', Integer, primary_key=True),
                 Column("name", String),
                 Column("address", String),
                 Column("age", Integer)
                 )

meta.create_all(engine)

insertstatemen1 = students.insert().values(
    name="Henry", address="Vienna", age="31")

connection = engine.connect()
connection.execute(insertstatemen1)

select1 = students.select().where(students.c.age > 30)

result = connection.execute(select1)

for row in result:
    print(row)
