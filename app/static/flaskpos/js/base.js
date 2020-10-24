// display messages
function dse(n, b, c, t) {
    $('#sysmessage').css('white-space', 'pre-line');
    $('#sysmessage').text(t + "\n" + n)
    $('#sysmessage').css('background-color', b);
    $('#sysmessage').css('color', c);
    $('#sysdiv').css('visibility', n ? 'visible' : 'hidden');
    $('#sysdiv').css('display', 'block');
    $('#sysdiv').css('background-color', b);
}

function date() {
    $('#thedate').text(moment().format('l'));
};

function time() {
    $('#thetime').text(moment().format('LTS'));
};

// call every minute the time function
$(function() {
    setInterval(function() {
        time();
    }, 1000)        // one second
    setInterval(function() {
        date();
    }, 1000 * 60)   // one minute
});