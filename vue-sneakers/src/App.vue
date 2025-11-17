<script setup>
import { onMounted } from 'vue'
import axios from 'axios'

import Header from './components/header.vue'
import CardList from './components/CardList.vue'
import Drawer from './components/Drawer.vue'


// onMounted(() => {
  // fetch('https://fd7b389119d99f32.mokky.dev/items')
  // .then(res => res.json())
  // .then(data => {
  //   console.log(data)
  // })
  // 
  // axios.get('https://fd7b389119d99f32.mokky.dev/items').then((resp) => console.log(resp.data));
// })

onMounted(async () => {
  try {
    // const data = await axios.get('https://fd7b389119d99f32.mokky.dev/items'); // без деструктуризации data - весь http ответ
    const {data} = await axios.get('https://fd7b389119d99f32.mokky.dev/items'); // с деструктуризацией 
    console.log(data);
  } catch (err) {
    console.log(err);
  }
})


</script>

<template>
  <!-- <Drawer /> -->
  <div class="bg-white w-4/5 m-auto rounded-xl shadow-xl mt-14">
    <Header />

    <div class="p-10">
      <div class="flex justify-between items-center">
        <h2 class="text-3xl font-bold mb-8">Все кроссовки</h2>

        <div class="flex gap-4">
          <select
            class="py-2 px-3 border rounded-md outline-none focus:border-gray-400"
            name=""
            id=""
          >
            <option value="">По названию</option>
            <option value="">По цене (дешевые)</option>
            <option value="">По цене (дорогие)</option>
          </select>

          <div class="relative">
            <img class="absolute left-4 top-3" src="/search.svg" alt="" />
            <input
              class="border rounded-md py-2 pl-11 pr-4 outline-none focus:border-gray-400"
              placeholder="Поиск..."
            />
          </div>
        </div>
      </div>
      <div class="mt-10">
        <CardList :items="items" />
      </div>  
    </div>
  </div>
</template>
