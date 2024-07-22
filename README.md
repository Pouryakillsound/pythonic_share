pythonic_share is a sharing system on your router which can be run on a Unix-like OS so far. 

In order to use it go to pythic_share directory and run the following commands:
```bash
pip3 install flask
python3 ./app.py
```

now you'll be given some IPs (Note: all your devices should be connected to one router
or you can connect all your devices to your phone's hotspot and use hotspot as a router).

Chose the on that is not 127.0.0.1 because this IP is only accessible to you computer locally.

for setting the folder to be shared you should pass it the environment variable path by for example using:

```bash
path=. python3 app.py
```
well < . > means where you currently are at.
