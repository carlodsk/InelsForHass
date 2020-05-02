{%- if version_installed == "master" %}
## You are running master!

This is **only** intended for development!

{%- elif (version_installed.split(".")[1] | int) < 17 and version_installed != "0.16.3" %}
## DO NOT UPGRADE TO THE LATEST VERSION!

First upgrade to version [0.16.3](https://github.com/hacs/integration/releases/tag/0.16.3), then upgrade to the latest version.
{% endif %}

## InelsForHass is a Home Assistant HACS itegration for Elko inels smart home

_Integrates all common devices from Inels BUS system into the Home Assistant._

### What?

InelsForHass gives you a chance to control your proprietary Inels devieces through the Home Assistant.

### Supported devices

- Common and dimmer lights
- Switches
- Shades
- Garage doors
- Heating
- Weather stations
- Lara radio
- Ventilation system

### Issues

~~If~~ When you experience issues/bugs with this the best way to report them is to open an issue in **this** repo.

[Issue link](https://github.com/JH-Soft-Technology/InelsForHass/issues/)

[![buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jhoralek)
