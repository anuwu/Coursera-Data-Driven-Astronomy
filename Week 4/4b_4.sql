create Table Star (
  kepler_id integer primary key,
  t_eff integer not NULL,
  radius float not NULL
) ;

create Table Planet (
  kepler_id integer references Star (kepler_id),
  koi_name varchar(20) primary key,
  kepler_name varchar(20),
  status varchar(20) not NULL,
  period float,
  radius float,
  t_eq integer
) ;

COPY Star FROM 'stars.csv' CSV;
COPY Planet FROM 'planets.csv' CSV;
