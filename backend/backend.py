
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import faiss  # 向量检索库
from FlagEmbedding import FlagAutoModel
from retrieve import retrieve_img_data

app = Flask(__name__)
CORS(app)

# 初始化密集检索模型和向量数据库
model = FlagAutoModel.from_finetuned('BAAI/bge-small-zh-v1.5',
                                     query_instruction_for_retrieval="为这个句子生成表示以用于检索相关文章：",
                                     use_fp16=True,
                                     devices=['cuda:0'])  # Setting use_fp16 to True speeds up computation with a slight performance degradation
index = faiss.read_index("./index.bin")
url = 'https://drive.miyago9267.com/d/file/img/mygo/'

# 路由：接收 POST 请求，传入文字，返回最匹配的图片 URL


@app.route('/search_image', methods=['POST'])
def get_image():
    data = request.json
    text = data.get('text', '')

    img_datas = retrieve_img_data(text, index, model, 10)
    image_urls = [{'url': url + img_data['file_name'],'alt': img_data['name_zh_cn']} for img_data in img_datas]

    if len(img_datas) > 0:
        return jsonify({"status": "success", "urls": image_urls}), 200
    else:
        return jsonify({"status": "fail", "message": "No image found for the given text"}), 404


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=36432,
        debug=False
    )
