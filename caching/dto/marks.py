import json
import time
from caching.connection.connectionsql import Session
from caching.connection.connectionredis import client

session=Session()

def avgtime(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(f"diff in seconds---{end_time-start_time} seconds")
    return inner


@avgtime
def checkDataInCache(sql):
    '''Get data from redis or postgres'''
    res=client.get(sql)
    if res:
        print('data getting from es')
        print(json.loads(res))
    else:
        print('getting data from postgres')
        res=session.execute(sql).fetchall()
        client.setex(sql,100,json.dumps(res))
        print(res)

if __name__=="__main__":
    sql="""select id,marks,subject,
            case 
            when marks>=90 then 'A'
            when marks>=80 then 'B'
            when marks>=70 and marks<=79 then 'C'
            else 'D'
            end as grade
            from marks"""
    print(sql)
    checkDataInCache(sql)