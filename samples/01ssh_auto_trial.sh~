#!/bin/zsh

PW="aniyamato"

expect -c "
set timeout 5
spawn env LANG=C /usr/bin/ssh katsurou@plata.ar.media.kyoto-u.ac.jp
expect \"password:\"
send \"${PW}\n\"
expect \"$\"
exit 0
"

