[core]
nick = ${IRC_NICK} 
host = ${IRC_HOST}
use_ssl = false
port = ${IRC_PORT}
owner = ${IRC_OWNER}
admins = ${IRC_ADMINS}
channels = ${IRC_CHANS}
auth_method = nickserv
auth_password = ${IRC_PASSWD}
reply_errors = false
extra = ${SOPEL_EXTRA}
enable = ${ENABLE_MODULES}

[admin]
hold_ground = true
auto_accept_invite = false


