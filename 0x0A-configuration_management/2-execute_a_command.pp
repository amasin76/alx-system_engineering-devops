# stop a process named killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => $::path,
}
