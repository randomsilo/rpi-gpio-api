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
sudo openssl req -new -newkey rsa:2048 -nodes -keyout ssl.key -out ssl.crt
```