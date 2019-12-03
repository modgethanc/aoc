## ADVENT OF CODE 2019 DAY 3
#
# part 1:
#
# part 2:

## part 1

defmodule PartOne do
    def crossings(wire1, wire1) do
        # find conjunction of two lines

    end

    def process_wire([head | tail ], loc, coords) do
        input = String.codepoints(head)
        distance = String.to_integer(Enum.join(tl(input)))
        newloc =
        case hd(input) do
            "U" -> {elem(loc, 0)+distance,elem(loc, 1)}
            "D" -> {elem(loc, 0)-distance,elem(loc, 1)}
            "L" -> {elem(loc, 0),elem(loc, 1)-distance}
            "R" -> {elem(loc, 0),elem(loc, 1)+distance}
        end
        line = draw_line(loc, hd(input), distance, [])
        #IO.puts(length(line))
        process_wire(tail, newloc, record_line(line, coords))
    end

    def process_wire([], loc, coords) do
        coords
    end

    def draw_line(start, direction, distance, points) do
      #return list of tuples for every point on this line
      if distance == 0 do
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
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input


#list_input = String.split(String.trim(File.read!("2019-03-input.txt")))
#wire1 = String.split(hd(list_input), ",")
#wire2 = String.split(hd(tl(list_input)), ",")

wire1 = String.split("R8,U5,L5,D3", ",")
wire2 = String.split("U7,R6,D4,L4", ",")

IO.puts(length(Map.keys(PartOne.process_wire(wire1, {0,0}, %{}))))
PartOne.process_wire(wire2, {0,0}, %{})
PartOne.process_wire(wire2, {0,0}, %{})

## part 2



IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
