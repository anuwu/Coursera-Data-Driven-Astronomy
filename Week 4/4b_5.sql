alter Table Star
add column ra float,
add column decl float ;

delete from Star ;
copy Star from 'stars_full.csv' csv; 
