
<template>
    <div class="flex flex-col w-screen h-full bg-tggray-50">
        <Header class="outline outline-offset-0 outline-tggray-300 outline-2" />
        <div class="p-10">
            <SearchBar class="mb-5" @update:search="handleSearch"/>
            <ViewPanel class="mt-5" :searchQuery="searchQuery"/>
        </div>
        <Footer class=""/>
    </div>
        <BackToTop class="fixed bottom-5 right-5"/>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const searchQuery = ref('');

const handleSearch = (newSearch: string) => {
    searchQuery.value = newSearch;
}

</script>