import json
from flask_security import current_user, roles_accepted
from flask import render_template

import core.config.config
from core.helpers import combine_dicts
from core.helpers import list_apps

def display_possible_subscriptions():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return json.dumps(core.config.config.possible_events)
    return __func()

def list_all_apps():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return json.dumps({"apps": list_apps()})
    return __func()

def list_all_apps_and_actions():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        core.config.config.load_function_info()
        return json.dumps(core.config.config.function_info['apps'])
    return __func()

def display_filters():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return json.dumps({"status": "success", "filters": core.config.config.function_info['filters']})
    return __func()

def display_flags():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        core.config.config.load_function_info()
        return json.dumps({"status": "success", "flags": core.config.config.function_info['flags']})
    return __func()

def render_interface(interface_name, widget_args):
    from server.context import running_context
    from server import interface
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func(interface_name, widget_args):
        if current_user.is_authenticated and interface_name:
            args = getattr(interface, interface_name)(widget_args)
            combine_dicts(args, {"authKey": current_user.get_auth_token()})
            return render_template("pages/" + interface_name + "/index.html", **args)
        else:
            running_context.app.logger.debug('Unsuccessful login attempt')
            return {"status": "Could Not Log In."}
    return __func(interface_name, widget_args)

def display_key():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        if current_user.is_authenticated:
            return {"auth_token": current_user.get_auth_token()}
        else:
            running_context.app.logger.debug('Unsuccessful login attempt')
            return {"status": "Could Not Log In."}
    return __func()

def list_all_widgets():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()


