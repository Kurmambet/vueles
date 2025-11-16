<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
  console.log(count)
}

function updateCount(event) {
  count.value = Number(event.target.value)
}
</script>



<template>
  <h1 class="text">{{ count }}</h1>
  <button @click="increment">+</button>

    <div class="dinp">
        <p>through @input & func increment</p>
        <!-- <input v-on:input=""/> -->
        <input @input="updateCount" />
    </div>

    <div class="dmod"> 
        <p>through v-model</p>
        <input v-model="count">
    </div>

    <div class="dkeyup"> 
        <p>through keyup ctrl+enter</p>
        <input @keyup.ctrl.enter="increment">
    </div>
</template>



<style scoped>
    .text {
    background: rgba(136, 184, 91, 0.572);
    }

    .dinp, .dmod, .dkeyup {
        margin-right: 5em;
        margin-left: 5em;
    }
</style>
