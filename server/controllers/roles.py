from flask_security import roles_accepted

def display_roles():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def get_role():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def edit_role():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def create_role():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()
