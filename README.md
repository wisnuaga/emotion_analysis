# Emotion Analysis

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage
### Endpoint
```bash
https://localhost:8001/emotion_analysis
```

### Input
```json
{
    "text": "aku terkejut melihat kamarku berantakan"
}
```

### Output
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)