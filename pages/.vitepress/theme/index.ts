// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import type { ContentOptions, Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'

import ProjectEulerProblem from './components/ProjectEulerProblem.vue'
import StartLayout from './components/StartLayout.vue'

import articles from './composables/articles.data.ts'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
    })
  },
  async enhanceApp({ app, router, siteData }) {
    //app.component('start', StartLayout)
    app.component('pe100-problem', ProjectEulerProblem)

    //app.provide('articles', articles.load())
  }
} satisfies Theme
