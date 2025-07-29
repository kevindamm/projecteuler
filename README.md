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

Other contributions such as documentation, style/design, Vue components, or
corrections in spelling or citations, are also welcome, as long as they don't
depart too much from the existing site layout and page organization.  If you
are interested in contributing solutions in a different language, open an issue
to discuss which language and your reasoning for selecting that language.  I
would love to have a broad representation here but I also don't think most
esolanguages will be useful.  There is certainly some potential for turning this
into a kind of Rosetta Stone of code solutions, as long as they are idiomatic to
the language conventions (they should be good representations).


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
