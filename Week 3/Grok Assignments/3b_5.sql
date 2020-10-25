select kepler_id, count(*)
from Planet
group by kepler_id
having count(*) > 1
order by count(*) desc
