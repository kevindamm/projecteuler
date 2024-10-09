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
          { text: 'Problem 001', link: '/blog/001' }
        ]
      },
      {
        text: 'in progress',
        items: [
          { text: 'Problem 002', link: '/blog/002' },
          { text: 'Problem 003', link: '/blog/003' }
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
