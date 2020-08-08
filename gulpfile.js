
// Load plugins
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    notify = require('gulp-notify'),
    del = require('del'),
    plumber = require('gulp-plumber'),
    browserSync = require('browser-sync'),
    changed = require('gulp-changed')

gulp.task('styles', gulp.series(function(callback_finished) {
    var years = ['2018', '2019', '2020'];
    years.forEach(function(year) {
      gulp.src('docs/_static/conf/scss/main-' + year + '.scss', {style: 'expanded'})
          .pipe(sass().on('error', sass.logError))
          .pipe(plumber())
          .pipe(autoprefixer({browsers: ['last 2 version']}))
          .pipe(gulp.dest('docs/_static/conf/css/'))
          .pipe(rename({suffix: '.min'}))
          .pipe(cssnano())
          .pipe(gulp.dest('docs/_static/conf/css/'))
          .pipe(notify({message: 'Styles task complete for ' + year}));
    });
    callback_finished()
}));

// Browser sync appears actually broken:
// https://github.com/writethedocs/www/issues/1042

// Static server
gulp.task('browser-sync', gulp.series(function() {
    browserSync.init([
      "docs/_static/conf/css/*.css",
      "docs/_static/conf/js/*.js",
      'docs/_templates/conf/*.html'], {
        proxy:  "http://localhost:8888"
    });
}));

//Watch
gulp.task('watch', gulp.series('browser-sync', function() {
  gulp.watch('docs/_static/conf/scss/main.scss', ['styles']);
}));

//Default task
gulp.task('default', gulp.series('browser-sync', function() {
    gulp.start('styles');
    gulp.start('watch');
}));
