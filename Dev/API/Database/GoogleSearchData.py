from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert
from sqlalchemy import *
from sqlalchemy import exc
from sqlalchemy.engine import reflection
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.inspection import inspect
from sqlalchemy.engine import *

def Google_Search_Upsert(Googlefeeddata):
    #print(Googlefeeddata)
    engine = create_engine("postgresql+pg8000://postgres:password@localhost:5432/SearchTrends")
    connect = engine.connect()
    meta = MetaData(bind=engine)
    meta.reflect(bind=engine)
    #table = meta.tables['GoogleSearchTrends']
    GoogleFeedData_table = Table('googlesearchtrends', meta)
    meta = MetaData(engine)
    stmt = insert(GoogleFeedData_table).values(Googlefeeddata)
    primary_keys = [key.name for key in inspect(GoogleFeedData_table).primary_key]
    insp = reflection.Inspector.from_engine(engine)
    print(insp.get_columns(GoogleFeedData_table))
    update_dict = {
        c.name: c
        for c in stmt.excluded
        if not c.primary_key and c.name != 'created_date'
        }
    print(update_dict)
    update_stmt = stmt.on_conflict_do_update(
        index_elements=primary_keys,
        set_=update_dict,
    )
    with engine.connect() as conn:
        result = conn.execute(update_stmt)
        return "Success"

