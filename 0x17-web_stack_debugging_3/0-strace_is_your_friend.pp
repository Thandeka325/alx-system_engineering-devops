# Fixes the 500 error
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart-apache':
  command => 'systemctl restart apache2',
  path    => '/sbin/:/bin/:/usr/sbin/:/usr/bin/',
  require => Exec['fix-wordpress'],
}
