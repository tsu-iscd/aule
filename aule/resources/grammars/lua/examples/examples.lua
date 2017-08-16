#begin
print("Hello World")
#end

#begin
-- defines a factorial function
    function fact (n)
      if n == 0 then
        return 1
      else
        return n * fact(n-1)
      end
    end

    print("enter a number:")
    a = io.read("*number")        -- read a number
    print(fact(a))
#end

#begin
local P = {}
    complex = P

    local function checkComplex (c)
      if not ((type(c) == "table") and
         tonumber(c.r) and tonumber(c.i)) then
        error("bad complex number", 3)
      end
    end

    function P.add (c1, c2)
      checkComplex(c1);
      checkComplex(c2);
      return P.new(c1.r + c2.r, c1.i + c2.i)
    end
#end