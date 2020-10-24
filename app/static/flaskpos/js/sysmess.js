// get notification
$(function() {
    setInterval(function() {
        $.ajax('/notification').done(
            function(no) {
                for (var i = 0; i < no.length; i++) {
                    var o = no[i];
                    var b = o.bc, c = o.fc , n = o.data, t = o.title;
                    dse(n, b, c, t)
                }
            }
        );
    }, 1000 * 30)   // 30 seconds
});