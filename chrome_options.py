from selenium import webdriver


class ChromeOptions:

    def __init__(self):
        self.__chrome_options = webdriver.ChromeOptions()
        self.__chrome_options.add_argument("--disable-notifications")
        self.__chrome_options.add_argument("--start-maximized")
        self.__chrome_options.add_argument("--no-sandbox")
        self.__chrome_options.add_argument("--verbose")
        self.__chrome_options.add_experimental_option(
            "prefs",
            {
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False,
                'profile.default_content_setting_values': {'images': 2,
                                                           'geolocation': 2,
                                                           'notifications': 2, 'auto_select_certificate': 2,
                                                           'fullscreen': 2,
                                                           'mouselock': 2, 'media_stream': 2,
                                                           'media_stream_mic': 2, 'media_stream_camera': 2,
                                                           'protocol_handlers': 2,
                                                           'ppapi_broker': 2, 'automatic_downloads': 2,
                                                           'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                           'metro_switch_to_desktop': 2,
                                                           'app_banner': 2,
                                                           'site_engagement': 2,
                                                           'durable_storage': 2}
            },
        )

        """
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-dev-shm-usage")"""

    @property
    def chrome_options(self):
        return self.__chrome_options


""" DUTRA SETTINGS
self.__chrome_options.add_experimental_option(
            "prefs",
            {
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False,
                'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                                                           'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                           'notifications': 2, 'auto_select_certificate': 2,
                                                           'fullscreen': 2,
                                                           'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                           'media_stream_mic': 2, 'media_stream_camera': 2,
                                                           'protocol_handlers': 2,
                                                           'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                           'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                           'metro_switch_to_desktop': 2,
                                                           'protected_media_identifier': 2, 'app_banner': 2,
                                                           'site_engagement': 2,
                                                           'durable_storage': 2}
            },
        )

       # PLUS not using
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-dev-shm-usage")"""
