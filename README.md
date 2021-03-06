# rpi-gpio-api
restful web api for controlling rpi gpio

# run commands

## start web server

```
export FLASK_APP=rpi-gpio-api.py
flask run --host=0.0.0.0
```

## make ssl key

```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl.key -out ssl.crt
```

## run unit tests

```
python3 -m unittest discover -v
```

## crontab

```
sudo bash
chmod 750 /shop/randomsilo/rpi-gpio-api/run-rpi-gpio-api.sh
crontab -e
@reboot bash /shop/randomsilo/rpi-gpio-api/run-rpi-gpio-api.sh &

#/etc/rc.local, add the following line before exit 0
/etc/init.d/cron/start

tail /var/log/syslog
```

# references

[Ashok Raja](http://www.ashokraja.me/post/Raspberry-Pi-System-Information-Web-Application-with-Python-and-Flask.aspx)