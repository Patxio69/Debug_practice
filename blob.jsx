
const canvas = document.getElementById("myCanvas");
const context = canvas.getContext("2d");

function blob(size) {
    context.beginPath();
    context.arc(750,100,size, 0, 2*Math.PI);
    context.stroke();
}

function print(that) {
    let t = that
}

blob(20)
print("blob")