<script setup>
import Card from './Card.vue'

defineProps({
  items: Array
});


const onClickFavorite = () => {
    alert(2)
}
const onClickAdd = () => {
    alert(111)
}
</script>

<template>
  <div class="grid grid-cols-4 gap-5">
    <Card
      v-for="item in items"
      :key="item.id"
      :title="item.title"
      :image-url="item.imageUrl"
      :price="item.price"
      :onClickAdd="onClickAdd"
      :isFavorite="item.isFavorite"
    />

  </div>
</template>
