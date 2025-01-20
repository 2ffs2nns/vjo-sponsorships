# Sponsors

## Install

Run the following cmds

* sudo apt-get update -y && apt-get upgrade -y
* sudo apt-get install midori unclutter -y

## Autostart config

edit `/etc/xdg/lxsession/LXDE-pi/autostart`

```bash
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash

# prevent hdmi timeout w/no activity
@xset s off
@xset -dpms
@xset s noblank
@unclutter -idle 0

@lxterminal -e python3 /home/vjo/banners/app.py
@/usr/bin/python /home/vjo/banners/run_midori.py
```

## VJO user

Create a `vjo` user, add a `/home/vjo/banners` dir
Put the `app.py`, `run_midori.py` and flask dirs `static`
and `templates` in the `banners` dir.

Update the password in `app.py`

## WiFi

Install RaspAP by following the [guide](https://raspap.com/#quick).

```bash
curl -sL https://install.raspap.com | bash
```

# Sponsor Images

Connect to the `vjo-sponsors` wifi. Then, open a browser and navigate to `http://10.3.141.1:8000/upload` Choose the images you want to upload or delete.