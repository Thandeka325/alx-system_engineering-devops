# Fixes the 500 error
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php && echo "" >> /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}
