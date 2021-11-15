program dz;
var a,p,l,n,d,h:real;
begin
  writeln('Введите дину одной строки (в метрах)');
  readln(l);
  writeln('Введите кол-во строк на странице тетради ');
  readln(n);
  writeln('Введите кол-во страниц ');
  readln(p);
  d:=(l*n*p)*2;
  writeln('Введите длину письма ручки указанную на упаковке (в метрах) ');
  readln(a);
  h:=a/d;
  writeln('Количество тетрадей ',h:0:0);
end.