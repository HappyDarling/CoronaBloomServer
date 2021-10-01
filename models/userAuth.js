module.exports = function (sequelize, DataTypes) {
  const userAuth = sequelize.define("userAuth", {
    SNS: {
      type: DataTypes.STRING(20),
      allowNull: false,
    },
    account: {
      type: DataTypes.STRING(30),
      allowNull: false,
    },
    auth: {
      type: DataTypes.STRING(30),
      allowNull: false,
    },
  });
  return userAuth;
};
