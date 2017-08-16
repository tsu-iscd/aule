#begin
-- Parsed with SLL(*)-mode
select 1
#end
#begin
-- Parsed with LL(*)-mode
if @a=5 select 1 if @b=5 select 3 else select 2
#end
