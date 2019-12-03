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
        process_wire(tail, List.last(line), record_line(line, coords))
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
            "U" -> draw_line({elem(start, 0)+1,elem(start, 1)}, direction, distance-1, points++[start])
            "D" -> draw_line({elem(start, 0)-1,elem(start, 1)}, direction, distance-1, points++[start])
            "L" -> draw_line({elem(start, 0),elem(start, 1)-1}, direction, distance-1, points++[start])
            "R" -> draw_line({elem(start, 0),elem(start, 1)+1}, direction, distance-1, points++[start])
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
wire3 = String.split("R75,D30,R83,U83,L12,D49,R71,U7,L72", ",")
wire4 = String.split("U62,R66,U55,R34,D71,R55,D58,R83", ",")
wire5 = String.split("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", ",")
wire6 = String.split("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", ",")

IO.write("1.1: ")
IO.puts(PartOne.calc(wire1, wire2) == 6)
IO.write("1.2: ")
IO.puts(PartOne.calc(wire3, wire4) == 159)
IO.write("1.3: ")
IO.puts(PartOne.calc(wire5, wire6) == 135)

# puzzle input

list_input = String.split(String.trim(File.read!("2019-03-input.txt")))
input1 = String.split(hd(list_input), ",")
input2 = String.split(hd(tl(list_input)), ",")
PartOne.calc(input1, input2)
|> IO.puts()

## part 2

defmodule PartTwo do
    def calc(wire1, wire2) do
        wire1_path = wire_list(wire1, {0,0}, [{0,0}])
        wire1_coords = PartOne.process_wire(wire1, {0,0}, %{})
        wire2_path = Map.keys(PartOne.process_wire(wire2, {0,0}, %{}))
        crossings = PartOne.find_crossings(wire1_coords, wire2_path, [])
        wire1_trace = find_traces(wire1_path, crossings, [])
        wire2_trace = find_traces(wire2_path, crossings, [])
        sum(wire1_trace, wire2_trace, [])
        |> Enum.sort()
        |> Enum.map(&IO.puts/1)
        #|> Enum.at(1)
        #|> IO.puts()
        IO.puts(wire1_path)
    end

    def wire_list([head | tail ], loc, coords) do
        input = String.codepoints(head)
        distance = String.to_integer(Enum.join(tl(input)))
        line = tl(PartOne.draw_line(loc, hd(input), distance, []))
        wire_list(tail, List.last(line), coords++line)
    end

    def wire_list([], loc, coords) do
        coords
    end

    def find_traces(path, [crossing|remainder], traces) do
        find_traces(path, remainder, traces++[trace(path, crossing, 0)])
    end

    def find_traces(path, [], traces) do
        traces
    end

    def trace([head|tail], crossing, length) when head != crossing do
        trace(tail, crossing, length+1)
    end

    def trace(path, crossing, length) do
        length
    end

    def sum([a|b], [x|y], acc) do
        sum(b, y, [a+x]++acc)
    end

    def sum([], [], acc) do
        acc
    end
end

IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(PartTwo.calc(wire1, wire2) == 30)

# puzzle input
