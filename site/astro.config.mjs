import { defineConfig } from 'astro/config';

// Replace <username> with your GitHub username before deploying.
// If deploying to a custom domain or to the root of <username>.github.io,
// remove the `base` line.
export default defineConfig({
  site: 'https://username.github.io',
  base: '/skimr',
  output: 'static',
  trailingSlash: 'ignore',
});
