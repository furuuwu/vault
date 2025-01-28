var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

// Drawing a red rectangle
ctx.fillStyle = "#FF0000";
ctx.fillRect(50, 50, 150, 100);

// Drawing text
ctx.font = "30px Arial";
ctx.fillText("Hello, Canvas!", 50, 200);
