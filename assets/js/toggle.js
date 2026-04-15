function toggleAbstract(id, btnEl) {
  var el = document.getElementById(id);
  if (!el) return;
  var isHidden = el.hasAttribute('hidden') || el.style.display === 'none';
  if (isHidden) {
    el.removeAttribute('hidden');
    el.style.display = '';
  } else {
    el.setAttribute('hidden', '');
    el.style.display = 'none';
  }
}
