from flask_security import roles_accepted

def render_widgets():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()