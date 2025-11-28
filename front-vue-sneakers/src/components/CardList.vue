<script setup>
import Card from './Card.vue';

defineProps({
  items: Array,
});

const emit = defineEmits(['addToFavorite']);

const onClickAdd = () => {
}
</script>

<template>
  <div class="grid grid-cols-4 gap-5">
    <Card
      v-for="item in items"
      :key="item.id"
      :id="item.id"
      :title="item.title"
      :image-url="item.imageUrl"
      :price="item.price"
      :onClickAdd="onClickAdd"
      :onClickFavorite="() => emit('addToFavorite', item)"
      :isFavorite="item.isFavorite"
    />

  </div>
</template>
