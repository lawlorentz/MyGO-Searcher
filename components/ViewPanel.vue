<template>
    <div class="flex w-full justify-center">
        <div class="image-row">
            <ImageView v-for="image in images" :url="image.url" :alt="image.alt" class="image" />
        </div>
    </div>
</template>
<script setup lang="ts">
import { watch, ref, onMounted } from 'vue';
import { getAllImageList } from '~/apis/base';

const config = useRuntimeConfig();

interface img {
    url: string,
    alt: string
}

const images = ref<img[]>([
    // 'https://i.imgur.com/olWo9xr.jpg',
    // 'https://i.imgur.com/83sKGOi.jpg',
    // 'https://i.imgur.com/XSzy1Hq.jpg',
    // 'https://i.imgur.com/z5fMg6I.jpg',
    // 'https://i.imgur.com/rPU8WDd.jpg'
]);

const props = defineProps({
    searchQuery: String
});

const getImageList = async (query: string, config: any) => {
    try {
        images.value = await getAllImageList(query, config);
    } catch (error) {
        images.value = [];
    }
}

// 監視 searchQuery 變化
watch(() => props.searchQuery, (newQuery) => {
    getImageList(newQuery || '', config);
}, { immediate: true });

onMounted(() => {
    getImageList('', config);
});

</script>

<style scoped>
.image-row {
    display: grid;
    /* grid-template-columns: repeat(4, 1fr); */
    grid-template-columns: repeat(4, minmax(16rem, 1fr));
    gap: 10px;
    margin-bottom: 10px;
}

@media screen and (max-width: 768px) {
    .image-row {
        grid-template-columns: repeat(1, 1fr);
    }
}

@media screen and (max-width: 1024px) {
    .image-row {
        grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
    }
}
</style>