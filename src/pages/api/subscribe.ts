import type { APIRoute } from 'astro';
import { env } from 'cloudflare:workers';

export const prerender = false;

const json = (data: unknown, status: number) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });

export const POST: APIRoute = async ({ request }) => {
  let email: string | undefined;
  let website: string | undefined;
  try {
    ({ email, website } = await request.json() as { email?: string; website?: string });
  } catch {
    return json({ error: 'Invalid request' }, 400);
  }

  // Honeypot: bots fill every field. Pretend success so they don't retry.
  if (website) return json({ ok: true }, 200);

  email = email?.trim();
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 254) {
    return json({ error: 'Please enter a valid email address.' }, 400);
  }

  if (!env.MAILERLITE_API_KEY) {
    return json({ error: 'Newsletter is not set up yet. Please try again later.' }, 503);
  }

  const payload: Record<string, unknown> = { email };
  if (env.MAILERLITE_GROUP_ID) payload.groups = [env.MAILERLITE_GROUP_ID];

  try {
    const res = await fetch('https://connect.mailerlite.com/api/subscribers', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.MAILERLITE_API_KEY}`,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(payload),
    });
    if (res.ok) return json({ ok: true }, 200);
    console.error('MailerLite', res.status, await res.text());
  } catch (e) {
    console.error('MailerLite fetch failed', e);
  }
  return json({ error: 'Subscription failed. Please try again.' }, 502);
};
