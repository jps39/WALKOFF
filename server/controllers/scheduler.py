from flask_security import roles_accepted

def start_scheduler():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def stop_scheduler():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def pause_scheduler():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def resume_scheduler():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def pause_scheduler_job():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def resume_scheduler_job():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()

def get_scheduler_jobs():
    from server.context import running_context
    @roles_accepted(*running_context.user_roles['/cases'])
    def __func():
        return
    return __func()