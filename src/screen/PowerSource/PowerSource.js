import React, { Component } from 'react';
import SimplePanelLayout from '../../components/SimplePanelLayout';
import Settings from './components/Settings';
import roundOff from '../../util/arithmetics';
import debounce from 'lodash/debounce';
const electron = window.require('electron');
const { ipcRenderer } = electron;
const loadBalancer = window.require('electron-load-balancer');

class PowerSouce extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pv1: -5,
      pv2: -3.3,
      pv3: 0,
      pcs: 0,
    };
  }

  sendConfigToDevice = values =>
    debounce(() => {
      console.log('command fired', {
        command: 'CONFIG_PWR_SRC',
        ...values,
      });
      loadBalancer.send(ipcRenderer, 'linker', {
        command: 'CONFIG_PWR_SRC',
        ...values,
      });
    }, 500);

  onChangeSlider = pinType => (event, value) => {
    this.setState(
      {
        [pinType]: roundOff(value),
      },
      () => {
        this.sendConfigToDevice({
          ...this.state,
        })();
      },
    );
  };

  onPressButton = (pinType, isPositive) => event => {
    this.setState(
      {
        [pinType]: roundOff(this.state[pinType] + (isPositive ? 0.01 : -0.01)),
      },
      () => {
        this.sendCommand({
          ...this.state,
        })();
      },
    );
  };

  render() {
    const { pv1, pv2, pv3, pcs } = this.state;

    return (
      <SimplePanelLayout
        panel={
          <Settings
            pv1={pv1}
            pv2={pv2}
            pv3={pv3}
            pcs={pcs}
            onPressButton={this.onPressButton}
            onChangeSlider={this.onChangeSlider}
          />
        }
      />
    );
  }
}

export default PowerSouce;
