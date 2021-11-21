const express = require("express");
const cors = require("cors");
const models = require("./models");

// Module Import
const auth = require("./controllers/AuthController");
const router = require("./controllers/RouterControllers");

const app = express();
const port = 8080;

app.use(express.json());
app.use(cors());

app.post("/", auth.root, router.index);

app.post("/result", auth.result, router.result);

app.listen(port, function () {
  console.log("Corona BLoom Server Running");
  models.sequelize
    .sync()
    .then(() => {
      console.log("DB Connect Success ✓");
    })
    .catch(function (err) {
      console.error(err);
      console.log("DB Connect Error ✗");
      process.exit();
    });
});
