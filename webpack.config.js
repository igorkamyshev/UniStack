var path = require('path');

module.exports = {
    entry: './web_client/App.js',
    output: {
        path: path.resolve(__dirname, './front/static'),
        filename: 'app.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['env']
                    }
                }
            }
        ]
    }
};