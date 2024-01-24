# manifest to configure my server

package { 'nginx:
	ensure => installed,
}

exec { 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/abdullateef-yusuff.tec\/;\\n\\t}" /etc/nginx/sites-available/default':
	provider => shell,
}

#file_line { '301 redirection':
#	ensure => 
#	path => '/etc/nginx/sites-available/default',
#	after => 'listen 80 default server;',
#	line => 'rewrite ^/redirect_me https://abdullateef.tech permanent;',
#}

file { '/var/www/html/index.html':
	content => 'Hello World!',
}

service { 'nginx':
	ensure => running,
	require => Packae['nginx'],
}
