#!/bin/bash

set -x
package=meta_api

[ ! -d .git ] && git init
if [ ! -f deploy/scripts/maketag.sh ]; then
    git clone git@github.com:spilgames/erl-project.git
    mv erl-project/make/scripts/tag/maketag.sh deploy/scripts
    rm -rf erl-project
fi

# move actual project tree
for f in `find tmp/ -type f`; do
  sed -i "s/{{package}}/${package}/g" $f;
done
sed -i "s/{{email}}/$(git config --get user.email)/" tmp/setup.py

mkdir -p docs/coverage
mkdir -p deploy/{nginx,specfiles,supervisord}
mv tmp/module $package
mv tmp/vhost.ngx deploy/nginx/${package/_/-}-conf.ngx
mv tmp/* .

cat <<IGNORE > docs/coverage/.gitignore > tmp/.gitignore
*
!.gitignore
IGNORE

cat <<EOF > deploy/supervisord/${package}.ini
[program:${package/_/-}-server]
autorestart=true
startsecs=10
stopsignal=INT
user=${package}
environment=USER="${package}",HOME="/var/lib/${package}"
directory=/opt/virtualenv/${package}/
command=/opt/virtualenv/${package}/bin/start_gunicorn
EOF



add_pypi_packages(){
  virtualenv venv
  source ./venv/bin/activate
  pip install -r dev-requirements.txt
}
[ ! -d venv ] && add_pypi_packages
echo "Done"

cat <<MSG
run the following to test the application:
  . ./venv/bin/activate
  python run.py
  # in a new shell run
  curl -H "Content-Type: application/json" localhost:8000

  # OR
  ./start_gunicorn
  curl -H "Content-Type: application/json" localhost:8000
MSG
