<script setup>
  import myhello from './components/myhello.vue';
</script>


<template>
  
  <myhello title="puma"  :price="9500 + 555" :isAdded="true"/>
  <myhello title="puma2" :price="9500"        is-added/>
  <myhello title="puma3" :price="9500"        isAdded/>
  <myhello title="puma3" :price="9500"       :isAdded="false"/>
  <myhello title="adidas" price="19500 + 456" isAdded="trddwdwue"/>
  <myhello title="nike"  :price="19500"        />
  <myhello />
</template>


