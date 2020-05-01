select maker, c_m as "count models" 
from (select maker, count(maker) as c_m 
      from product 
      where product.type = "PC" 
      group by maker) 
where c_m > 2 