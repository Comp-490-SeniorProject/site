const path = require("path")
const BundleTracker = require("webpack-bundle-tracker")

module.exports = {
    output: {
        path: path.resolve("../static"),
        filename: "[name]-[contenthash].js",
    },
    plugins: [
        new BundleTracker({
            filename: process.env.WEBPACK_STATS ?? "./webpack-stats.json",
        }),
    ],
}
