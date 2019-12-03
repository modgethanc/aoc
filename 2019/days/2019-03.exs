## ADVENT OF CODE 2019 DAY 3
#
# part 1:
#
# part 2:

## part 1

defmodule PartOne do
    def process_wire([head | tail ], loc, coords) do
        input = String.codepoints(head)
        distance = String.to_integer(Enum.join(tl(input)))
        if hd(input) == "U" do
            newloc = { elem(loc, 0) + distance, elem(loc, 1) }
            IO.puts(newloc)
        end
        process_wire(tail, newloc, Map.put(coords, newloc, true))
    end

    def process_wire([], loc, coords) do
        coords
    end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input


list_input = String.split(String.trim(File.read!("2019-03-input.txt")))
wire1 = String.split(hd(list_input), ",")
wire2 = String.split(hd(tl(list_input)), ",")

PartOne.process_wire(wire1, {0,0}, %{})
|> IO.puts()
## part 2



IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
