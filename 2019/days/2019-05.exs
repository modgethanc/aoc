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

    case code do
      99 -> input
      1 -> op1(input, step)
      2 -> op2(input, step)
      nil -> input
    end
  end

  def op1(input, pointer) do
    op1 = Enum.at(input, pointer+1)
    op2 = Enum.at(input, pointer+2)
    store = Enum.at(input, pointer+3)
    value = Enum.at(input, op1) + Enum.at(input, op2)

    calc_unit(List.insert_at(List.delete_at(input, store), store, value), pointer+4)
  end

  def op2(input, pointer) do
    op1 = Enum.at(input, pointer+1)
    op2 = Enum.at(input, pointer+2)
    store = Enum.at(input, pointer+3)
    value = Enum.at(input, op1) * Enum.at(input, op2)

    calc_unit(List.insert_at(List.delete_at(input, store), store, value), pointer+4)
  end

  def transform(input, noun, verb) do
    List.insert_at(List.delete_at(List.insert_at(List.delete_at(input, 1), 1, noun), 2), 2, verb)
  end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(PartOne.calc([1,0,0,0,99]) == [2,0,0,0,99])

# puzzle input


#list_input = String.split(String.trim(File.read!("2019-xx-input.txt")))

## part 2



IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
