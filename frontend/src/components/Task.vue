<script>
export default {
  name: "Task",
  props: ['task'],
  methods: {
    deleteTask() {
      this.$emit('delete', this.task)
    },
    editTask() {
      this.$emit('edit', this.task)
    }
  }
}
</script>

<template>
  <li class="list-group-item d-flex" :class="{'list-group-item-success': task.is_done}">
    <div class="d-inline-block">
      <input class="me-2" type="checkbox" v-model="task.is_done"/>
      {{ task.title }}
    </div>
    <div class="d-inline-block position-absolute end-0 top-50 translate-middle-y me-3">
      <button class="btn btn-danger btn-sm me-3" @click="deleteTask">
        <i class="bi bi-trash"></i>
      </button>
      <button class="btn btn-sm btn-warning" @click="editTask">
        <i class="bi bi-pencil"></i>
      </button>
    </div>
  </li>
</template>

<style scoped>

</style>