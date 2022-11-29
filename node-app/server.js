const createError = require("http-errors");
const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");
const logger = require("morgan");
const bodyParser = require("body-parser");
const flash = require("express-flash");
const session = require("express-session");
const app = express();
const mysql = require("mysql2");
const db = require("./database");

// CREATE USER 'docker'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'docker';
// GRANT ALL PRIVILEGES ON docker.*  TO 'docker'@'localhost';
// FLUSH PRIVILEGES;

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use(
    session({
        secret: "123456catr",
        resave: false,
        saveUninitialized: true,
        cookie: {maxAge: 60000},
    })
);

app.use(flash());

app.get("/", function (req, res) {
    let host = req.get("host").split(":")[0];
    res.redirect(`http://${host}:5000`);
});

app.get("/home", function (req, res, next) {
    res.render("index");
});

app.post("/submit-perc", function (req, res, next) {
    let percentage = req.body.percentage;
    if (percentage.length === 0) {
        console.log(`Cant be empty`);
        res.redirect("/home");
    }
    if (isNaN(percentage)) {
        console.log(`Must be number not ${percentage}`);
        res.redirect("/home");
    }
    if (percentage >= 0 && percentage <= 100) {
        // let value = [percentage]
        let sql = `INSERT INTO percentages (percent) VALUES (?)`;
        db.query(sql, percentage, function (err, result) {
            if (err) throw err;
            console.log("record inserted");
            req.flash("success", "Data added successfully!");
            res.redirect("/home");
        });
    }
    else {
        console.log(`Must be between 0-100 not ${percentage}`);
        res.redirect("/home");
    }
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
    next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get("env") === "development" ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render("error");
});

// port must be set to 3000 because incoming http requests are routed from port 80 to port 8080
app.listen(3000, function () {
    console.log("Node app is running on port 3000");
});

module.exports = app;
