## ADVENT OF CODE 2019 DAY 1
#
# part 1:
#
# part 2:

## part 1

defmodule PartOne do
  def calc(input) do
    calc_unit(input, 0)
  end

  def calc_unit(input, step) do
    code = Enum.at(input, step*4)
    op1 = Enum.at(input, step*4+1)
    op2 = Enum.at(input, step*4+2)
    store = Enum.at(input, step*4+3)

    if code == 99 do
      input
    else
      if code == 1 do
        value = Enum.at(input, op1) + Enum.at(input, op2)
      else
        if code == 2 do
          value = Enum.at(input, op1) * Enum.at(input, op2)
        end
      end

      calc_unit(List.insert_at(List.delete_at(input, store), store, value), step + 1)
    end
  end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(PartOne.calc([1,0,0,0,99]) == [2,0,0,0,99])
IO.write("1.2: ")
IO.puts(PartOne.calc([2,3,0,3,99]) == [2,3,0,6,99])
IO.write("1.3: ")
IO.puts(PartOne.calc([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
IO.write("1.4: ")
IO.puts(PartOne.calc([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

# puzzle input, read from file and translated to a list of ints

list_input = Enum.map(String.split(String.trim(File.read!("2019-02-input.txt")), ","), &String.to_integer/1)

# apply some transforms

list_input = List.insert_at(List.delete_at(list_input, 1), 1, 12)
list_input = List.insert_at(List.delete_at(list_input, 2), 2, 2)

# calc

IO.puts(hd(PartOne.calc(list_input)))

## part 2



IO.puts("\nPART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
