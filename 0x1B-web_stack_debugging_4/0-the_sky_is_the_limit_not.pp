#this pupet script will fix nginx request limit error
exec { 'increase limit':
  path    => '/bin/:/usr/bin/',
  command => '/bin/sed -i "s/15/4096/g" /etc/default/nginx;service nginx restart'
}

exec { 'restart nginx':
  path    => '/etc/init.d/',
  command => 'nginx restart'
}

