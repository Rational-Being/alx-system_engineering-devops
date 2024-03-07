#this puppet code debugs a server error in a wordpress website
exec { 'remove phpp':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-setti\
ngs.php",
  path    => '/bin'
}

