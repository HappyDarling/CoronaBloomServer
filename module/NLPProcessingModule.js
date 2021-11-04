// https://www.youtube.com/watch?v=1s9k2GxH2g4&t=245s&ab_channel=BhaveshBhatt
// https://computer-science-student.tistory.com/297

const tf = require("@tensorflow/tfjs");

const { PythonShell } = require("python-shell");

// JSON 데이터로 되어있는 대화문을 변수에 할당
const conv = require("../NLP_DATA/myConv.json");

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
  model = undefined;
  model = await tf.loadLayersModel(
    "https://raw.githubusercontent.com/HappyDarling/CoronaBloomServer/main/ML/machineData/best_model/model.json"
  );
  console.log("model loaded");
}
loadModel();

var convToken;

// 자연어 처리를 하기 위해 분석할 대화문을 토큰화
var options = {
  args: [JSON.stringify({ conv })],
};

PythonShell.run(
  "D://21-2/MachineLearning/VSCode/coronabloomserver/module/NLPTokenizer.py", // 절대경로 반드시 지정해야 인식 (Python 특징?)
  options,
  function (err, data) {
    console.log(err);
    convToken = JSON.parse(data);
    console.log(convToken["2021.09"]);
  }
);
