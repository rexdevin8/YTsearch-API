# main.py
from fastapi import FastAPI
from youtubesearchpython import *
import uvicorn

app = FastAPI()

def youtube(keyword,counts):
    customSearch = VideosSearch(keyword, limit=int(counts)+2)

    title = []
    pub = []
    dura = []
    count = []
    link = []

    print(counts)
    for i in range(int(counts)):
        # print(customSearch.result()['result'][i]['title'])
        text = customSearch.result()['result'][i]['title']
        utext = text.encode("utf-8")
        utext = utext.decode('utf-8')
        title.append(utext)
        # print(customSearch.result()['result'][i]['link'])
        link.append(customSearch.result()['result'][i]['link'])
        # print(customSearch.result()['result'][i]['publishedTime'])
        pub.append(customSearch.result()['result'][i]['publishedTime'])
        # print(customSearch.result()['result'][i]['duration'])
        dura.append(customSearch.result()['result'][i]['duration'])
        # print(customSearch.result()['result'][i]['viewCount']['text'])
        count.append(customSearch.result()['result'][i]['viewCount']['text'])

    d = {'data': [{'Title': a, 'Published': b, 'Duration': c, 'Views': d, 'Link': e} for a, b, c, d, e in
                  zip(title, pub, dura, count, link)]}
    data = d#json.dumps(d, indent=4)
    return data

@app.get("/")
async def root():
    return {"message": "YT-Search Api By DiyRex", "Usage":"host:port/ytsearch/keyword/count"}

@app.get("/ytsearch/{keyword}/{counts}")
def ytsearch(keyword,counts):
    p = youtube(keyword,counts)
    return p

@app.get("/ytsearch/{keyword}")
def ytsearch(keyword):
    p = youtube(keyword,5)
    return p
