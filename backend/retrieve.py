import json
from FlagEmbedding import FlagAutoModel
import faiss
import numpy as np
import os



with open('image_map_zh_cn.json', 'r') as f:
    image_map = json.load(f)
    image_map_keys = [_['name_zh_cn'] for _ in image_map]
    # 检测是否有重复的名称
    for i in range(len(image_map)):
        img_name = image_map[i]['name_zh_cn']
        for j in range(i+1, len(image_map)):
            if img_name == image_map[j]['name_zh_cn']:
                print(f"Duplicate name: {img_name}")
    new_image_map = {}
    for idx, key in enumerate(image_map_keys):
        new_image_map[key] = image_map[idx]
    image_map_list = image_map
    image_map = new_image_map

with open('mygo_zh_cn.json', 'r') as f:
    word_map = json.load(f)
    words = list(word_map.keys())


def retrieve_img_data(query, index, model, num=10):
    data1 = []
    data2 = []
    data3 = []
    if query in words:
        keys = word_map[query]['value']
        for key in keys:
            for img in image_map_list:
                if key == img['name']:
                    data1.append(img)
        
        
    if query in image_map_keys:
        data2 = [image_map[query]]
    
    query_embeddings = model.encode_queries([query]).astype(np.float32)
    dists, ids = index.search(query_embeddings, k=num)
    data3 = [image_map_list[int(i)] for i in ids[0]]
    
    # 去掉names1和names2中已经出现过的图片
    names1 = [d['name_zh_cn'] for d in data1]
    names2 = [d['name_zh_cn'] for d in data2]

    for d in data3:
        if d['name_zh_cn'] in names1 or d['name_zh_cn'] in names2:
            data3.remove(d)
    
    return data1 + data2 + data3


if __name__ == '__main__':
    model = FlagAutoModel.from_finetuned('BAAI/bge-small-zh-v1.5',
                                         query_instruction_for_retrieval="为这个句子生成表示以用于检索相关文章：",
                                         use_fp16=True,
                                         devices=['cuda:0'])  # Setting use_fp16 to True speeds up computation with a slight performance degradation
    if os.path.exists("./index.bin"):
        index = faiss.read_index("./index.bin")
    else:
        corpus = [_['name_zh_cn'] for _ in image_map_list]
        corpus_embeddings = model.encode(corpus).astype(np.float32)
        dim = corpus_embeddings.shape[-1]
        index = faiss.IndexFlatIP(dim)
        # # use a single GPU
        # rs = faiss.StandardGpuResources()
        # co = faiss.GpuClonerOptions()

        # # then make it to gpu index
        # index_gpu = faiss.index_cpu_to_gpu(
        #     provider=rs, device=0, index=index, options=co)
        # index_gpu.add(corpus_embeddings)
        index.add(corpus_embeddings)
        print(f"total number of vectors: {index.ntotal}")
        path = "./index.bin"
        faiss.write_index(index, path)
        # index = faiss.read_index("./index.bin")
    
    query = '我不知道'
    print(retrieve_img_data(query, index, model))
