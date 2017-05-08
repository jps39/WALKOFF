import os
import sys
import importlib
import json

from flask_security import roles_accepted
from flask import Blueprint, render_template, request, g, current_app
from server import forms
import core.config.config
import core.config.paths



def read_app(app_name, app_args):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func(app_name, app_args):
        path = '{0}/interface/templates/{1}'.format(app_name, app_args["page"])  # Do not use os.path.join
        args = load_app(app_name, app_args["args"].keys(), app_args["args"].values())

        template = render_template(path, **args)
        return template
    return __func(app_name, app_args)

def list_app_actions(app_name):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def list_app_devices(app_name):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def import_devices(app_name):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def export_devices(app_name):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()


def load_module(app_name):
    module_name = 'apps.{0}.display'.format(app_name)
    try:
        return sys.modules[module_name]
    except KeyError:
        pass
    try:
        return importlib.import_module(module_name, '')
    except ImportError:
        return None


def load_app(name, keys, values):
    module = load_module(name)
    args = dict(zip(keys, values))
    return getattr(module, 'load')(args) if module else {}


def data_stream(app_name, stream_name):
    module = load_module(app_name)
    if module:
        return getattr(module, 'stream_generator')(stream_name)