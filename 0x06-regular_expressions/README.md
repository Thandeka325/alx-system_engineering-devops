# Project: 0x06. Regular expression

For this project,had to build regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this project was to play with regular expressions (regex), we were given the Ruby code that we should use, just had to replace the regexp part, meaning the code in between the `//`:

```
example.rb

#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join

```
