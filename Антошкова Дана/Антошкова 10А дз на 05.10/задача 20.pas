program zadacha20;
var a:real;
begin
  write('Введите уголв радианах:',a);
  read(a);
  writeln('градусы:',a*(180/pi):3:2);
  writeln('минуты:',a*(180*60/pi):3:2);
  writeln('секунды:',a*(180*60*60/pi):3:2);
end.