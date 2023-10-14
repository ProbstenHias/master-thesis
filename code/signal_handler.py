TASK_STATUS_CHANGED.connect(task_status_changed_handler)


def task_status_changed_handler(sender, db_id: int):
    task_data: ProcessingTask = ProcessingTask.get_by_id(id_=db_id)
    callback_urls = task_data.data.get("status_changed_callback_urls", [])
    task_url = task_data.data.get("task_view", None)
    for callback_url in callback_urls:
        requests.post(callback_url, json={"url": task_url, "status": task_data.status})
