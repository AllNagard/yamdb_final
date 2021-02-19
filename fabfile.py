# -*- coding: UTF-8 -*-

from fabric.api import run, env

env.shell = "sh -c"


def runmigrations():
    run("python manage.py migrate")
