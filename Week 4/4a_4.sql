select round(avg(t_eq), 1), min(t_eff), max(t_eff)
from Star s
join Planet p using(kepler_id)
where t_eff > (select avg(t_eff) from Star)
