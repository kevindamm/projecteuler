# OCaml solutions to ProjectEuler 100

[OCaml](https://ocaml.org) was chosen as the representative [Functional Language](
    https://wikipedia.org/wiki/Functional_programming)
for PE100 solutions because of its expressiveness and type-safety, its deep
integration with VSCode (and vim and emacs), its utop REPL and its succinctness.
It has seen continuous development for over 25 years and includes a very rich type
system and collection of libraries out of the box.

Although the "O" stands for Object, the object system of ocaml is rarely used in
these examples, with occasional use of modules/interfaces and heavy use of the
functional programming paradigm.  Where suitable, Sequences and other resource-
efficient techniques are used.

I find that in comparison to the other languages here, such as Go, TypeScript and
even Python, that OCaml comes closest to poetry in the way its programs are
structured.  Even when compared to other functional languages, OCamls tendency toward
single expression forms (while not hugging everything in parens) gives it a rhythm
of its own.  If you know of a more elegant or creative way to solve a problem than
any of the examples here, send a note or a pull request and I'll be sure to include
you in the credits.  I'm always interested in new and intersting ways to do things.


## Environment Setup

[Install OCaml](https://ocaml.org/docs/installing-ocaml), if not installed already.

For developing with language tool support, including an LSP server,
[install OPAM](https://opam.ocaml.org/)

* OPAM is a source-based package manager for OCaml, and is how the language
  server and many other packages are commonly distributed.  With OPAM installed,
  run its initialization in this directory, or where you want to put your workspace.

```bash
opam init
```

With OPAM installed and initialized, install the language server:

```bash
opam install ocaml-lsp-server
```

Optionally, you may also want to install the code formatter:

```bash
opam install ocamlformat
```

During development, you can set up Dune to continuously build.  Building the project
with Dune also enables some QoL features like go-to-definition and auto-completion.

```bash
dune build --watch
```
