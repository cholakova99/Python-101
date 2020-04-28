SELECT starname
from STARSIN
join MOVIESTAR
on STARSIN.starname = MOVIESTAR.NAME
where STARSIN.movietitle LIKE "%Terms%" and MOVIESTAR.GENDER = "M";