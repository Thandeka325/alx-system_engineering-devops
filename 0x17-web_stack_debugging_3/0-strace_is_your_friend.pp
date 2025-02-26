# This Puppet manifest fixes Apache 500 error by ensuring PHP is installed and permissions are correct

class apache_fix {
  package { 'php5':
    ensure => installed,
  }

  package { 'libapache2-mod-php5':
    ensure => installed,
    require => Package['php5'],
  }

  file { '/var/www/html/index.php':
    ensure  => file,
    content => '<?php phpinfo(); ?>',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    require => Package['php5'],
  }

  exec { 'fix-permissions':
    command => 'chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html',
    path    => ['/bin', '/usr/bin'],
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['php5'],
  }
}

include apache_fix
