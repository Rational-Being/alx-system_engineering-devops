#manifest to install a program called flask

package {'python3-pip':
    ensure => installed,
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'
}

package { 'werkzeug':
    ensure   => '2.0.1',
    provider => 'pip',
    require  => package['pyton3-pip'],
}
