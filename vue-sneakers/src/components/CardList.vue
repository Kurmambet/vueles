<script setup>
import Card from './Card.vue'

const onClickAdd = () => {
    alert(111)
}
</script>

<template>
  <div class="grid grid-cols-4 gap-5">
    <Card
      image-url="/sneakers/sneakers-1.jpg"
      title="Мужские кроссовки Nike Blazer Mid Suede"
      :price="1205"
      :is-added="false"
      :is-favorite="true"
      :onClickAdd="onClickAdd"
    />

  </div>
</template>
