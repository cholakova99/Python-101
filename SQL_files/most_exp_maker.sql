select maker as "most expensive maker" 
from product 
join (select model as mod 
      from pc 
      order by price desc) 
where product.model = mod 
limit 1