#!/bin/bash

set -x
package=dawkins

[ ! -d .git ] && git init
if [ ! -f deploy/scripts/maketag.sh ]; then
    git clone git@github.com:spilgames/erl-project.git
    mv erl-project/make/scripts/tag/maketag.sh deploy/scripts
    rm -rf erl-project
fi

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

for f in `find tmp/ -type f`; do
  sed -i "s/{{package}}/${package}/g" $f;
done
sed -i "s/{{email}}/$(git config --get user.email)/" tmp/setup.py

mv tmp/module $package
mv tmp/* .
mkdir -p docs/coverage
mkdir -p deploy/{nginx,specfiles,supervisord}

cat <<IGNORE > docs/coverage/.gitignore > tmp/.gitignore
*
!.gitignore
IGNORE



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
  curl localhost:8000/
MSG
