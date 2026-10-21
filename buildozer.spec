ini
[app]
title = VK Downloader
package.name = vkdownloader
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivymd,yt-dlp,openssl,requests,urllib3,certifi,chardet,idna

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# Запрос прав на чтение и запись в память устройства
android.permissions = WRITE_EXTERNAL_STORAGE