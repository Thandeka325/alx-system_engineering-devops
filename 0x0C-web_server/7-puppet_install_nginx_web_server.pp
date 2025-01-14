# Puppet manifest toi install and configure Nginx to serve "Hello World!" and redirect /redirect_me to /.

class nginx_server {
  # Install the nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  # Configure the default site for nginx
  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
    require => Package['nginx'],
  }

  # Configure nginx to redirect /redirect_me to /
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.conf.erb'),
    notify  => Service['nginx'],
  }

  # Ensure that the nginx configuration is reloaded to apply changes
  exec { 'reload_nginx':
    command => '/etc/init.d/nginx reload',
    refreshonly => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

# Apply the nginx_server class
include nginx_server
