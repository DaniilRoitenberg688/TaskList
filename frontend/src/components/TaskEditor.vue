<script>
export default {
  name: "TaskEditor",
  props: {
    task: {
      type: Object,
    }
  },
  data(){
    return {
      localTask: this.task
    }
  },
  methods:{
    saveTask() {
      this.$emit("save", this.localTask)
    }
  }
}
</script>

<template>
  <form @submit.prevent="saveArtist">
    <!-- Имя артиста -->
    <div class="mb-3">
      <label for="artist-name" class="form-label">Задача</label>
      <input
          id="artist-name"
          v-model="localTask.title"
          type="text"
          class="form-control"
          placeholder="Введите имя"
          required
      />
    </div>

    <!-- Описание артиста -->
    <!-- Кнопки -->
    <div class="d-flex justify-content-between">
      <button type="submit" class="btn btn-success" @click="saveTask">Сохранить</button>
    </div>
  </form>
</template>

<style scoped>

</style>