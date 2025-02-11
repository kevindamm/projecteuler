import footnote from 'markdown-it-footnote'
import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'Project Euler solutions',
  description: 'Exploring various problems from the wonderful math puzzle site [Project Euler](https://projecteuler.net)',
  
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

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
    ],

    sidebar: [
      {
        text: 'completed',
        items: [
          { text: '0001: Multiples of 3 or 5', link: '/blog/0001' },
          { text: '0002: Even Fibonacci Numbers', link: '/blog/0002' },
        ]
      },
      {
        text: 'code complete',
        items: [
          { text: '0003: Largest Prime Factor', link: '/blog/0003' },
          { text: '0004: Largest Palindrome Product', link: '/blog/0004' },
          { text: '0005: Smallest Multiple', link: '/blog/0005' },
          { text: '0006: Sum Square Difference', link: '/blog/0006' },
          { text: '0007: 10001st Prime', link: '/blog/0007' },
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
      copyright: 'Copyright (c) 2024 Kevin Damm - MIT licensed source code'
    }
  },

  markdown: {
    math: true,
    config: (md) => {
      md.use(footnote)
    }
  }
})
