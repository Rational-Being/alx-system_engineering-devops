#!/usr/bin/env ruby
#this script use regex to match the word school

puts ARGV[0].scan(/\[from:(.*)\].*\[to:(.*)\].*\[flags:(.*?)\]/).join
