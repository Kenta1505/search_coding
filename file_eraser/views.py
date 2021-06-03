from django.shortcuts import render
import os
import glob
from . import file_eraser
from . import file_eraser2

# Create your views here.
def main():
    file_eraser.main()
