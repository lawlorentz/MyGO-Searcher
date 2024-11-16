# MyGo贴图搜索引擎

支持模糊查询版

你愿意一辈子跟我一起MyGO吗？


## 对原项目的修改

- 重写检索部分，增加了模糊查询功能，使用[BAAI/bge-small-zh-v1.5](https://github.com/FlagOpen/FlagEmbedding)进行密集检索


## 部署指南

1. clone下本项目
2. 安装dependencies

```bash
cd MyGo_Searcher
npm install # or yarn install
```
3. 设定环境变数(非必要)
```
echo "API_BASE_URL=<API_BASE_URL>" >> .env.development
```
4. 启动模糊检索服务
```
python retrieve.py
python backend.py
```
修改nuxt.config.ts中的BACKEND_API_URL为backend.py运行的地址。
（没有GPU的朋友可能需要自行修改代码）

5. 启动及部署Nuxt

```bash
yarn dev # with devmode
yarn build # for production
```
