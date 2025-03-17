import { defineLoader } from 'vitepress'

type NameToPath = { [key: string]: string }
export interface Data {
  cuelang?: NameToPath,
  GEL?: NameToPath,
  golang: NameToPath,
  prolog: NameToPath,
  python: NameToPath,
}

declare const data: Data
export { data }

export default defineLoader({
  watch: [
    '../cuelang',
    '../GEL',
    '../golang',
    '../prolog',
    '../python'
  ],
  load(files: string[]): Data {
    // Hard-coded for convenience during development, will be refactored to
    // read these dynamically from the directory listings in the near future.
    return {
      golang: {
        "0001": "golang/p0001/solve.go",
        "0002": "golang/p0002/solve.go",
        "0003": "golang/p0003/solve.go",
        "0004": "golang/p0004/solve.go",
        "0005": "golang/p0005/solve.go",
        "0006": "golang/p0006/solve.go",
        "0007": "golang/p0007/solve.go",
        "0008": "golang/p0008/solve.go",
        "0009": "golang/p0009/solve.go",
        "0010": "golang/p0010/solve.go",
        "0011": "golang/p0011/solve.go",
        "0012": "golang/p0012/solve.go",
        "0013": "golang/p0013/solve.go",
        "0014": "golang/p0014/solve.go",
        "0015": "golang/p0015/solve.go",
      },
      prolog: {
        "0001": "prolog/p0001.select.prolog",
        "0002": "prolog/p0002.select.prolog",
        "0003": "prolog/p0003.prolog",
        "0004": "prolog/p0004.prolog",
      },
      python: {
        "0001": "python/p0001.py",
        "0002": "python/p0002.py",
        "0003": "python/p0003.py",
        "0004": "python/p0004.py",
        "0005": "python/p0005.py",
        "0006": "python/p0006.py",
        "0007": "python/p0007.py",
        "0008": "python/p0008.py",
        "0009": "python/p0009.py",
        "0010": "python/p0010.py",
        "0011": "python/p0011.py",
        "0012": "python/p0012.py",
        "0013": "python/p0013.py",
        "0014": "python/p0014.py",
        "0015": "python/p0015.py",
        "0016": "python/p0016.py",
        "0017": "python/p0017.py",
        "0018": "python/p0018.py",
        "0019": "python/p0019.py",
        "0020": "python/p0020.py",
        "0021": "python/p0021.py",
        "0022": "python/p0022.py",
        "0023": "python/p0023.py",
        "0024": "python/p0024.py",
        "0025": "python/p0025.py",
        "0026": "python/p0026.py",
        "0027": "python/p0027.py",
      },
    } as Data
  }
})
