program treugolnik;
var a,b,c,al,be,ga,p,s,h:real;
begin
  writeln('Введите сторону ВС');
  read(a);
  writeln('Введите сторону АС');
  read(b);
  writeln('Введите угол гамма');
  read(ga);
  c:=sqrt(a*a+b*b-2*a*b*cos(pi*ga/180));
  al:=arccos((b*b+c*c-a*a)/(2*b*c))*180/pi;
  be:=180-al-ga;
  h:=b*sin(al*pi/180);
  s:=c*h*0.5;
  p:=a+b+c;
  writeln('Сторона АВ = ',c:7:3);
  writeln('Угол альфа = ',al:7:3);
  writeln('Угол бета = ',be:7:3);
  writeln('Высота трегольника = ',h:7:3 );
  writeln('Плрщадь = ',s:7:3);
  writeln('Переметр = ',p:7:3);
  
end.