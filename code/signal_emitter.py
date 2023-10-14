TASK_SIGNALS = blinker.Namespace()

TASK_STATUS_CHANGED = TASK_SIGNALS.signal("task-status-changed")


@CELERY.task(name=f"{_name}.save-result", bind=True, ignore_result=True)
def save_task_result(self, task_log: str, db_id: int):
    # ...
    task_data: ProcessingTask = ProcessingTask.get_by_id(id_=db_id)
    # ...
    task_data.task_status = "SUCCESS"
    # ...
    TASK_STATUS_CHANGED.send(self, db_id=db_id)


@CELERY.task(name=f"{_name}.save-error", bind=True, ignore_result=True)
def save_task_error(self, failing_task_id: str, db_id: int):
    # ...
    task_data: ProcessingTask = ProcessingTask.get_by_id(id_=db_id)
    # ...
    task_data.task_status = "FAILURE"
    # ...
    TASK_STATUS_CHANGED.send(self, db_id=db_id)
    # ...
