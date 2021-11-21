const models = require("../models");

module.exports.root = async (req, res, next) => {
  const { SNS, account, password } = req.body;

  if (!SNS || !account || !password || password !== "0000") {
    // 방어 코드
    // 인증키 값이 다를 경우와 필드가 비어있을 경우 나눠서 생성해야 함
    res.send("에러가 발생하였습니다");
  } else next();
};

module.exports.result = async (req, res, next) => {
  const { SNS, account, auth } = req.body;

  // 방어코드 (SNS, account, auth가 비어있을 경우) (Client)
  if (!SNS || !account || !auth) {
    res.status(400).send({
      Code: 1,
      Title: "ERROR",
      Message: "비정상적인 접근입니다",
    });
  }

  // 방어코드 (데이터베이스와 정보가 다를 경우) (Server)
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
      } else {
        next();
      }
    })
    .catch((error) => {
      console.log(error);
    });
};
