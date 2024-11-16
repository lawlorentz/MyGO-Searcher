<template>
	<NuxtPage></NuxtPage>
</template>


<style>
html,
body {
	padding: unset !important;
	margin: unset !important;
	font-family: 'Microsoft JhengHei', sans-serif;
}
</style>

<script setup lang="ts">
const onLoaded = ref(false);

useSeoMeta({
	title: 'MyGO表情包搜索引擎',
	ogTitle: 'MyGO表情包搜索引擎',
	description: '愿意一辈子跟我组乐团吗。MyGO表情包搜索引擎，收集来自MyGO动画的各种生草截图，没有看MyGO的人只能过上相对失败的人生，和我一起踏上能够仅用MyGO截图就能聊天的人生吧。',
	ogDescription: '愿意一辈子跟我组乐团吗。MyGO表情包搜索引擎，收集来自MyGO动画的各种生草截图，没有看MyGO的人只能过上相对失败的人生，和我一起踏上能够仅用MyGO截图就能聊天的人生吧。',
});

onMounted(() => {
	if (process.client) {
		onLoaded.value = true;
	}
});
</script>