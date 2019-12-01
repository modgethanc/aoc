## ADVENT OF CODE 2019 DAY 1
#
# part 1: take each input, divide by three, round down, subtract two; sum all
# inputs.
#
# part 2: same formula, but run again on result until it reaches negative or
# zero; sum all inputs.

## part 1

defmodule PartOne do
  def calc(input) do
    div(input, 3) - 2
  end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(PartOne.calc(12) == 2)
IO.write("1.2: ")
IO.puts(PartOne.calc(14) == 2)
IO.write("1.3: ")
IO.puts(PartOne.calc(1969) == 654)
IO.write("1.4: ")
IO.puts(PartOne.calc(100756) == 33583)

# puzzle input, read from file and translated to a list of ints

list_input = Enum.map(String.split(String.trim(File.read!("2019-01-input.txt"))), &String.to_integer/1)
list_ans = Enum.map(list_input, &PartOne.calc/1)
IO.write("solution: ")
Enum.reduce(list_ans, 0, &+/2)
|> IO.puts()

## part 2

defmodule PartTwo do
  def calchelp(input) do
    # doing this because i don't know how to reduce to something that needs a
    # second argument so i gotta get that empty accumulator in somehow!!
    calc(input, 0)
  end

  def calc(input, acc) do
    p1 = PartOne.calc(input)
    if p1 > 0 do
      calc(p1, p1+acc)
    else
      acc
    end
  end
end

IO.puts("\nPART TWO")

# test input

IO.write("2.1: ")
IO.puts(PartTwo.calc(14, 0) == 2)
IO.write("2.2: ")
IO.puts(PartTwo.calc(1969, 0) == 966)
IO.write("2.3: ")
IO.puts(PartTwo.calc(100756, 0) == 50346)

# puzzle input

list_ans = Enum.map(list_input, &PartTwo.calchelp/1)

IO.write("solution: ")
Enum.reduce(list_ans, 0, &+/2)
|> IO.puts()
