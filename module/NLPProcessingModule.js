// https://maruzzing.github.io/study/nodejs/node.js%EC%97%90%EC%84%9C-python-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/
// https://www.youtube.com/watch?v=1s9k2GxH2g4&t=245s&ab_channel=BhaveshBhatt
// https://computer-science-student.tistory.com/297
// https://github.com/tensorflow/tfjs/issues/613

const { PythonShell } = require("python-shell");
const tf = require("@tensorflow/tfjs");

// JS에서 L2 Norm을 사용하기 위해 클래스를 따로 정의
class L2 {
  static className = "L2";
  constructor(config) {
    return tf.regularizers.l1l2(config);
  }
}
tf.serialization.registerClass(L2);

// Github에 업로드 되어있는 Keras로 만들어진 model load
async function loadModel() {
  console.log("loadModel()");
  model = undefined;
  model = await tf.loadLayersModel(
    "https://raw.githubusercontent.com/HappyDarling/CoronaBloomServer/main/ML/machineData/best_model/model.json"
  );
  console.log("model loaded");
  return model;
}
loadModel();

function tokenizer(conv) {
  return new Promise((resolve, reject) => {
    // 자연어 처리를 하기 위해 분석할 대화문을 토큰화
    var options = {
      args: [JSON.stringify({ conv })],
    };
    PythonShell.run("module/NLPTokenizer.py", options, function (err, data) {
      if (err) throw err;
      convToken = JSON.parse(data);
      resolve(convToken);
    });
  });
}

function predict(convToken) {
  let ctJson = new Object(); // 예측값을 받아올 변수
  return new Promise((resolve, reject) => {
    for (i in convToken) {
      pre = [];
      for (j of convToken[i]) {
        pre.push(model.predict(tf.tensor(j)).dataSync()[0]);
      }
      ctJson[i] = new Array();
      ctJson[i].push(pre);
    }
    resolve(ctJson);
  });
}

module.exports = {
  tokenizer,
  predict,
};
