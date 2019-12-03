## ADVENT OF CODE 2019 DAY 3
#
# part 1:
#
# part 2:

## part 1

defmodule PartOne do
    def calc(wire1, wire2) do
        wire1_coords = process_wire(wire1, {0,0}, %{})
        wire2_coords = Map.keys(process_wire(wire2, {0,0}, %{}))
        #find_crossings(wire1_coords, wire2_coords, [])
        Enum.map(find_crossings(wire1_coords, wire2_coords, []), &manhattan/1)
        |> Enum.sort()
        |> Enum.at(1)
    end

    def find_crossings(coords, [ check | remainder ], crossings) do
        if coords[check] do
            find_crossings(coords, remainder, [check]++crossings)
        else
            find_crossings(coords, remainder, crossings)
        end
    end

    def find_crossings(coords, [ ], crossings) do
        crossings
    end

    def process_wire([head | tail ], loc, coords) do
        input = String.codepoints(head)
        distance = String.to_integer(Enum.join(tl(input)))
        line = draw_line(loc, hd(input), distance, [])
        process_wire(tail, hd(line), record_line(line, coords))
    end

    def process_wire([], loc, coords) do
        coords
    end

    def draw_line(start, direction, distance, points) do
      #return list of tuples for every point on this line
      if distance == -1 do
        points
      else
        case direction do
            "U" -> draw_line({elem(start, 0)+1,elem(start, 1)}, direction, distance-1, [start|points])
            "D" -> draw_line({elem(start, 0)-1,elem(start, 1)}, direction, distance-1, [start|points])
            "L" -> draw_line({elem(start, 0),elem(start, 1)-1}, direction, distance-1, [start|points])
            "R" -> draw_line({elem(start, 0),elem(start, 1)+1}, direction, distance-1, [start|points])
        end
      end
    end

    def record_line([head|tail], coords) do
      # return a map with all the coord points drawn in
        record_line(tail, Map.put(coords, head, true))
    end

    def record_line([], coords) do
        coords
    end

    def manhattan({x,y}) do
        abs(x) + abs(y)
    end
end

IO.puts("PART ONE")

# test input

wire1 = String.split("R8,U5,L5,D3", ",")
wire2 = String.split("U7,R6,D4,L4", ",")

IO.write("1.1: ")
IO.puts(PartOne.calc(wire1, wire2) == 6)

# puzzle input

#list_input = String.split(String.trim(File.read!("2019-03-input.txt")))
#wire1 = String.split(hd(list_input), ",")
#wire2 = String.split(hd(tl(list_input)), ",")
#PartOne.calc(wire1, wire2)
#|> IO.puts()

## part 2



IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
