import footnote from 'markdown-it-footnote'
import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'Project Euler 100',
  description: 'Exploring various problems from the wonderful math puzzle site [Project Euler](https://projecteuler.net)',
  cleanUrls: true,
  
  sitemap: {
    hostname: 'https://projecteuler.kevindamm.com',
    transformItems: (items) => {
      items.map((item) => {
        if (item.changefreq && item.changefreq != 'weekly') {
          item.changefreq = 'weekly'
        }})
      return items
    }
  },

  srcDir: "..", // allow direct importing of solutions' code in vitepress pages.
  rewrites: {
    // The project root is `/pages` and srcDir at `/`, this allows us to use the
    // root path for URLs instead of having the `/pages` directory in the URL.
    "pages/:path*": ":path*"
  },

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
    ],

    sidebar: [
      {
        text: 'completed',
        items: [
          { text: '0001: Multiples of 3 or 5', link: '/0001' },
          { text: '0002: Even Fibonacci Numbers', link: '/0002' },
        ]
      },
      {
        text: 'code complete',
        items: [
          { text: '0003: Largest Prime Factor', link: '/0003' },
          { text: '0004: Largest Palindrome Product', link: '/0004' },
          { text: '0005: Smallest Multiple', link: '/0005' },
          { text: '0006: Sum Square Difference', link: '/0006' },
          { text: '0007: 10001st Prime', link: '/0007' },
        ]
      },
      {
        text: 'in progress',
        items: [
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/kevindamm/projecteuler' }
    ],

    footer: {
      copyright: 'Copyright &copy; 2024-2025 Kevin Damm - MIT licensed source code'
    }
  },

  markdown: {
    math: true,
    config: (md) => {
      md.use(footnote)
    }
  }
})
