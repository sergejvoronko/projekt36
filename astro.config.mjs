import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import fs from 'node:fs';

// Sitemap lastmod from article frontmatter (reviewed, else date) so the
// IndexNow cron can spot changed guides. /guides/ takes the newest one.
const lastmod = new Map();
for (const f of fs.readdirSync('./src/content/articles')) {
  if (!f.endsWith('.md')) continue;
  const fm = fs.readFileSync(`./src/content/articles/${f}`, 'utf8').split('---')[1] ?? '';
  if (/^draft:\s*true/m.test(fm)) continue;
  const ds = (fm.match(/^reviewed:\s*"?([\d-]+)/m) ?? fm.match(/^date:\s*"?([\d-]+)/m) ?? [])[1];
  if (!ds) continue;
  const d = new Date(ds);
  lastmod.set(`/guides/${f.replace(/\.md$/, '')}/`, d);
  if (!lastmod.has('/guides/') || lastmod.get('/guides/') < d) lastmod.set('/guides/', d);
}

export default defineConfig({
  site: 'https://projekt36.com',
  output: 'static',
  trailingSlash: 'always',
  prefetch: true,
  build: {
    inlineStylesheets: 'always',
  },
  adapter: cloudflare(),
  integrations: [
    mdx(),
    sitemap({
      serialize(item) {
        const d = lastmod.get(new URL(item.url).pathname);
        if (d) item.lastmod = d.toISOString();
        return item;
      },
    }),
  ],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
});
