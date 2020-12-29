create Table Planet (
  kepler_id integer not NULL,
  koi_name varchar(15) not NULL unique,
  kepler_name varchar(15),
  status varchar(20) not null,
  radius float not null
) ;

insert into Planet values (6862328, 'K00865.01', NULL, 'CANDIDATE', 119.021), 
(10187017, 'K00082.05', 'Kepler-102 b',	'CONFIRMED', 5.286),
(10187017, 'K00082.04',	'Kepler-102 c',	'CONFIRMED', 7.071) ;
