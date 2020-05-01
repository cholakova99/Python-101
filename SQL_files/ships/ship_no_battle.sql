 select name, country 
 from (select name, country 
       from `SHIPS` 
       join (select country, class as c_C 
            from `CLASSES`)
       where class = c_c) 
 join (select name as ship_no_battle 
       from `SHIPS` 
       left join (select ship as ship_in_battle 
                  from `OUTCOMES`) on name=ship_in_battle 
       where ship_in_battle IS NULL) 
 where name = ship_no_battle