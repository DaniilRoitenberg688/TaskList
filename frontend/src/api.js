let url = 'http://localhost:5000/api/tasks';

function getTasksApi() {
    let artists = fetch(url)
    return artists.json()
}

function addTaskApi(task) {
    console.log('adaadf')
    let newTask = fetch(url, {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(task)
    }).then(res => res.json());
    return task.value;
}

function deleteTaskApi(task) {
    fetch(`${url}/${task.id}`, {method: 'DELETE'}).then(res => res.json());

}

function editTaskApi(task) {
    fetch(`${url}`, {method: 'PATCH', body: JSON.stringify(task)}).then(res => res.json());
}


export {getTasksApi, addTaskApi, deleteTaskApi, editTaskApi};