select s.radius, count(*)
from Star as s
join planet using(kepler_id)
group by kepler_id
having s.radius > 1 and count(*) > 1
order by s.radius desc
