#!/usr/bin/env ruby
# Regular expression that matches CAPS only
puts ARGV[0].scan(/[A-Z]*/).join
