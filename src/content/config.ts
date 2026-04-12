import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title:       z.string(),
    description: z.string(),
    pillar:      z.enum(['engine', 'swap', 'body', 'suspension', 'interior', 'reference']),
    keywords:    z.string().optional(),
    date:        z.string().optional(),
    draft:       z.boolean().optional().default(false),
  }),
});

export const collections = { articles };
