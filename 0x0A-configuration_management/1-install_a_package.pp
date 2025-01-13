#!/usr/bin/pup
# Install a specific package of Flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
