from flask_security import roles_accepted

def get_users():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def read_user(username):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def update_user(username, body):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def add_user(username, body):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def delete_user(username):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()