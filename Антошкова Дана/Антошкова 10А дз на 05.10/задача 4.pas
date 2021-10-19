program zadacha4;
var r1, r2, r3, r: real;
begin
  write('Введите r1: ');  
  read(r1);
  write('Введите r2: ');  
  read(r2);
  write('Введите r3: ');  
  read(r3);
  r := (r1 * r2 * r3)/(r1 * r2 + r2 * r3 + r3 * r1);
  writeln('Сопротивление всей цепи =  ', r:3:2);
end.