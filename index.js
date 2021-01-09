const { PythonShell } = require('python-shell')
var path = require("path")

function joinMeet() {
    var meetCode = document.getElementById("google-meet-code").value

    var options = {
        scriptPath: path.join(__dirname, '/'),
        args: [meetCode]
    }

    var pyshell = new PythonShell('ah101.py', options);

    pyshell.on('message', function(message) {
        console.log(message);
    })
}