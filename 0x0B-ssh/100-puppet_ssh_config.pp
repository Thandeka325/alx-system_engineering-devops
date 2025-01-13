#!/usr/bin/env bash
# Script creates Client configuration file with Puppet

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH Client configuration
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentication no
}
