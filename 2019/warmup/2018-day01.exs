defmodule Math do
    def sum_list([head | tail], accumulator) do
          sum_list(tail, head + accumulator)
    end

    def sum_list([], accumulator) do
          accumulator
    end

    def better_sum_list(list, acc) do
          Enum.reduce(list, acc, &+/2)
    end
end


## part one

# test against examples

test1 = Math.sum_list([+1, +1, +1],0)
test1b = Math.better_sum_list([+1, +1, +1],0)
test2 = Math.sum_list([+1, +1, -2],0)
test2b = Math.better_sum_list([+1, +1, -2],0)
test3 = Math.sum_list([-1, -2, -3],0)
test3b = Math.better_sum_list([-1, -2, -3],0)

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

File.read!("2018-day01-input.txt")
|> String.trim()
|> String.split()
|> Enum.map(&String.to_integer/1)
|> Math.better_sum_list(0)
|> IO.puts()
