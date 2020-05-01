select name, launched, country, numguns  
from `SHIPS`
join (select country, numguns, class as cl 
      from `CLASSES`) 
where class=cl