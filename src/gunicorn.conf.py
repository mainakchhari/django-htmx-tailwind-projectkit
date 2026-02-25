##
# Used only in docker environments
#
import gunicorn_color

bind = "0.0.0.0:8000"
wsgi_app = "{{ project_name }}.wsgi:application"
workers = 2
threads = 4
control_socket = "/tmp/gunicorn.ctl"
accesslog='-'
error_log='-'
loglevel='info'
logger_class=gunicorn_color.Logger
