#this puppet code debugs a server error in a wordpress website

exec { 'remove phpp':
  path => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin',
  command => "sed -i 's/ .phpp/ .php/g' /var/www/html/wp-settings.php",
}
