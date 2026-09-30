// assets/js/copy-to-clipboard.js
  document
    .querySelectorAll('.post-content figure.highlight')
    .forEach(function (figure) {
      var button = document.createElement('button');
      var copyText = 'Copy';
      button.type = 'button';
      button.ariaLabel = 'Copy BibTeX to clipboard';
      button.innerText = copyText;
      button.addEventListener('click', function () {
        var code = figure.querySelector('code').innerText;
        try {
          code = code.trimEnd();
        } catch (e) {
          code = code.trim();
        }
        navigator.clipboard.writeText(code);
        button.innerText = 'Copied';
        setTimeout(function () {
          button.blur();
          button.innerText = copyText;
        }, 2e3);
      });
      figure.prepend(button);
    });
