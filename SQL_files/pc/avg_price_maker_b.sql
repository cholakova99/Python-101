select avg(price)
from (select pc.price from pc 
    join product on pc.model = product.model 
    where product.maker = "B" 
    union all select laptop.price from laptop 
    join product on laptop.model = product.model 
    where product.maker = "B")