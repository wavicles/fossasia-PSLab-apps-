import threading
import sys
import time
import json
import numpy as np


class Oscilloscope:
    def __init__(self, I):
        self.oscilloscope_data_read_thread = None
        self.device = I
        self.is_reading = False

        self.number_of_samples = 1000
        self.time_base = 0.5
        self.ch1 = True
        self.ch2 = False
        self.ch3 = False
        self.mic = False
        self.ch1_map = 'CH1'
        self.ch2_map = 'CH2'
        self.mic_map = 'Inbuilt'
        self.trigger_voltage = 0
        self.trigger_channel = 'CH1'
        self.is_trigger_active = False
        self.is_fourier_transform_active = False
        self.transform_type = 'Sine'
        self.transform_channel1 = 'CH1'
        self.transform_channel2 = 'CH2'
        self.is_xy_plot_active = False
        self.plot_channel1 = 'CH1'
        self.plot_channel2 = 'CH2'

        self.number_of_channels = self.ch1 + self.ch2 + self.ch3 + self.mic
        self.channels_to_read = self.calculate_channels_to_read(
            self.ch1, self.ch2, self.ch3, self.mic)
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)

    def calculate_delay_time_gap(self, time_base, number_of_samples):
        time_gap = (time_base * 10 * 1e3) / number_of_samples
        delay = time_gap * number_of_samples * 1e-6
        if delay < 0.05:
            if self.is_fourier_transform_active:
                return (0.075, time_gap)
            else:
                return (0.05, time_gap)
        else:
            return (delay, time_gap)

    def calculate_channels_to_read(self, ch1, ch2, ch3, mic):
        if ch3 or mic:
            return 4
        elif ch2:
            return 2
        elif ch1:
            return 1
        else:
            return 0

    def fft(self, ya, si):
        ns = len(ya)
        if ns % 2 == 1:
            ns -= 1
            ya = ya[:-1]
        v = np.array(ya)
        tr = abs(np.fft.fft(v)) / ns
        frq = np.fft.fftfreq(ns, si)
        x = frq.reshape(2, ns // 2)
        y = tr.reshape(2, ns // 2)
        return x[0], y[0]

    def set_config(self, time_base, number_of_samples, ch1, ch2, ch3, mic, is_trigger_active, trigger_channel, trigger_voltage, is_fourier_transform_active):
        self.time_base = time_base
        self.number_of_samples = number_of_samples
        self.ch1 = ch1
        self.ch2 = ch2
        self.ch3 = ch3
        self.mic = mic
        self.is_trigger_active = is_trigger_active
        self.trigger_channel = trigger_channel
        self.trigger_voltage = trigger_voltage
        self.is_fourier_transform_active = is_fourier_transform_active

        self.number_of_channels = ch1 + ch2 + ch3 + mic
        self.channels_to_read = self.calculate_channels_to_read(
            self.ch1, self.ch2, self.ch3, self.mic)
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)
        trigger_channel_number = None
        if self.trigger_channel == 'CH1':
            trigger_channel_number = 0
        elif self.trigger_channel == 'CH2':
            trigger_channel_number = 1
        elif self.trigger_channel == 'CH3':
            trigger_channel_number = 2
        else:
            trigger_channel_number = 3
        self.device.configure_trigger(
            trigger_channel_number, self.trigger_channel, self.trigger_voltage)

    def get_config(self):
        output = {'type': 'GET_CONFIG_OSC',
                  'timeBase': self.time_base,
                  'ch1': self.ch1,
                  'ch2': self.ch2,
                  'ch3': self.ch3,
                  'mic': self.mic,
                  'ch1Map': self.ch1_map,
                  'ch2Map': self.ch2_map,
                  'micMap': self.mic_map,
                  'isTriggerActive': self.is_trigger_active,
                  'triggerVoltage': self.trigger_voltage,
                  'triggerChannel': self.trigger_channel,
                  'isFourierTransformActive': self.is_fourier_transform_active,
                  'transformType': self.transform_type,
                  'transformChannel1': self.transform_channel1,
                  'transformChannel2': self.transform_channel2,
                  'isXYPlotActive': self.is_xy_plot_active,
                  'plotChannel1': self.plot_channel1,
                  'plotChannel2': self.plot_channel2,
                  }
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        if self.is_fourier_transform_active:
            self.oscilloscope_data_read_thread = threading.Thread(
                target=self.capture_loop_fft,
                name='osc_fft')
        else:
            self.oscilloscope_data_read_thread = threading.Thread(
                target=self.capture_loop,
                name='osc')
        self.oscilloscope_data_read_thread.start()

    def stop_read(self):
        self.is_reading = False
        self.oscilloscope_data_read_thread.join()

    def capture_loop(self):
        self.is_reading = True
        while self.is_reading:
            self.device.capture_traces(
                self.channels_to_read, self.number_of_samples, self.time_gap, trigger=self.is_trigger_active)
            time.sleep(self.delay)
            keys = ['time']
            vector = ()
            x = None
            if self.ch1:
                x, y1 = self.device.fetch_trace(1)
                keys.append('ch1')
                vector = vector + (y1, )
            if self.ch2:
                x, y2 = self.device.fetch_trace(2)
                keys.append('ch2')
                vector = vector + (y2, )
            if self.ch3:
                x, y3 = self.device.fetch_trace(3)
                keys.append('ch3')
                vector = vector + (y3, )
            if self.mic:
                x, y4 = self.device.fetch_trace(4)
                keys.append('mic')
                vector = vector + (y4, )
            x = x * 1e-3
            vector = (x, ) + vector
            output = {'type': 'START_OSC', 'data': np.stack(
                vector).T.tolist(), 'keys': keys,
                'numberOfChannels': self.number_of_channels}
            print(json.dumps(output))
            sys.stdout.flush()

    def capture_loop_fft(self):
        self.is_reading = True
        while self.is_reading:
            self.device.capture_traces(
                self.channels_to_read, self.number_of_samples, self.time_gap, trigger=self.is_trigger_active)
            time.sleep(self.delay)
            keys = ['freq']
            vector = ()
            freq = None
            if self.ch1:
                x, y1 = self.device.fetch_trace(1)
                freq, amp1 = self.fft(y1, self.time_gap * 1e-3)
                keys.append('ch1')
                vector = vector + (amp1, )
            if self.ch2:
                x, y2 = self.device.fetch_trace(2)
                freq, amp2 = self.fft(y2, self.time_gap * 1e-3)
                keys.append('ch2')
                vector = vector + (amp2, )
            if self.ch3:
                x, y3 = self.device.fetch_trace(3)
                freq, amp3 = self.fft(y3, self.time_gap * 1e-3)
                keys.append('ch3')
                vector = vector + (amp3, )
            if self.mic:
                x, y4 = self.device.fetch_trace(4)
                freq, amp4 = self.fft(y4, self.time_gap * 1e-3)
                keys.append('mic')
                vector = vector + (amp4, )
            vector = (freq, ) + vector
            output = {'type': 'START_OSC', 'isFFT': True, 'data': np.stack(
                vector).T.tolist(), 'keys': keys,
                'numberOfChannels': self.number_of_channels}
            print(json.dumps(output))
            sys.stdout.flush()
