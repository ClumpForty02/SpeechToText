var speechRecognition = window.webkitSpeechRecognition
var recognition = new speechRecognition()

var textbox= $("#textbox")
var instructions= $("#instructions")
var content = ''
var isListening = false;
recognition.continuous = true

recognition.onstart = function()
{
    instructions.text("Voice Recognition is on.");
    isListening = true;
}


recognition.onspeechend = function()
{
    if (isListening)
        {
            instructions.text("No activity")
        }
}

recognition.onerror = function()
{
    instructions.text("Try again")
}

recognition.onresult = function(event)
{
    var current = event.resultIndex;
    var transcript = event.results[current][0].transcript

    content += transcript

    textbox.val(content)
}


$("#start-btn").click(function(event)
{
    if (!isListening)
        {
            content ="";
            textbox.val("");
            recognition.start();
            isListening = true;
        }
})

$("#stop-btn").click(function(event)
{
    if(isListening)
        {
            recognition.stop();
            instructions.text("Voice Recognition is off.");
            isListening = false;
        }
})

textbox.on('input', function()
{
    content = $(this).val()
})