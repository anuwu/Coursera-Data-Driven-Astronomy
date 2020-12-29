select koi_name, p.radius, Star.radius
from Planet as p
join (
  select kepler_id, radius
  from Star as s
  order by radius desc
  limit 5
) as Star using(kepler_id)
