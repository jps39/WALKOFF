from flask_security import roles_accepted

def edit_event_note(event_id, config_value):
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()