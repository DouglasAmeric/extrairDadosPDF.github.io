<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>teste</title>
</head>
<body>
    <div class="conteiner">
        <label for="DADO">COLOQUE O DADO</label>
        <input type="text" id="DADO">
        <button id="enviar" onclick="enviart()">ENVIAR</button>
    </div>

    <script>
            function enviart(){
                let btn = document.getElementById("enviar")
               
                if(btn){
                   window.alert("erro!")    
                }
            }


    </script>



</body>
</html>