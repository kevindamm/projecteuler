#!/usr/bin/env node

/**
 * @file new_ocaml.js
 * @example npm x new-ocaml 42
 * 
 * Generates the boilerplate of a new OCaml solution.
 * 
 * @param integer (required) the problem number (according to ProjectEuler.net)
 */

import path from 'node:path';
import { existsSync } from 'node:fs';
import { Buffer } from 'node:buffer';
import { readFile, writeFile } from 'node:fs/promises';

if (!process.argv[2]) {
  console.error('must call with a numeric argument (the problem ID)');
  process.exit(1);
}
const problem_number = Number(process.argv[2]);
if (!problem_number) {
  console.error('failed to parse the problem ID from the first argument (it must be a number)');
  process.exit(1);
}

const digits_padded = String(problem_number).padStart(4, '0');
const filepath = path.join('.', 'ocaml',
  'p'.concat(digits_padded).concat('.ml'));
if (existsSync(filepath)) {
  error(`File ${filepath} already exists, ` +
    `delete it first if you intended to overwrite it.`);
  process.exit(1);
}

const { titles } = JSON.parse(await readFile("./public/pe100.json", "utf-8"))
const title = title_if_known(titles, problem_number);

// If you aren't me, feel free to change the author name.
const template = `(*
Copyright (c) 2025 Kevin Damm
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

github:kevindamm/projecteuler/ocaml/p${digits_padded}.ml
*)

(* Problem ${digits_padded} - ${title} *)

let _ =
  print_newline "oh!"
`;


try {
  await writeFile(
    filepath,
    new Uint8Array(Buffer.from(template)));
} catch (err) {
  console.error(err);
}

console.log(`Done writing OCaml boilerplate to ${filepath}.`);
process.exit(0);


// retrieves the title for any problem between #1 to #100.
function title_if_known(titles, pe_num) {
  if (!pe_num ||
    typeof(pe_num) != "number" ||
    pe_num < 1 || pe_num >= titles.length) {
    return titles[0] || "<<UNK>>";
  }
  return titles[pe_num];
}
