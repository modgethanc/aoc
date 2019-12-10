## ADVENT OF CODE 2019 DAY 6
#
# part 1:
#
# part 2:


## part 1

defmodule PartOne do

  def process_input(inputfile) do
    File.read!(inputfile)
    |> String.trim()
    |> String.split()
  end

  def calc(orbits) do
    build_map(orbits, %{})
    |> count_orbits()
  end

  def build_map(orbits, chart) do
    Enum.reduce(orbits, chart, fn x, c ->
      {center,orbiter} = List.to_tuple(String.split(x, ")"))
      Map.put(c, orbiter, center)
    end)
  end

  def count_orbits(chart) do
    Enum.reduce(Map.keys(chart), 0, fn core, count ->
      #IO.puts(count)
      check_indirects(chart, core, count)
    end)
  end

  def check_indirects(chart, orbiter, count) when orbiter != "COM" do
    #IO.puts(orbiter)
    check_indirects(chart, Map.get(chart, orbiter), count + 1)
  end

  def check_indirects(chart, orbiter, count) do
    count
  end
end

IO.puts("PART ONE")

# test input

IO.write("1.1: ")
PartOne.process_input("2019-06-sample.txt")
|> PartOne.calc()
|> IO.puts()

# puzzle input

PartOne.process_input("2019-06-input.txt")
|> PartOne.calc()
|> IO.puts()

## part 2



IO.puts("PART TWO")

# test input

IO.write("1.1: ")
IO.puts(1=1)

# puzzle input
