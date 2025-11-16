<script setup>
  import myhello from './components/myhello.vue';
</script>


<template>
  <myhello title="puma"  :price="9500 + 555" :isAdded="true">
    <button>Добавить</button>
    <h4>eed</h4>
    <myhello/>
    <myhello/>
  </myhello>

  <myhello/>
</template>


