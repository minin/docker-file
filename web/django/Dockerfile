#it will run pip install requiremnts.txt
FROM python:2.7-onbuild
COPY start.sh /start.sh
RUN chmod +x /start.sh
EXPOSE 8000
#RUN /usr/local/bin/python manage.py migrate
#celery -A moonShot worker --loglevel=info
CMD ["/start.sh"]