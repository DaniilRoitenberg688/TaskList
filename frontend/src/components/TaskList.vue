<script>
import Task from "@/components/Task.vue";
import NewTask from "@/components/NewTask.vue";
import TaskEditor from "@/components/TaskEditor.vue";
import {th} from "vuetify/locale";
import {getTasksApi, addTaskApi, editTaskApi, deleteTaskApi} from "@/api.js";
import task from "@/components/Task.vue";

export default {
  name: "TaskList",
  components: {NewTask, Task, TaskEditor},
  data() {
    return {
      tasks: [
        {
          id: 0,
          title: "Купить слона",
          is_done: false
        },
        {
          id: 1,
          title: "Купить слона",
          is_done: false
        }
      ],
      isEditorVisible: false,
      editingTask: null
    }
  },
  methods: {
    async addTask(title) {
      let taskToAdd = {
        title: title,
        is_done: false
      }
      let newTask = await addTaskApi(taskToAdd)
      this.tasks.push(newTask)
    },
    deleteTask(taskToDelete) {
      console.log(taskToDelete);
      deleteTaskApi(taskToDelete)
      this.tasks = this.tasks.filter(task => task.id !== taskToDelete.id);
    },
    saveTask(taskToChange) {
      console.log(taskToChange);
      let task = this.tasks.find((task) => task.id === taskToChange.id)
      let index = this.tasks.indexOf(task[0])
      this.tasks[index] = taskToChange
      editTaskApi(taskToChange)
      this.closeEditor()
    },
    openEditor(task) {
      this.isEditorVisible = true;
      this.editingTask = task;
    },

    setDone(taskToChange) {
      let task = this.tasks.find((task) => task.id === taskToChange.id)
      let index = this.tasks.indexOf(task[0])
      this.tasks[index] = taskToChange
      editTaskApi(taskToChange)
    },

    closeEditor() {
      this.isEditorVisible = false;
    }
  },
  async mounted() {
    this.tasks = await getTasksApi()
  }
}
</script>

<template>
  <div class="container mt-4">
    <ul class="list-group d-flex justify-content-center mb-3">
      <Task v-for="task in tasks" :task="task" @delete="deleteTask" @edit="openEditor" @setDone="setDone">{{ task.title }}</Task>
    </ul>

    <NewTask @newTask="addTask"></NewTask>
  </div>
  <div
      class="modal fade show"
      v-if="isEditorVisible"
      style="display: block; background-color: rgba(0, 0, 0, 0.5);">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Изменени задачи</h5>
          <button type="button" class="btn-close" aria-label="Закрыть" @click="closeEditor"></button>
        </div>
        <div class="modal-body">
          <TaskEditor
              :task="editingTask"
              @save="saveTask"
          />
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>

</style>