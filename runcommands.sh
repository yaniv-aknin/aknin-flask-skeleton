# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
root="$( cd "$( dirname "$0" )" && pwd )"

export DATABASE_URL="postgres://localhost/$USER"
export DEBUG=1
export SECRET_KEY="secret"

[ -f runcommands.local.sh ] && source runcommands.local.sh || true

unset root
