<!-- C:\projects\vueles\front-vue-sneakers\src\App.vue -->
<script setup>
import { onMounted, ref, watch, reactive, provide} from 'vue'
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


const  fetchFavorites = async () => {
    try {
    const {data: favorites} = await axios.get("http://127.0.0.1:8000/api/favorites")
    
    items.value = items.value.map(item => {
      
      const favorite = favorites.favorites.find(favorite => favorite.product_id === item.id);
      if (!favorite) {
        return item;
      }

      return {
        ...item,
        isFavorite: true,
        favoriteId: favorite.id,
      }
    })
    // console.log(items.value)
  } catch (err) {
    console.log(err)
  } 
}

const addToFavorite = async (item) => {
  try {
    if (!item.isFavorite) {
      const obj = {
        product_id: item.id
    };

    item.isFavorite = true;
    const {data} = await axios.post("http://127.0.0.1:8000/api/favorites", obj)

    item.favoriteId = data.id;
    } else {

    await axios.delete(`http://127.0.0.1:8000/api/favorites/${item.favoriteId}`)
    item.isFavorite = false
    item.favoriteId = null
    }

  } catch (err) {
    console.log(err);
  }
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
    items.value = data.products.map(obj => ({
      ...obj,
      isFavorite: false,
      favoriteId: null,
      isAdded: false,
    }));
  } catch (err) {
    console.log(err)
  } 
}

onMounted(async () => {
  await fetchItems();
  await fetchFavorites();
});
watch(filters, fetchItems);



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
        <CardList :items="items" @addToFavorite="addToFavorite"/>
      </div>  
    </div>
  </div>
</template>
