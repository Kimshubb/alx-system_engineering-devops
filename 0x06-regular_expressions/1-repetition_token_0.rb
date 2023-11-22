#!/usr/bin/env ruby

# Check if the argument matches the regular expression
def match_expression(argument)
  regex = ^hb(t{1,4})n$
  if argument.match?(regex)
    puts argument.scan(regex).join
  else
    puts ''
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts 'Usage: ./match_expression.rb <string>'
else
  # Call the matching method with the provided argument
  match_expression(ARGV[0])
end

