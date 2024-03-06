#this puppet code debugs a server error in a wordpress website
exec { 'remove phpp':
  path    => '/bin'
  command => "sed -i 's/class-wp-local.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
