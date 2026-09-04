import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title:       z.string(),
    // shorter tag for the SERP; the H1 keeps the full descriptive title
    seoTitle:    z.string().optional(),
    description: z.string(),
    pillar:      z.enum(['engine', 'swap', 'body', 'suspension', 'interior', 'reference']),
    keywords:    z.string().optional(),
    date:        z.string().optional(),
    hero:        z.string().optional(),
    draft:       z.boolean().optional().default(false),
  }),
});

export const collections = { articles };
