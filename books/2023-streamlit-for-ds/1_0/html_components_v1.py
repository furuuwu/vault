import streamlit as st

# HTML + JavaScript code to create a canvas and draw something
canvas_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h3>Canvas Example</h3>
    <canvas id="myCanvas" width="400" height="400"></canvas>
    <script>
        var canvas = document.getElementById("myCanvas");
        var ctx = canvas.getContext("2d");

        // Drawing a red rectangle
        ctx.fillStyle = "#FF0000";
        ctx.fillRect(50, 50, 150, 100);

        // Drawing text
        ctx.font = "30px Arial";
        ctx.fillText("Hello, Canvas!", 50, 200);
    </script>
</body>
</html>
"""

# Use st.components.v1.html to embed the canvas in Streamlit
st.components.v1.html(canvas_code, height=450)
