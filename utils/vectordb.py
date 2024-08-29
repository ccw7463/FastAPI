from . import *
from langchain_community.vectorstores import FAISS
from models.model import embedding_model

class VectorDB():
    def __init__(self):
        self.DB = None
        
    def generate_vector_db(self):
        ALLCONE_QNA = json.load(open("data/CustomerService/sft_qna_base_single.json"))
        DATA_LST = []
        for data in tqdm(ALLCONE_QNA):
            text = f"""제목 : {data['metadata']['title']}
        사용자 요청문 : {data['input']}
        해결 방법 : {data['response']}"""
            DATA_LST.append(text)
        
        FAQ_DATA = json.load(open("data/CustomerService/FAQ.json"))
        DATA_LST += FAQ_DATA
        self.DB = FAISS.from_texts(DATA_LST, embedding_model)
        
        
        
