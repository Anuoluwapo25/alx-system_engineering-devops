# configure SSH client with puppet

file_line { 'Host':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'Host 54.242.177.175',
}

file_line { 'PasswordAuthentication OFF':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
}

file_line { 'Private Key identity File':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
}
