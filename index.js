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

        if (message == "attendance") {
            Notification.requestPermission().then(function(result) {
                var myNotification = new Notification('Attendance Alert', {
                    body: "Attendance is been taken !!"
                });
            })
        }


        console.log(message);
    })
}