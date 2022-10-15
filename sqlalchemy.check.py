from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric, Text, Date

engine = create_engine('sqlite:///clean_stations.csv')
engine2 = create_engine('sqlite:///clean_measure.csv')
meta = MetaData()

clean_measure = Table(
   'clean_measure', meta,
   Column('station', Integer, primary_key=True),
   Column('date', Date),
   Column('precip', Numeric),
   Column('tobs', Numeric)
)


clean_stations = Table(
   'clean_stations', meta,
   Column('station', Integer, primary_key=True),
   Column('latitude', Numeric),
   Column('longitude', Numeric),
   Column('elevation', Numeric),
   Column('name', Text),
   Column('country', String),
   Column('state', String)
)

meta.create_all(engine)
meta.create_all(engine2)
print(engine.table_names())