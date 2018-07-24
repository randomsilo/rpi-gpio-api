# rpi-gpio-api
restful web api for controlling rpi gpio


# run commands

## start web server

```
export FLASK_APP=rpi-api-gpio.py
flask run --host=0.0.0.0
```

# make ssl key

```
# x509
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl.key -out ssl.crt

# Positive SSL
sudo openssl req -new -newkey rsa:2048 -nodes -keyout ssl.key -out ssl.csr
```