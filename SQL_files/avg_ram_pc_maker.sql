select avg(ram), maker_pc 
from pc 
join (select model as model_pc, maker as maker_pc 
      from product 
      join (select maker as mk 
            from product 
            where type = "Printer") 
      where type = "PC" and mk=maker) 
where pc.model = model_pc 
group by maker_pc