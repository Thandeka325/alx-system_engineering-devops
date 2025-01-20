# Configures Nginx with a custom HTTP response header

# Ensure Nginx package is updated
exec {'update':
  provide => shell,
  command => 'sudo apt-get -y update',
  before  => Exec['install Nginx'],
}

# Ensure Nginx package is installed
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header']
}

# Custom add HTTP response header
exec { 'add_header':
  provide     => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf'
  before      => Exec['restart Nginx'],
}

# Ensure Nginx service restarts after installation
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
