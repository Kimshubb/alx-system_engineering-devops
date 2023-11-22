#!/usr/bin/env ruby

# Method to extract sender, receiver, and flags from a log entry
def extract_info(log_entry)
  sender = log_entry.match(/\[from:(.+?)\]/)[1]
  receiver = log_entry.match(/\[to:(.+?)\]/)[1]
  flags = log_entry.match(/\[flags:(.+?)\]/)[1]
  "#{sender},#{receiver},#{flags}"
end

# Check if an argument is provided
if ARGV.empty?
  puts 'Usage: ./100-textme.rb <log_file>'
else
  log_file_path = ARGV[0]

  # Read the log file line by line
  File.foreach(log_file_path) do |line|
    # Check if the line contains "Receive SMS" to filter relevant entries
    if line.include?('Receive SMS')
      result = extract_info(line)
      puts result
    end
  end
end

