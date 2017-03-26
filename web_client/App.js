import React, { Component, PropTypes } from 'react';
import ReactDOM from 'react-dom';
import injectTapEventPlugin from "react-tap-event-plugin";

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import UniNavigationBar from './Components/UniNavigationBar'

class App extends Component {
    render() {
        return (
        <MuiThemeProvider>
            <div>
                <UniNavigationBar/>
            </div>
        </MuiThemeProvider>
        )
    }
}

function run() {
    injectTapEventPlugin();
    ReactDOM.render(<App />, document.getElementById('app'));
}

const loadedStates = ['complete', 'loaded', 'interactive'];

if (loadedStates.includes(document.readyState) && document.body) {
    run();
} else {
    window.addEventListener('DOMContentLoaded', run, false);
}