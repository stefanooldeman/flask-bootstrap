#!/bin/bash

set -x
package=dawkins

mkdir -p docs/coverage
mkdir -p deploy/{nginx,specfiles,supervisord}
mkdir -p $package/tests/{unit,functional}

touch README.md
for dir in `find $package -type d`; do
  touch $dir/__init__.py;
done

echo '__version__ = "0.1.0"' > $package/__init__.py

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

echo * > tmp/.gitignore
echo !.gitignore >> tmp/.gitignore



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
