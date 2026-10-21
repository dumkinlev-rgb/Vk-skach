import os
import threading
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from yt_dlp import YoutubeDL

class VkDownloaderApp(MDApp):
    def build(self):
        # Настройка темы оформления
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        
        # Главный контейнер
        layout = MDBoxLayout(orientation='vertical', spacing="20dp")
        
        # Шапка приложения
        toolbar = MDTopAppBar(title="VK Video Downloader")
        layout.add_widget(toolbar)
        
        # Контентная часть с отступами
        content = MDBoxLayout(orientation='vertical', spacing="20dp", padding="20dp")
        
        # Поле ввода ссылки
        self.url_input = MDTextField(
            hint_text="Вставьте ссылку на видео ВК",
            helper_text="Например: https://vk.com",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        content.add_widget(self.url_input)
        
        # Кнопка скачивания
        download_btn = MDRaisedButton(
            text="СКАЧАТЬ ВИДЕО",
            pos_hint={"center_x": 0.5},
            on_release=self.start_download_thread
        )
        content.add_widget(download_btn)
        
        # Статус-бар (текст состояния)
        self.status_label = MDLabel(
            text="Ожидание ссылки...",
            halign="center",
            theme_text_color="Secondary"
        )
        content.add_widget(self.status_label)
        
        layout.add_widget(content)
        return layout

    def start_download_thread(self, instance):
        # Запускаем загрузку в отдельном потоке, чтобы интерфейс не зависал
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = "Ошибка: Ссылка не может быть пустой!"
            return
            
        self.status_label.text = "Анализ видео... Пожалуйста, подождите."
        threading.Thread(target=self.download_video, args=(url,), daemon=True).start()

    def download_video(self, url):
        # Путь к папке "Загрузки" на Android
        # В Pydroid 3 обычно есть доступ к стандартной папке Download
        download_path = '/storage/emulated/0/Download/%(title)s.%(ext)s'
        
        # Если доступа к общей папке нет, сохраняем в локальную папку приложения
        if not os.path.exists('/storage/emulated/0/Download'):
            download_path = '%(title)s.%(ext)s'

        ydl_opts = {
            'outtmpl': download_path,
            'format': 'best', # скачивать в лучшем доступном качестве
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "Успешно! Видео сохранено в папку Загрузки."
        except Exception as e:
            self.status_label.text = f"Ошибка: {str(e)}"

if __name__ == '__main__':
    VkDownloaderApp().run()