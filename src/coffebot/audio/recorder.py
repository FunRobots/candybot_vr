#!/usr/bin/env python3
'''
record audio
'''

import pyaudio
import time
import audioop

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class Recorder:


    def __init__(self, pyaudio_config: dict, min_rms=100):
        try:
            self.set_min_rms(min_rms=min_rms)
            #set up pyaudio configuration and start audio stream
            self.format = pyaudio_config['format']
            self.channels = pyaudio_config['channels']
            self.rate = pyaudio_config['rate']
            self.chunk_size = pyaudio_config['frames_per_buffer']

            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk_size)
            self.stream.start_stream()
        except Exception as e:
            logging.error(str(e))

    def set_min_rms(self, min_rms):
        self.min_rms = min_rms

    def record_audio(self, last_chunk):
        print('rec')
        '''Records speech until silence
        Args:
            last_chunk: last chunk before record starting
            stream: audio stream
            min_rms: minimal rms value that is not silence
        Returns:
            buf: contains recorded audio data, bytes type
        '''
        try:
            buf = last_chunk
            silence_start = time.time()
            while (time.time() - silence_start) < 1.2:
                chunk = self.stream.read(self.chunk_size)
                if audioop.rms(chunk, 2) >= self.min_rms / 3 :
                    buf += chunk
                if audioop.rms(chunk, 2) >= self.min_rms:
                    silence_start = time.time()
            return buf
        except Exception as e:
            logging.error(str(e))
            return None

    def listen_audio(self):
        try:
            while True:
                chunk = self.stream.read(self.chunk_size)
                #if sound detected record raw data until silence
                if audioop.rms(chunk, 2) >=  self.min_rms:
                    buf = self.record_audio(last_chunk=chunk)
                    return buf
        except Exception as e:
            logging.error(str(e))
