select class as "Class that has no ships" 
from `CLASSES` 
left join (select class as cl_b 
           from `CLASSES` 
           join (select class as cl 
                 from `SHIPS`) 
           where class = cl)
on class = cl_b 
where cl_b IS NULL