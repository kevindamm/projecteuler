import { createContentLoader } from 'vitepress'

interface Post {
  title: string
  url: string
  date: {
    time: number
    string: string
  }
  excerpt: string | undefined
}

declare const data: Post[]
export { data }

// The glob path is relative to srcDir.
export default createContentLoader('pages/*.md', {
  excerpt: true,
  transform(raw): Post[] {
    return raw
      .map(({ url, frontmatter, excerpt }) => ({
        title: frontmatter.title,
        url,
        excerpt,
        date: formatDate(frontmatter.date)
      }))
      .sort((a, b) => b.date.time - a.date.time)
  }
})

// Convert a date string into a DateTime value (for comparisons) and
// a consistently-formatted string.
function formatDate(dateString: string): Post['date'] {
  const date = new Date(dateString)
  // actual hour is arbitrary as long as it's the same for all
  date.setUTCHours(11)  

  return {
    time: +date,
    string: date.toLocaleDateString('en-US', { dateStyle: 'long' })
  }
}
