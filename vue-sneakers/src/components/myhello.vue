<script> 
    export default {
        data(){
            return {
                count: 0
            }     
        },
    methods: {
        increment(){
            this.count++
        }
    }
   }
</script>




<template>
    <h1 class="text">{{ count }}</h1>
    <button @click="increment">+</button>
    <button @click="count--">-</button>
</template>


<style scoped>
    .text {
        background: rgb(255, 159, 159);
    }
</style>
