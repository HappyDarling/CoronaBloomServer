const tf = require("@tensorflow/tfjs");

class L2 {
  static className = "L2";
  constructor(config) {
    return tf.regularizers.l1l2(config);
  }
}
tf.serialization.registerClass(L2);

async function loadModel() {
  model = undefined;
  model = await tf.loadLayersModel(
    "https://raw.githubusercontent.com/HappyDarling/CoronaBloomServer/main/ML/best_model.json"
  );
  console.log("model loaded");
}

loadModel();
