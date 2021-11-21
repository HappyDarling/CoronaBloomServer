const models = require("../models");
const rs = require("../module/randomString.js");
const NLP = require("../module/NLPProcessingModule.js");
const conv = require("../NLP_DATA/myConv.json");

module.exports.index = async (req, res) => {
  const { SNS, account } = req.body;

  // RandomString 생성
  const auth = rs.randomString();

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
};

module.exports.result = async (req, res) => {
  NLP.tokenizer(conv)
    .then((res) => NLP.predict(res))
    .then((result) => res.send({ predict: result, conv: conv }));
};
