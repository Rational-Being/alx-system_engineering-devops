#a manifest that elp configure a server wit rsa key

file_line { 'using ssh key for login'
    path => '/etc/ssh/ssh_config'
    line => 'PasswordAuthentication no'
}

file_line { 'path to keys for identity'
    path => '/etc/ssh/ssh_config'
    line => 'IdentityFile ~/.ssh/school'
}