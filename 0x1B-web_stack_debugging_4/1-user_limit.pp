#this puppet script allows holberton user to login without hinges

exec { 'increaser soft and hard file limit':
  command => 'sed -i "s/nofile 4/nofile 6000/g; s/nofile 5/nofile 6000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
