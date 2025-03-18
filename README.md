# Project Euler 100

Solutions and commentary on [Project Euler](https://projecteuler.net/about)
puzzles.

This includes some blog posts written in Markdown and Vue3 (using Vitepress) and
example programs written in Go, Python, TypeScript and GEL (Goal Expression
Language).  I've used this collection of math puzzles for practice and mastery
of new programming languages and programming techniques.  This time, I'm using
it to hone my Typescript/Vue3 skills and I also thought it would be a good way
to share my expertise on the topics touched on in the puzzles themselves.

## Contributing

If you would like to contribute, reach out to me on GitHub or by email.  I am
open to new writeups for problems that are not included yet, if they are in the
first 100 problems
(in line with [ProjectEuler.net publishing terms](https://projecteuler.net/about#publish)).
Solutions and writeups can be authored out of sequence.  

I would also be interested in a full set of solutions given in an
alternative language, such as Haskell or Lua or Lisp or C++ or others,
as long as there is enough of a difference from the current language set and
as long as it isn't too esoteric
(please no [brainf*ck](https://esolangs.org/wiki/Brainfuck),
 no [APL](https://esolangs.org/wiki/APL), no polyglot languages)
as I will be reviewing the code too.

Other contributions such as documentation, style/design, Vue components, or
corrections in spelling or citations, are also welcome, as long as they don't
depart too much from the existing site layout and page organization.


Here are some included utilities for generating per-language boilerplate that
you can use from any project, whether you decide to contribute solutions here
or not.  See the corresponding `/bin/*.js` code for more details.  The following
examples use Problem #64, you can substitute for any projecteuler problem ID.


### Starting a markdown page

Generating the article boilerplate will also fetch the problem description from
projecteuler.net and wrap it in a `<pe100-problem>...</pe100-problem>` tag,
corresponding to the component for problem descriptions.  The page's frontmatter
and article layout are also included.

```sh
npm x begin 64 "Odd Period Square Roots"
```

There isn't a convenient way to get the title from the original source.  You
can choose to only specify the problem number and a stub title will be used
instead.


### Starting a solution in Go

A new golang source file includes the copyright notice, filename and package.

```sh
npm x new-golang 64
```

### Starting a solution in Python

A new python source file includes the copyright & filename as well as
the `__main__` guard.

```sh
npm x new-python 64
```

### Starting a solution in Prolog

A new Prolog source file assumes the SWI-Prolog environment.  It only includes
the header (copyright & source file) but perhaps a root query would be helpful.

```sh
npm x new-prolog 64
```
