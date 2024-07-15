from faster_whisper import WhisperModel

import os
import time

Model_Size = "./medium"
CN_PROMPT = '聊一下基于faster-whisper的实时/低延迟语音转写服务'


def transcribe(file_str, language='en'):
    model = WhisperModel(Model_Size, device="auto", compute_type="int8")
    # model.feature_extractor.mel_filters = model.feature_extractor.get_mel_filters(
    # model.feature_extractor.sampling_rate, model.feature_extractor.n_fft, n_mels=128)
    start_time = time.time()
    segments, info = model.transcribe(file_str, language, beam_size=5)
    text = ''
    for segment in segments:
        text += segment.text
    end_time = time.time()
    period = end_time - start_time
    return text + str(period)


# transcribe()
# print(os.path.isdir('../large-v3'))
