function toggleAbstract(id, btnEl) {
  var el = document.getElementById(id);
  if (!el) return;
  var isHidden = el.hasAttribute('hidden');
  if (isHidden) {
    el.removeAttribute('hidden');
    if (btnEl) btnEl.textContent = btnEl.textContent.replace(/^show/, 'hide');
  } else {
    el.setAttribute('hidden', '');
    if (btnEl) btnEl.textContent = btnEl.textContent.replace(/^hide/, 'show');
  }
}
