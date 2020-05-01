select ship as "Ship in battle 1942", battle as "battle - 1942"  
from `OUTCOMES` 
join (select name as bat_name 
      from `BATTLES` 
      where date like "%1942%") 
where battle=bat_name