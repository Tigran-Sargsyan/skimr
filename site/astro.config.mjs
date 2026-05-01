import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://tigran-sargsyan.github.io',
  base: '/skimr',
  output: 'static',
  trailingSlash: 'ignore',
});
