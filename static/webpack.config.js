var debug = process.env.NODE_ENV !== "production";
const webpack = require('webpack');
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

// const fronthtmlPlugin = new HtmlWebPackPlugin({
//   template: "./front.html",
//   filename: "./front.html"
// });


console.log(path.resolve(__dirname, 'build'));
console.log(__dirname + '\\src\\*.html');
module.exports = {
  context: path.join(__dirname, "src"),
  devtool: debug ? "inline-sourcemap" : null,
  entry: {
    front: "./js/front.js",
    back:"./js/back.js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: [
              {loader: "style-loader"},
              {loader: "css-loader"}
          ]
      },
      // {
      //   test: /\.(html)$/,
      //   use: [{
      //     loader: "file-loader",
      //     options: {
      //       name: '[name].[ext]',
      //       emitFile: true,
      //       context: path.join(__dirname, "src"),
      //       outputPath: path.join(__dirname, "build")
      //     }
      //   }]
      // }
    ]
  },
  output: {
    path: path.join(__dirname, "build\\static"),
    chunkFilename: '[name].bundle.js',
    filename: "[name].bundle.js"
  },
  // optimizations: {
  //   splitChunks: {
  //     chunks:'all'
  //   }
  // },
  plugins: [
    new CopyWebpackPlugin([
      {
       from: __dirname + '\\src\\*.html',
       to: path.resolve(__dirname, 'build')
     }
   ])
  ],
};
