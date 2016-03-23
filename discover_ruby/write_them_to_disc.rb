#!/usr/bin/ruby
require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 87dcb7285da83a1bfb4c59c23ec02c8df1940aa1'
}

clnt = HTTPClient.new
open('/tmp/16', 'w') { |f|
f.puts clnt.get_content ("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc")
}
puts "The file was saved!"
