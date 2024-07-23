pythonic_share is a sharing system on your router which can be run on Unix-like operating systems and Windows.

**On Unix-likes**:
In order to use it go to pythic_share directory and run the following commands:
```bash
pip3 install flask
python3 ./app.py
```

now you'll be given some IPs (Note: all your devices should be connected to one router
and if you don't have one then you can connect all your devices to your phone's hotspot and use hotspot as a router).

Chose the on that is not 127.0.0.1 (because this IP is only accessible to your computer locally) and open it in any device connected to the same network.

for setting the folder to be shared you should pass it ```-d``` or ```--directory```argument for example:

```bash
python3 app.py -d ~/Music
```

if you dont pass the argument ```-d``` it will set to ```~/Downloads```

**if you want to use it somewhere other than the main directory of the project as a tool run:**
```bath
sudo ln -s [source_folder]/app.py /usr/local/bin/pythonic_share
```


**On Windows**
Download the ```.exe```  file with [this link](https://github.com/Pouryakillsound/pythonic_share/releases/download/v0.0.1/pythonic_share.exe) and place it somewhere.

**if you want to use it somewhere other than the main directory of the project as a tool run:**
add that folder to the windows ```path environment variables```