// Wires every <form data-subscribe> on the page to /api/subscribe/.
// The form needs an email input; its status line is the element named by data-note.
export function wireSubscribeForms() {
  document.querySelectorAll<HTMLFormElement>('form[data-subscribe]:not([data-wired])').forEach(form => {
    form.dataset.wired = '';
    const note = document.getElementById(form.dataset.note ?? '');
    const btn = form.querySelector<HTMLButtonElement>('button[type="submit"]');
    const input = form.querySelector<HTMLInputElement>('input[type="email"]');
    if (!input) return;

    // Hidden honeypot so bots get filtered server-side without a captcha.
    const hp = document.createElement('input');
    Object.assign(hp, { type: 'text', name: 'website', tabIndex: -1, autocomplete: 'off' });
    hp.setAttribute('aria-hidden', 'true');
    hp.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;opacity:0';
    form.append(hp);

    const say = (text: string, ok?: boolean) => {
      if (!note) return;
      note.textContent = text;
      note.style.color = ok === undefined ? 'var(--text-mid)' : ok ? 'var(--green)' : 'var(--red)';
    };

    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (btn) btn.disabled = true;
      say('Subscribing…');
      try {
        const res = await fetch('/api/subscribe/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: input.value, website: hp.value }),
        });
        const data = await res.json().catch(() => ({}));
        if (res.ok) {
          form.querySelectorAll<HTMLElement>('input, button').forEach(el => (el.style.display = 'none'));
          say('✓ You\'re in. Build updates on the way.', true);
          return;
        }
        say(data.error ?? 'Subscription failed. Please try again.', false);
      } catch {
        say('Network error. Please try again.', false);
      }
      if (btn) btn.disabled = false;
    });
  });
}
