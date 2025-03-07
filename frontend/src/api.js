let url = 'http://localhost:8000/api/tasks';

function getTasksApi() {
    let artists = fetch(url).then(a => a.json())
    return artists
}

function parseJson(a) {
    return a.json()
}

async function addTaskApi(task) {
    let result;
    let b = await fetch(url, {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(task)
    })
    console.log(b)
    return await b.json();
}

function deleteTaskApi(task) {
    fetch(`${url}/${task.id}`, {method: 'DELETE'});

}

function editTaskApi(task) {
    let task_id = task.id
    task = {
        "title": task.title,
        "is_done": task.is_done 
    }
    fetch(`${url}/${task_id}`, {
        method: 'PUT',
        headers: {"Content-Type": "application/json"}, 
        body: JSON.stringify(task)}).then(res => res.json());
}


export {getTasksApi, addTaskApi, deleteTaskApi, editTaskApi};