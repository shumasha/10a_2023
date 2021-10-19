program zadacha16;
var a, b, c, d, e: integer;
begin
  write('Введите черытехзначное число: ');  
  read(a);
  b:=a mod 10;
  c:=(a div 10) mod 10;
  d:=(a div 100) mod 10;
  e:=(a div 1000) mod 10;
  write('Произведение всех цифр = ',b*c*d*e);
end.