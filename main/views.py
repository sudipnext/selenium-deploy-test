# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
import os

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from django.contrib import messages
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def scrap(request):
    options = Options()
    options.headless = True
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/lib/chromium-or-chrome-stable-path"
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)
    url = "https://www.tiktok.com/@khaby.lame/"

    driver.get(url)
    page_source = driver.page_source
    with open("tiktok.txt", "w") as f:
        f.write(page_source)
    driver.close()
    messages.success(request, "Timetable extraction successful.")
    return render(request, 'result.html', {'page_source': page_source})
