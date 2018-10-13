---
title: 'termux - Termux:API'
date: 2018-10-13 08:19:38
tags: [termux]
---

要讓 termux 可以獲取手機資訊或是跟手機進行互動，可以安裝 Termux:API application。  

<!-- more -->

{% asset_img 1.jpg %}

</br>


然後在 termux 安裝 termux-api。  

    pkg install termux-api

</br>


Termux:API 提供如下功能:  

```
termux-battery-status
Get the status of the device battery.
termux-brightness
Set the screen brightness between 0 and 255.
termux-call-log
List call log history.
termux-camera-info
Get information about device camera(s).
termux-camera-photo
Take a photo and save it to a file in JPEG format.
termux-clipboard-get
Get the system clipboard text.
termux-clipboard-set
Set the system clipboard text.
termux-contact-list
List all contacts.
termux-dialog
Show a text entry dialog.
termux-download
Download a resource using the system download manager.
termux-fingerprint
Use fingerprint sensor on device to check for authentication.
termux-infrared-frequencies
Query the infrared transmitter's supported carrier frequencies.
termux-infrared-transmit
Transmit an infrared pattern.
termux-location
Get the device location.
termux-media-player
Play media files.
termux-media-scan
MediaScanner interface, make file changes visible to Android Gallery
termux-microphone-record
Recording using microphone on your device.
termux-notification
Display a system notification.
termux-notification-remove
Remove a notification previously shown with termux-notification --id.
termux-sensor
Get information about types of sensors as well as live data.
termux-share
Share a file specified as argument or the text received on stdin.
termux-sms-inbox
List received SMS messages.
termux-sms-send
Send a SMS message to the specified recipient number(s).
termux-storage-get
Request a file from the system and output it to the specified file.
termux-telephony-call
Call a telephony number.
termux-telephony-cellinfo
Get information about all observed cell information from all radios on the device including the primary and neighboring cells.
termux-telephony-deviceinfo
Get information about the telephony device.
termux-toast
Show a transient popup notification.
termux-torch
Toggle LED Torch on device.
termux-tts-engines
Get information about the available text-to-speech engines.
termux-tts-speak
Speak text with a system text-to-speech engine.
termux-vibrate
Vibrate the device.
termux-volume
Change volume of audio stream.
termux-wallpaper
Change wallpaper on your device.
termux-wifi-connectioninfo
Get information about the current wifi connection.
termux-wifi-enable
Toggle Wi-Fi On/Off. termux-wifi-enable false or termux-wifi-enable true.
termux-wifi-scaninfo
Get information about the last wifi scan.
```

</br>


像是 termux-battery-status 可以取得電池資訊。  

{% asset_img 2.jpg %}

</br>


termux-camera-info 可以取得相機資訊。  

{% asset_img 3.jpg %}

</br>


termux-clipboard-set 可設定資料到剪貼簿。  

{% asset_img 4.jpg %}

</br>


termux-clipboard-get 可取得剪貼簿內的資料。  

{% asset_img 5.jpg %}

</br>


Link
----
* [Termux:API](https://wiki.termux.com/wiki/Termux:API)
