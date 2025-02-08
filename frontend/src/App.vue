<script>

import {defineComponent} from "vue";
import Navbar from "@/components/Navbar.vue";
import TaskList from "@/components/TaskList.vue";

export default defineComponent({
    components: {TaskList, Navbar},
})
</script>

<template>
    <Navbar/>

    <TaskList></TaskList>

</template>

<style scoped>

</style>
