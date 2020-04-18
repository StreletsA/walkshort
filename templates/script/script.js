function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
var op = 0;
async function setOpacity() {
  while(op < 1){
    op += 0.1;
    document.getElementById('tip').style.opacity=op;
    await sleep(30);
  }
  await sleep(500);
  while(op > 0){
    op -= 0.1;
    document.getElementById('tip').style.opacity=op;
    await sleep(30);
  }
}

function copytext(){
  var copyText = document.getElementById("ans");
  copyText.select();
  document.execCommand("copy");
  setOpacity();
}
function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("ans");

    copyText.select();
    document.execCommand("copy");

    /* Alert the copied text */
    alert("Скопировано в буфер обмена");
}
