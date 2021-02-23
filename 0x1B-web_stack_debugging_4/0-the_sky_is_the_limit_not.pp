# Change requests limit
exec { 'fix--for-nginx' :
  command => '/bin/sed -i "s/15/1000/" /etc/default/nginx'
}

exec { 'restart-nginx' :
  require => Exec['fix--for-nginx'],
  command => '/usr/sbin/service nginx restart'
}
