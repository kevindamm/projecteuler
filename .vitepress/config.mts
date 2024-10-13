import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Project Euler solutions",
  description: "Exploring various problems from the wonderful math puzzle site [Project Euler](https://projecteuler.net)",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
    ],

    sidebar: [
      {
        text: 'completed',
        items: [
          { text: '0001: Multiples of 3 or 5', link: '/blog/0001' }
        ]
      },
      {
        text: 'code complete',
        items: [
          { text: '002: Even Fibonacci Numbers', link: '/blog/0002' },
          { text: '003: Largest Prime Factor', link: '/blog/0003' },
        ]
      },
      {
        text: 'in progress',
        items: [
          { text: '004: Largest Palindrome Product', link: '/blog/0004' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/kevindamm/projecteuler' }
    ]
  },

  markdown: {
    math: true
  }
})
