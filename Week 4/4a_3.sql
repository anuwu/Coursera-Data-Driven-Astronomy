select s.kepler_id, t_eff, s.radius
from Star as s
left outer join planet p using(kepler_id)
where p.kepler_id is NULL
order by t_eff desc, kepler_id
