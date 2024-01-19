# learning to execute a command with puppet
exec { 'killmenow': 
    command => 'pkill killmenow',
    path => '/usr/bin/'
}