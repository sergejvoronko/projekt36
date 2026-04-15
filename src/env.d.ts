/// <reference types="astro/client" />

interface Env {
  PRINTIFY_API_TOKEN: string;
  PRINTIFY_SHOP_ID: string;
  PRINTIFY_STORE_URL: string;
}

type Runtime = import("@astrojs/cloudflare").Runtime<Env>;

declare namespace App {
  interface Locals extends Runtime {}
}
