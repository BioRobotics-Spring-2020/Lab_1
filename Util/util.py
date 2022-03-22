from pylsl import StreamInlet
import pandas as pd
from pandas import Timestamp
from datetime import datetime


def obtain_stream_channel_names(stream):
    if stream.name() == 'Unicorn':
        header=['EEG1','EEG2','EEG3','EEG4','EEG5','EEG6','EEG7','EEG8',
                        'Acclerometer X','Acclerometer Y','Acclerometer Z',
                        'Gyroscope X','Gyroscope y','Gyroscope Z','Battery Level','Counter','Validation Indicator']
    else:
        header = []
        inlet = StreamInlet(stream)
        info = inlet.info()
        ch = info.desc().child("channels").child("channel")
        for k in range(info.channel_count()):
            header.append(ch.child_value("label"))
            ch = ch.next_sibling()
    return header


def format_data_into_dataframe(samples, timestamps, header):
    if len(header) > 0:
        df = pd.DataFrame(columns=header)
    else:
        df = pd.DataFrame()
    for sample, timestamp in zip(samples, timestamps):
        converted_time = datetime.fromtimestamp(timestamp)
        current_time = Timestamp(0).now()
        sample.append(converted_time)
        df.at[current_time] = sample
    return df