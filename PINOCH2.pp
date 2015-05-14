program ideone;
var
t:integer;
N,i,count,temp,a,b: LongInt;
begin
	readln(t);
	while t > 0 do
		begin
		readln(N);
		count:=0;temp:=0;
		for i:=0 to N-1 do
			begin
			read(a);
			if i = 0 then
				b:=a
			else
				if a = b then
					begin
					count:=count+1;
					if count > temp then
						temp:=count
					end
					else
						count:=0;
						b:=a;
			end;
	writeln(temp);
	t:= t-1;
	end
end.
