function setAmount(v) {
  amount = v;
  if (amount < prefilled) {
    amount = prefilled;
  }
  $('#money').val(parseFloat(amount).toFixed(2));
  $('#abrechnen').val(parseFloat(amount).toFixed(2));
}
function addMoney(v) {
    v = Math.round(v * m) / m;
    amount += v;
    amount = Math.round(amount * m) / m;
    setAmount(amount);
}
function setCurrent(v) {
    v = Math.round(v * m) / m;
    amount = v;
    setAmount(amount);
}