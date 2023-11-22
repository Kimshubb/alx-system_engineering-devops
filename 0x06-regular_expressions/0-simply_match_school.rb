#!/usr/bin/env ruby

# Check if the argument matches the regular expression
def match_school(argument)
  regex = /School/
  if argument.match?(regex)
    puts argument.gsub(regex, 'School')
  else
    puts ''
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts 'Usage: ./0-simply_match_school.rb <string>'
else
  # Call the matching method with the provided argument
  match_school(ARGV[0])
end
