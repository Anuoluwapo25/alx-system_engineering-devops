# Puppet manifest to optimize Nginx configuration

# Define a class to manage Nginx configuration
class nginx {
    # Ensure Nginx package is installed
    package { 'nginx':
        ensure => installed,
    }

    # Define Nginx configuration file
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        content => template('nginx/nginx.conf.erb'),
        notify  => Service['nginx'],
    }

    # Ensure Nginx service is running and enabled
    service { 'nginx':
        ensure => running,
        enable => true,
    }
}


