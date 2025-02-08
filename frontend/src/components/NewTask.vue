<script>
export default {
    name: "NewTask",
    data() {
        return {
            title: '',
            error: ''
        }
    },
    methods: {
        add() {
            if (!this.title) {
                this.error = 'Введите название'
            }
            else {
                this.$emit('newTask', this.title);
                this.title = ''
            }
        }
    }
}
</script>

<template>
    <div class="input-group mb-3 mt-3">
        <input type="text" class="form-control" placeholder="Задача..." aria-label="Задача..."
               aria-describedby="button-addon2" v-model="title">
        <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="add">Добавить</button>
    </div>
    <small class="form-text text-muted" style="color: red;">{{ error }}</small>
</template>

<style scoped>

</style>