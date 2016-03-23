#!/usr/bin/ruby
require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 87dcb7285da83a1bfb4c59c23ec02c8df1940aa1'
}

clnt = HTTPClient.new
new_arr = []
new_arr << (clnt.get_content ("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"))
puts new_arr.join(" ")
