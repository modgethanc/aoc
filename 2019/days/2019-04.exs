## ADVENT OF CODE 2019 DAY 3
#
# part 1:
#
# part 2:

## part 1

defmodule PartOne do
  def calc(start, stop, count) when start <= stop do
    if validate(start) do
      calc(start+1, stop, count+1)
    else
      calc(start+1, stop, count)
    end
  end

  def calc(start, stop, count) when start > stop do
    count
  end

  def validate(target) do
    ans = check(String.codepoints(Integer.to_string(target)), {false,false})
    elem(ans, 0) and not elem(ans, 1)
  end

  def check([head|tail], {double,decreasing}) when tail != [] do
    a = String.to_integer(head)
    b = String.to_integer(hd(tail))
    if a > b do
      decreasing = true
    else
      if a == b do
        double = true
      end
    end

    check(tail, {double,decreasing})
  end

  def check([head|tail], {double,decreasing}) when tail == [] do
    {double,decreasing}
  end

end


IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(PartOne.validate(111111)==true)
IO.write("1.2: ")
IO.puts(PartOne.validate(223450)==false)
IO.write("1.3: ")
IO.puts(PartOne.validate(123789)==false)

# puzzle input


list_input = String.split(String.trim(File.read!("2019-04-input.txt")), "-")
start = String.to_integer(hd(list_input))
stop = String.to_integer(hd(tl(list_input)))
IO.puts(start)
IO.puts(stop)
PartOne.calc(start, stop, 0)
|> IO.puts()

## part 2

defmodule PartTwo do
  def calc(start, stop, count) when start <= stop do
    if validate(start) do
      calc(start+1, stop, count+1)
    else
      #IO.puts(start)
      calc(start+1, stop, count)
    end
  end

  def calc(start, stop, count) when start > stop do
    count
  end

  def validate(target) do
    ans = check(String.codepoints(Integer.to_string(target)), {false,false,false}, "99")
    elem(ans, 0) and not elem(ans, 1)
  end

  def check([head|tail], {double,decreasing,safe}, last) when tail != [] do
    a = String.to_integer(head)
    b = String.to_integer(hd(tail))

    if a > b do
      decreasing = true
    end

    if a == b do
      double = true
    end

    if a == String.to_integer(last) and double and a != b do
      safe = true
    end

    if a == String.to_integer(last) and not safe do
      double = false
    end

    check(tail, {double,decreasing,safe}, head)
  end

  def check([head|tail], {double,decreasing,safe}, last) when tail == [] do
    {double,decreasing}
  end

end

IO.puts("PART TWO")

# test input

IO.write("2.1: ")
IO.puts(PartTwo.validate(112233)==true)
IO.write("2.2: ")
IO.puts(PartTwo.validate(123444)==false)
IO.write("2.3: ")
IO.puts(PartTwo.validate(111122)==true)

IO.puts(PartTwo.validate(110222)==false)
IO.puts(PartTwo.validate(111233)==true)
IO.puts(PartTwo.validate(112333)==true)
IO.puts(PartTwo.validate(022333)==true)
# puzzle input

PartTwo.calc(start, stop, 0)
|> IO.puts()
