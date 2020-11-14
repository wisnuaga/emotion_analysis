# Emotion Analysis

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```
Requirements.txt
```bash
pydantic~=1.7.2
tensorflow~=2.3.1
numpy~=1.16.0
pandas~=1.1.4
psycopg2~=2.8.6
asyncpg~=0.21.0
fastapi~=0.61.2
databases~=0.4.0
SQLAlchemy~=1.3.20
python-dotenv~=0.15.0
uvicorn~=0.12.2
PySastrawi~=1.2.0
gunicorn~=20.0.4
uvloop~=0.14.0
httptools~=0.1.1
```
Running app
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001 apps:app --timeout 1800
```

## Usage
##### Endpoint LSTM model
```text
https://dominant-emotion-analysis.herokuapp.com/emotion_analysis
```
Request Method
```text
POST
```

JSON Input
```json
{
    "text": "aku terkejut melihat kamarku berantakan"
}
```

JSON Output
```json
{
    "version": 0.1,
    "expressions": [
        {
            "tag": "MARAH",
            "score": 0.0574
        },
        {
            "tag": "JIJIK",
            "score": 0.0009
        },
        {
            "tag": "TAKUT",
            "score": 0.0003
        },
        {
            "tag": "SENANG",
            "score": 0.0013
        },
        {
            "tag": "SEDIH",
            "score": 0.0002
        },
        {
            "tag": "KAGET",
            "score": 0.7954
        }
    ],
    "status": 201,
    "message": "success",
    "text": "aku terkejut melihat kamarku berantakan",
    "processing_time": 1.364778757095337
}
```

##### Endpoint Multinomial Naive Bayes with Persamaan Batas Dominan model
```text
https://dominant-emotion-analysis.herokuapp.com/emotion_analysis
```
Request Method
```text
POST
```

JSON Input
```json
{
    "text": "bangsat kamu kurang ajar",
    "beta": 0.03
}
```

JSON Output
```json
{
    "version": 0.1,
    "status": 200,
    "message": "success",
    "text": "bangsat kamu kurang ajar",
    "expressions": [
        {
            "tag": "MARAH",
            "score": 0.38449304073161356
        },
        {
            "tag": "JIJIK",
            "score": 0.10118560415607536
        },
        {
            "tag": "TAKUT",
            "score": 0.1038166002029496
        },
        {
            "tag": "SENANG",
            "score": 0.1017323574239034
        },
        {
            "tag": "SEDIH",
            "score": 0.20164869680214054
        },
        {
            "tag": "KAGET",
            "score": 0.10712370068331822
        }
    ],
    "dominant_threshold": {
        "score": 0.13118560415607536,
        "beta": 0.03
    },
    "dominant_emotion": [
        {
            "tag": "MARAH",
            "score": 0.38449304073161356
        },
        {
            "tag": "SEDIH",
            "score": 0.20164869680214054
        }
    ],
    "dominant_emotion_percentage": [
        {
            "tag": "MARAH",
            "score": 0.6559728067641178
        },
        {
            "tag": "SEDIH",
            "score": 0.34402719323588216
        }
    ],
    "dominant_emotion_softmax": [
        {
            "tag": "MARAH",
            "score": 0.5455841590167495
        },
        {
            "tag": "SEDIH",
            "score": 0.4544158409832505
        }
    ],
    "processing_time": 0.024735689163208008
}
```

## Authors
```
Wisnu Agastya
wisnu.aga@gmail.com
```

## License
[MIT](https://choosealicense.com/licenses/mit/)