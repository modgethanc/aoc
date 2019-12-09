## ADVENT OF CODE 2019 DAY 1
#
# part 1:
#
# part 2:

## part 1


defmodule PartOne do
  def calc(program) do
    calc_unit(program, 0)
  end

  def make_digits(mode) do
    Integer.to_string(mode)
    |> String.codepoints()
    |> Enum.map(&String.to_integer/1)
    |> Enum.reverse()
  end

  def calc_unit(program, pointer) do
    
    mode = Enum.at(program, pointer)
    IO.puts(mode)
    digits = make_digits(mode)
    #Enum.map(digits, &IO.write/1)

    #IO.puts("")

    opcode = String.to_integer(Enum.join([Enum.at(digits, 1), Enum.at(digits, 0)]))

    case opcode do
      99 -> halt()
      1 -> op1(digits, program, pointer)
      2 -> op2(digits, program, pointer)
      3 -> op3(digits, program, pointer)
      4 -> op4(digits, program, pointer)
      5 -> op5(digits, program, pointer)
      6 -> op6(digits, program, pointer)
      7 -> op7(digits, program, pointer)
      8 -> op8(digits, program, pointer)
    end
  end

  def halt() do
    "HALT" 
  end

  def op1(digits, program, pointer) do
    # (a+b)
    m1 = Enum.at(digits, 2, 0)
    m2 = Enum.at(digits, 3, 0)
    m3 = Enum.at(digits, 4, 0)

    p1 = Enum.at(program, pointer+1)
    p2 = Enum.at(program, pointer+2)
    p3 = Enum.at(program, pointer+3)

    op1 =
      if m1 == 0 do
        Enum.at(program, p1)
      else
        p1
      end

    op2 =
      if m2 == 0 do
        Enum.at(program, p2)
      else
        p2
      end

    #IO.puts(op1)
    #IO.puts(op2)

    value = op1 + op2

    calc_unit(List.insert_at(List.delete_at(program, p3), p3, value), pointer+4)
  end

  def op2(digits, program, pointer) do
    # (a*b)
    m1 = Enum.at(digits, 2, 0)
    m2 = Enum.at(digits, 3, 0)
    m3 = Enum.at(digits, 4, 0)

    p1 = Enum.at(program, pointer+1)
    p2 = Enum.at(program, pointer+2)
    p3 = Enum.at(program, pointer+3)

    op1 =
      if m1 == 0 do
        Enum.at(program, p1)
      else
        p1
      end

    op2 =
      if m2 == 0 do
        Enum.at(program, p2)
      else
        p2
      end

    #IO.puts(op1)
    #IO.puts(op2)

    value = op1 * op2

    calc_unit(List.insert_at(List.delete_at(program, p3), p3, value), pointer+4)
  end

  def op3(digits, program, pointer) do
    # (input)
    input = String.to_integer(String.trim(IO.gets("input: ")))
    store = Enum.at(program, pointer+1)
    calc_unit(List.insert_at(List.delete_at(program, store), store, input), pointer+2)
  end

  def op4(digits, program, pointer) do
    # (output)
    loc = Enum.at(program, pointer+1)
    Enum.at(program, loc)
    |> IO.puts()
    calc_unit(program, pointer+2)
  end

  def op5(digits, program, pointer) do
    m1 = Enum.at(digits, 2, 0)
    m2 = Enum.at(digits, 3, 0)

    p1 = Enum.at(program, pointer+1)
    p2 = Enum.at(program, pointer+2)

    op1 =
      if m1 == 0 do
        Enum.at(program, p1)
      else
        p1
      end

    op2 =
      if m2 == 0 do
        Enum.at(program, p2)
      else
        p2
      end

    IO.puts(op1)
    IO.puts(op2)

    if op1 != 0 do
      IO.puts("jump")
      calc_unit(program, op2)
    else
      IO.puts("walk")
      calc_unit(program, pointer+3)
    end
  end

  def op6(digits, program, pointer) do
    m1 = Enum.at(digits, 2, 0)
    m2 = Enum.at(digits, 3, 0)

    p1 = Enum.at(program, pointer+1)
    p2 = Enum.at(program, pointer+2)

    op1 =
      if m1 == 0 do
        Enum.at(program, p1)
      else
        p1
      end

    op2 =
      if m2 == 0 do
        Enum.at(program, p2)
      else
        p2
      end

    IO.puts(op1)
    IO.puts(op2)

    if op1 == 0 do
      IO.puts("jump")
      calc_unit(program, op2)
    else
      IO.puts("walk")
      calc_unit(program, pointer+3)
    end
  end

  def op7(digits, program, pointer) do
  end

  def op8(digits, program, pointer) do
  end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
#IO.puts(PartOne.calc([1,0,0,0,99]) == [2,0,0,0,99])
#IO.puts(PartOne.calc([4,0,99]))
#IO.puts(PartOne.calc([1203,0,1004,0,99]))
#IO.puts(PartOne.calc([1002,4,3,4,33]))
IO.puts(PartOne.calc([1101,100,-1,4,0]))
# puzzle input


list_input = Enum.map(String.split(String.trim(File.read!("2019-05-input.txt")), ","), &String.to_integer/1)
#IO.puts(PartOne.calc(list_input))

## part 2



IO.puts("PART TWO")

# test input

IO.write("2.1: ")
#IO.puts(PartOne.calc([1101,100,-1,4,0]))
#IO.puts(PartOne.calc([1105,1,5,0,0,99]))
#IO.puts(PartOne.calc([1105,0,5,99,0,0]))

#IO.puts(PartOne.calc([1106,1,5,99,0,0]))
#IO.puts(PartOne.calc([1106,0,5,0,0,99]))
# puzzle input
