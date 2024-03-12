#this pupet script will fix nginx request limit error
exec { 'increase limit':
  path    => '/bin/',
  command => 'sed -i "s/15/4096/g" /etc/default/nginx',
}

exec { 'restart nginx':
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
