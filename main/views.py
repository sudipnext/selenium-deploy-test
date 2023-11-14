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


def scrap(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    url = "https://www.tiktok.com/@khaby.lame/"
    driver.get(url)
    page_source = driver.page_source
    with open("tiktok.txt", "w") as f:
        f.write(page_source)
    driver.close()
    messages.success(request, "Timetable extraction successful.")
    return HttpResponseRedirect('/main/')
