function toggleAbstract(id, btnEl) {
  var el = document.getElementById(id);
  if (!el) return;
  var isHidden = el.hasAttribute('hidden') || el.style.display === 'none';
  if (isHidden) {
    el.removeAttribute('hidden');
    el.style.display = '';
    if (btnEl) btnEl.textContent = btnEl.textContent.replace(/^show/, 'hide');
  } else {
    el.setAttribute('hidden', '');
    el.style.display = 'none';
    if (btnEl) btnEl.textContent = btnEl.textContent.replace(/^hide/, 'show');
  }
}
