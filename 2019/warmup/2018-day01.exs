## 2018 ADVENT OF CODE DAY ONE
# part one: given an input of positive and negative integers, return sum of all
#   of them
# part two: given same input, return the first duplicated result when summing
#   one at a time (repeating input values until a duplicate is found)

## part one

defmodule PartOne do

  # recursive version
  
    def sum_list([head | tail], accumulator) do
          sum_list(tail, head + accumulator)
    end

    def sum_list([], accumulator) do
          accumulator
    end

  # fancy version

    def better_sum_list(list, acc) do
          Enum.reduce(list, acc, &+/2)
    end
end

# test against examples
# (oh god there is a less ugly way to set up these tests)

test1 = PartOne.sum_list([+1, +1, +1],0)
test1b = PartOne.better_sum_list([+1, +1, +1],0)
test2 = PartOne.sum_list([+1, +1, -2],0)
test2b = PartOne.better_sum_list([+1, +1, -2],0)
test3 = PartOne.sum_list([-1, -2, -3],0)
test3b = PartOne.better_sum_list([-1, -2, -3],0)

IO.puts("test 1:")
IO.puts(test1 == 3)
IO.puts("test 1b:")
IO.puts(test1b == 3)
IO.puts("test 2:")
IO.puts(test2 == 0)
IO.puts("test 2b:")
IO.puts(test2b == 0)
IO.puts("test 3:")
IO.puts(test3 == -6)
IO.puts("test 3b:")
IO.puts(test3b == -6)

# using puzzle input

IO.puts("PART ONE SOLUTION:")

list_input = Enum.map(String.split(String.trim(File.read!("2018-day01-input.txt"))), &String.to_integer/1)

# todo: figure out how to pipe and store the result instead, this is ugly af

PartOne.better_sum_list(list_input, 0)
|> IO.puts()

## part two

defmodule PartTwo do
  def sum_list([head | tail], original, acc, master) do
    if master[acc] do
      acc
    else
      master = Map.put(master, acc, true)
      sum_list(tail, original, head+acc, master)
    end
  end

  def sum_list([], original, acc, master) do
    sum_list(original, original, acc, master)
  end
end

# tests

IO.puts("2.1: ")
IO.puts(PartTwo.sum_list([+1, -1], [+1, -1], 0, %{}) == 0)
IO.puts("2.2: ")
IO.puts(PartTwo.sum_list([+3, +3, +4, -2, -4], [+3, +3, +4, -2, -4], 0, %{}) == 10)
IO.puts("2.3: ")
IO.puts(PartTwo.sum_list([-6, +3, +8, +5, -6], [-6, +3, +8, +5, -6], 0, %{}) == 5)
IO.puts("2.4: ")
IO.puts(PartTwo.sum_list([+7, +7, -2, -7, -4], [+7, +7, -2, -7, -4], 0, %{}) == 14)

# using puzzle input

IO.puts("PART TWO SOLUTION:")

PartTwo.sum_list(list_input, list_input, 0, %{})
|> IO.puts()
