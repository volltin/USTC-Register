/**
 * Created by vollt on 2017/5/7.
 */

$( window ).on( "load", function() {
    $("#ustc_id").on("click", function(e) {
      if ($("#ustc_id").val() == "") {
          window.location.href = $('#bind_ustc_id').attr('href');
      }
    })
})
