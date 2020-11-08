import uvicorn
import time
import logging
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.emotion import EmotionAnalysis
from app.models.emotion import Emotion
from app.models.corpus import Corpus
from database.database_config import database, corpus_schema
from config.config import Config

OBJ_CONFIG = Config()
emotion_controller = EmotionAnalysis()
logging.Formatter("[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")

app = FastAPI(title='Dominant Emotion Mapping')
app.add_middleware(
    CORSMiddleware,
    # allow_origins=['client-facing-example-app.com', 'localhost:5000']
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post('/emotion_analysis')
async def emotion_analysis(emotion_model: Emotion):
    # start timer
    s_time = time.time()

    # retrieve data from request
    text = emotion_model.text

    # response template initialize
    response = {
        'version': 0.1,
        'expressions': '',
        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
        'message': 'Internal server error.',
        'text': None
    }

    try:
        predict_emotion = emotion_controller.predict([text])

        query = corpus_schema.insert().values(
            text=text,
            anger=predict_emotion[0]['score'],
            disgust=predict_emotion[1]['score'],
            fear=predict_emotion[2]['score'],
            happiness=predict_emotion[3]['score'],
            sadness=predict_emotion[4]['score'],
            surprise=predict_emotion[5]['score'],
        )
        await database.execute(query)

        # Success response
        response['expressions'] = predict_emotion
        response['message'] = 'success'
        response['status'] = status.HTTP_201_CREATED
        response['text'] = text

        # Add Elapsed time
        e_time = time.time()
        elapsed_time = e_time - s_time
        response['processing_time'] = elapsed_time
    except Exception as e:
        response['message'] = 'Internal server error | {}'.format(e)

    return response


@app.post('/corpus', response_model=Corpus, status_code=status.HTTP_201_CREATED)
async def create_corpus(corpus: Corpus):
    query = corpus_schema.insert().values(
        text=corpus.text,
        anger=corpus.anger,
        disgust=corpus.disgust,
        fear=corpus.fear,
        happiness=corpus.happiness,
        sadness=corpus.sadness,
        surprise=corpus.surprise
    )
    await database.execute(query)
    return {**corpus.dict()}


@app.get('/corpus')
async def get_all_corpus():
    response = {
        'version': 0.1,
        'corpus': None,
        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
        'message': 'success',
        'count': None
    }

    try:
        query = corpus_schema.select()
        rows = await database.fetch_all(query)
        response['corpus'] = rows
        response['count'] = len(rows)
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['message'] = 'Internal server error | {}'.format(e)

    return response


if __name__ == "__main__":
    uvicorn.run(app, log_level='info', workers=4)
