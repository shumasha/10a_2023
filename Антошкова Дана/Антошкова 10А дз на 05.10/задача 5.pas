program zaacha5;
var a, d, n, s: real;
begin
  write('Введите первый член прогрессии: ');  
  read(a);
  write('Введите разность членов: ');  
  read(d);
  write('Введите число членов: ');  
  read(n);
  s:= ((2*a+d*(n-1))/2)*n;
  writeln('Сумма членов арифметической прогрессии = ', s);
end.