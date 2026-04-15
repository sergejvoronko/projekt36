export const prerender = false;

import type { APIRoute } from 'astro';

interface PrintifyProduct {
  id: string;
  external?: { id: string; handle: string };
}

export const GET: APIRoute = async ({ params, locals, redirect }) => {
  const { id } = params;
  if (!id) return redirect('/shop', 302);

  const { env } = locals.runtime;
  const token    = env?.PRINTIFY_API_TOKEN;
  const shopId   = env?.PRINTIFY_SHOP_ID;
  const storeUrl = env?.PRINTIFY_STORE_URL ?? '';

  if (!token || !shopId) return redirect('/shop', 302);

  try {
    const res = await fetch(
      `https://api.printify.com/v1/shops/${shopId}/products/${id}.json`,
      { headers: { Authorization: `Bearer ${token}` } }
    );
    if (!res.ok) return redirect('/shop', 302);

    const product = await res.json() as PrintifyProduct;
    const handle = product.external?.handle;

    if (handle && storeUrl) {
      return redirect(`${storeUrl}/products/${handle}`, 302);
    }
    // Fall back to product detail page if no external URL configured
    return redirect(`/shop/${id}`, 302);
  } catch {
    return redirect('/shop', 302);
  }
};
