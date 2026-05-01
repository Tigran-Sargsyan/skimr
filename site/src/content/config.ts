import { defineCollection, z } from 'astro:content';

const items = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    author: z.string(),
    source_id: z.number(),
    source_slug: z.string(),
    url: z.string().url(),
    published_at: z.string(),
    duration_seconds: z.number().nullable(),
    primary_theme: z.enum(['tech', 'business', 'science', 'thinking', 'culture']),
    secondary_theme: z.enum(['tech', 'business', 'science', 'thinking', 'culture']).nullable(),
    relevance: z.number().min(1).max(10),
    hook: z.string(),
    tldr: z.string(),
    caveats: z.string().nullable(),
    pitch: z.string(),
  }),
});

export const collections = { items };
