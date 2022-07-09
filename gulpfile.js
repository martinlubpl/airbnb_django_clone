const gulp = require("gulp");

// npm i gulp-postcss gulp-csso gulp-sass node-sass
const css = () => {
    const postCSS = require("gulp-postcss");
    const sass = require("gulp-sass")(require("node-sass"));
    const minify = require("gulp-csso");
    /* sass.compiler = require("node-sass"); */
    /* // node-sass is a compiler for gulp-sass */
    return gulp
        .src("assets/scss/styles.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(postCSS([
            require("tailwindcss"),
            require("autoprefixer"),
        ]))
        .pipe(minify())
        .pipe(gulp.dest("static/css"));
};

exports.default = css;