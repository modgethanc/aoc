## 2018 ADVENT OF CODE DAY 2
# part one: count the number that have an ID containing exactly two of any
#   letter and then separately count those with exactly three of any letter,
#   multiply counts together
# part two:

## part one

# test against examples

test_input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
test_ans = 12

# using puzzle input

list_input = String.split(String.trim(File.read!("2018-day02-input.txt")))
IO.puts(list_input)

## part two
