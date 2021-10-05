const express = require("express");
const cors = require("cors");
const models = require("./models");
const rs = require("./module/randomString.js");
const app = express();
const port = 8080;

app.use(express.json());
app.use(cors());

app.post("/", (req, res) => {
  const body = req.body;
  const { SNS, account, password } = body;
  const auth = rs.randomString();
  setTimeout(function () {
    console.log("Works!");

    if (!SNS || !account || !password || password !== "0000") {
      // 방어 코드
      // 인증키 값이 다를 경우와 필드가 비어있을 경우 나눠서 생성해야 함
      res.send("에러가 발생하였습니다");
    } else {
      // 데이터베이스 연동 코드
      // 조회 시작할 때 인증키를 생성
      // 만약 SNS와 account가 동일한 사람이 없다면 새로 생성, 있다면 Update
      models.userAuth
        .findOne({ where: { SNS: SNS, account: account } })
        .then((user) => {
          user
            .update({ SNS: SNS, account: account, auth: auth })
            .then(() => console.log("Data Update Success ✓"))
            .catch(() => console.log("Data Update Error ✗"));
        })
        .catch(() => {
          models.userAuth
            .create({ SNS: SNS, account: account, auth: auth })
            .then(() => console.log("Data Create Success ✓"))
            .catch(() => console.log("Data Create Error ✗"));
        });
      res.send({
        SNS: SNS,
        account: account,
        auth: auth,
      });
    }
  }, 3000);
});

app.post("/result", (req, res) => {
  const body = req.body;
  const { SNS, account, auth } = body;
  if (!SNS || !account || !auth) {
    // 방어 코드 (SNS, account, auth가 비어있을 경우)
    res.send({
      Code: 1,
      Title: "ERROR",
      Message: "비정상적인 접근입니다",
    });
  }
  models.userAuth
    .findOne({ where: { SNS: SNS, account: account } })
    .then((user) => {
      if (user.dataValues.auth !== auth) {
        res.send({
          Code: 2,
          Title: "ERROR",
          Message:
            "입력한 정보와 인증키가 일치하지 않습니다. 다시 시도해주세요.",
        });
      }
      // 여기서부터
      // 이제 인증키 전부 맞은걸 확인했으니 머신러닝 모듈 파트를 구현해야 함
    })
    .catch(() => {});
});

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
