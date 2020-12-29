select s.radius as "sun_radius" , p.radius as "planet_radius"
from Star as s
inner join Planet p
on s.kepler_id = p.kepler_id
where s.radius/p.radius > 1
order by s.radius desc
