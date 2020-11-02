import sys
sys.path.append('/home/ec2-user/cahcing-0.0.0-py3.7.egg')
from caching.dto.marks import checkDataInCache
sql="""select id,marks,subject,
            case
            when marks>=90 then 'A'
            when marks>=80 then 'B'
            when marks>=70 and marks<=79 then 'C'
            else 'D'
            end as grade
            from marks"""
checkDataInCache(sql)