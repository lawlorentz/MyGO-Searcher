export const getAllImageList = async (query: string, config: any) => {
	let API_BASE_URL = config.public.API_BASE_URL;
	let BACKEND_API_URL = 'http://leian.natapp1.cc/search_image';
	let url = '';
	try {
		if (query) {
			// 获取请求中的文本参数
			const text = query;
			// 使用 fetch 请求本地 API
			const response = await fetch(BACKEND_API_URL, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ text }), // 发送包含 text 的 JSON 数据
			});
			const data = await response.json();
			return data.urls;

		} 
		else {
			url = `${API_BASE_URL}/all_img`;
			

			const response = await fetch(url, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				},
			});
			const data = await response.json();
			return data.urls;
		}
	} catch (error) {
		console.error('Error fetching data: ', error);
		return [];
	}
};