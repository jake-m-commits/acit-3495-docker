const env = require("dotenv");
const mysql = require("mysql2");


env.config()

const db = mysql.createConnection({
  host: process.env.MYSQL_SERVICE_SERVICE_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

db.connect((err) => {
  if (err) throw err;
  console.log("Connected to MySQL Server!");
  let SQL = "create database IF NOT EXISTS docker"
  db.query(SQL, (err, result) => {
    if (err) throw err;
    let SQL1 = "create table IF NOT EXISTS docker.percentages (percent INT NOT NULL);"
    console.log(result)
    db.query(SQL1, (err, result) => {
      if (err) throw err;
      console.log(result)
    })
  })
});

module.exports = db

