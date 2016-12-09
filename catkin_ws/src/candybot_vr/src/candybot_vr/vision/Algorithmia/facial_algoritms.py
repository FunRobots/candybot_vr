import Algorithmia
import logging

logging.basicConfig(filename='facial_algotithms.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

api_key = 'simAkHd6NFelROawvgBT9ouDB6C1'

def get_emotions(photo):
    '''Returns emotions by face image
    Args:
        photo: photo file name
    Returns:
        {'emotion1': confidence1, 'emotion2': confidence2, ...}: if data recieved
        None: if failed
    '''
    
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')
        img = bytearray(open(photo,'rb').read())
        emotions = algo.pipe(img).result['results']
        d_emotions = dict()
        for emotion in emotions:
            d_emotions[emotion[1]] = emotion[0]
        return d_emotions
        
    except Exception as e:
        logging.error(str(e))
        return None


def celebrities_similarity(photo):
    '''Returns person similarity to some celebrity
    Args:
        photo: photo file name
    Returns:
        [Celebrity name, confidence]: if data recieved
        None: if failed
    '''
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/DeepFaceRecognition/0.1.1')
        img = bytearray(open(photo,'rb').read())
        celebrities = algo.pipe(img).result['results']
        return [' '.join(celebrities[0][1].split('_')), celebrities[0][0]]
        
    except Exception as e:
        logging.error(str(e))
        return None
    
