# Fix  error 500 internal server Strace is your friend
exec { 'FixApache':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}