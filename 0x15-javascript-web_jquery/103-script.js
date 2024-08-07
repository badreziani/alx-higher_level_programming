const handleTranslate = function () {
  const lang = $('input#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
  $.get(url, function (data) {
    $('div#hello').html(data.hello);
  });
};

$(function () {
  $('input#language_code').focus();
  $('input#btn_translate').on('click', handleTranslate);
  $('input#language_code').on('keydown', function (e) {
    if (e.which === 13) {
      handleTranslate();
    }
  });
});
