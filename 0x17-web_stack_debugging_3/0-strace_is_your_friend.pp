# 0-strace_is_your_friend.pp

# Define a file resource to manage the Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure  => present,
  content => template('apache/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Define a service resource to ensure Apache is running and restart if necessary
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

