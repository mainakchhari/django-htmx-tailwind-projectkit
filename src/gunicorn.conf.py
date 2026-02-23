import gunicorn_color

bind = "127.0.0.1:8000"
workers = 1
threads = 4
control_socket = "/tmp/gunicorn.ctl"
accesslog='-'
logger_class=gunicorn_color.Logger
