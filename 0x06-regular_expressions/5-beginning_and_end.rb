#!/usr/bin/env ruby
#this script use regex to match the word school

#puts ARGV[0].scan(/h.n/).join
#The above line works so is the line below
puts ARGV[0].scan(/^h.n$/).join
