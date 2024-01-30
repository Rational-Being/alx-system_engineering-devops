#usind puppet to automate creating a cuat HTTP header response

exec {'apt-update':
  command => '/usr/bin/apt-get -y update'
}

package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'setting nginx header':
  path  => '/etc/nginx/nginx.conf',
  line  => "\tadd_header X-Served-By \${hostname};",
  after => 'http {',
}

exec { 'run nginx':
  command => '/usr/sbin/service nginx restart'
}
