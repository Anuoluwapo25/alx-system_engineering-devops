# Define a class for Nginx configuration
class nginx {

  # Install the nginx package
  package { 'nginx': ensure => installed }

  # Allow HTTP traffic on port 80 in the firewall
  ufw {
    rule {
      name => 'allow http'
      allow => 'http'
    }
  }

  # Create the directory structure for the web root
  file { '/var/www/html':
    ensure => directory,
    owner   => 'root',
    group   => 'root',
    mode    => '0755',
  }

  # Create an index file with "Hello World!" content
  file { '/var/www/html/index.html':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "Hello World!",
  }

  # Define the server configuration
  nginx::resource::server { 'default':
    ensure        => present,
    server_name   => '_',
    listen_ports  => [80],
    root          => '/var/www/html',
    index         => ['index.html index.htm index.nginx-debian.html'],

    location {
      path_info  => '/redirect_me';
      return     => 301 https://example.com$request_uri;
    }

    location {
      try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
  }

  # Include a blank 404 page (optional)
  file { '/var/www/html/404.html':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => '',
  }
}

# Include the class
class { 'nginx': }

# Enable and start the firewall
service { 'ufw':
  ensure => running,
  enabled => true,
}

# Reload the Nginx configuration (avoiding systemctl)
exec { 'reload_nginx':
  command => '/etc/init.d/nginx reload',
  unless  => '/usr/sbin/nginx -s reload',
}

