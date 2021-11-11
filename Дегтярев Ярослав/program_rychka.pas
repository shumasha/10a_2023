program b1;
var S:integer;
    N,K,V:real ;
begin
 write('Длинна одной тетради S = ');
 read(s);
 write('Объем одного стрежня V = ');
 read(v);
 write('Расход чернил в шариковой ручке K = ');
 read(k);
 writeln('Количество тетрадей на которое хватит одной ручки N = ', V/(s*k):3:1);
end.
