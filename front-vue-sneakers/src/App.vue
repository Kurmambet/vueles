<!-- C:\projects\vueles\front-vue-sneakers\src\App.vue -->
<script setup>
import { onMounted, ref, watch, reactive} from 'vue'
import axios from 'axios'

import Header from './components/header.vue'
import CardList from './components/CardList.vue'
import Drawer from './components/Drawer.vue'



const items = ref([]);  // { value: [] } - хранит все товары - state

const filters = reactive({
  sortBy: 'title',
  searchQuery: '',
});                     // реактивный state



const onChangeSelect = event => {
  filters.sortBy = event.target.value
}

const onChangeSearchInput = event => {
  filters.searchQuery = event.target.value
}



const fetchItems = async () => {
  try {
    const params = {
      sortBy: filters.sortBy,
      // searchQuery: filters.searchQuery
    }

    if (filters.searchQuery) {
      params.title = `*${filters.searchQuery}*`;
    }

    // const {data} = await axios.get('http://127.0.0.1:8000/api/products'); // с деструктуризацией 
    // items.value = data.products;
    // const {data} = await axios.get('https://fd7b389119d99f32.mokky.dev/items?sortBy=' + filters.sortBy)


    // const {data} = await axios.get("https://fd7b389119d99f32.mokky.dev/items", { params })
    const {data} = await axios.get("http://127.0.0.1:8000/api/products", { params })
    items.value = data.products
  } catch (err) {
    console.log(err)
  } 
}

onMounted(fetchItems);
watch(filters, fetchItems);







// onMounted(async () => {
//   try {
//     // const {data} = await axios.get('http://127.0.0.1:8000/api/products'); // с деструктуризацией 
//     // items.value = data.products;

//     const {data} = await axios.get('https://fd7b389119d99f32.mokky.dev/items'); // с деструктуризацией  
//     items.value = data;
//   } catch (err) {
//     console.log(err);
//   }
// });


// // для конкретного свойства - () => watch(filters.sortBy, ... )
// watch(filters, async () => {
//   try {
//     // const {data} = await axios.get('http://127.0.0.1:8000/api/products'); // с деструктуризацией 
//     // items.value = data.products;
//     const {data} = await axios.get('https://fd7b389119d99f32.mokky.dev/items?sortBy=' + filters.sortBy)
//     items.value = data
//   } catch (err) {
//     console.log(err)
//   }  
// });

</script>





<template>
  <!-- <Drawer /> -->
  <div class="bg-white w-4/5 m-auto rounded-xl shadow-xl mt-14">
    <Header />

    <div class="p-10">
      <div class="flex justify-between items-center">
        <h2 class="text-3xl font-bold mb-8">Все кроссовки</h2>

        <div class="flex gap-4">
          <select @change="onChangeSelect"
            class="py-2 px-3 border rounded-md outline-none focus:border-gray-400"
            name=""
            id=""
            >
            <option value="title">По названию</option>
            <option value="price">По цене (дешевые)</option>
            <option value="-price">По цене (дорогие)</option>
          </select>

          <div class="relative">
            <img class="absolute left-4 top-3" src="/search.svg" alt="" />
            <input
              @input="onChangeSearchInput"
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
