
#!/bin/sh

#exit script on error
set -e

#gather static files data
python manage.py collectstatic --no-input

uwsgi --socket :8000 --master --enable-threads --module project0001api.wsgi